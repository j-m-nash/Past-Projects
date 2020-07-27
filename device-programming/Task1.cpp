#include "mbed.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);
int t=1;
int t2=0;
const int N =10;
int a[N+4] = {4,5,4,5};
int c=4;

Timeout button_debounce_timeout;
float debounce_time_interval = 0.3;

InterruptIn button(USER_BUTTON);

Ticker cycle_ticker;
float cycle_time_interval = 1;



void onButtonStopDebouncing(void);

void onButtonPress(void)
{
        a[c] = ((t+1)%3)+1;
        c = c+1;
            
        button.rise(NULL);
        button_debounce_timeout.attach(onButtonStopDebouncing, debounce_time_interval);

}

void onButtonStopDebouncing(void)
{
        button.rise(onButtonPress);
}

void select_led(int l)
{
        
        if (l==1) {
                led1 = true;
                led2 = false;
                led3 = false;
        }
        else if (l==2) {
                led1 = false;
                led2 = true;
                led3 = false;
        }
        else if (l==0) {
                led1 = true;
                led2 = true;
                led3 = false;
        }
        else if (l==3) {
                led1 = false;
                led2 = false;
                led3 = true;
        }
        else if (l==4) {
                led1 = true;
                led2 = true;
                led3 = true;
        }
        else if (l==5) {
                led1 = false;
                led2 = false;
                led3 = false;
        }
}

void onCycleTicker1(void)
{
        if (c < N+4) {
        select_led(t);
        t=(t%3)+1;
        }
        else{
        select_led(a[t2]);
        t2=(t2+1)%(N+4);
            }
}

int main()
{   
        button.rise(onButtonPress);
        cycle_ticker.attach(onCycleTicker1, cycle_time_interval);
        
        
}