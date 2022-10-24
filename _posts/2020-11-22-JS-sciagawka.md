---
layout: post
title:  "JavaScript ściągawka"
date:   2020-11-23 17:00:00 +0100
categories: Programowanie
---

Moja ściągawka (zapewne tylko do użytku własnego) ...

### 0: <small> *skondensowana przypominajka bez objaśnień* </small>

````js
$(document).ready(function () {...});// - może wystąpić wielokrotnie  
String.prototype.fun1 = function  () {...}
$.get('https://domain.pl/rss/70.xml', function (data){
  $(data).find('item').each( function () {let $el = $(this);...
$div.append($li1.clone());
`x: ${x}`
str.replace(patternStr, replacementStr) //jednorazowo
str.replace(RegExp, replacement) //można użyć /g, np. str.replace(/ab/g, '');
````


### 1: Inne nazwy plików po załadowaniu do CMS

Podczas umieszczania plików w systemie CMS nazwy plików podlegają konwersji, np.:
1. PL -> nie-PL (bezogonkowe)
2. Duże znaki na małe
3. " " na "_"
4. Zachowaj ostatnią "." (tu na chwilę zamienianą na '/')
5. Pomijaj znaki (regexp) [^-_a-z0-9]

````js
String.prototype.toCmsFNameExt = function  () { //nie powinno być '/' w nazwie
  return this //ES2015/ES6 str.normalize() - działa w przeglądarkach od roku 2014
    .toString().trim().toLowerCase().replace(/ /g, '_')//znaki małe, ' ' -> '_'
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') //usuwa wszelkie ogonki, ...
                     .replace(/ł/g, 'l')             //... ale na "Ł" i "ł" nie działa.
    .replace(/\.([^\.]*)$/, '/$1')                  //na chwilę ostatnią kropkę zamień na '/'
    .replace(/[^-_a-z0-9\/]/g,'').replace('/','.');//usuń wszystkie nie:  -, _, a-z, 0-9 i przywróć '.'
}; 
//np.
("c m s_~!@#$%^()_+`-=-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ{}[];'-.. ,.txt".toCmsFNameExt()==="c_m_s__--acelnoszzacelnoszz-_.txt")
&& ("c m s_~!@#$%^()_+`-=-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ{}[];'- -".toCmsFNameExt()==="c_m_s__--acelnoszzacelnoszz-_-");

String.prototype.toCmsFName = function  () { //dotyczy samej nazwy (bez rozszerzenia po ostatniej kropce)
  return this //ES2015/ES6 String.prototype.normalize() - działa w przeglądarkach od roku 2014
    .toString().trim().normalize('NFD').replace(/[\u0300-\u036f]/g, '')//usuwa wszelkie ogonki, ...
    .toLowerCase().replace(/ /g, '_')  .replace(/ł/g, 'l')            //... ale na "Ł" i "ł" nie działa.
    .replace(/[^-_a-z0-9]/g, '');                                    //usuń wszystkie nie:  -, _, a-z, 0-9
};
//np.
("c m s_~!@#$%^()_+`-=ąaćęłńóśźżĄĆĘŁŃÓŚŹŻ{}[];'-..,".toCmsFName()==="c_m_s__--acelnoszzacelnoszz-")
````

### # Nie będziesz używał!

`let x=y=...`  
`with `

<style> 
  pre code {font-size: smaller;} 
  h3 small em {font-size: 14px;} 
  ul {font-size: smaller;} 
</style>


