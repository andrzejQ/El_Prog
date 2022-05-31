import csv
from collections import namedtuple
''''
Kanały i częstotliwości - Standard D/K (CCIR) - wynik w "tvMHz.csv"
'''
tvMHzcsv = 'tvMHz.csv'
maxMHz = 862

Band = namedtuple("Band", 'CSE Nr F0 dF')
bands = (          Band( 'C',21,470.0,8.0 ),
                   Band( 'S', 9,230.0,8.0 ),
                   Band( 'E', 5,174.0,7.0 ),
                   Band( 'S', 1,110.0,8.0 )
)
tvMHz = [ ['C','MHz'] ]
for j in range(len(bands)-1, -1, -1):
  maxF = maxMHz if j == 0 else bands[j-1].F0
  b = bands[j]
  MHz = b.F0+b.dF/2
  i = b.Nr
  while (MHz < maxF):
    tvMHz += [ [f'''{b.CSE}{i}''', f'''{MHz:g}'''] ]
    i += 1
    MHz += b.dF

print('- zob.',tvMHzcsv)
with open(tvMHzcsv,'w',newline='',encoding='utf-8-sig') as csvF:
  csvWr = csv.writer(csvF, delimiter=';',quoting=csv.QUOTE_MINIMAL)
  csvWr.writerows(tvMHz)
