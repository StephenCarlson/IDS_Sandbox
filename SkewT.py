import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
# import numpy as np
# from numpy.fft import fft, ifft

filename = '23March2024.csv'
# timestamp(ms),GPS.Alt,WIND.Mag,WIND.Dir,BARO.Alt,BARO.Press,ARSP.Temp
dataframe = pd.read_csv(filename)

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html


# dataframe['PowerIn'] = dataframe["Solar mA"] * dataframe["Solar 10mV"] / 1000.0
# dataframe['PowerOut'] = dataframe["Main mA"] * dataframe["Main 10mV"] / 1000.0
# dataframe['CurrTotal'] = (dataframe["Main mA"].cumsum())/3600.0

plt.style.use('dark_background')

plt.subplot(2, 1, 1)
plt.title("Wind")
plt.plot(dataframe["timestamp(ms)"], dataframe["WIND.Mag"],       label='Wind Velocity (m/s)',     marker=',', color='#ff0000')
plt.plot(dataframe["timestamp(ms)"], dataframe["WIND.Dir"],       label='Wind Direction',          marker=',', color='#0000ff')
plt.legend(loc=1, borderaxespad=1.)



sorted_df = dataframe.sort_values(by='BARO.Press', ascending=True)



plt.subplot(2, 1, 2)
plt.title("Pressure Sorted")
plt.plot(dataframe["WIND.Mag"],  dataframe["BARO.Press"],      label='Wind Velocity (m/s)',       marker=',', color='#ff0000')
# plt.plot(dataframe["WIND.Dir"],  dataframe["BARO.Press"],      label='Wind Direction',            marker=',', color='#0000ff')
plt.plot(dataframe["ARSP.Temp"], dataframe["BARO.Press"],      label='Temperature (C)',           marker=',', color='#ccaa00')
plt.gca().invert_yaxis()
plt.legend(loc=1, borderaxespad=1.)

plt.grid(alpha=0.2)
plt.suptitle("Skew-T Log-P")
plt.show()