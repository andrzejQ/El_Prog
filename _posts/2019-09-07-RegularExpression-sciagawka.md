---
layout: post
title:  "Regular Expression - ściągawka"
date:   2019-09-07 08:08:49 +0100
categories: Programowanie
docs: https://github.com/notepad-plus-plus/npp-usermanual/blob/master/content/docs/searching.md
    # Powyżej długi odnośnik do którego są częste odwołania => ` page.docs `
---

Moja ściągawka Regular Expression (zapewne tylko do użytku własnego)... 

Głównie dotyczy Notepad++ - zob. 
[Notepad++ User Manual](https://github.com/notepad-plus-plus/npp-usermanual) - 
[Searching]({{ page.docs }}#user-content-regular-expressions)

#### Znaki specjalne

[Dla znajdź (>> PerlRegExp)](https://www.boost.org/doc/libs/1_70_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html)  
`.[{}()\*+?|^$`  
<small>Czasem zalecane jest też traktowanie `]` jako znaku specjalnego</small>  

W zbiorze znaków "jeden z"/"żaden z" po `[`/`[^`...  
`]\-^`  
<small>, przy czym `^` nie na początku  i `-` na pocz. lub końcu nie jest zn. specjalnym</small>  



[Dla zamień (>> PerlRegExp repl.)](https://www.boost.org/doc/libs/1_70_0/libs/regex/doc/html/boost_regex/format/boost_format_syntax.html)  
`$\()?:`


#### Opisy na tej stronie

Wyrażenia regularne są pokazywane jako kod z podświetleniem, które pozwala zauważyć spacje, np. poniżej mamy kolejno `a<spacja>` i `a`:
````regexp
a 
a
````

Aby wyraźnie zaznaczyć, że część "zamień na" ma być pusta, stosowany będzie znak `¤` np.:

````regexp
 
¤
````

Dla operacji "Znajdź i zamień" będą stosowane zawsze 2 wiersze. Powyższy przykład to zamiana spacji na "nic".  
Gdy chodzi o wyrażenia tylko dla "Znajdź", to będzie 1 wiersz abo 3+ .

#### Różne przykłady


Usuwanie całych wierszy, które nie zaczynają się od "abc" (łącznie z końcem wiersza)

````regexp
^(?=abc).*\R
¤
````

`\R` jest [uniwersalnym znakiem końca wiersza]({{ page.docs }}#user-content-special-control-escapes)
 i może obejmować 2 znaki np. `\r\n` (Windows) czy 1 znak `\n` (Unix). 
<small>Nie może być używany wewnątrz `[...]`.</small>

Dowolny ciąg znaków obejmujący także znaki końca wiersza (przydatne w javascript)
````regexp
[\s\S]*
````

Sklejanie pojedynczych liter z kolejnym wyrazem - zamiana na spację nierozdzielającą \xA0 ([Alt+0160]) spacji (1+) poprzedzonej jedną z liter 'awizou', po której następuje 
[początek wyrazu]({{ page.docs }}#user-content-anchors):

````regexp
(?<=\<[awizou]) +\<
\xA0
````

Kompletne usuwanie tagu HTML (tu `<(\S+) ...<\/\1>`) z zadanym fragmentem nazwy klasy (ale bez zagnieżdżeń takich samych tagów)
````regexp
<(\S+) class="[^"]*FragmentKlasy[^>]*>(.*?)<\/\1>
¤
````

------
* <https://www.regular-expressions.info/>
* <https://regex101.com/> - testowanie
* [Regular_Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) -> developer.mozilla.org
* Wyrażenia regularne, Marcin Kuta, AGH (obecnie niedostępne - tu kopia w formacie MarkDown): [RegEx-Marcin_Kuta,_AGH.md]({{ site.baseurl }}/assets/files/RegEx-Marcin_Kuta,_AGH.md)
[...html]({{ site.baseurl }}/assets/files/RegEx-Marcin_Kuta,_AGH.md.html)




* zob. też: 
[Przydatne znaki unicode]({% if jekyll.environment == "production" %}{{ site.baseurl }}{% endif %}{% post_url 2019-09-07-PrzydatneZnakiUnicode %})


<style> pre > code {font-size: 95%;} 
code.language-regexp {background-color: Aqua;} </style>
