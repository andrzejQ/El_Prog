---
layout: post
title:  "Seryjne wypełnianie formularza HTML"
date:   2022-10-17 06:30:49 +0100
categories: Programowanie
---

Chodzi o sposób zapełniania formularza danymi z kolejnych wierszy arkusza kalkulacyjnego np. Excel.

**Przykładowe pliki:**

* [FormTest-Wstaw-kolejne-paczki-danych.zip]({{ site.baseurl }}/assets/files/FormTest-Wstaw-kolejne-paczki-danych.zip  "FormTest-Wstaw-kolejne-paczki-danych.zip  ") 


1. "FormTest-Wstaw-kolejne-paczki-danych.html"  
Formularz ze strony www najlepiej zapisać jako plik HTML i na nim ćwiczyć działanie skryptów

2. "Paczki danych do formularza.xlsx"  
To przykładowy plik Excela.  
* Pierwszy wiersz arkusza to przyjazne nazwy danych - będzie ignorowany.  
* Drugi wiersz to albo "name" pól formularza, albo ich "id" - poprzedzone "#".  
* Gdy pole "radio" jest wskazywane przez "id", to wstawiasz "x" dla wyboru, lub <nic> aby odznaczyć.  
* x lub brak oznacza "zaznacz" lub "odznacz" i powoduje kliknięcie na elemencie, gdy stan elementu jest inny niż wpisany/brakujący "x".  
* Gdy pole "radio" jest wskazywane przez "name", to wstawiasz wartość "value", która ma być wybrana.  
* Aby wywołać funkcję javascript w nagłówku w 2-gim wierszu wpisz "new Function()()", a w danych  - treść funkcji.  
* Całość arkusza skopiuj z pomocą edytora tekstowego do pliku "Zapisz dane do localStorage.user.js" powyżej ostatniego wiersza, poniżej wiersza "let lista1=". Wygodnie jest używać wtyczki https://www.tampermonkey.net/        
* Łamanie wiersza w komórce Excela [Alt+Enter] nie jest obecnie możliwe (tzn. nie jest oprogramowane). Nie można też nigdzie używać odwrotnego apostrofu.        

Aby obsłużyć edytor WYSIWYG Tiny MCE, możesz wstawić trść funkcji js:  
    tinymce.activeEditor.setContent("Gdy w formularzu jest jeden edytor Tiny MCE,");')

3. "Zapisz dane do localStorage.user.js"
* Wpisuje dane skopiowane z Excela do localStorage.user.

4. "Wstawiaj kolejne paczki danych.js" 
* Po odświeżeniu strony zatwierdzamy dane do seryjnego wypełniania.
* Następnie pojawia się przycisk dla kolejnej paczką danych do wypełnienia
* Po jego kliknięciu zatrzymujemy się na jego wypełnionym panelu - można wysłać dane, albo je zignorować.
* Można klikać dowolną liczbę razy - będą się wypełniały kolejne dane.
* Po wyczerpaniu listy danych wraca się do ich początku.


<style> pre > code {font-size: 95%;} </style>
