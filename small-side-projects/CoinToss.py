import random
import matplotlib.pyplot as plt
def run():

    #Input No. of tosses here:
    tosses = 5

    #Input how many times you want to do those tosses:
    sets = 100000

    #Would you like graph plotted? (Y/N)
    graph = 'Y'

    #Probability of getting a heads:
    phead = 0.0

    x = []
    for i in range(tosses+1):
        x.append(i)
    y = [0]*len(x)

    for i in range(sets):
        heads = 0
        for i in range(tosses):
            if random.random()<phead:
                heads += 1
            else: 
                pass
        
        y[heads] += 1
    print()
    print("Number of instances of each number of heads for {} sets:".format(sets))
    print()
    for i in range(tosses+1):
        print("{} sets returned {} heads".format(y[i],i))
    plt.plot(x, y)
    if graph == 'Y':
        plt.show()
    else: 
        pass


if __name__ == "__main__":
    run()