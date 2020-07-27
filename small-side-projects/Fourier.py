import numpy as py
import math
import matplotlib.pyplot as plt

def run():
    x = []
    step = 1000
    lines = 2
    r = 1000
    for i in range(lines):
        p = step*(i)+2
        for i in range(r+1):
            x.append((2*math.pi)-(math.pi*4*i)/r)
        y = []
        for i in range(len(x)):
            y.append(0)
            n = 1
            while n<p:
                m=2*n-1
                y[i] += (4/math.pi)*(math.sin(m*x[i])/m)
                n+=1   
        plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    run()