import requests 
import json
import time
from datetime import datetime 


#Setup
startDatetime = datetime.now()
filename = "logfile-" + startDatetime.strftime("%Y%m%d %H-%M-%S")
with open('%s.txt' % filename, mode='a') as file:
    file.write('rssi, rscp, ecio, rsrp, rsrq, bars, sinr, end, datetime\n') #mind the spaces after commas!
url = 'http://10.74.36.1/api/model.json?internalapi=1'
durationToLog = 12*60 #minutes
timeCheck = True
print('**************************************\n')
print('*\n')
print('*    Hello!   Running getData.py     *\n')
print('*\n')
print('**************************************')

while timeCheck:
    
    #go grab the JSON data and load it into a dict
    response = requests.get(url)
    r = response.json()

    #grab only the pertinent data and add current time
    data = r['wwan']['signalStrength']
    data['datetime'] = datetime.now().isoformat() #don't bother with now_string at all
    logline = str(list(data.values())).strip('[]')
    
    logline = logline.replace("'","")  #why can't i log the time without the single quotes?  i makes cvs_read choke on the datetime
    
    

    #write JSON formatted data to the logfile and close it
    with open('%s.txt' % filename, mode='a') as file:
        file.write('%s\n' %logline)
        #json.dump(data, file)
        file.close

    timeCheck = (datetime.now() - startDatetime ).total_seconds() < durationToLog*60
    time.sleep(1)
    
print('All Done!')
#(r['wwan']['signalStrength'])
#print(r['wwan']['signalStrength']['sinr'])
