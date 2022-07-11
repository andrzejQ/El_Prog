#!/usr/bin/env python
import json
import csv
from collections import namedtuple

'''Standard D/K (CCIR) '''

Band = namedtuple("Band",'CSE Nr   F0   dF   ac1000')
bands = (          Band( 'C', 21, 470.0, 8.0,'C1021'),
                   Band( 'S',  9, 230.0, 8.0,'A1009'),
                   Band( 'E',  5, 174.0, 7.0,'A10081005'),
                   Band( 'S',  1, 110.0, 8.0,'A1001'),
)

def cTV (MHz_): 
  '''>>> [cTV(f) for f in \
( 99,  114,  170, 177.5, 226.5, 234,   466,   474,   858,  866)]
['?', 'S1', 'S8', 'E5', 'E12', 'S9', 'S38', 'C21', 'C69', 'C70']
'''                                                      # ^out of range
  try: MHz = float(MHz_ or 0)
  except ValueError: MHz = 0.0
  for b in bands:
    if MHz > b.F0 : break
  else: return '?'
  return b.CSE+str(int( b.Nr + (MHz-b.F0)/b.dF ))

def tvMHz (cTV_): 
  '''>>> [tvMHz(c) for c in \
(  '',  '?','S0',  'S1',  'S8',  'E5', 'E12',  'S9', 'S38', 'C21', 'C69','C70')]
[-0.0, -0.0, 0.0, 114.0, 170.0, 177.5, 226.5, 234.0, 466.0, 474.0, 858.0, 866.0]
'''                                                                     # ^out of range
  c = cTV_[:1].upper();
  try: nr = int(cTV_[1:])
  except ValueError: return -0.0
  cNr = c.replace('S','A').replace('E','A1008')+str(1000+nr)
  #     'A....' < 'C....',   'A1008' < 'A1008....' < 'A1009'
  for b in bands:
    if cNr >= b.ac1000 : break
  else: return 0.0
  # print(f'''{cTV_=}, {cNr=}, {b.ac1000=}''')
  return (nr - b.Nr + 0.5)*b.dF + b.F0
  
if __name__ == "__main__":
  import doctest
  doctest.testmod()

