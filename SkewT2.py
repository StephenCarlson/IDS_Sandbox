import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import add_metpy_logo, SkewT
from metpy.units import units

# filename = '23March2024.csv'
filename = '27April2024.csv'
# timestamp(ms),GPS.Alt,WIND.Mag,WIND.Dir,BARO.Alt,BARO.Press,ARSP.Temp
df = pd.read_csv(filename)

# Change default to be better for skew-T
# plt.rcParams['figure.figsize'] = (9, 9)

p = df['BARO.Press'].values * units.Pa
T = df['ARSP.Temp'].values * units.degC
Td = np.zeros_like(df['ARSP.Temp'].values) # df['ARSP.Temp'].values * units.degC
wind_speed = df['WIND.Mag'].values * units.knots
wind_dir = df['WIND.Dir'].values * units.degrees
u, v = mpcalc.wind_components(wind_speed, wind_dir)


skew = SkewT()

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(p, T, 'r')
skew.plot(p, Td, 'g')
skew.plot_barbs(p, u, v)

# Set some better labels than the default
skew.ax.set_xlabel('Temperature (\N{DEGREE CELSIUS})')
skew.ax.set_ylabel('Pressure (mb)')

# Add the relevant special lines
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()
skew.ax.set_ylim(1000, 100)
skew.ax.set_xlim(10, 30)

fig = plt.gcf()
# plt.suptitle("Silver Knolls - 23 March 2024")
plt.suptitle("Gardnerville - 27 April 2024")
plt.show()
