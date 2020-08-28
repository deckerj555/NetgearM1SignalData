#py -m pip install pandas

import matplotlib.pyplot as plt
#import json
#import csv
import pandas
import numpy

#pathToFile = 'logfile-20200815 10-59-29.txt' ; comments = 'test file with real datetime objects'
#pathToFile = 'logFile-logfile-20200806 12-06-08.csv'; comments = 'baseline 1/3, antenna on electrical panel and paint can (pic on phone)'
#pathToFile = 'logFile-logfile-20200807 13-52-13.csv'; comments = 'baseline 3/3'
#pathToFile = 'logfile-20200808 10-01-20.txt' # eh?
#pathToFile = 'logfile-20200808 22-32-43.txt'; comments = '1/4 removed external antennae; internal antennae only'
#pathToFile = 'logfile-20200809 10-33-08.txt'; comments = '2/4 of no external antennae'
#pathToFile = 'logfile-20200809 23-08-07.txt'; comments = '3/4 no external anteannae PM -> AM'
#pathToFile = 'logfile-20200810 11-32-53.txt'; comments = '4/4 no external antennae AM -> PM'
#pathToFile = 'logfile-20200811 19-30-56.txt'; comments = '1/? baseline; antenna on panel and paint can pic (8/6)'
#pathToFile = 'logfile-20200812 08-11-24.txt'; comments = '2/? baseline; AM -> PM'
#pathToFile = 'logfile-20200812 20-36-01.txt'; comments = '3/? baseline PM - > AM'
#pathToFile = 'logfile-20200813 08-59-11.txt'; comments = '4/? baseline AM -> PM'
#pathToFile = 'logfile-20200813 22-50-28.txt'; comments = '5/5 baseline PM -> AM'
#pathToFile = 'logfile-20200814 18-40-18.txt'; comments = '1/1 antennae on tablesaw and paint can; before real datetimes'


#pathToFile = 'logfile-20200815 11-02-38.txt'; comments = '2/3 antennae on tablesaw and paint can; first with real datetimes'
#pathToFile = 'logfile-20200816 10-11-21.txt'; comments = '3/3 antennae on tablesaw and paint can; first with real datetimes'
#pathToFile = 'logfile-20200817 07-43-27.txt'; comments = '4/3 antennae on tablesaw and paint can; first with real datetimes'
#pathToFile = 'logfile-20200817 19-26-06.txt'; comments = '1/6 no external antennae'
#pathToFile = 'logfile-20200818 12-45-21.txt'; comments = '2/6 no external antennae'
#pathToFile = 'logfile-20200819 11-59-43.txt'; comments = '3/6 no external antennae'
#pathToFile = 'logfile-20200819 22-27-55.txt'; comments = '4/6 no external antennae'
#pathToFile = 'logfile-20200821 09-26-18.txt'; comments = '5/6 no external antennae'
#pathToFile = 'logfile-20200821 21-21-26.txt'; comments = '6/6 no external antennae'
#pathToFile = 'logfile-20200822 10-06-56.txt'; comments = '1/5 antennae on paint can & electrical panel'
#pathToFile = 'logfile-20200822 23-54-03.txt'; comments = '2/5 antennae on paint can & electrical panel'
#pathToFile = 'logfile-20200823 11-54-14.txt'; comments = '3/5 antennae on paint can & electrical panel'
#pathToFile = 'logfile-20200824 00-10-26.txt'; comments = '4/5 antennae on paint can & electrical panel'
pathToFile = 'logfile-20200824 22-59-57.txt'; comments = '5/5 antennae on paint can & electrical panel'


with open(pathToFile, 'r') as file:
    #TODO need to parse both ', ' and ',' delimiters; tell read_csv() how many cols to expect
    df = pandas.read_csv(pathToFile, parse_dates=['datetime'], sep=', ', engine='python')

#window size should be 60 for 1 min, but it takes 1.3s for the loop to run.
df['avg_1min'] = df.iloc[:,6].rolling(window=50).mean() 


#mean and stdev
avgInst = df['sinr'].mean()
sigmaInst = df['sinr'].std()


p = plt.figure(1)
plt.grid(True)
plt.plot('datetime', 'sinr', data=df, label=('Inst. $\mu$ = {:2.2f}'.format(avgInst) + ', ' + '1$\sigma$ = {:2.2f}'.format(sigmaInst)))
plt.plot('datetime', 'avg_1min', data=df, label='1min Avg')
#plt.plot('datetime', 'bars', data=df, label='Bars')
#plt.plot('sinr', data=df, label=('Inst. $\mu$ = {:2.2f}'.format(avgInst) + ', ' + '1$\sigma$ = {:2.2f}'.format(sigmaInst)))
#plt.plot('avg_1min', data=df, label='1min Avg')
plt.legend()
plt.title(pathToFile + '\n' + comments)
plt.ylabel('SINR (dBm)')
plt.xlabel('HH:MM:SS')
plt.show()


plt.figure(2)
plt.grid(True)
plt.plot('datetime', 'rsrq', data=df, label='RSRQ')
plt.plot('datetime', 'rsrp', data=df, label='RSRP')
plt.plot('datetime', 'rssi', data=df, label='RSSI')
plt.legend()
plt.title(pathToFile + '\n' + comments)
plt.ylabel('RSRQ & RSRP (dBm)')
plt.show()
'''
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot('datetime', 'rsrq', data=df, label='RSRQ')
ax1.plot('datetime', 'rsrp', data=df, label='RSRP')
ax2.plot('datetime', 'rssi', data=df, label='RSSI')
ax1.set_xlabel('HH:MM:SS')
ax1.set_ylabel('RSRP & RSRP (dBm)')
ax2.set_ylabel('RSSI (dBm)')
plt.show()
'''


#avg1min = df['avg_1min'].mean()
#sigma1min = df['avg_1min'].std()


print('done\n')
print('Filename = ', pathToFile)
print('Average SNR = ', avgInst)
print('1sigma = ',  sigmaInst)
