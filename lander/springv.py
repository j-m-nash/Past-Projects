import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x0 = 0
v = 1

# simulation time, timestep and time
t_max = 500
# dt stable for dt<2
dt = 1.6
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

x1=x0 + v*dt

# Euler integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x0)
    v_list.append(v)

    # calculate new position and velocity
    x2 = 2*x1 - x0 - (dt**2)*k*(x1/m)
    v = (1/dt)*(x2-x1)
    x0 = x1
    x1 = x2
    
# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()
   