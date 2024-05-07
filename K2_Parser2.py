import pandas as pd
import matplotlib.pyplot as plt

# filename = 'K2MPPT_DumpCycle12a.csv'
# filename = 'K2MPPT_22Nov2023_0000_14hr.log'
# filename = 'K2MPPT_1Dec2023_0010PST_198hr.log'
# filename = 'K2MPPT_28Feb2024.csv' 
# filename = 'K2MPPT_27Feb2024-FullSet.csv' 
# filename = 'K2MPPT_18Jan2024_2230PST_980hr.log' 
# filename = 'K2MPPT_7March2024_Debugging2.log' 
# filename = 'K2MPPT_11March2024_0000PST_17hr.log' 
filename = 'K2MPPT_11March2024_0000PST_63hr.log' 
dataframe = pd.read_csv(filename)

# dataframe["TS"] = pd.to_datetime(dataframe['DSTM32 Time sec']) # , format="%Y-%m-%d")

# fig, ax = plt.subplots()
# ax.plot(dataframe["STM32 Time sec"], dataframe["Solar mA"])
# ax.plot(dataframe["STM32 Time sec"], dataframe["Temperature ADC"])
# fig.autofmt_xdate()
# fig.show()

dataframe['PowerIn'] = dataframe["Solar mA"] * dataframe["Solar 10mV"] / 1000.0
dataframe['PowerOut'] = dataframe["Main mA"] * dataframe["Main 10mV"] / 1000.0
dataframe['CurrTotal'] = (dataframe["Main mA"].cumsum())/3600.0

# plt.plot(dataframe["STM32 Time sec"], marker='.', markersize=2.0, linestyle='None')

plt.style.use('dark_background')
plt.plot(dataframe["STM32 Time sec"], dataframe["PowerIn"],           label='Solar Power mW',               color='#cccc00')
# plt.plot(dataframe["STM32 Time sec"], dataframe["PowerOut"])
plt.plot(dataframe["STM32 Time sec"], dataframe["Solar 10mV"],        label='Solar 10mV',                   color='#00cc00')
plt.plot(dataframe["STM32 Time sec"], dataframe["Main mA"],           label='Batt mA',                      color='#ff0000')
plt.plot(dataframe["STM32 Time sec"], dataframe["CurrTotal"],         label='Accum Batt mA',                color='#ff5500', linestyle='dashdot')
plt.plot(dataframe["STM32 Time sec"], dataframe["Main 10mV"],         label='Batt 10mV',                    color='#00aaff')
plt.plot(dataframe["STM32 Time sec"], dataframe["Accel-Z milliGee"],  label='Z-Accel mG',       marker='.', color='#ff00ff')
plt.plot(dataframe["STM32 Time sec"], dataframe["IMU Temp 10mC"]*1.0, label='IMU Temp 10mC',    marker='.', color='#00ffff')
plt.plot(dataframe["STM32 Time sec"], dataframe["MPPT Setpoint"],     label='MPPT Setpoint',                color='#7f7f7f')
plt.axhline(0, linewidth=0.5, color='#ffffff')
plt.legend(loc=1, borderaxespad=1.)

plt.grid(alpha=0.2)
plt.show()