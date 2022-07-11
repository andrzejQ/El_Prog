#!/usr/bin/env python -i
import xmltodict
import json
import csv
import os
from DTV_DK_CCIR import cTV

listaProgramów = 'Programlist_d_1'
with open(f'''{os.getenv('localAppData')}\\HiDTV\\{listaProgramów}.xml''') as fd: # %localAppData%\HiDTV\
  di = xmltodict.parse(fd.read()) # di JSON like
# {
#   "p1": {
#     "@ChannelName": "TV HD",
#      ...
#     "@Freqency": "474000",
d = []
hdr = {} # nagłówek z unikalnymi polami
for k,v in di['root'].items():
  MHz = int(v['@Freqency'])/1000.0
  d += [{'p':k, 'MHz':f'{MHz:g}', 'canal':cTV(MHz), **v}]
  hdr = dict.fromkeys(list(hdr.keys()) + list(d[-1].keys())) 
  # py 3.7+ - uwzględnij (zachowując kolejność) pojawiające się nowe klucze w ostatnio dodanym d[-1]

print(json.dumps(d, ensure_ascii=False, indent=2))
print(hdr)

#csvHeader=hdr.keys()
csvHeader=list(hdr.keys())[:4] # lub [:26] dalsze dane są raczej mniej istotne...
with open(f'''{listaProgramów}.csv''','w',newline='',encoding='utf-8-sig') as csvF:
  csvDiWr=csv.DictWriter(csvF,csvHeader, delimiter=';',quoting=csv.QUOTE_MINIMAL,extrasaction='ignore')
  csvDiWr.writeheader()
  csvDiWr.writerows(d)

print(f'''
Zobacz: .\\{listaProgramów}.csv
''')