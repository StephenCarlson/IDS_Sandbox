import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
# import numpy as np
# from numpy.fft import fft, ifft

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
plt.legend(loc=1, borderaxespad=1.)

plt.subplot(3, 1, 2)
plt.title("Accel")
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].AccX"],       label='Accel X (Surge)',       marker=',', color='#ff0000')
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].AccY"],       label='Accel Y (Sway)',        marker=',', color='#00ff00')
plt.plot(dataframe["timestamp(ms)"], dataframe["IMU[0].AccZ"],       label='Accel Z (Heave)',       marker=',', color='#0000ff')
plt.legend(loc=1, borderaxespad=1.)

plt.subplot(3, 1, 3)
# plt.title("Pose")
# plt.plot(dataframe["timestamp(ms)"], dataframe["XKF1[0].VN"],        label='Velocity - North',      marker=',', color='#ff0000')
# plt.plot(dataframe["timestamp(ms)"], dataframe["XKF1[0].VE"],        label='Velocity - East',       marker=',', color='#00ff00')
# plt.plot(dataframe["timestamp(ms)"], dataframe["XKF1[0].Yaw"],       label='Heading Angle',         marker=',', color='#0000ff')

# X = fft(dataframe["IMU[0].GyrY"])
# N = len(X)
# n = np.arange(N)
# T = N/10
# freq = n/T 

freq = 10
f, Pxx_den_gyro_y  = signal.periodogram(dataframe["IMU[0].GyrY"], freq)
f, Pxx_den_accel_z = signal.periodogram(dataframe["IMU[0].AccZ"], freq)
# f, Pxx_spec = signal.periodogram(dataframe["IMU[0].GyrY"], freq, 'blackmanharris', scaling='spectrum')
plt.semilogy(f, Pxx_den_gyro_y,  label='Gyro Y deg/s (Pitch)')
plt.semilogy(f, Pxx_den_accel_z, label='Accel Z m/s^2 (Surge)')
# plt.semilogy(f, Pxx_spec)
plt.ylim([1e-5, 1e1])
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [(Unit)^2/Hz]')
plt.legend(loc=1, borderaxespad=1.)

# plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
# plt.xlabel('Freq (Hz)')
# plt.ylabel('FFT Amplitude |X(freq)|')
# plt.xlim(0, 5)





# plt.axhline(0, linewidth=0.5, color='#ffffff')
# plt.legend(loc=1, borderaxespad=1.)

plt.grid(alpha=0.2)
plt.suptitle("Wave Spectra")
plt.show()