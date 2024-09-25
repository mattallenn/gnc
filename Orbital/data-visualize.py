#%% 
import pandas as pd
from matplotlib import pyplot as plt
#%% 
data_l = pd.read_csv("rotdata/data_l_1.csv")
data_r = pd.read_csv("rotdata/data_r_1.csv")
#%% 
# Offset time of right side
data_r.loc[:,' Time'] += 8

# Concatenate data from both tests and reset index
data_raw = pd.concat([data_l, data_r])
data_raw = data_raw.reset_index()

# Create a new frame and add scaled/offset values
accel_scale = 2 / (2**15)
gyro_scale = 250 / (2**15)
data = pd.DataFrame()
data['t'] = data_raw[' Time']
data['acc_x'] = (data_raw[' Gyro X'] - data_raw[' Gyro X'][0]) * accel_scale
data['acc_y'] = (data_raw[' Gyro Y'] - data_raw[' Gyro Y'][0]) * accel_scale
data['acc_z'] = (data_raw[' Gyro Z'] - data_raw[' Gyro Z'][0]) * accel_scale
data['gyro_x'] = (data_raw[' Accel X'] - data_raw[' Accel X'][0]) * gyro_scale
data['gyro_y'] = (data_raw[' Accel Y'] - data_raw[' Accel Y'][0]) * gyro_scale
data['gyro_z'] = (data_raw[' Accel Z'] - data_raw[' Accel Z'][0]) * gyro_scale

# Compute angular acceleration from dw/dt
data['ang_acc_x'] = data['t']*0
data['ang_acc_y'] = data['t']*0
data['ang_acc_z'] = data['t']*0
data.loc[1:,'ang_acc_x'] = (data['gyro_x'][1:].to_numpy() - data['gyro_x'][0:-1].to_numpy()) / (data['t'][1:].to_numpy() - data['t'][0:-1].to_numpy()) 
data.loc[1:,'ang_acc_y'] = (data['gyro_y'][1:].to_numpy() - data['gyro_y'][0:-1].to_numpy()) / (data['t'][1:].to_numpy() - data['t'][0:-1].to_numpy())
data.loc[1:,'ang_acc_z'] = (data['gyro_z'][1:].to_numpy() - data['gyro_z'][0:-1].to_numpy()) / (data['t'][1:].to_numpy() - data['t'][0:-1].to_numpy())

#%% 
# Subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10,4))

# Linear acceleration plot
ax1.plot(data['t'], data['acc_x'], label="x")
ax1.plot(data['t'], data['acc_y'], label="y")
ax1.plot(data['t'], data['acc_z'], label="z")
ax1.legend()
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Acceleration (g)")

# Angular velocity plot
ax2.plot(data['t'], data['gyro_x'], label="x")
ax2.plot(data['t'], data['gyro_y'], label="y")
ax2.plot(data['t'], data['gyro_z'], label="z")
ax2.legend()
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Angular Velocity (deg/s)")

# Angular acceleration plot
ax3.plot(data['t'], data['ang_acc_x'], label="x")
ax3.plot(data['t'], data['ang_acc_y'], label="y")
ax3.plot(data['t'], data['ang_acc_z'], label="z")
ax3.legend()
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Angular Acceleration (deg/s^2)")
plt.show()

#%% 
# 17.8 weight (idk units)
# 18in