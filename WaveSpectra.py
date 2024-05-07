import pandas as pd
import matplotlib.pyplot as plt

filename = 'SilverLake_Drift_Upright_11March2024.csv' 
dataframe = pd.read_csv(filename)

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html


# dataframe['PowerIn'] = dataframe["Solar mA"] * dataframe["Solar 10mV"] / 1000.0
# dataframe['PowerOut'] = dataframe["Main mA"] * dataframe["Main 10mV"] / 1000.0
# dataframe['CurrTotal'] = (dataframe["Main mA"].cumsum())/3600.0


plt.style.use('dark_background')

plt.subplot(3, 1, 1)
plt.title("Gyro")
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].GyrX"],       label='Gyro X (Roll)',         marker=',', color='#ff0000')
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].GyrY"],       label='Gyro Y (Pitch)',        marker=',', color='#00ff00')
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].GyrZ"],       label='Gyro Z (Yaw)',          marker=',', color='#0000ff')

plt.subplot(3, 1, 2)
plt.title("Accel")
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].AccX"],       label='Accel X (Roll)',        marker=',', color='#ff0000')
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].AccY"],       label='Accel Y (Pitch)',       marker=',', color='#00ff00')
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].AccZ"],       label='Accel Z (Yaw)',         marker=',', color='#0000ff')

plt.subplot(3, 1, 3)
plt.title("Pose")
plt.plot(dataframe["timestamp(ms)"], dataframe["XKF1[0].VN"],        label='Velocity - North',      marker=',', color='#ff0000')
plt.plot(dataframe["timestamp(ms)"], dataframe["XKF1[0].VE"],        label='Velocity - East',       marker=',', color='#00ff00')
plt.plot(dataframe["timestamp(ms)"], dataframe["XKF1[0].Yaw"],       label='Heading Angle',         marker=',', color='#0000ff')
# plt.plot(dataframe["timestamp(ms)"], dataframe["Main mA"],           label='Batt mA',                      color='#00ff00')
# plt.plot(dataframe["timestamp(ms)"], dataframe["CurrTotal"],         label='Accum Batt mA',                color='#ff5500', linestyle='dashdot')
# plt.plot(dataframe["timestamp(ms)"], dataframe["Main 10mV"],         label='Batt 10mV',                    color='#00aaff')
# plt.plot(dataframe["timestamp(ms)"], dataframe["Accel-Z milliGee"],  label='Z-Accel mG',       marker='.', color='#ff00ff')
# plt.plot(dataframe["timestamp(ms)"], dataframe["IMU Temp 10mC"]*1.0, label='IMU Temp 10mC',    marker='.', color='#00ffff')
# plt.plot(dataframe["timestamp(ms)"], dataframe["MPPT Setpoint"],     label='MPPT Setpoint',                color='#7f7f7f')


plt.axhline(0, linewidth=0.5, color='#ffffff')
plt.legend(loc=1, borderaxespad=1.)

plt.grid(alpha=0.2)
plt.suptitle("Wave Spectra")
plt.show()