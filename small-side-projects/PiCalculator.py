
def run():
    #number of terms:
    n = 10**9




    total = 0
    for i in range(n):
        b = i+1
        total += ((-1)**(b+1))/b**2
    
    pi = (12 * total)**0.5
    print(pi)



if __name__ == "__main__":
    run()