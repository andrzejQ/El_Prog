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
[Searching]({{page.docs}}#user-content-regular-expressions)

#### Znaki specjalne

[Dla znajdź (>> PerlRegExp)](https://www.boost.org/doc/libs/1_70_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html)  
`.[{}()\*+?|^$`  
<small>Czasem zalecane jest też traktowanie `]` jako znaku specjalnego</small>  

W zbiorze znaków "jeden z" lub "żaden z" po `[` lub `[^`...  
`]\-^`  
<small>, przy czym  `-` na początku lub końcu i `^` nie-na-początku nie jest zn. specjalnym</small>  



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


* Usuwanie całych wierszy, które nie zaczynają się od "abc" (łącznie z końcem wiersza)

````regexp
^(?=abc).*\R
¤
````

`\R` ro [uniwersalny znak końca wiersza]({{page.docs}}#user-content-special-control-escapes)
czyli  `(?>\r\n|\n|\x0B|\f|\r|\x85|\x{2028}|\x{2029})`, np. 2 znaki `\r\n` (Windows) lub 1 znak `\n` (Unix). 
<small>Nie może być używany wewnątrz `[...]`.</small>


* Znajdź cały wiersz, który nie kończy się na "xyz" (w tym pusty)

````regexp
^.*(?<!xyz)$
````


* Dowolny ciąg znaków obejmujący także znaki końca wiersza (przydatne w javascript)

````regexp
[\s\S]*
````

* Sklejanie pojedynczych liter z kolejnym wyrazem - zamiana na spację nierozdzielającą \xA0 ([Alt+0160]) spacji (1+) poprzedzonej jedną z liter 'awizou', po której następuje 
[początek wyrazu]({{page.docs}}#user-content-anchors):

````regexp
(?<=\<[awizou]) +\<
\xA0
````
* Kompletne usuwanie tagu HTML (tu `<(\S+) ...<\/\1>`) z zadanym fragmentem nazwy klasy o ile nie zawiera zagnieżdżeń takich samych tagów jak tag `(\S+)`.

````regexp
<(\S+) class="[^"]*FragmentNazwyKlasy[^>]*>(.*?)<\/\1>
¤
````

* Scalenie akapitów, np. skopiowanych z PDF - gdy faktyczny podział  akapitu wyznacza pusty wiersz, a inne łamania wierszy wewnątrz akapitu należy zamienić na spację. Tzn. mamy pojedyncze łamanie wiersza `\r?\n` z opcjonalną dodatkową spacją ` ?` poprzedzone nie-białym znakiem `(?<=\S)` i występującym po łamaniu wiersza nie-białym znakiem `(?=\S)`:

````regexp
(?<=\S) ?\r?\n(?=\S)
 
````


* Import e-maili **z pliku vCard *.VCF do Excela**. Chodzi o wieloktorne dane w pliku VCF w rodzaju:

```txt
...
FN:Nazwisko Imię
TEL;TYPE=work:1700000000
EMAIL;TYPE=INTERNET;TYPE=HOME:abc@abc.pl
EMAIL:biuro@abc.pl
ADR;TYPE=work:
...
```

Plik otwieram w Notepad++ lub innym edytorze z obsługą wyrażeń regularnych (opcja `gm`) i zamieniam na kolumny rozdzielone tabulacją, które można skopiować do Excela. Kol. 2 - nazwa wyświetlana (tj. FN), kol. 3 - e-mail. Opcjonalnie kol. 4 i 5  - dalsze emaile. W kol. 1 są śmieci (na końcu)

````regexp
[\S\s]*?^FN.*:(.+)$[\S\s]*?^EMAIL.*:(.+)$([\r\n]+EMAIL.*:(.+)$)?([\r\n]+EMAIL.*:(.+)$)?
\t$1\t$2\t$4\t$6\n
````
<small>(lub w Pythonie zamień na: `\t\1\t\2\t\4\t\6\n`)</small>


------
* <https://www.regular-expressions.info/>
* <https://regex101.com/> - testowanie
* [Regular_Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) -> developer.mozilla.org
* Wyrażenia regularne, Marcin Kuta, AGH (obecnie niedostępne - tu kopia w formacie MarkDown): [RegEx-Marcin_Kuta,_AGH.md]({{site.baseurl}}/assets/files/RegEx-Marcin_Kuta,_AGH.md)
[...html]({{site.baseurl}}/assets/files/RegEx-Marcin_Kuta,_AGH.md.html)




* zob. też: 
[Przydatne znaki unicode]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2019-09-07-PrzydatneZnakiUnicode %})


<style> pre > code {font-size: 95%;} 
code.language-regexp {background-color: Aqua;} </style>

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
