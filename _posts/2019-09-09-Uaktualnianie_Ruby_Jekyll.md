---
layout: post
title:  "Uaktualnienie Ruby i Jekyll"
date:   2019-09-09 11:21:59 +0100
categories: Programowanie
---

...np. po tym gdy nadejdzie ponaglenie z Github, że coś muszę uaktualnić. 2023-01-07 - dodatek: Giscus - komentarze w Jekyll 

Po ponagleniu o konieczności uaktualnienia można np. wykonać synchronizację lokalnej kopii. Następnie w dowolnym wybranym blogu:

### Zmiana na wyższą wersję Ruby

1. W przypadku zmiany numeru głównego wersji **X.Y.** na nowszy: [**instalacja Ruby**](https://rubyinstaller.org/downloads/#with-devkit) w nowym miejscu; MSYS2 basic; ścieżka w PATH do nowego Ruby pojawi się najwyżej (będzie ważniejsza od starszych) .  
Natomiast w przypadku uakt. podwersji X.Y. **Z** - tylko aktualizacja, bez miany foldera i [**bez DevKit**]((https://rubyinstaller.org/downloads/#without-devkit)). Potem jest pytanie co z MSYS2 - [2], tj. uaktualnienie działa choć rzuca błędami; a są porady, żeby wybierać opcję [3] !
2. `gem install bundler`


### Zmiana na wyższą wersję Jekyll

1. <https://jekyllrb.com/docs/installation/windows/>
````bat
gem install jekyll bundler
````
Może pojawić się porada, np: `gem update --system 3.5.10`
2. Wymuszamy instację potrzebnych bibliotek w najnowszej wersji
````bat
bundle add bbbbbb  
````
(lub?) W `gemfile` dopisujemy wersję, która podlega aktualizacji, np.:
````bat
gem "rexml", "~> 3.2"
````
3. gems installed `bundle exec jekyll -v`
4. Instalacja brakujących gem, a może wystarczy `bundle update`
````bat
bundle update
bundle install
````
Ale pojwia się czasen błąd dot. natywnych rozszerzeń, np. dla `gem install wdm`  
Wtedy może pomóc (ale niew wiem czy to sensowne)
```bat
gem install wdm -v '0.1.1' -- --with-cflags="-Wno-error=implicit-function-declaration" 
```
5. `bundle info --path minima` - sprawdzanie ścieżki do szablonu.  
   Jest kiepska sprawa - minima 2.5.1 ma przestarzałe operacje dzielenia, które należałoby objąć funkcją `calc()`. Dla przypudrowania problemu można wpisać w `_config.yml`:  `sass:`  
   `quiet_deps: true`.
6. UWAGA- w nazwach plików chyba nie może być nie-ascii, np. w URL. Dodanie `_` przed nazwą pliku/foldera chyba powoduje ignorowanie tego
podczas `bundle exec jekyll serve`. Dodałem `_` przed *.URL i *.cmd.
7. `git commit`

Uruchamianie podglądu `_r.cmd`:

````bat
:: ostatni człon aktulanego foldera %cd% poprzedzony http://localhost/ oraz wywołanie przeglądarki
@FOR /F "delims=|" %%i IN ("%cd%") DO (
  start "jekyll-localhost-%%~ni" http://localhost:4000/%%~ni/
  start "jekyll-www-%%~ni" https://andrzejq.github.io/%%~ni/ )
::uruchomienie lokalnego serwera www
bundle exec jekyll serve
````

### W kolejnych blogach:

Jeśli kolejne blogi są analogiczne do uaktualnionego:

1. Nadpisuję nowy `gemfile` (i dopisuję w `_config.yml` jak w p.5 powyżej, gdy trzeba)
2. `bundle update --bundler`
3. `bundle update`
4. Czy działa? `_r.cmd`
5. `git commit`


### Jeśli trzeba - instalacja szablonu "minima"

<https://github.com/jekyll/minima>

1. Gemfile: (dopisz) `gem "minima"`
2. `bundle`

- - - -

### Giscus - komentarze w Jekyll 

* <https://blog.jakelee.co.uk/migrating-from-utterances-to-giscus-comments/>

1. Repository -> Settings -> discussions enabled.   ## 👋 Witaj!  
  Będzie mi bardzo miło jeśli zechcesz skomentować moje wpisy. 
2. Strona "discussion" - edycja (ikona ołówka). Można usunąć zbędne kategorie i dodać nową, np. Title: "Komentarze" ;  Description: "Komentarze gości" ;  Discussion Format: (*) Annoucement. Można wybrać też ikonę dla kategorii.
3. Dodanie Giscus <https://github.com/apps/giscus> do każdego repozytorium: [Configure] (*) Only select repositories - wybranych lista repozytoriów.
4. <https://giscus.app> ( =  Website ) - dla każdego repozytorium generujemy parametry:  
  repository: "andrzejQ/El_Prog" (np.) ;  Page ↔️ Discussions Mapping: (*) Discussion title contains page pathname ;  Discussion Category: ;-) Komentarze ;  [x] Only search for discussions in this category ;  [x] Enable reactions for the main post ;  [x] Wczytaj komentarze leniwie ;  Theme [Preferred].
5. Wygenerowany `<script>` wklejam do "El_Prog\_includes\giscus_js.html"
6. "El_Progs\_includes\footer.html" <small>(tu trzeba usunąć spację z `{ %`)</small>
````html
...
    { %- if page.comments == true -%}
      <p style="font-size:small"> Włącz się do dyskusji. 
      Będą zachowane te komentarze, które jakoś dotyczą treści na blogu. 
      <br> Na początek trzeba mieć (darmowe) konto na   <a href="https://github.com/">GitHub</a>.</p>
      { %- include giscus_js.html -%}
    { %- endif -%}
````
7. W każdym poście inicjalny wpis (pozwala każdemu na "odpowiedz")  
Nowa wersja komentarzy z użyciem `giscus -> GitHub Discussions`.


<style> pre code, small code {font-size: smaller;} </style>

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