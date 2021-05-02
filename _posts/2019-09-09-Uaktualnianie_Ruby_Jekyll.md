---
layout: post
title:  "Uaktualnienie Ruby i Jekyll"
date:   2019-09-09 11:21:59 +0100
categories: Programowanie
---

...np. po tym gdy nadejdzie ponaglenie z Github, że coś muszę uaktualnić.

Po takim ponagleniu można np. wykonać synchronizację lokalnej kopii. Następnie w dowolnym wybranym blogu:

### Zmiana na wyższą wersję Ruby

1. W przypadku zmiany numeru głównego wersji **X.Y.** na nowszy: [**instalacja Ruby**](https://rubyinstaller.org/downloads/#with-devkit) w nowym miejscu; MSYS2 basic; ścieżka w PATH do nowego Ruby pojawi się najwyżej (będzie ważniejsza od starszych) .  
Natomiast w przypadku uakt. podwersji X.Y. **Z** - tylko aktualizacja, bez miany foldera i [**bez DevKit**]((https://rubyinstaller.org/downloads/#without-devkit)). Potem jest pytanie co z MSYS2 - [2], tj. uaktualnienie działa choć rzuca błędami; może warto dawać [1], tj. nowa instalacja MSYS2.
2. `gem install bundler`


### Zmiana na wyższą wersję Jekyll

1. <https://jekyllrb.com/docs/installation/windows/>
````bat
gem install jekyll bundler
````
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
bundle install
````

5. `bundle info --path minima` - sprawdzanie ścieżki do szablonu
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

1. Nadpisuję nowy `gemfile`
2. `bundle update`
3. `git commit`


### Jeśli trzeba - instalacja szablonu "minima"

<https://github.com/jekyll/minima>

1. Gemfile: (dopisz) `gem "minima"`
2. `bundle`

<style> pre code {font-size: smaller;} </style>
