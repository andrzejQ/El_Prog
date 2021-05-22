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

JSON

````py
import json # load(file) loads(str)
with open('d.json', 'r', encoding='utf-8') as fj:
  d = json.load(fj) # ordered dict py 3.7

json.dumps({'4': 5, '6': 7}, ensure_ascii=False, indent=2) #-> str
````

Dla dość prostych struktur json, gdzie mamy listę słowników można uzyskać "hybrydowy format" json/csv, który ułatwia wkopiowanie takiego tekst do arkusza kalkulacyjnego (rozdzielany '\t'). Można też zastosować kodowanie `UTF-16 (=UCS-2) Little Endian with BOM`, tj. `encoding='utf-16'` i od razu otwierać w arkuszu kalk., albo wcześniej dodać rozszerzenie `CSV`.

````py
with open('d.json', 'w', encoding='utf-8') as fj:
    fj.write(json.dumps(di, ensure_ascii=False, separators=(',', ':\t')).replace('},','},\n'))
````
CSV

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
  
csvHeader=['col1','col2','col3'] # dicts = [ {'col1':...}, ...]
with open('y.csv','w',newline='',encoding='utf-8-sig') as csvF:
  csvDiWr=csv.DictWriter(csvF,csvHeader, delimiter=';',quoting=csv.QUOTE_MINIMAL)
  csvDiWr.writeheader()
  csvDiWr.writerows(dicts)
````

````py
import csv
#read
from collections import namedtuple
with open('x.csv', newline='', encoding='utf-8-sig') as csvF:
  reader = csv.reader(csvF, delimiter=';')
  nTuple = namedtuple('nTuple', next(reader))  # get names from column headers
  print(1, nTuple.__doc__) #$# np.:1 nTuple(col1,col2,col3)
  arr = [ nTuple._make(row) for row in reader ] 
print(2, f'{arr}'.replace('),','),\n')) #$#2 [nTuple(col1=...

# write:
nTuple = namedtuple('nTuple', ['col1', 'col2', 'col3'])
with open('y.csv','w',newline='',encoding='utf-8-sig') as csvF:
  writer = csv.writer(csvF, delimiter=';', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(nTuple._fields) # write csv header
  for row in arr:
    writer.writerow(row)

## nTuple -> dict
di = row._asdict()
print(3, di)                   #3 OrderedDict([('col1', ...
print(4, dict(di))             #4 {'col1':

## dict -> nTuple
d = {'col1':'xx', 'col2':'yy', 'col3':'zz'}
print(5, nTuple(**d))          #5 nTuple(col1='xx', col2='yy', col3='zz')
di = {'col1':'xx', 'col3':'zz'} # missing 'col2'
for x in set(nTuple._fields).difference(di.keys()): di[x] = None
print(6, nTuple(**di))         #6 nTuple(col1='xx', col2=None, col3='zz')
di = {'col1':'xx', 'col3':'zz'}
print(7, [di.get(k,'') for k in nTuple._fields] ) #7 ['xx', '', 'zz']
````

````py
x = set( open(lista.txt,'r',encoding='utf-8-sig').read().upper().splitlines() )
````


2 . Str

````py
f'x: {x!r}'; 'x: '+repr(x)

print ('opis: ',end ='')
print (x)

x or '' - gdy x=None albo jest łańcuchem, to zamiast None jest ''
' '.join(filter(None,[di.get(k) for k in ['k1','k2',...]])) - scal, pomijając None

x = x.replace('a','aa') # wszystkie wystąpienia
x = x.replace('a','A',1) # 1 wystąpienie
````

````py
import re
match = re.search(r'(\d+).*?(\d+)','x=01 y=02 z=03 z4=04') #nie re.match, które tylko szuka na pocz.
>>> match[0],match[1],match[2] #znajduje 1-sze wystąpienie
('01 y=02', '01', '02')
x=re.sub(r'\S+?(\d+)',r'\1','x=01 y=02 z=03 z4=04')
>>> x   # zamienia wszystkie wystąpienia
'01 02 03 404'
````

3 . List, Tuple

````py
>>> len(['abc','def',]) # przecinek na końcu jest ignorowany
2
>>> len(('abc',)) # 1-el. krotka
1
````

4 . Konwersja typów

````py
>>> [1*x for x in (True, False, '', [])]
[1, 0, '', []]

>>> '-'.join([])
''
````

5 . Zmienne globalne, pamięć stanu

"
W Pythonie zmienne, do których istnieją odwołania tylko wewnątrz funkcji, są niejawnie globalne. Jeśli zmiennej przypisano wartość w dowolnym miejscu w treści funkcji, przyjmuje się, że jest to wartość lokalna, chyba że jawnie zadeklarowano ją jako globalną `global x`.
"  
Ta zasada nie dotyczy modyfikowalnych (mutable) typów zmiennych, jak `[], {}, class`, bo wewnątrz funkcji mamy zawsze tylko referencję do zmiennej (czyli przypisanie wartości nie wymaga dekl. `global`)

````py
_G1 = None
def f1():
  global _G1
  _G1=1
f1();  print(_G1) # 1
#-------------
_G2 = [None]
def f2():
  _G2[0]=22
f2();  print(_G2[0]) # 22
#-------------
class GVars: pass
_gv = GVars()
_gv.G3 = None;
def f3():
  _gv.G3=333
f3();  print(_gv.G3) # 333
````

Gdy nie jest to uzasadnione to nie używaj zmiennych globalnych (wartości wynikowe funkcji najlepiej zwracać jako krotkę).

Podobnie unikaj w funkcjach wartości domyślnych modyfikowalnych (mutable), jak `[], {}, ...`, gdyż takie wartości domyślne są inicjowane raz - przy pierwszym wywołaniu funkcji i są pamiętane przy kolejnych wywołaniach. Można tego użyć do pamiętania stany z poprzedniego wywołania - [zob.>>](https://docs.python.org/3.9/faq/programming.html#why-are-default-values-shared-between-objects)
````py
def expensive(arg1, arg2, *, _cache={}):  # po `*` mogą wystąpić tylko pary `k=v`
  if (arg1, arg2) in _cache:
    return _cache[(arg1, arg2)]

  result = ... expensive computation ...  # Calculate the value
  _cache[(arg1, arg2)] = result           # Store result in the cache
  return result
````


- - - - - -


Linki 1:

* [namedtuple()](https://docs.python.org/3/library/collections.html#collections.namedtuple)  -> docs.python.org/3/
* [testCsvNamedtuple.py (.zip)]({{ site.baseurl }}/assets/files/testCsvNamedtuple.zip "testCsvNamedtuple.zip") 

Linki 5:
* [create module-wide vars](https://stackoverflow.com/questions/1977362/how-to-create-module-wide-variables-in-python)  -> stackoverflow.com/questions
* [global variables in a function](https://stackoverflow.com/questions/423379/using-global-variables-in-a-function)  -> stackoverflow.com/questions
* [default values shared between objects](https://docs.python.org/3.9/faq/programming.html#why-are-default-values-shared-between-objects)  -> docs.python.org/3.9/faq

Linki:
* [Python - programing FAQ](https://docs.python.org/3/faq/programming.html)  -> docs.python.org/3/faq/


<style> pre code {font-size: smaller;} </style>

