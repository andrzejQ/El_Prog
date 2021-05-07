#!/usr/bin/env python -i

import csv
from collections import namedtuple
with open('x.csv', newline='', encoding='utf-8-sig') as csvF: #read
  reader = csv.reader(csvF, delimiter=';')
  nTuple = namedtuple('nTuple', next(reader))  # get names from column headers
  print(f'{nTuple.__doc__}\n') #$# np.: nTuple(col1,col2,col3)
  arr = []
  # map(nTuple._make, reader): - ale jest sporo zbędnych spacji
  for row in reader: 
    r = nTuple._make([x.strip() for x in row])
    arr += [r]
print(arr)

# write:
nTuple = namedtuple('nTuple', ['col1', 'col2', 'col3'])
with open('y.csv','w',newline='',encoding='utf-8-sig') as csvF:
  writer = csv.writer(csvF, delimiter=';', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(nTuple._fields) # write csv header
  for row in arr:
    writer.writerow(row)

## nTuple -> dict
di = row._asdict()
print(1, di)                   #1 OrderedDict([('col1', ...
print(2, dict(di))             #2 {'col1':

## dict -> nTuple
d = {'col1':'xx', 'col2':'yy', 'col3':'zz'}
print(3, nTuple(**d))          #3 nTuple(col1='xx', col2='yy', col3='zz')
di = {'col1':'xx', 'col3':'zz'} # missing 'col2'
for x in set(nTuple._fields).difference(di.keys()): di[x] = None
print(4, nTuple(**di))         #4 nTuple(col1='xx', col2=None, col3='zz')
di = {'col1':'xx', 'col3':'zz'}
print(5, [di.get(k,'') for k in nTuple._fields] ) #5 ['xx', '', 'zz']
