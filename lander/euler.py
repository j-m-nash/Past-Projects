import numpy as np

def euler3d(pos0,vel0,m,M,t_max,dt,R):
    m = m
    G = 6.674*(10**-11)
    pos = [0]*len(pos0)
    for i in range(len(pos0)):
        pos[i]=pos0[i]
    vel = [0]*len(vel0)
    for i in range(len(vel0)):
        vel[i]=vel0[i]
    success = -1

    # simulation time, timestep and time
    t_max = t_max
    dt = dt
    t_array = np.arange(0, t_max, dt)

    # initialise empty lists to record trajectories
    pos_list = []
    vel_list = []

    
    # Euler integration
    for t in t_array:

        if np.linalg.norm(pos) > R:
            # append current state to trajectories
            pos_list.append(pos[:])
            vel_list.append(vel[:])

            # calculate new position and velocity
            a = [0]*len(pos)
            for i in range(len(pos)):
                if pos[i] != 0:
                    a[i] = -(G*M*pos[i])/(np.linalg.norm(pos)**3)
                else: 
                    a[i] = 0
                
                pos[i] = pos[i] + dt * vel[i]
                vel[i] = vel[i] + dt * a[i]
            success+=1
        else:
            pos_list.append(pos_list[success])
            vel_list.append([0]*len(vel))
            
        

    # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    pos_array = np.array(pos_list)
    vel_array = np.array(vel_list)

    return pos_array, vel_array