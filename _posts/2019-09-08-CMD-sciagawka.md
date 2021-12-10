---
layout: post
title:  "Wiersz polceń CMD - ściągawka"
date:   2019-09-08 08:08:59 +0100
categories: Programowanie
---

[Edycja treści tekstowej]({{ site.url }}{{ site.baseurl }}{{ page.url }}#edycja-treści-tekstowej) &nbsp; 
[Zmiana litery dysku]({{ site.url }}{{ site.baseurl }}{{ page.url }}#zmiana-litery-dysku) &nbsp; 

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




<style> pre code {font-size: smaller;} </style>
