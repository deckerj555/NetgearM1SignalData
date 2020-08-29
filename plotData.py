#py -m pip install pandas

import matplotlib.pyplot as plt
import pandas
import numpy


pathToSaw = ['logfile-20200815 11-02-38.txt']; commentsSaw = ['1/4 antennae on tablesaw and paint can; first with real datetimes']
pathToSaw.append('logfile-20200816 10-11-21.txt'); commentsSaw.append('2/4 antennae on tablesaw and paint can; first with real datetimes')
pathToSaw.append('logfile-20200817 07-43-27.txt'); commentsSaw.append('3/4 antennae on tablesaw and paint can; first with real datetimes')
pathToSaw.append('logfile-20200829 10-59-30.txt'); commentsSaw.append('4/4 after a couple weeks, back to the tablesaw and paint can')

pathToNone = ['logfile-20200817 19-26-06.txt']; commentsNone = ['1/6 no external antennae']
pathToNone.append('logfile-20200818 12-45-21.txt'); commentsNone.append('2/6 no external antennae')
pathToNone.append('logfile-20200819 11-59-43.txt'); commentsNone.append('3/6 no external antennae')
pathToNone.append('logfile-20200819 22-27-55.txt'); commentsNone.append('4/6 no external antennae')
pathToNone.append('logfile-20200821 09-26-18.txt'); commentsNone.append('5/6 no external antennae')
pathToNone.append('logfile-20200821 21-21-26.txt'); commentsNone.append('6/6 no external antennae')

pathToPanel = ['logfile-20200822 10-06-56.txt']; commentsPanel = ['1/5 antennae on paint can & electrical panel']
pathToPanel.append('logfile-20200822 23-54-03.txt'); commentsPanel.append('2/5 antennae on paint can & electrical panel')
pathToPanel.append('logfile-20200823 11-54-14.txt'); commentsPanel.append('3/5 antennae on paint can & electrical panel')
pathToPanel.append('logfile-20200824 00-10-26.txt'); commentsPanel.append('4/5 antennae on paint can & electrical panel')
pathToPanel.append('logfile-20200824 22-59-57.txt'); commentsPanel.append('5/5 antennae on paint can & electrical panel')

#gotta manually change the pathToNone, pathToPanel, pathToSaw
for pathToFile in pathToPanel:
    with open(pathToFile, 'r') as file:
        #TODO need to parse both ', ' and ',' delimiters; tell read_csv() how many cols to expect
        df = pandas.read_csv(pathToFile, parse_dates=['datetime'], sep=', ', engine='python')
    print('Loaded ' + pathToFile)
    #window size should be 60 for 1 min, but it takes 1.3s for the loop to run.
    df['avg_1min'] = df.iloc[:,6].rolling(window=50).mean() 

    #mean and stdev
    avgInst = df['sinr'].mean()
    sigmaInst = df['sinr'].std()


    p = plt.figure(num=1, figsize=(12,8))
    plt.grid(True)
    #plt.plot('datetime', 'sinr', data=df, label=('Inst. $\mu$ = {:2.2f}'.format(avgInst) + ', ' + '1$\sigma$ = {:2.2f}'.format(sigmaInst)))
    #plt.plot('datetime', 'avg_1min', data=df, label='1min Avg')
    #plt.plot('datetime', 'bars', data=df, label='Bars')
    #plt.plot('sinr', data=df, label=('Inst. $\mu$ = {:2.2f}'.format(avgInst) + ', ' + '1$\sigma$ = {:2.2f}'.format(sigmaInst)))
    plt.plot('avg_1min', data=df, label=('Inst. $\mu$ = {:2.2f}'.format(avgInst) + ', ' + '1$\sigma$ = {:2.2f}'.format(sigmaInst)))

plt.legend()
#plt.title(pathToFile + '\n' + comments)

plt.title('Antennae on Paint Can and Electrical Panel')
#plt.title('Antennae on Tablesaw and Paint Can')
plt.ylabel('SINR (dBm)')
#plt.xlabel('HH:MM:SS')
plt.xlabel('Sample $N^o$')
plt.ylim(0, 8)
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
