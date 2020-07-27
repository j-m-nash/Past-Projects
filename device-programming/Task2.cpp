#include "mbed.h"
#define LM75_REG_TEMP (0x00) // Temperature Register
#define LM75_REG_CONF (0x01) // Configuration Register
#define LM75_ADDR     (0x90) // LM75 address

I2C i2c(I2C_SDA, I2C_SCL);

DigitalOut led3(LED3);
DigitalOut led1(LED1);

Serial pc(SERIAL_TX, SERIAL_RX);

volatile char TempCelsiusDisplay[] = "+abc.d C";
float temps [60] = {};
int listprinted = 0;
float currenttemp = 0.0;
int alarm = 0;

void tempsense()
{
                char data_write[2];
                char data_read[2];
                data_write[0] = LM75_REG_TEMP;
                i2c.write(LM75_ADDR, data_write, 1, 1);
                i2c.read(LM75_ADDR, data_read, 2, 0);
                int tempval = (int)((int)data_read[0] << 8) | data_read[1];
                tempval >>= 7;
                if (tempval <= 256) {
                        TempCelsiusDisplay[0] = '+';
                } else {
                        TempCelsiusDisplay[0] = '-';
                        tempval = 512 - tempval;
                }
                if (tempval & 0x01) {
                        TempCelsiusDisplay[5] = 0x05 + 0x30;
                } else {
                        TempCelsiusDisplay[5] = 0x00 + 0x30;
                }
                tempval >>= 1;
                TempCelsiusDisplay[1] = (tempval / 100) + 0x30;
                TempCelsiusDisplay[2] = ((tempval % 100) / 10) + 0x30;
                TempCelsiusDisplay[3] = ((tempval % 100) % 10) + 0x30;
                led1 = !led1;
}    

void tempwrite()
{
    currenttemp = 100*int(TempCelsiusDisplay[1]-'0')+10*int(TempCelsiusDisplay[2]-'0')+int(TempCelsiusDisplay[3]-'0')+0.1*int(TempCelsiusDisplay[5]-'0');
    for (int a=0;a<=58;a++)
    {
        temps[a] = temps[a+1];
    }
    temps[59] = currenttemp;
    
}

void alarmcheck()
{
    pc.printf("Current temp: %+5.1f",currenttemp); //can be removed if you dont want live feed
    pc.printf("C \n"); //can be removed if you dont want live feed
    if (currenttemp>=28)
    {
        alarm = 1;
    }
}    

void runalarm()
{
    led3 = !led3;
    led1 = 0;
    if (listprinted==0)
    {
        listprinted = 1;
        pc.printf("Warning! Temperature exceeded 28C! Past 60 Recordings: \n");
        for (int b=0;b<=59;b++)
        {
            pc.printf("%+5.1f",temps[b]);
            pc.printf("C \n");   
        }         
    }
}    

int main()
{
    while (1)
    {
        if(alarm==0)
        {   
            tempsense();
            tempwrite();
            alarmcheck();
        }
        else
        {   
            runalarm();
        } 
    wait(1.0); 
    }
}