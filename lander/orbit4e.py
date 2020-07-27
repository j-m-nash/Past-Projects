from euler import euler3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

def run():
    x0 = 6*10**7
    xdot0 = -6900
    y0 = -10**7
    ydot0 = 800
    z0 = 10**7
    zdot0 = -800
    pos0 = [float(x0),float(y0),float(z0)]
    vel0 = [float(xdot0),float(ydot0),float(zdot0)]
    M = 6.42*10**23
    R = 3.390*10**6
    m = 360
    t_max = 30000
    dt = 2
    pos = euler3d(pos0,vel0,m,M,t_max,dt,R)[0]
    vel = euler3d(pos0,vel0,m,M,t_max,dt,R)[1]

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
    ax.set_xlim([-10*R,10*R])
    ax.set_ylim([-10*R,10*R])
    ax.set_zlim([-10*R,10*R])
    plt.plot(posx, posy, posz, color = "red")

    
    plt.show()




if __name__ == "__main__":
    run()