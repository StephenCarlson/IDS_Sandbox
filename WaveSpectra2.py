import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
# import numpy as np
# from numpy.fft import fft, ifft

filename = 'SilverLake_Drift_Upright_11March2024.csv' 
dataframe = pd.read_csv(filename)

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html



plt.style.use('dark_background')


plt.subplot(2, 1, 1)

freq = 10
f, Pxx_den_gyro_y  = signal.periodogram(dataframe["IMU[0].GyrY"], freq)
f, Pxx_den_accel_z = signal.periodogram(dataframe["IMU[0].AccZ"], freq)
# f, Pxx_spec = signal.periodogram(dataframe["IMU[0].GyrY"], freq, 'blackmanharris', scaling='spectrum')

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html#scipy.signal.lfilter


b, a = signal.butter(3, 0.05)
# zi = signal.lfilter_zi(b, a)
# z, _ = signal.lfilter(b, a, Pxx_den_gyro_y, zi=zi*Pxx_den_gyro_y[0])
# z2, _ = signal.lfilter(b, a, z, zi=zi*z[0])
Pxx_den_gyro_y_filtered = signal.filtfilt(b, a, Pxx_den_gyro_y)

plt.semilogy(f, Pxx_den_gyro_y,          label='Raw Gyro Y deg/s (Pitch)',         marker=',', color='c', alpha=0.75)
plt.semilogy(f, Pxx_den_gyro_y_filtered, label='Filtered Gyro Y deg/s (Pitch)',    marker=',', color='r')
# plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice', 'filtfilt'), loc='best')

# plt.semilogy(f, Pxx_den_gyro_y,  label='Gyro Y deg/s (Pitch)')
# plt.semilogy(f, Pxx_den_accel_z, label='Accel Z m/s^2 (Surge)')
# plt.semilogy(f, Pxx_spec)
plt.ylim([1e-5, 1e1])
# plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [(deg/s)^2/Hz]')
plt.legend(loc=1, borderaxespad=1.)
plt.grid(alpha=0.2)


plt.subplot(2, 1, 2)


Pxx_den_accel_z_filtered = signal.filtfilt(b, a, Pxx_den_accel_z)
plt.semilogy(f, Pxx_den_accel_z,          label='Raw Accel Z m/s^2 (Heave)',         marker=',', color='y', alpha=0.75)
plt.semilogy(f, Pxx_den_accel_z_filtered, label='Filtered Accel Z m/s^2 (Heave)',    marker=',', color='r')

plt.ylim([1e-5, 1e1])
plt.ylabel('PSD [(m/s^2)^2/Hz]')
plt.xlabel('Frequency [Hz]')

# plt.axhline(0, linewidth=0.5, color='#ffffff')
plt.legend(loc=1, borderaxespad=1.)

plt.grid(alpha=0.2)
plt.suptitle("Filtered Wave Power Spectrum Density (PSD)")
plt.subplots_adjust(hspace=0.4)
plt.show()