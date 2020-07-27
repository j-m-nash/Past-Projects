import numpy as np

def verlet3d(pos0,vel0,m,M,t_max,dt,R):
    m = m
    G = 6.674*(10**-11)
    pos = [0]*len(pos0)
    for i in range(len(pos0)):
        pos[i]=pos0[i]
    vel = [0]*len(vel0)
    for i in range(len(vel0)):
        vel[i]=vel0[i]
    success = 0

    # simulation time, timestep and time
    t_max = t_max
    dt = dt
    t_array = np.arange(0, t_max, dt)

    # initialise empty lists to record trajectories
    pos_list = []
    vel_list = []
    pos2 = [0]*len(pos)
    vel2 = [0]*len(vel)
    pos1 = [0]*len(pos)
    vel1 = [0]*len(vel)    

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
        pos1[i] = pos[i] + dt * vel[i]
        vel[i] = vel[i] + dt * a[i]
    
    

    #verlet from then on
    for t in range(len(t_array)-1):
        if np.linalg.norm(pos) > R:
            # append current state to trajectories
            pos_list.append(pos1[:])
            vel_list.append(vel[:])

            # calculate new position and velocity
            a = [0]*len(pos)
            for i in range(len(pos)):
                if pos[i] != 0:
                    a[i] = -(G*M*pos[i])/(np.linalg.norm(pos)**3)
                else: 
                    a[i] = 0
                pos2[i] = 2*pos1[i] - pos[i] + (dt**2)*a[i]
                vel[i] = (1/(2*dt))*(pos2[i]-pos[i])
                pos[i] = pos1[i]
                pos1[i] = pos2[i]
        else:
            pos_list.append(pos[:])
            vel_list.append([0]*len(vel))
            


    # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    pos_array = np.array(pos_list)
    vel_array = np.array(vel_list)

    return pos_array, vel_array