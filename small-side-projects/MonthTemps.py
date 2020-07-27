import random
import matplotlib.pyplot as plt
import numpy as np
def run():

    #Prbobabilities of L/M/H:
    qlow = 7.5/30
    qmed = 16.0/30
    qhigh = 6.5/30
    qlist = [qlow,qmed,qhigh]

    #Trial count:
    trials = 10000

    t=[]
    
    for i in range(trials):
        ttot=0
        for i in range(2):
            plist = [0,0,0]
            for i in range(30):
                plist[np.random.choice(3,p=np.array([qlow,qmed,qhigh]))]+=1/30
            for i in range(3):
                ttot += ((plist[i]-qlist[i])**2)/qlist[i]            
        t.append(ttot)

    observed = np.array([[10,18,2],[5,14,11]])
    tobserved = 0
    for i in range(2):
        for j in range(3):
            plist[j] = observed[i][j]/30
            tobserved += ((plist[j]-qlist[j])**2)/qlist[j]

 
    p = np.mean(t>tobserved)
    q = np.mean(t<tobserved)

    plt.hist(t,200)
    plt.axvline(tobserved, color='red')
    #y,binedges = np.histogram(t,200)
    #bincentres = []
    #for i in range(len(binedges)-1):
 #       bincentres.append(0.5*(binedges[i]+binedges[i+1]))
    #plt.plot(bincentres,y)
    print(q)
    print(p)
    plt.show()



if __name__ == "__main__":
    run()