import numpy as np

def run():
    x0 = 4.0*10**6
    xdot0 = 0.0
    y0 = 0.0
    ydot0 = 0.0
    z0 = 0.0
    zdot0 = 0.0
    pos0 = [x0,y0,z0]
    vel0 = [xdot0,ydot0,zdot0]
    M = 6.42*10**23
    R = 3.390*10**6
    m = 360
    t_max = 10
    dt = 1


    m = m
    G = 6.674*(10**-11)
    pos = pos0
    vel = vel0
    k = (G*M*m)/np.linalg.norm(pos)**2

    # simulation time, timestep and time
    t_max = t_max
    dt = dt
    t_array = np.arange(0, t_max, dt)

    # initialise empty lists to record trajectories
    pos_list = []
    vel_list = []

    
    # Euler integration
    for t in t_array:

        # append current state to trajectories
        pos_list.append(pos[:])
        vel_list.append(vel[:])

        # calculate new position and velocity
        a = [0]*len(pos)
        for i in range(len(pos)):
            if pos[i] != 0:
                a[i] = -(G*M)/(np.linalg.norm(pos)*pos[i])
            else: 
                a[i] = 0
            pos[i] = pos[i] + dt * vel[i]
            vel[i] = vel[i] + dt * a[i]
            
    print(vel_list)

if __name__ == "__main__":
    run()
