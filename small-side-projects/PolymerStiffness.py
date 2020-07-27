import random
import matplotlib.pyplot as plt
def run():
    c = 10 #number of crosslinks
    trials = 10000
    total_stiffnesses = []
    position_list = [0]*(c+2)
    differences = [0]*(c+1)
    histogram = []
    frequencies = []
    for p in range(trials):        
        position_list[0] = 1.0
        for i in range(c): 
            position_list[i+1] = random.random()
        position_list = sorted(position_list)       
        for i in range(c+1):
            differences[i]=position_list[i+1]-position_list[i]
        total_stiffness = 0.0
        for i in range(c+1):
            total_stiffness += differences[i]**2
        total_stiffness = total_stiffness**-1
        #print(total_stiffness)
        total_stiffnesses.append(int(total_stiffness))
        total_stiffnesses = sorted(total_stiffnesses)
    f=1
    if total_stiffnesses[0] == total_stiffnesses[1]:
        pass
    else:
        histogram.append(total_stiffnesses[0])
        frequencies.append(f)
    
    for k in range(trials-1):
        if total_stiffnesses[k+1] == total_stiffnesses[k]:
            f+=1
        else:
            histogram.append(total_stiffnesses[k+1])
            frequencies.append(f)
            f=1
    plt.hist(total_stiffnesses, bins=len(histogram), rwidth = 0.9)
    plt.show()


if __name__ == "__main__":
    run()
