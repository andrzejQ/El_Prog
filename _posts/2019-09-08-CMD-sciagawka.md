---
layout: post
title:  "Wiersz poleceń CMD - ściągawka"
date:   2019-09-08 08:08:59 +0100
categories: Programowanie
---

_+ 14.05.2025_{: .date}  
[Edycja treści tekstowej]({{site.url}}{{site.baseurl}}{{page.url}}#edycja-treści-tekstowej) &nbsp; *
[Zmiana litery dysku]({{site.url}}{{site.baseurl}}{{page.url}}#zmiana-litery-dysku) &nbsp; *
[Wykonanie operacji na najnowszym pliku]({{site.url}}{{site.baseurl}}{{page.url}}#wykonanie-operacji-na-najnowszym-pliku) &nbsp; * 
[Wybierz i podstaw do zmiennej]({{site.url}}{{site.baseurl}}{{page.url}}#wybierz-i-podstaw-do-zmiennej) &nbsp; * 
[Wiersz polecenia w Eksploratorze plików]({{site.url}}{{site.baseurl}}{{page.url}}#wiersz-polecenia-w-eksploratorze-plików) &nbsp; 

<style>.date{font-size: smaller;color:#828282;}</style>

### Edycja treści tekstowej

Gdy w oknie CMD potrzebujemy coś zmienić, dopisać, zapisać fragment ekranu jako nieduży plik tekstowy itp.
1. Można wybrać kodowanie ANSI: `chcp 1250`, gdy będą jakieś polskie znaki (domyślne kodowanie OEM to archaiczne cp852).
2. Wyświetlamy sobie coś do kopiowania, np. `more plik1.txt`.
3. `more >plik2.txt`. Teraz kopiujemy dowolne fragmenty ekranu [Ctrl+C] / [Ctrl+V], piszemy (także [Enter]), aż do ...
4. [Ctrl+Z] &nbsp; [Enter]


### Zmiana litery dysku

Czasem potrzeba sprawdzić / zmienić literę przypisaną do dysku, np w trybie awaryjnym system startuje na dysku wirtualnym `[X:\]` i mapuje dyski fizyczne do innych liter. Jeśli w tym trybie w wierszu polecenia używasz `robocopy` do zaawansowanego kopiowania albo `mklink /j`, żeby utworzyć dowiązanie symboliczne do folderu, to mogą się przydać instrukcje:
````
diskpart
list volume
select volume <nr>
list volume
assign letter=L
````
* [Robocopy (Robust File Copy)](https://andrzejq.github.io/Office_S_Tips/system/2020/02/20/Backup_dysku_SSD.html#6-robocopy-robust-file-copy) -> andrzejq.github.io/Office_S_Tips
.


### Wykonanie operacji na najnowszym pliku

Tutaj przykładowa operacja to `echo ...`

```` bat
@echo off & for /F "delims=" %%G in ('dir *.* /b /a-d /o-d') do (set LATEST=%%G & goto found)
:found
echo "%LATEST%"
````
Krócej:
```` bat
@echo off & for /F "delims=" %%G in ('dir *.* /b /a-d /o-d') do (
echo %%G & goto:EOF)
````

Do wklejenia w oknie CMD:

```` bat
for /F "delims=" %G in ('dir *.* /b /a-d /o-d') do (echo %G & pause & exit)
````


### Wybierz i podstaw do zmiennej

```` bat
@echo off & chcp 1250 >nul
echo:&echo Jedna z wybranych opcji w zmiennej !_%%opt%%!
setlocal enabledelayedexpansion
echo:&echo =================&echo:
set "_1=Akcja pierwsza"
set "_2=Akcja druga"
set "_3=Akcja trzecia"
for /L %%o in (1,1,3) do (
  echo %%o - !_%%o!
)
echo:&set "err=Nie ma takiego numeru!"
set "opt=nic"
set /p "opt=Wybierz numer: "
echo Wybrano opcję: %opt%
if 1 LEQ %opt% ( if 3 GEQ %opt% (

echo Akcja dla tej opcji: "!_%opt%!"

) else ( echo %err% ) ) else ( echo %err% )
echo Koniec.
endlocal
````

### Wiersz polecenia w Eksploratorze plików


![Eksplorator_cmd_k.png]({{site.baseurl}}/assets/img/Eksplorator_cmd_k.png "Eksplorator_cmd_k.png"){: style="float:left;width:38%;margin-right:15px;"}
W eksploratorze ustawiając się na wybranym folderze można od razu wywołać polecenia konsoli. W tym celu czyścimy pasek adresu i wpisujemy polecenie, np. 
```` bat
cmd /k tree
````
które wyświetli nam okno konsoli z tekstową wersją drzewa podfolderów, co można skopiować choćby do notatnika (`/k` - remains).

Gdy chcemy użyć `echo off` np. z powodu użycia `for` w dalszej części w celu iteracji po podfolderach, to warto w zakończeniu użyć `echo on`.

```` bat
cmd /k @echo off & echo === %cd% === & (for /D %G in (*.*) do (echo %G)) & echo on
````

A tu najlepiej używać przełącznika `/Q` (- turns echo off):
```` bat
cmd /Q /k echo === %cd% === & (for /D %G in (*.*) do (echo %G))
````

<style> pre code {font-size: smaller;} </style>

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