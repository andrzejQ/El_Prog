---
layout: post
title:  "Seryjne wypełnianie formularza HTML"
date:   2022-10-17 06:30:49 +0200
categories: Programowanie
---

Sposób seryjnego wypełniania formularza danymi z kolejnych wierszy arkusza kalkulacyjnego np. Excel.

**Przykładowe pliki** - [FormTest-Wstaw-kolejne-paczki-danych.zip]({{ site.baseurl }}/assets/files/FormTest-Wstaw-kolejne-paczki-danych.zip  "FormTest-Wstaw-kolejne-paczki-danych.zip  ") :

![form.png]({{ site.baseurl }}/assets/img/form.png "form.png"){:style="float:right;width:25%;"}
![html-form.png]({{ site.baseurl }}/assets/img/html-form.png "html-form.png"){:style="float:right;width:31%;"}

1. "FormTest-Wstaw-kolejne-paczki-danych.html"  
Formularz ze strony www najlepiej zapisać jako plik HTML i na nim ćwiczyć działanie skryptów.  
Tu jest testowy przykład.

2. "Paczki danych do formularza.xlsx"  
To przykładowy plik Excela pasujący do powyższego formularza.  
![dane-excel.png]({{ site.baseurl }}/assets/img/dane-excel.png "dane-excel.png"){:style="float:right;width:57%;"}
* Pierwszy wiersz arkusza to przyjazne nazwy danych - będzie ignorowany. 
* Drugi wiersz to albo "name" pól formularza, albo ich "id" - poprzedzone "#". 
* Gdy pole "radio" jest wskazywane przez "id", to wstawiasz "x" dla wyboru, lub <nic> aby odznaczyć. 
* x lub brak oznacza "zaznacz" lub "odznacz" i powoduje kliknięcie na elemencie, gdy stan elementu jest inny niż wpisany/brakujący "x". 
* Gdy pole "radio" jest wskazywane przez "name", to wstawiasz wartość "value", która ma być wybrana. 
* Aby wywołać funkcję javascript w nagłówku w 2-gim wierszu wpisz "new Function()()", a w danych  - treść funkcji. 
* Całość arkusza skopiuj z pomocą edytora tekstowego do pliku "Zapisz dane do localStorage.user.js" powyżej ostatniego wiersza, poniżej wiersza "let lista1=". Wygodnie jest używać wtyczki https://www.tampermonkey.net/ 
* Łamanie wiersza w komórce Excela [Alt+Enter] nie jest obecnie możliwe (tzn. nie jest oprogramowane). Nie można też nigdzie używać odwrotnego apostrofu. 
* Aby obsłużyć edytor WYSIWYG Tiny MCE, możesz wstawić treść funkcji js:  
`tinymce.activeEditor.setContent("gdy w formularzu jest jeden edytor Tiny MCE.");`

3. "Zapisz dane do localStorage.user.js"
* Wpisuje dane skopiowane z Excela do localStorage.user.

4. "Wstawiaj kolejne paczki danych.js" 
* Po odświeżeniu strony zatwierdź dane do seryjnego wypełniania.
* Po tym pojawia się przycisk dla kolejnej paczki danych do wypełnienia
* Po jego kliknięciu otrzymujemy wypełniony formularz - można wysłać dane, albo je zignorować.
* Można klikać dowolną liczbę razy - będą się wypełniały kolejne dane.


<style> code {font-size: 85%;} </style>
