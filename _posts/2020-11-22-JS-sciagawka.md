---
layout: post
title:  "JavaScript ściągawka"
date:   2020-11-23 17:00:00 +0100
categories: Programowanie
---

Moja ściągawka ...

### 0: <small> *skondensowana przypominajka bez objaśnień* </small>

````js
String.prototype.fun1 = function  () {...}
`x: ${x}`
str.replace(patternStr, replacementStr) //jednorazowo
str.replace(RegExp, replacement) //np. str.replace(/ab/g, '');
if (str.match(/;|"/)) str=`"${str.replace(/"/g, '""')}"`;
"123"+1 //"1231" 
+"123"+1 //124

$(document).ready(function () {...});// - może wystąpić wielokrotnie  

$.get('https://domain.pl/rss/70.xml', function (data){
  $(data).find('item').each( function () {let $el = $(this);...

$div.append($li1.clone());
````


````js
const obj = { a:'d1', ą:'d2' }; obj.a = 'x';
[ obj.a, obj['a'], obj.ą, obj['ą'] ] //[ "x", "x", "d2", "d2" ]

const obj1 = Object.assign({}, obj); //shallow clone

for (const key in obj) { ... };
obj->arr:
Object.entries(obj).forEach ( ([key, value], index) => { ... } ); 
Object.keys(obj)     //key - liczbowe nieujemne są na początku (choć są typu string),
Object.values(obj)   //poza tą regułą kolejność wprowadzania jest zachowana.
````

````js
arr.push(el1, el2);
arr = [].concat( arr1, arr2 ) //shallow clone
````
````js
JSON.stringify() //prawie jak py repr()
````

### 1: Inne nazwy plików po załadowaniu do CMS

Podczas umieszczania plików w systemie CMS nazwy plików podlegają konwersji, np.:
1. PL -> nie-PL (bezogonkowe)
2. Duże znaki na małe
3. " " na "_"
4. Zachowaj ostatnią "." (tu na chwilę zamienianą na '/')
5. Pomijaj znaki (regexp): [^-_a-z0-9]

````js
String.prototype.toCmsFNameExt = function  () { //nie powinno być '/' w nazwie
  return this //ES2015/ES6 str.normalize() - działa w przeglądarkach od roku 2014
    .toLowerCase().replace(/ /g, '_')//znaki małe, ' ' -> '_'
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') //usuwa wszelkie ogonki, ...
                     .replace(/ł/g, 'l')             //... ale na "Ł" i "ł" nie działa.
    .replace(/\.([^\.]*)$/, '/$1')                  //na chwilę ostatnią kropkę zamień na '/'
    .replace(/[^-_a-z0-9\/]/g,'').replace('/','.');//usuń wszystkie nie:  -, _, a-z, 0-9 i przywróć '.'
}; 
//np.
("c m s_~!@#$%^()_+`-=-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ{}[];'-.. ,.txt".toCmsFNameExt()==="c_m_s__--acelnoszzacelnoszz-_.txt")
&& ("c m s_~!@#$%^()_+`-=-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ{}[];'- -".toCmsFNameExt()==="c_m_s__--acelnoszzacelnoszz-_-");
````

### 2: Data

````js
String.prototype.numDateYMdHms = function  () { //date_time -> YYYY-MM-dd HH:mm:ss
  let dt = new Date(this);
  return `${dt.getFullYear()}-${('0'+(1+dt.getMonth())).slice(-2)}-${('0'+dt.getDate()).slice(-2)} ${dt.toTimeString().substring(0,8)}`; 
}; //np. 
("Thu Oct 27 2022 00:17:21 GMT+0200".numDateYMdHms()==="2022-10-27 00:17:21")
````

### # Nie będziesz używał!

`let x=y=...`  
`with `

- - - -
zob.:

* <https://andrzejq.github.io/El_Prog/programowanie/2022/10/17/Seryjne_wypelnianie_formularza.html>
* <https://kursjs.pl/> - kurs Javascript dla superbohaterów autorstwa Marcina Domańskiego

<style> 
  pre code {font-size: smaller;} 
  h3 small em {font-size: 14px;} 
</style>


