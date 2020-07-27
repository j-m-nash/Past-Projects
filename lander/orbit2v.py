from verlet import verlet3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

def run():
    x0 = 3.5*10**6
    xdot0 = 0
    y0 = 0
    ydot0 = 3273
    z0 = 1.9365*10**6
    zdot0 = 0
    pos0 = [float(x0),float(y0),float(z0)]
    vel0 = [float(xdot0),float(ydot0),float(zdot0)]
    M = 6.42*10**23
    R = 3.390*10**6
    m = 360
    t_max = 10000
    dt = 2
    pos = verlet3d(pos0,vel0,m,M,t_max,dt,R)[0]
    vel = verlet3d(pos0,vel0,m,M,t_max,dt,R)[1]

    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = R*np.cos(u)*np.sin(v)
    y = R*np.sin(u)*np.sin(v)
    z = R*np.cos(v)
    ax.plot_wireframe(x, y, z, color="blue", alpha=0.2)
    posx = [0]*len(pos)
    posy = [0]*len(pos)
    posz = [0]*len(pos)
    for i in range(len(pos)):
        posx[i] = pos[i][0]
        posy[i] = pos[i][1]
        posz[i] = pos[i][2]
    ax.set_xlim([-2*R,2*R])
    ax.set_ylim([-2*R,2*R])
    ax.set_zlim([-2*R,2*R])
    plt.plot(posx, posy, posz, color = "red")

    
    plt.show()



if __name__ == "__main__":
    run()