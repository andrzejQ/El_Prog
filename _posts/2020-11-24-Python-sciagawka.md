---
layout: post
title:  "Python ściągawka"
date:   2020-11-24 06:55:00 +0100
categories: Programowanie
---

Moja ściągawka Python 3.8+ (f-str., dict. insertion order) (zapewne tylko do użytku własnego)... <br/> 
 [1.&nbsp;Pliki]({{site.url}}{{site.baseurl}}{{page.url}}#1--pliki) &nbsp; 
 [2.&nbsp;Str]({{site.url}}{{site.baseurl}}{{page.url}}#2--str) &nbsp; 
 [3.&nbsp;List, Tuple]({{site.url}}{{site.baseurl}}{{page.url}}#3--list-tuple) &nbsp; 
 [4.&nbsp;Konwersja typów]({{site.url}}{{site.baseurl}}{{page.url}}#4--konwersja-typów) &nbsp; 
 [5.&nbsp;Zmienne globalne, pamięć stanu]({{site.url}}{{site.baseurl}}{{page.url}}#5--zmienne-globalne-pamięć-stanu) &nbsp; 
 [6.&nbsp;Tree]({{site.url}}{{site.baseurl}}{{page.url}}#6--tree) &nbsp; 
 [7.&nbsp;sorted]({{site.url}}{{site.baseurl}}{{page.url}}#7--sorted) 
 [8.&nbsp;filter() replacement]({{site.url}}{{site.baseurl}}{{page.url}}#8--filter-replacement") &nbsp; 
 [9.&nbsp;linux sendmail]({{site.url}}{{site.baseurl}}{{page.url}}#9--linux-sendmail) &nbsp; 
[10.&nbsp;Czytanie danych z wwww]({{site.url}}{{site.baseurl}}{{page.url}}#10--czytanie-danych-z-www) &nbsp; 
[11.&nbsp;GUI - dane wejściowe]({{site.url}}{{site.baseurl}}{{page.url}}#11--gui---dane-wejściowe) &nbsp; 
[12.&nbsp;Galeria JPG w pliku HTML]({{site.url}}{{site.baseurl}}{{page.url}}#12--galeria-jpg-w-pliku-html) &nbsp; 
[13.&nbsp;Notepad++ QuickText, NppExec]({{site.url}}{{site.baseurl}}{{page.url}}#13--notepad-quicktext-nppexec) &nbsp; 
[14.&nbsp;Pola statyczne]({{site.url}}{{site.baseurl}}{{page.url}}#14--pola-statyczne) &nbsp; 
[15.&nbsp;mingus.midi, fluidsynth]({{site.url}}{{site.baseurl}}{{page.url}}#15--mingusmidi-fluidsynth) &nbsp; 
[16.&nbsp;subprocess run()]({{site.url}}{{site.baseurl}}{{page.url}}#16--subprocess-run) &nbsp; 
[17.&nbsp;doctest_or_main]({{site.url}}{{site.baseurl}}{{page.url}}#17--doctest_or_main) &nbsp; 

## 1 . Pliki:

````py
try:
  with open('a.txt', encoding='utf-8-sig') as txt:
    a = txt.read().splitlines()
except FileNotFoundError as e: print(e); exit()

with open('a.txt','w',newline='\r\n',encoding='utf-8-sig') as txt: txt.write('\n'.join(a))

with open('a.txt','w',newline='',encoding='utf-8-sig') as txt: print(s, file=txt)
````

<small>Przy okazji uniwersalna obsługa wyjątków:</small>
````py
try: ... except Exception as e:  print(str(e)); exit()
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

### Usuwanie pustych podfolderów

<details markdown=1><summary markdown="span">... począwszy od najbardziej zagłębionych pustych podfolderów: <br> . . . </summary>

````py
import os
#https://stackoverflow.com/questions/23488924/how-to-delete-recursively-empty-folders-in-python3

def remove_empty_dirs(dir0):
  def remove_empty_dir(path):
    try:
      os.rmdir(path)
      return True
    except OSError: #not empty
      return False

  print(f'Usuwam puste foldery poniżej {dir0!r}:')
  for root, dirnames, filenames in os.walk(dir0, topdown=False):
  #  print(f'{root=} >>> {dirnames=} >>> {filenames=}')
    for dirname in dirnames:
      d = os.path.realpath(os.path.join(root, dirname))
      if remove_empty_dir(d):
        print(d)
  print('Koniec.')

remove_empty_dirs('wFolderze')
````
* <https://stackoverflow.com/questions/23488924/how-to-delete-recursively-empty-folders-in-python3>

</details>



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
* [xml2dict2csv_test.zip]({{site.baseurl}}/assets/files/xml2dict2csv_test.zip  "xml2dict2csv_test.zip ") 

Można [spłaszczać strukturę zagnieżdżoną](https://www.freecodecamp.org/news/how-to-flatten-a-dictionary-in-python-in-4-different-ways) (najprościej z pomocą [FlatDict](https://github.com/gmr/flatdict/)).


### CSV

````py
import csv
with open('x.csv','r',newline='',encoding='utf-8-sig') as csvF:
  csvRd = csv.reader(csvF, delimiter=';')
  csvHeader = next(csvRd)
  for r in csvRd:
    print(r)

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
[unicodeDoubleQuote.py]({{site.baseurl}}/assets/files/unicodeDoubleQuote.py.html ) 
(zob. przy okazji [Przydatne znaki unicode]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2019-09-07-PrzydatneZnakiUnicode %}))
</small>.

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
print(3, di)       #3 {'col1':... | py.3.1 .. 3.7: 3 OrderedDict([('col1', ...
print(4, dict(di)) #4 {'col1': (also for py.3.1 .. 3.7)
di_nonempty = {k: v for k, v in row._asdict().items() if v} # pomija puste v

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
* [testCsvNamedtuple.py (.zip)]({{site.baseurl}}/assets/files/testCsvNamedtuple.zip "testCsvNamedtuple.zip") 



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
html = response.text
# Ta prymitywna metoda nie uwzględnia drzewiastej struktury HTML
# więc czasem wato usuwać zbędne fragmenty, np. z początku
html = re.sub(r'^.*(<h2 class="post-list-head)', r'\1', html, 
  count=1, flags=re.DOTALL) # '<h2 class="post-list-heading">Spis ...
#...<h3> ... <a class="post-link" href="/El_Prog/...
# warto rozdzielić tekst na wiersze z interesującymi nas sekcjami:
html = html.replace('\n','\t').replace('<h3','\n<h3') #;print(html)
aLi2 = re.findall(r'<h3>\s+' + re.escape('<a class="post-link"')
+ r'.+?href="(.+?)">(.+?)</a>', html) ;print(f'{aLi2}'.replace(', ',',\n'))
#[('/El_Prog/programowanie/2022/10/17/Seryjne_wypelnianie_formularza.html',
#'\t            Seryjne wypełnianie formularza HTML\t          '), ...
````

<small>Można też rozdzielić wszystkie tagi jako listę i liczyć `....startswith()` ich zamknięcia: `tags = re.split(r'(?=<)', html)`</small> 

Treść w UTF-8 z dowolnego kodowania:

````py
#!/usr/bin/env python
import requests #python -m pip install requests bs4 lxml
from bs4 import BeautifulSoup as bs4

def anyEncodingToUtf8(url):
  class response: content = ''
  try:
    response = requests.get(url) #;print( vars(response) )
  except Exception as e:
    print('### ' + str(e))
  soup = bs4(response.content, "lxml") #(not: response.text)
  return str(soup) # charset=utf-8
````
HTMLSession świetnie sobie radzi z konwersją kodowania do utf-8. Choć w poniższym przykładzie po `r.html.render(...` kodowanie nie-utf-8 nie jest poprawnie konwertowane.

````py
from requests_html import HTMLSession
import re
#url= '...' #<meta http-equiv="refresh" content="0;url=....
url = 'https://aka.ms/ppac' # 301 # r.url='https://admin.powerplatform.microsoft.com'
#url = 'https://python.org/'
start_url = url if url.endswith('/') else f'{url}/' ;print(f'\n{start_url=}\n')
## Get redirect or refresh info
#''' #### version 1 - recommended (with optionally html.render js, without keep_page)
RENDER_JS = 0
while True:
  with HTMLSession() as session:
    r = session.get(start_url) #;print(f'...{f"{dir(r)}"[-300:]=}\n\n...{f"{vars(r)}"[-300:]=}\n')
    redirect_url = r.url if (r.url != start_url) else '' ;print(f'{redirect_url=}\n')
    if r.html and len(r.html.text) < 100: # usually len()==0
      metaRefresh = r.html.find("""meta[http-equiv*='efresh']""",first=True)#r'[Rr]efresh'
      if metaRefresh:
        metaRefrUrl = metaRefresh.attrs['content'] # '0;url=http://...
        refresh_url = (re.split(r'url\s*=\s*',metaRefrUrl,1,re.IGNORECASE)+[''])[1]
        print(f'{"^"*33}\n{refresh_url=}\n')
        if 'http' in refresh_url: start_url = refresh_url; continue #^^^^^^^^^^
    if RENDER_JS: r.html.render(sleep=3) # like browser (with JavaScript)
    print(f'{r.html.text=}'[:200],'...\n'); #...
    break #>>>>>>>>>>>>>>
#''' #### version 2 (with .html.render...keep_page and js)
with HTMLSession() as session:
  r = session.get(start_url) #;print(f'...{f"{dir(r)}"[-300:]=}\n\n...{f"{vars(r)}"[-300:]=}\n')
  redirect_url = r.url if (r.url != start_url) else ''     ;print(f'{redirect_url=}\n')
  r.html.render(sleep=3,keep_page=True) # like browser (with JavaScript)
  target_url = r.html.page.target.url if r.html.page else '' ;print(f'{target_url=}\n')
  print(f'{r.html.text=}'[:200],'...\n'); #...
  session.close() # ? close browser after .render
#'''
````

REST API, gdy bez logowania

````py
import requests
def RESTapi(service: str, api_base='https://httpbin.org', timeout=15, **kwargs):
  response = requests.post(api_base + service, timeout=timeout, data=kwargs)
  if not (response.ok): # OK - response code 200
    response.raise_for_status()
  return response.json()
print(RESTapi('/post', d1='coś', d2=112))
````

## 11 . GUI - dane wejściowe

Można wyświetlić okno dialogowe do pobrania danych dla skryptu (GUI tkinter działa w dowolnym systemie operacyjnym)

<details markdown=1><summary markdown="span"> `TkEntryWidget.py ...` <br> . . . </summary>

````py
#!/usr/bin/env python
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

![TkEntryWidget.png]({{site.baseurl}}/assets/img/TkEntryWidget.png "TkEntryWidget.png"){: style="float:right;width:30%;"}


* [TkEntry_json.zip]({{site.baseurl}}/assets/files/TkEntry_json.zip  "TkEntry_json.zip ") 
* <https://python-course.eu/tkinter_entry_widgets.php>
* <https://www.pythontutorial.net/tkinter/tkinter-grid/>


## 12 . Galeria JPG w pliku HTML

Pliki JPG zakodowane w BASE64 scalone w jednym pliku HTML jako responsywna galeria.

* [jpgGallery_1html.py]({{site.baseurl}}/assets/files/jpgGallery_1html.py.html)
* [jpgGallery_1html.zip]({{site.baseurl}}/assets/files/jpgGallery_1html.zip) - test



## 13 . Notepad++ QuickText, NppExec


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

- - - -

<br>
**Można też skorzystać z wtyczki N++ `NppExec`:**

<small>Na podstawie - NppExec help/manual - 4.6.4. "Running Python & wxPython" oraz  
<https://mountcreo.com/article/running-and-debugging-python-in-notepad-with-idle/></small>

Skrypt "RunPython" dla wersji interaktywnej Pythona:

1. Wtyczki \ NppExec: Execute NppExec Script...  
````bat
npp_console 1
npp_console local -
npp_save
cd "$(CURRENT_DIRECTORY)"
set local @exit_cmd_silent = exit()
npp_setfocus con
npp_console local +
python -i -u -X utf8 "$(FILE_NAME)"
````
 \ [Save] \ Nazwa np. "RunPython" \ [OK]

2. Wtyczki \ NppExec \ Console Output Filters \ HighLight:  
[x] `*File "%ABSFILE%", line %LINE%`  
Red 0x`FF`

3. Console Output...: UTF8

<small>(dalsze 4..6 chyba zbędne)  
4.Wtyczki \ NppExec \ Advanced Options... :  
\ Associated script (na dole z lewej): RunPython \ [Add/Modify]  
[x] Place to the Macros submenu (z lewej u góry)  
Restart Notepad++  
5.Uruchom \ Zmień skrót/usuń polecenie... \ Polecenia Wtyczek \ "RunPython" - dodaj gorący klawisz  
6.Wtyczki \ NppExec \ Show NppExec Console lub [Ctrl + ~]
</small>

`[Ctrl+W]` w oknie konsoli przełącza łamanie długich wierszy.

Podobnie można sprawdzać [**jakość stylu kodu źródłowego**](https://peps.python.org/pep-0008/) z pomocą [**Pylint**](https://pypi.org/project/pylint/),
także z wykorzystaniem [NppExec](https://stackoverflow.com/questions/4987920/python-correctness-i-e-lint-analyzing-for-notepad),
gdzie ostatni wiersz w skrypcie jak pozwyżej (p.1) zastępujemy przez  
`python -X utf8 -u -m pylint --rcfile %USERPROFILE%\.pylintrc "$(FILE_NAME)"`  
i zapisujemy jako np. "PyLint".  
Dodajemy kolejny filtr (zob. p.3, Red: 0xFF) [x] `%FILE%:%LINE%:%CHAR%` 
<details markdown=1>
<summary markdown="span"> <small>Tutaj mamy przywołane dodatkowe własne reguły poprawności w pliku `%USERPROFILE%\.pylintrc`.</small> <br> . . . </summary>

````yaml
# python -m pip install pylint
# pylint --generate-rcfile > .pylintrc
# --rcfile %USERPROFILE%\.pylintrc

[BASIC]

# Good variable names regexes, separated by a comma. If names match any regex,
# they will always be accepted
# good-names-rgxs=^[a-z_]\w*
# argument-rgx=^[a-z_]\w*
# attr-rgx=^[a-z_]\w*
# function-rgx=^[a-z_]\w*

[FORMAT]

# Expected format of line ending, e.g. empty (any line ending), LF or CRLF.
expected-line-ending-format=

# Regexp for a line that is allowed to be longer than the limit.
ignore-long-lines=^\s*(# )?<?https?://\S+>?$

# Number of spaces of indent required inside a hanging or continued line.
# indent-after-paren=4
indent-after-paren=2

# String used as indentation unit. This is usually "    " (4 spaces) or "\t".
# indent-string='    '
indent-string='  '

# Maximum number of characters on a single line.
max-line-length=100

[MESSAGES CONTROL]

disable=
    missing-function-docstring,
    multiple-statements,
````
</details>

- - - - 

<small>  
W **Notepad++** można też zapamiętać sobie w _Uruchom_ wywołanie programu właściwego dla rozszerzenia aktualnie edytowanego pliku (to działa uniwersalnie na dowolne rozszerzenia, nie tylko _*.py_):</small>  
`%ComSpec% /c chcp 65001 & cd /D "$(CURRENT_DIRECTORY)" & "$(FULL_CURRENT_PATH)" & pause`{: style="font-size: smaller;"}

<small>
Natomiast w celu skorzystania ze środowiska wirtualnego bez konieczności aktywowania jak opisano pod odnośnikiem 
[Uruchamianie Pythona w Windows]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2019-09-20-drobne_podpowiedzi_3 %})
 (analogicznie działa powyższy skrypt dla NppExec):</small>  
`%ComSpec% /c chcp 65001 & cd /D "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & pause`{: style="font-size: smaller;"}


- - - - - -

&nbsp;

## 14 . Pola statyczne

````py
class Test:
  c = 1;  d = {'x':3}
  def log(self): print('class c d :', Test.c, Test.d, ' self c d :', self.c, self.d)

class T2(Test): pass
t2 = T2()
t2.log()    # class c d : 1 {'x': 3}  self c d : 1 {'x': 3}
t2.c = 100;  t2.d['x'] = 44
t2.log()    # class c d : 1 {'x': 44}  self c d : 100 {'x': 44}
````

- - - - - -

&nbsp;

## 15 . mingus.midi, fluidsynth

1. Instalacja FluidSynth: <https://github.com/FluidSynth/fluidsynth/releases>  
Rozpakowuję `fluidsynth-....zip`, np. `c:\AUDIO\fluidsynth\`. Do PATH (zm. środowiskowe) dodaję `c:\AUDIO\fluidsynth\bin`
2. SoundFonts: <https://member.keymusician.com/Member/FluidR3_GM/>. Plik `FluidR3_GM.sf2` kopiuję do `c:\ProgramData\soundfonts\default.sf2` (a może też do `c:\soundfonts\default.sf2`). Od tego momentu działa: `fluidsynth coś.midi`
3. `py -m pip install pyfluidsynth`
4. `py -m pip install pygame`. Gdy niepowodzenie, to z <https://www.lfd.uci.edu/~gohlke/pythonlibs/> pobieram odpowiedni do systemu `pygame-...whl`, potem `py -m pip install pygame-...whl`.
5. `py -m pip install mingus`.  
W `...\Python\Lib\site-packages\mingus\midi\pyfluidsynth.py`  poprawka:
````py
lib = (
    find_library("libfluidsynth-3")
    or find_library("fluidsynth")
    or find_library("libfluidsynth")
...
````
Można testować działanie skryptem `...\Python\mingus_examples\pygame-piano\pygame-piano.py`. <small>Nie działa w `NppExec` - tylko `cmd`. Trzeba podawać ścieżkę do `default.sf2`</small>
6. <small>Podczas startu skryptu słychać czasem nieprzyjemny trzask w głośnikach. Być może skopiowanie `libfluidsynth-3.dll` do foldera skryptu coś porawia. A może paczkę z `...\fluidsynth\bin` warto skopiować do `C:\Windows\System32`? - Nie sprawdzałem.</small>


- - - - - -

&nbsp;

## 16 . subprocess run()

````py
from subprocess import run
# args=[...] or '...'
result = run(args, capture_output=True, text=True, check=True) 
# if check -> raise CalledProcessError if non-zero return code 
print(f'{result=}')
````

Albo - gdy zależy nam na pokazywaniu kolejnych wierszy wpisywanych przez długotrwały proces:
````py
from subprocess import Popen, PIPE, CalledProcessError
def run(args): # args=[...] or '...'
  print('>>>', args)
  with Popen(args, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
      print(line, end='')
  if p.returncode == 0: print('ok.')
  else: raise CalledProcessError(p.returncode, p.args)
````

Sprawdzanie czy "prog.exe" jest uruchomiony
````py
from subprocess import check_output
app = 'prog.exe'; cmd = f'tasklist /fi "imagename eq {app}"'
if app not in check_output(cmd, shell=True, encoding='1250'):
  print(f'''{'!'*44}\n  Najpierw uruchom {app}\n{'!'*44}''')
````
* <small> <https://www.datacamp.com/tutorial/python-subprocess> </small>
* <small> [https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running](https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running#answer-28319191) </small>
* <small> <https://docs.python.org/3/library/subprocess.html#converting-an-argument-sequence-to-a-string-on-windows> </small>


- - - - - -


&nbsp;

## 17 . doctest_or_main

````py
def add(a,b):
  """ a+b
  >>> add(2,2)
  2+2=4
  4
  """
  print(f'{a}+{b}={a+b}')
  return a+b

# zakomentuj ten wiersz aby wywołać funkcję poniżej:
import doctest; doctest.testmod() or \
add(5,10)
print('.')
````

- - - - - -

&nbsp;

Różne odnośniki:

* [Python - programing FAQ](https://docs.python.org/3/faq/programming.html)  -> docs.python.org/3/faq/

* [utils_AK (.zip) files.py misc1.py]({{site.baseurl}}/assets/files/utils_AK.zip "utils_AK.zip") 

* [Uruchamianie Pythona w Windows]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2019-09-20-drobne_podpowiedzi_3 %})  



<style> pre code {font-size: smaller;} </style>
<style> small code {font-size: smaller;} </style>

<!-- {% unless jekyll.environment %} -->
<script>

(function() {
  const images = document.getElementsByTagName('img'); 
  for(let i = 0; i < images.length; i++) {
    images[i].src = images[i].src.replace('%7B%7Bsite.baseurl%7D%7D','..');
  } //{{site.baseurl}} - without spaces!  
})();

</script>
<!-- {% endunless %} -->
