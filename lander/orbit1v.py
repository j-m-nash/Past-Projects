from verlet import verlet3d
import matplotlib.pyplot as plt
import numpy as np


def run():
    x0 = 4*10**6
    xdot0 = 0
    y0 = 0
    ydot0 = 0
    z0 = 0
    zdot0 = 0
    pos0 = [float(x0),float(y0),float(z0)]
    vel0 = [float(xdot0),float(ydot0),float(zdot0)]
    M = 6.42*10**23
    R = 3.390*10**6
    m = 360
    t_max = 1000
    dt = 1
    t_array = np.arange(0, t_max, dt)
    pos = verlet3d(pos0,vel0,m,M,t_max,dt,R)[0]
    vel = verlet3d(pos0,vel0,m,M,t_max,dt,R)[1]


    altitude = []
    for i in range(len(pos)):
        altitude.append(np.linalg.norm(pos[i])-R)

    plt.plot(t_array, altitude, color = "red")
    plt.show()
    



if __name__ == "__main__":
    run()