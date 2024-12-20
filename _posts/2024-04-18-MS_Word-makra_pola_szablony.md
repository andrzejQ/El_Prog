---
layout: post
title:  "MS Word - makra, pola, szablony"
date:   2024-04-18 07:00:00 +0100
categories: Programowanie
---

Kilka odnośników do stron z zaawansowanymi operacjami MS Word  
[1.&nbsp;Masowa zamiana tekstów w wielu plikach docx]({{site.url}}{{site.baseurl}}{{page.url}}#1masowa-zamiana-tekstów-w-wielu-plikach-docx) * 
[2.&nbsp;Pola - główny plik docx z wstawionymi treściami z wielu plików docx]({{site.url}}{{site.baseurl}}{{page.url}}#2pola---główny-plik-docx-z-wstawionymi-treściami-z-wielu-plików-docx) * 
[3.&nbsp;Style]({{site.url}}{{site.baseurl}}{{page.url}}#3style) 


<style>.date{font-size: smaller;color:#828282;}</style>

### 1. Masowa zamiana tekstów w wielu plikach docx

* [`ReplaceAll_inDocxs.zip`]({{site.baseurl}}/assets/files/ReplaceAll_inDocxs.zip)

W pliku `ReplaceAll_inDocxs.dotm` - szablonie z makrami - są 2 skopiowane z Internetu i przetestowane makra, 
które pozwalają na masową zmianę tekstu w plikach **docx** zgromadzonych w wybranym folderze. Opis jest w tekście szablonu. 
W kodzie w makrach są zapisane linki do stron, z których pochodzi źródło.

Przy okazji jest tam opis jak wystartować z używaniem makr w MS Word, np. tych, których źródła skopiowaliśmy sobie z Internetu.
Zob. też: 
* <https://gregmaxey.com/word_tip_pages/installing_employing_macros.html>
* <https://addbalance.com/word/>
* <http://www.gmayor.com/installing_macro.htm>

Kilka skrótów klawiaturowych przydatnych do pracy z makrami:  
Wklejanie kodu: `[Alt+F11]`, `[Ctrl+R]`=Okno: Project \ Template Project.  
`[F5]` - uruchom, `[F8]` krok po kroku

### 2. Pola - główny plik docx z wstawionymi treściami z wielu plików docx

Tutaj kopalnią wiedzy jest 

* <http://www.addbalance.com/word/download.htm> - wyszukaj "IncludeText Field Tutorial" - spakowany dokument z przykładami.
* <https://www.msofficeforums.com/word/38722-word-fields-relative-paths-external-files.html> - sztuczka ze ścieżkami względnymi do plików

Założenie: w głównym pliku chcę scalić dynamicznie treści z wielu innych plików, które podlegają czasem aktualizacji. Wydawało by się, ze sprawa jest załatwiona w menu:  
Wstawianie \ obiekt \ obiekt... \ Microsoft Word Document.  
Ale są 2 problemy: wstawiana jest tylko pierwsza strona tekstu i dodatkowo wiersze nie przełamują się pomiędzy stronami w scalonym dokumencie. Oczywiście odpada Wstawianie \ obiekt \ tekst z pliku... - taki tekst nie podlega auto-aktualizacji. 

Z pomocą przychodzi opisane powyżej pole **`{IncludeText}`** i sztuczka ze ścieżkami względnymi do plików.


<details markdown=1><summary markdown="span">Gdy mam **równocześnie** **`{IncludeText}`** **i** wstawiony **obiekt** to (chyba) pojawia się groźne ostrzeżenie **...**▼ <br> . </summary>
{: style="font-size:0.9em;color:DarkSlateBlue;"}

... po otwarciu docx:  
"Ten dokument zawiera pola, które mogą udostępniać dane zewnętrznym plikom i
witrynom internetowym".  
I to pomimo tego, że używam w **`{IncludeText}`** przełącznika `\!` ( = Zapobiegaj aktualizacji pól), a potem aktualizuję pola pojedynczo lub hurtowo (nie wiem, czy ten przełącznik coś daje).  
Warto więc nie stosować wstawiania obiektów, gdy korzystamy z **`{IncludeText}`**. Można też przerwać łącza do plików zewnętrznych automatycznie aktualizowanych: <br>* 
"Plik" (menu lewy, górny róg) \ otwiera się menu "Informacje" \ <br>* 
"Edytuj linki do plików" (prawy, dolny róg - to pojawia się poniżej menu: "Powiązane dokumenty", o ile są jakieś linki w dokumencie)
{: style="font-size:0.9em;color:DarkSlateBlue;"}

</details>

**Przepis wstawiania treści z wielu plików DOCX** <small>(tu wstawiane są całe dokumenty - można też wstawiać tylko fragmenty korzystając z zakładek)</small>:

1. **Treści w plikach wstawianych** umieszczam w ich głównej części, a pozostałe elementy w nagłówku i stopce - te są pomijane podczas scalania. Pliki umieszczam w podfolderze, np. "docs" (gdy jest ich dużo).
2. Dla każdego scalanego pliku umieszczam w dokumencie głównym pole  
   **`{ IncludeText "{ FileName \p }\\..\\docs\\NazwaPliku.docx"}`**,  
   gdzie nawiasy klamrowe oznaczają wstawione pole uzyskane naciśnięciem `[Ctrl+F9]`,  
   **`{ FileName \p }`** to zagnieżdżone pole odpowiadające pełnej nazwie pliku głównego,  
   a `\\..\\` wyznacza ścieżkę tej dla nazwy, pomijając nazwę pliku.  
   `[Ctrl+F9]` ma przydatną właściwość - można najpierw wpisać treść wnętrza pola, zaznaczyć i nacisnąć `[Ctrl+F9]`. Treść zostanie otoczona znacznikiem pola. 
     1. Ale można też z powodu takiego działania zaliczyć nieprzyjemna sytuację - po zaznaczeniu całego, dużego dokumentu i przypadkowym naciśnięciu `[Ctrl+F9]` całość robi się ogromnym polem, a wynikowy dokument jest jakby pusty! Żeby wyciąć wnętrze tego mega-pola i skopiować obok warto sobie wpisać kilka spacji obok zewnętrznych znaczników pola.
     2. <span id=limit260>Sztuczka </span> z `{ FileName \p }\\..\\` wymaga stosowania nie za długich nazw plików i folderów.  
        Po rozwinięciu pola i dołożeniu nazwy pliku wstawianego całość musi się zmieścić w 260 znakach. 
        I nie ma tu znaczenia, czy w rejestrze zostało zadeklarowane używanie dłuższych nazw `LongPathsEnabled=1`.  
        Na szczęście nie przeszkadza używanie liter diakrytycznych w nazwach.  
        Zob. [`pole_IncludeText-BARDZO_DLUGIE_nazwy_plikow.zip`]({{site.baseurl}}/assets/files/pole_IncludeText-BARDZO_DLUGIE_nazwy_plikow.zip)
     {: style="font-size:0.9em;color:DarkSlateBlue;margin:10px auto 10px 30px;"}
   
3. Z zagnieżdżonym polem jest jakaś tajemnica - udaje się wpisać to ze zwykłymi nawiasami klamrowymi. Ale po aktualizacji może pojawiać się "Błąd! Nieprawidłowa nazwa pliku". 
    * Wtedy można skorzystać z notatki 2 z linku dot. ścieżki względnej, czyli: 
        * `[Alt+F9]` - żeby pojawiły się kody pól.
        * Utwórz w dowolnym miejscu `[Ctrl+F9]` - pole **`{ FileName \p }`**, zaznacz go i wytnij do schowka `[Ctrl+X]`.
        * `[Ctrl+H]`, w znajdź tekst `{ FileName \p }` tj. ze zwykłymi nawiasami klamrowymi, w zamień na `^c` tj. zawartość schowka.
        * `[Zamień wszystko]`
        * `[Ctrl+A]`=zaznacz wszystko, `[F9]`=aktualizuj, `[Alt+F9]`=przełącz na wynik
     {: style="font-size:0.84em;color:DarkSlateBlue;"}

[Kilka skrótów klawiaturowych](https://support.microsoft.com/pl-pl/office/skr%C3%B3ty-klawiaturowe-w-programie-word-95ef89dd-7142-4b50-afb2-f762f663ceb2#bkmk_fieldswin) 
przydatnych do pracy z polami:  
`[Shift+F9]` - Przełącz kod/wynik  
`[Alt+F9]` - Przełącz jednocześnie wszystkie kody/wyniki (także kody zagnieżdżone)  
     bardzo wygodnie do jakichś operacji "znajdź i zamień"  
`[Ctrl+F9]` - Wstaw pole. Natomiast menu:  
    Wstawianie \ Szybkie części \ Pole... - otwiera kreatora wstawiania pola z podpowiedziami.  
`[F9]` - Aktualizowanie zaznaczonych pól.  
`[F11]` / `[Shift+F11]` - Następne / poprzednie pole.


Zob. też 
* <https://www.addbalance.com/usersguide/fields.htm>,
* <https://www.addbalance.com/usersguide/fields.htm#Function>

### 3. Style

* <https://addbalance.com/usersguide/styles.htm> - kopalnia wiedzy o stylach, a na początek potężna dawka linków.

### 4. Inne odnośniki

* [MS Word - symbole wieloznaczne »]( https://andrzejq.github.io/Office_S_Tips/docx/2019/09/21/DOCX_wyszukiwanie_symboli_wieloznacznych.html)
* [Po pierwszej instalacji MS Office »]( https://andrzejq.github.io/Office_S_Tips/system/2019/09/20/drobne_podpowiedzi_2.html#po-pierwszej-instalacji-ms-office)
* [Obrazy z PDF w DOCX](https://andrzejq.github.io/Office_S_Tips/pdf_docx/2019/09/23/z_PDF_do_DOCX.html)
* [Problem ogromnego rozmiaru plików RTF i DOC](https://andrzejq.github.io/Office_S_Tips/system/2019/09/20/drobne_podpowiedzi_2.html#problem-ogromnego-rozmiaru-plik%C3%B3w-rtf-i-doc)

<style> code {font-size: 0.93em;}  div.zmniejsz code {font-size: 0.88em;}  </style>
