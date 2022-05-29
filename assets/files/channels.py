import json 
import csv
from collections import namedtuple
''''
Po wyszukaniu kanałów w programie SichboPVR -> https://sichbopvr.com/pl-pl/
powstaje plik "%ProgramData%\SichboPVR4\service-channels.json",
z aktualną informacją o dostępnych kanałach DVB-T/T2 - wynik w "chInfo.csv"
'''
chInfocsv = 'chInfo.csv'
with open(r'C:\ProgramData\SichboPVR4\service-channels.json', 'r', encoding='utf-8') as fj:
  d = json.load(fj) 

def cTV (MHz): 
  '''cTV(474) -> "C21"; cTV(177.5) -> "E5"'''
  MHz = float(MHz)
  Band = namedtuple("Band", 'CSE Nr F0 dF')
  bands = (          Band( 'C',21,470.0,8.0 ),
                     Band( 'S', 9,230.0,8.0 ),
                     Band( 'E', 5,174.0,7.0 ),
                     Band( 'S', 1,110.0,8.0 )
  )
  for b in bands:
    if MHz > b.F0 : break
  else: return '?'
  return b.CSE+str(int( b.Nr + (MHz-b.F0)/b.dF ))
  
Transponders = {}
for t in d['Transponders']:
  transp = t.get('Info').split(' ')
  ch = cTV(transp[1])
  Transponders[t['UID']] = [ch]+transp
# Transponders/1?/Info  #  "Info": "dvbt2 690 8 -1",

# Channels/3?/Name/s/0/v  #  Science Poland HD
# Channels/3?/Streams/0?/Video/Height  #  1080
chInfo = []
for chn in d['Channels']:
  nm = chn.get('Name')
  if nm:
    chName = nm.get('s')[0].get('v')
    h = 0
    for strm in chn.get('Streams') or []:
      h = strm.get('Video',{}).get('Height',0)
      if h: break
    chInfo += [ [chName]+ [h] + Transponders.get(chn.get('TransponderUID')) ]

print(len(chInfo),'kanałów - zob.',chInfocsv)

with open(chInfocsv,'w',newline='',encoding='utf-8-sig') as csvF:
  csvWr = csv.writer(csvF, delimiter=';',quoting=csv.QUOTE_MINIMAL)
  csvWr.writerow( ['nazwa','h','C','t2','MHz','8','1'] )
  csvWr.writerows(chInfo)
  