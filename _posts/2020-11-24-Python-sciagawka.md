---
layout: post
title:  "Python ściągawka"
date:   2020-11-24 06:55:00 +0100
categories: Programowanie
---

Moja ściągawka Python 3.7+ (f-str., dict. insertion order) (zapewne tylko do użytku własnego)... <br/> 
 [1.&nbsp;Pliki]({{ site.url }}{{ site.baseurl }}{{ page.url }}#1--pliki) &nbsp; 
 [2.&nbsp;Str]({{ site.url }}{{ site.baseurl }}{{ page.url }}#2--str) &nbsp; 
 [3.&nbsp;List, Tuple]({{ site.url }}{{ site.baseurl }}{{ page.url }}#3--list-tuple) &nbsp; 
 [4.&nbsp;Konwersja typów]({{ site.url }}{{ site.baseurl }}{{ page.url }}#4--konwersja-typów) &nbsp; 
 [5.&nbsp;Zmienne globalne, pamięć stanu]({{ site.url }}{{ site.baseurl }}{{ page.url }}#5--zmienne-globalne-pamięć-stanu) &nbsp; 
 [6.&nbsp;Tree]({{ site.url }}{{ site.baseurl }}{{ page.url }}#6--tree) &nbsp; 
 [7.&nbsp;sorted]({{ site.url }}{{ site.baseurl }}{{ page.url }}#7--sorted) 
 [8.&nbsp;filter() replacement]({{ site.url }}{{ site.baseurl }}{{ page.url }}#8--filter-replacement") &nbsp; 
 [9.&nbsp;linux sendmail]({{ site.url }}{{ site.baseurl }}{{ page.url }}#9--linux-sendmail) &nbsp; 
[10.&nbsp;Czytanie danych z wwww]({{ site.url }}{{ site.baseurl }}{{ page.url }}#10--czytanie-danych-z-www) &nbsp; 
[11.&nbsp;GUI - dane wejściowe]({{ site.url }}{{ site.baseurl }}{{ page.url }}#11--gui---dane-wejściowe) &nbsp; 
[12.&nbsp;Galeria JPG w pliku HTML]({{ site.url }}{{ site.baseurl }}{{ page.url }}#12--galeria-jpg-w-pliku-html) &nbsp; 
[13.&nbsp;Notepad++ QuickText]({{ site.url }}{{ site.baseurl }}{{ page.url }}#13--notepad-quicktext) &nbsp; 


## 1 . Pliki:

````py
try:
  with open('a.txt', encoding='utf-8-sig') as txt:
    a = txt.read().splitlines()
except FileNotFoundError as e: print(e); exit()

with open('a.txt','w',newline='\r\n',encoding='utf-8-sig') as txt: txt.write('\n'.join(a))

with open('a.txt','w',newline='',encoding='utf-8-sig') as txt: print(s, file=txt)
````

* [Check if a File or Directory Exists](https://linuxize.com/post/python-check-if-file-exists/) -> linuxize.com/

### Lista plików

````py
import os
with os.scandir(path='.') as it: # iterator
  for f in it:
    if f.is_file(): print(f.name)
````

*  [os.scandir](https://docs.python.org/3/library/os.html#os.scandir)   -> docs.python.org/3/

### JSON

````py
import json # load(file) loads(str)
with open('d.json', 'r', encoding='utf-8') as fj:
  d = json.load(fj) # ordered dict in py 3.7+

json.dumps({'4': 5, '6': 7}, ensure_ascii=False, indent=2) #-> str
````

Dla dość prostych struktur json, gdzie mamy listę słowników można uzyskać "hybrydowy format" json/csv, który ułatwia wkopiowanie takiego tekst do arkusza kalkulacyjnego (rozdzielany '\t'). Można też zastosować kodowanie `UTF-16 (=UCS-2) Little Endian with BOM`, tj. `encoding='utf-16'` i od razu otwierać w arkuszu kalk., dodając rozszerzenie `CSV` do nazwy pliku.

````py
d=[{'aa': 1, 'bb': 2},{'aa': 33, 'bb': 44},{'aa': 'abc', 'bb': 'ddd'}]
with open('d.json', 'w', encoding='utf-8') as fj:
  fj.write(json.dumps(d,ensure_ascii=False,separators=('\t,',':\t')).replace('}','\t}').replace('}\t,','},\n'))
````

<!-- https://github.com/root-project/web/pull/529#issue-832096581-->
<details markdown=1><summary markdown="span">Do skondensowanego wypisywania istotnych wartości w złożonej strukturze może się przydać  
`def allValuesList(d): ...` <br> . . . </summary>

````py
def allValuesList(d):
  ''' Lista wartości ze złożonej struktury, z pomijaniem pewnych kluczy i wartości None
>>> x = {'a':'aaa', 'b':'bb', 0:None, 'arr':[{'a':'AAA','b':'BB'},{'c':'CCC'}], '..':'..', 123:[1,2,3]}
>>> list(allValuesList(x))
['aaa', 'bb', 'AAA', 'BB', 'CCC', '1', '2', '3']
>>> list(allValuesList( [4,5] ))
['4', '5']
>>> list(allValuesList( {'a':None} ))
[]'''
  if isinstance(d, dict):
    for k,v in d.items():
      if k not in ['...','..']:
        yield from allValuesList(v)
  elif not isinstance(d,str) and hasattr(d,'__iter__'):
    for v in d: 
      yield from allValuesList(v)
  else:
    if not (d is None):
      yield str(d)

if __name__ == "__main__":
  import doctest
  doctest.testmod()
````
</details>

Można skorzystać z propozycji [konwersji XML <-> JSON](https://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html) i obsługiwać XML [z pomocą xmltodict](https://pypi.org/project/xmltodict/)

````py
import xmltodict
with open('a.xml') as fd:
  doc = xmltodict.parse(fd.read())
````
* [xml2dict2csv_test.zip]({{ site.baseurl }}/assets/files/xml2dict2csv_test.zip  "xml2dict2csv_test.zip ") 

Można [spłaszczać strukturę zagnieżdżoną](https://www.freecodecamp.org/news/how-to-flatten-a-dictionary-in-python-in-4-different-ways) (najprościej z pomocą [FlatDict](https://github.com/gmr/flatdict/)).


### CSV

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

<small>W korespondecji seryjnej MS Word 2016 jest błędna interpretacja cudzysłowów innych niż podstawowy `"`. Można zastosować konwersję jak w 
[unicodeDoubleQuote.py]({{ site.baseurl }}/assets/files/unicodeDoubleQuote.py.html )</small>.

### CSV & namedtuple:

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


* [namedtuple()](https://docs.python.org/3/library/collections.html#collections.namedtuple)  -> docs.python.org/3/
* [testCsvNamedtuple.py (.zip)]({{ site.baseurl }}/assets/files/testCsvNamedtuple.zip "testCsvNamedtuple.zip") 



## 2 . Str

````py
f'{x!r}' # v3.6 conversion: 's' str(), 'r' repr(), 'a' ascii().

"{" [field_name] ["!" conversion] [":" format_spec] "}"
format_spec  ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill         ::=  <any character>
align        ::=  "<" | ">" | "^" | "=" # left | right | center | v3.8 padding after the sign
sign         ::=  "+" | "-" | " " # +: a sign should be used for positive numbers
width        ::=  digit+
grouping_opt ::=  "_" | "," # for a thousands separator, or every 4 digits for hex, bin, ...
precision    ::=  digit+
type         ::=  "b"|"c"|"d"|"e"|"E"|"f"|"F"|"g"|"G"|"n"|"o"|"s"|"x"|"X"|"%"

>>> x=123; y=20
>>> f'{x:*^20}   {x:*^{y}}'
'********123*********   ********123*********'
>>> f'{x:06d} {x:06x} {x:#x}'
'000123 00007b 0x7b'
````

````py
>>> x=11; f"{x=}" # py 3.8+: 'x=11'
````


* [Format Specification Mini-Language](https://docs.python.org/pl/3/library/string.html#formatspec)  -> docs.python.org/3/
* [f-str 73 examples](https://miguendes.me/73-examples-to-help-you-master-pythons-f-strings) -> miguendes.me


````py
>>> print ('opis: ',end =''); print (x)
opis: 123

x or '' - gdy x=None albo jest łańcuchem, to zamiast None jest ''
' '.join(filter(None,[di.get(k) for k in ['k1','k2',...]])) - scal, pomijając None

x = x.replace('a','aa') # wszystkie wystąpienia
x = x.replace('a','A',1) # 1 wystąpienie
````

````py
>>> import re
>>> match = re.search(r'(\d+).*?(\d+)','x=01 y=02 z=03 z4=04') #nie re.match, które tylko szuka na pocz.
>>> match[0],match[1],match[2] #znajduje 1-sze wystąpienie
('01 y=02', '01', '02')
>>> x=re.sub(r'\S+?(\d+)',r'\1','x=01 y=02 z=03 z4=04')
>>> x   # zamienia wszystkie wystąpienia
'01 02 03 404'
````

## 3 . List, Tuple

````py
>>> len(['abc','def',]) # przecinek na końcu jest ignorowany
2
>>> len(('abc',)) # 1-el. krotka
1

#Odczyt 3-ciego parametru linii poleceń
sysArgv3 = (sys.argv+['']*3)[3]
````

## 4 . Konwersja typów

````py
>>> [1*x for x in (True, False, '', [])]
[1, 0, '', []]

>>> '-'.join([])
''
````

<small>Symulacja orderedSet za pomocą dict py 3.7+:</small>
````py
>>> ", ".join(dict.fromkeys("aa, b1, b1, aa, cd".split(", ")))
'aa, b1, cd'
````

<small>Konwersja z wartością domyślną:</small>
````py
try: y = float(xIn or 0) # 0 if None
except ValueError: y=0.0
````

## 5 . Zmienne globalne, pamięć stanu

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

Podobnie unikaj w funkcjach wartości domyślnych modyfikowalnych (mutable), jak `[], {}, ...`, gdyż takie wartości domyślne są inicjowane raz - przy pierwszym wywołaniu funkcji i są pamiętane przy kolejnych wywołaniach. Można tego użyć do pamiętania stanu z poprzedniego wywołania - [zob.>>](https://docs.python.org/3.9/faq/programming.html#why-are-default-values-shared-between-objects)
````py
def expensive(arg1, arg2, *, _cache={}):  # po `*` mogą wystąpić tylko pary `k=v`
  if (arg1, arg2) in _cache:
    return _cache[(arg1, arg2)]

  result = ... expensive computation ...  # Calculate the value
  _cache[(arg1, arg2)] = result           # Store result in the cache
  return result
````

* [create module-wide vars](https://stackoverflow.com/questions/1977362/how-to-create-module-wide-variables-in-python)  -> stackoverflow.com/questions
* [global variables in a function](https://stackoverflow.com/questions/423379/using-global-variables-in-a-function)  -> stackoverflow.com/questions
* [default values shared between objects](https://docs.python.org/3.9/faq/programming.html#why-are-default-values-shared-between-objects)  -> docs.python.org/3.9/faq


## 6 . Tree

<details markdown=1><summary markdown="span"> One-line Tree in Python `...` <br> . . . </summary>


````py
treeStr = f'''\
1
  11
  12
    121
    122
2
3
  31
  32
    321
  33
'''
#https://gist.github.com/hrldcpr/2012250  (autovivification)
from collections import defaultdict
import json
import re

def tree(): return defaultdict(tree)
def add(t, path):
  for node in path: t = t[node]
    
indent='  '; indentLen=len(indent)
dirsIn = treeStr.splitlines()

tree0 = tree(); path = []
for d in dirsIn:
  level=len(re.match(r'\s+',indent+d)[0]) // indentLen #; print(level) #-> 1, ...
  if level > len(path):
    path.append(d.strip())
  else:
    path = path[:level-1]  + [d.strip()]
  add(tree0, path)
  
print(json.dumps(tree0, ensure_ascii=False,indent=2,sort_keys=True))

def prnTree(t, depth = 0):
  for k in t.keys():
    print(f'''{depth}: {"".join(depth * ["+ "])}{k}''')
    depth += 1
    prnTree(t[k], depth)
    depth -= 1
print('tree0:'); prnTree(tree0)
  
print('kopia do `tree1` i (dla zobrazowania) wydruk pełnych ścieżek:')
tree1=tree()
def cpTree(t, depth = 0, path = []):
  for k in t.keys():
    path = path + [k]
    print(f'''{depth}: {path}''') #$#
    add(tree1,path) # kopia w `tree1`
    depth += 1
    cpTree(t[k], depth, path)
    depth -= 1
    path = path[:-1]

cpTree(tree0)
# 0: ['1']
# 1: ['1', '11']
# 1: ['1', '12']
# 2: ['1', '12', '121']
# 2: ['1', '12', '122']
# 0: ['2']
# 0: ['3']
# 1: ['3', '31']
# 1: ['3', '32']
# 2: ['3', '32', '321']
# 1: ['3', '33']

print('tree1:'); prnTree(tree1)
````
</details>

* [One-line Tree in Python](https://gist.github.com/hrldcpr/2012250) -> gist.github.com/hrldcpr/ (autovivification)


## 7 . sorted

````py
import locale
locale.setlocale(locale.LC_ALL, '')

liPrac = [ ['Kowal Jan', 'dr'], ['Zych Jan','prof.'], ['Zorba Jan','mgr'], ['Ślisz Jan','mgr'] ]

def odwrKluczTytSt(tytSt):
  if not tytSt: return 0 # 0 gdy pusty tytSt
  return -ord(tytSt[0] if tytSt[0]!='d' else 'n')
       # -ord: sortowanie odwr.tj. najpierw 'prof.', 'dr' przed 'mgr', stąd 'd' na 'n'; 
liPrac_ = sorted( liPrac, key = lambda r: (odwrKluczTytSt(r[1]), locale.strxfrm(r[0]) ))
                                                               # Nazwiska - alfabetycznie PL
#   [['Zych Jan', 'prof.'], ['Kowal Jan', 'dr'], ['Ślisz Jan', 'mgr'], ['Zorba Jan', 'mgr']]
````


## 8 . filter() replacement

````py
    # Equivalent list comprehension
list(filter(function, iterable))
[item for item in iterable if function(item)]
    # Use a generator expression
filter(function, iterable)
(item for item in iterable if function(item))
````

* <https://realpython.com/python-filter-function/#replacing-filter-with-a-list-comprehension>
* <https://www.programiz.com/python-programming/generator#expression>


## 9 . linux sendmail

````py
from email.message import EmailMessage
from subprocess import Popen, PIPE
def e_addrss(adrLi):
  return ', '.join(adrLi)
  #po przecinku MUSI BYĆ SPACJA - z powodu błędu Pythona(np.v3.9)
msg = EmailMessage()
msg.set_content('''Treść ĄĆĘŁŃÓŚŹŻ ąćęłńóśźż €''')
msg['From'] = 'a <a@x.y>'
msg['To'] = e_addrss(['Ab C <abc@x.y>','D. Żółw <dz@x.y>','A Ć<ac@x.y>'])
#   'Cc' 'Bcc' 'Reply-To' 'Subject'
print(msg.as_string()) #$#
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
p.communicate(msg.as_bytes())
````

Teksty nie-ascii są w EmailMessage automatycznie enkodowane na 'utf-8'.

* <https://bugs.python.org/issue45551>
* <https://www.ietf.org/rfc/rfc2822.txt> , 2.2.3. Long Header Fields




## 10 . Czytanie danych z www

````py
import requests #py -m pip install requests
import re
url='https://andrzejq.github.io/El_Prog/'
response = requests.get(url) #;print(response.text)
#...<h3>
#   <a class="post-link" href="/El_Prog/...
# można przeskakiwać łamanie wiersza z pomocą '\s+' lub '[^<]+',
# albo rozdzielić tekst na wiersze z interesującymi nas sekcjami:
html = response.text.replace('\n',' ').replace('<h3','\n<h3') #;print(html)
aLi2 = re.findall(r'<h3> +' + re.escape('<a class="post-link"')
+ r'.+?href=' + r'"(.+?)">' 
+ r'(.+?)'+r'</a>', html) ;print(f'{aLi2}'.replace(', ',',\n'))
#[('/El_Prog/programowanie/2020/11/24/Python-sciagawka.html',
#'             Python ściągawka           '), ...
````

REST API, gdy bez logowania

````py
import requests
def RESTapi(service: str, api_base='https://apps.edu.pl/', timeout=15, **kwargs):
  response = requests.post(api_base + service, timeout=timeout, data=kwargs)
  if not (response.ok): # OK - response code 200
    response.raise_for_status()
  return response.json()
print(RESTapi('services/a_index', fields='id|name'))
````

## 11 . GUI - dane wejściowe

Można wyświetlić okno dialogowe do pobrania danych dla skryptu (GUI tkinter działa w dowolnym systemie operacyjnym)

<details markdown=1><summary markdown="span"> `TkEntryWidget.py ...` <br> . . . </summary>

````py
#!/usr/bin/python3 -i
import tkinter as tk
# based on https://python-course.eu/tkinter_entry_widgets.php

def tkForm(fields):
  """tkForm(fields: dict)->dict
  fields: {'label1': 'defVal1', ...}
  return: modified fields or {} if Esc
  >_> tkForm( {'Imię':'iii', 'Imię 2':'iii 2', 'Nazwisko':'Nnn'} )
  {'Imię': 'iii 1', 'Imię 2': 'iii 2', 'Nazwisko': 'nnn 3'}
  """
  master = tk.Tk()
  entries = {}
  for i, (field, defVal) in enumerate(fields.items()):
    tk.Label(master, text=field).grid(row=i, sticky=tk.E, padx=3)
    ent = tk.Entry(master); ent.grid(row=i, column=1, padx=5, pady=5); ent.insert(0, defVal)
    if i==0: ent.focus_set()
    entries[field] = ent # ent.get() - value
  tk.Button(master, text='Esc', command=master.destroy).grid(row=len(fields), column=0, ipadx=5, pady=9)
  master.bind('<Escape>', lambda _: master.destroy())
  tk.Button(master, text='Ok', command=master.quit).grid(row=len(fields), column=1, ipadx=5, pady=9)
  master.bind('<Return>', lambda _: master.quit()) # [Enter] = [Ok]
    
  master.mainloop()
  try: # [Ok] - get modified values
    entries_di = {}
    for k,v in entries.items():
      entries_di[k] = v.get()
    master.destroy()
  except tk.TclError: # on master.destroy() = [x] or [Esc] - cancel
    entries_di = {}
  return entries_di


def tkFormConf(fields, confCsv='conf_0.csv'):
  """tkFormConf(fields: dict, confCsv: str)->dict (saving data in Csv)
  fields: {'label1': 'defVal1', ...} - used if confCsv is missing (on start)
  confCsv - text file UTF-16 (=UCS-2) Little Endian with BOM with <tab> separator
  return: modified fields saved in confCsv or {} if Esc (confCsv remain unchanged)
  >>> tkFormConf( {'Imię':'iii 1', 'Imię 2':'iii 2', 'Nazwisko':'nnn 3'}, confCsv='conf_0.csv')
  {'Imię': 'iii 1', 'Imię 2': 'iii 2', 'Nazwisko': 'nnn 3'}
  """
...
````
</details>

![TkEntryWidget.png]({{ site.baseurl }}/assets/img/TkEntryWidget.png "TkEntryWidget.png"){:style="float:right;width:30%;"}


* [TkEntry_json.zip]({{ site.baseurl }}/assets/files/TkEntry_json.zip  "TkEntry_json.zip ") 
* <https://python-course.eu/tkinter_entry_widgets.php>
* <https://www.pythontutorial.net/tkinter/tkinter-grid/>


## 12 . Galeria JPG w pliku HTML

Pliki JPG zakodowane w BASE64 scalone w jednym pliku HTML jako responsywna galeria.

* [jpgGallery_1html.py]({{ site.baseurl }}/assets/files/jpgGallery_1html.py.html)
* [jpgGallery_1html.zip]({{ site.baseurl }}/assets/files/jpgGallery_1html.zip) - test



## 13 . Notepad++ QuickText


Przykładowe ustawienia dodatku N++ - `QuickText`:  
<small> `[_] Use Scintilla Autocomplite`, `[_] Auto Insert Autocomplite`; Replace Tag: `Alt+Space`
</small>

`Alt+Space`, zaczynam pisać uściślając wybór z listy, `Tab`, `Alt+Space`. <small>Kolejne `Alt+Space` przeskakują do miejsc oznanczonych w "QuickText.ini" przez `$`</small>


<details markdown=1><summary markdown="span"> `QuickText.ini ...` <br> . . . </summary>

````ini
...
#LANGUAGE_NAME=Python
class=class $($object):\n  """$"""\n\n  def __init__(self, $):\n    $\n$
def=def $($):\n  """$"""\n\n  $\n$
elif=elif $:\n  $\n$
else=else:\n  $\n$
for=for $ in $:\n  $\n$
if=if $:\n  $\n$
ifelif=if $:\n  $\nelif $:\n  $\nelse:\n  $\n$
ifelse=if $:\n  $\nelse:\n  $\n$
main=if __name__ == '__main__':\n  main()\n$
maintest=if __name__ == "__main__":\n  import doctest\n  doctest.testmod()\n$
readjson=with open('$.json', 'r', encoding='utf-8') as fj:\n  d$ = json.load(fj)\n$
readtxt=try:\n  with open('$.txt', encoding='utf-8-sig') as txt:\n    a$ = txt.read().splitlines()\nexcept FileNotFoundError as e: print(e); exit()\n$
start=#!/usr/bin/env python\n\nimport os\nimport sys\n\n$
try=try:\n  $\nexcept $:\n  $\n$
writejson=with open('$.json', 'w', encoding='utf-8') as fj:\n  fj.write(json.dumps( d$ , ensure_ascii=False, separators=('\t,',':\t')).replace('}','\t}').replace('}\t,','},\\n'))\n$
writetxt=with open('$.txt','w',newline='\r\\n',encoding='utf-8-sig') as txt: txt.write('\\n'.join( a$ ))\n$
...
````
</details>
- - - - - -

&nbsp;

Różne odnośniki:

* [Python - programing FAQ](https://docs.python.org/3/faq/programming.html)  -> docs.python.org/3/faq/

* [utils_AK (.zip) files.py misc1.py]({{ site.baseurl }}/assets/files/utils_AK.zip "utils_AK.zip") 

* [Uruchamianie Pythona w Windows]({% if jekyll.environment == "production" %}{{ site.baseurl }}{% endif %}{% post_url 2019-09-20-drobne_podpowiedzi_3 %})  



<style> pre code {font-size: smaller;} </style>
<style> small code {font-size: smaller;} </style>
