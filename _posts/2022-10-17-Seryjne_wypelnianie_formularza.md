---
layout: post
title:  "Seryjne wypełnianie formularza HTML"
date:   2022-10-17 06:30:49 +0200
categories: Programowanie
---

Sposób seryjnego wypełniania formularza danymi z kolejnych wierszy arkusza kalkulacyjnego np. Excel (dla lekko zaawansowanych).

Dla strony HTML z formularzem przygotuj arkusz kalkulacyjny, gdzie w kolejnych wierszach są kolejne paczki danych do wypełniania. <small>Arkusz służy do przygotowania pliku tekstowego z polami oddzielonymi tabulatorem.</small>

**Przykładowe pliki** - [FormTest-Wstaw-kolejne-paczki-danych.zip]({{ site.baseurl }}/assets/files/FormTest-Wstaw-kolejne-paczki-danych.zip  "FormTest-Wstaw-kolejne-paczki-danych.zip  ") :

![form.png]({{ site.baseurl }}/assets/img/form.png "form.png"){:style="float:right;width:25%;"}
![html-form.png]({{ site.baseurl }}/assets/img/html-form.png "html-form.png"){:style="float:right;width:31%;"}

1. **"FormTest-Wstaw-kolejne-paczki-danych.html"**  
Formularz ze strony www najlepiej zapisać jako plik HTML i na nim ćwiczyć działanie skryptów.  
Tu jest testowy przykład.

2. **"Paczki danych do formularza.xlsx"**  
To przykładowy plik Excela pasujący do powyższego formularza.  
![dane-excel.png]({{ site.baseurl }}/assets/img/dane-excel.png "dane-excel.png"){:style="float:right;width:57%;"}
* Pierwszy wiersz arkusza to przyjazne nazwy danych - będzie ignorowany. 
* Drugi wiersz to albo "name" pól formularza, albo ich "id" - poprzedzone "#". 
* "x" lub brak oznacza "zaznacz" lub "odznacz" i powoduje kliknięcie na elemencie, gdy stan elementu jest inny niż wpisany/brakujący "x". 
* Gdy pojedyncze pole "radio" jest wskazywane przez "id", to wstawiasz "x" dla wyboru, lub <nic> aby odznaczyć. 
* Gdy pole "radio" jest wskazywane przez "name", to wstawiasz wartość "value", która ma być wybrana. 
* Aby wywołać funkcję javascript w nagłówku w 2-gim wierszu wpisz "new Function()()", a w danych  - treść funkcji. 
* Całość arkusza skopiuj z pomocą edytora tekstowego do pliku "Wstawiaj kolejne paczki danych.js" poniżej wiersza "let lista1=". 
* Łamanie wiersza w komórce Excela [Alt+Enter] nie jest obecnie możliwe (tzn. nie jest oprogramowane). Nie można też nigdzie używać odwrotnego apostrofu `\`. 
* Aby obsłużyć edytor WYSIWYG Tiny MCE, możesz wstawić treść funkcji js:  
`tinymce.activeEditor.setContent("gdy w formularzu jest jeden edytor Tiny MCE.");`

3. **"Wstawiaj kolejne paczki danych.js"** 
* Ten plik można w całości skopiować jako nowy skrypt we wtyczce <https://www.tampermonkey.net/> w przeglądarce internetowej.
* `lista1` to łańcuch wielowierszowy. Jest to tekstowa kopia z Excela - pola są oddzielone znakiem tabulatora `\t`.
* Uwaga pierwszy i ostatni wiersz jest pusty (zob. `` let lista1=` `` i `` `; ``).
* Początkowy wiersz danych to zrozumiałe dla człowieka nazwy, a drugi wiersz to atrybut "name" albo "id" poprzedzone "#".
* `formSel`, np `[name="form1"]` czy `#fomId` to selektor obszaru dla formy do wstawiania danych -> querySelector(), np. div, form, ...  
.
* Po odświeżeniu strony zatwierdź dane do seryjnego wypełniania.
* Po tym pojawia się przycisk dla kolejnej paczki danych do wypełnienia
* Po jego kliknięciu otrzymujemy wypełniony formularz - można wysłać dane, albo je zignorować. Równocześnie przycisk pokazuje **dane z następnego wiersza**, które zostaną podstawione po jego kliknięciu. Można go klikać dowolną liczbę razy bez wysyłania danych - w formularzu będą się pojawiały kolejne paczki danych.


<style> code {font-size: 85%;} </style>
