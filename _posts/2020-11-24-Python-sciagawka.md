---
layout: post
title:  "Python ściągawka"
date:   2020-11-24 06:55:00 +0100
categories: Programowanie
---

Moja ściągawka Python 3.6+ (zapewne tylko do użytku własnego) ... 

1 . Pliki:

````py
with open('a.txt', encoding='utf-8-sig') as txt: # 'utf-8', 'cp1250'
  a = txt.read().splitlines()

with open('a.txt','w',newline='\r\n',encoding='utf-8-sig') as txt:
  txt.write('\n'.join(a))

with open('a.txt','w',newline='',encoding='utf-8-sig') as txt: print(s, file=txt)
````
````py
import json # load(file) loads(str)
with open('d.json', 'r', encoding='utf-8') as fj:
  d = json.load(fj) # ordered dict py 3.7

json.dumps({'4': 5, '6': 7}, ensure_ascii=False, indent=2) #-> str
````
````py
import csv
with open('x.csv','r',newline='',encoding='utf-8-sig') as csvF:
  csvRd = csv.reader(csvF, delimiter=';')
  csvHeader = next(csvRd)
  r = next(csvRd)

with open('y.csv','w',newline='',encoding='utf-8-sig') as csvF:
  csvWr = csv.writer(csvF, delimiter=';',quoting=csv.QUOTE_MINIMAL)
  csvWr.writerow(['col1','col2','col3'])
  csvWr.writerows([k,v1,v2] for k,[v1,v2] in dic.items())

from collections import namedtuple 
with open('xCsv', newline='', encoding='utf-8-sig') as csvF:
  reader = csv.reader(csvF, delimiter=';')
  nTuple = namedtuple('nTuple', next(reader))  # get names from column headers
  print(f'{nTuple.__doc__}\n') #$# np.: nTuple(col1,col2,col3)
  arr = []
  # map(nTuple._make, reader): - ale jest sporo zbędnych spacji
  for row in reader: 
    r = nTuple._make([x.strip() for x in row])
    arr += [r]

````
````py
x = set( open(lista.txt,'r',encoding='utf-8-sig').read().upper().splitlines() )
````


2 . str:

````py
f'x: {x!r}'; 'x: '+repr(x)

print ('opis: ',end ='')
print (x)

````

Linki 1:

* [namedtuple()](https://docs.python.org/3/library/collections.html#collections.namedtuple)  -> docs.python.org/3
<style> pre code {font-size: smaller;} </style>

