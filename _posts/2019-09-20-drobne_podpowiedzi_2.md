---
layout: post
title:  "Drobne podpowiedzi 2"
date:   2019-09-20 10:21:59 +0100
categories: System
---

[Tekst z komputera przez QR-kod do tel. kom.]({{ site.url }}{{ site.baseurl }}{{ page.url }}#szybkie-przenoszenie-niewielkiego-tekstu-z-komputera-do-tel-komórkowego) * [Po pierwszej instalacji MS Office]({{ site.url }}{{ site.baseurl }}{{ page.url }}#po-pierwszej-instalacji-ms-office) * [Hurtowe zmniejszanie dużych obrazów *.jpg]({{ site.url }}{{ site.baseurl }}{{ page.url }}#hurtowe-zmniejszanie-dużych-obrazów-jpg) * [Problem ogromnego rozmiaru plików RTF i DOC]({{ site.url }}{{ site.baseurl }}{{ page.url }}#problem-ogromnego-rozmiaru-plików-rtf-i-doc)

----
### Szybkie przenoszenie niewielkiego tekstu z komputera do tel. komórkowego:

W edytorze tekstu [**Notatnik++**](https://notepad-plus-plus.org/downloads/) zainstaluj wtyczkę **NppQrCode** (menu: Wtyczki \ Plugins Admin...)

1. Zaznacz fragment tekstu i kliknij ikonę wtyczki ![NppQrCode.png]({{ site.baseurl }}/assets/img/NppQrCode.png "NppQrCode.png"){:style="width:10em;"} <br><small>Zamiast N++ można też użyć 1-plikowej mini-aplikacji [QR Code generator](https://andrzejq.github.io/Jekyll_app1htmlFile/jekyll/update/2019/01/21/Aplikacje_html.1.html#qr-code---generator-i-czytnik-off-line).</small>
 
2. W tel. komórkowym włącz aparat i nakieruj go na QR-kod (nie rób zdjęcia, tylko poczekaj na złapanie ostrości). Gdy pojawi się przycisk `( X Pokaż dane )` dotknij go i skopiuj tekst do schowka, a potem gdzieś wklej.  
<small>Są też specjalistyczne aplikacje do odczytywania QRkodu, np. **Czytnik Kodów QR i paskowych** / TeaCaps.</small>

Pamiętaj: Notatnik++ to jeden edytorów tekstowych w którym można włączyć wtyczki:
* **DSpellCheck** - z automatycznym sprawdzaniem pisowni; można nawet nie instalować słownika, a w ustawieniach włączyć _Library_: Native(Windows)
* **Compare** - porównuje teksty 2 plików (nawet nie muszą być zapisane); w MS Word też można porównywać pliki, ale tutaj można szybciej coś skopiować (np. z DOCX czy PDF) i teksty nie muszą być zapisane; dodatkowo mamy porównywany tylko czysty tekst (samą treść)
* Wykrywane są w tekście odnośniki do stron `http://` i `https://`, które stają się klikalne - otwierają stronę w przeglądarce.
* W _znajdź / zamień_ działają wyrażenia regularne.

- - - -

### Po pierwszej instalacji MS Office

Pliki konfiguracji w paczce

[**MS_office_exportedUI.zip**]({{ site.baseurl }}/assets/files/MS_office_exportedUI.zip)

("Dostosowania programu Word 2013.exportedUI", "Dostosowania programu Excel 2013.exportedUI", "MSO1045.acl") pochodzą z MS Office 2013, ale zdaje się zadziałają także w innych wersjach.

![Word-Opcje-Pasek.png]({{ site.baseurl }}/assets/img/Word-Opcje-Pasek.png "Word-Opcje-Pasek.png"){:style="float:right;width:77%;"} 
Pliki "*..exportedUI" można zaimportować poprzez `Plik \ Opcje \ Pasek ... \ Importuj` i nad wstążką pojawią się ikony szybkiego dostępu dla operacji jak "Zapisz jako...", "Podgląd wydruku" czy "Wklej specjalnie".
![Excel-Opcje-Pasek.png]({{ site.baseurl }}/assets/img/Excel-Opcje-Pasek.png "Excel-Opcje-Pasek.png"){:style="width:77%;"} 

- - - -

![Autokorekta.png]({{ site.baseurl }}/assets/img/Autokorekta.png "Autokorekta.png"){:style="float:right;width:60%;"} 
Jeśli nie przepadasz za agresywną autokorektą w MS Office to kopiując plik `MSO1045.acl`  do fodlera `%appdata%\Microsoft\Office` uzyskasz skrócony słownik autokorekty (1045 to wersja dla j.polskiego).


![MSO1045.acl.png]({{ site.baseurl }}/assets/img/MSO1045.acl.png "MSO1045.acl.png"){:style="width:30%;"} 



<br>
- - - -

### Hurtowe zmniejszanie dużych obrazów *.jpg

Gdy chcemy zapamiętać roczną kopię zdjęć, przesłać zdjęcia na dysk sieciowy czy przekazać do oglądania na pendrive to bardzo przydaje się zmniejszenie rozmiaru plików naszych obrazów, do takich, że jakość oglądania jest doskonała, a równocześnie szybko się je kopiuje i wczytuje.

Wtedy może przydać się 

* hurtowe zmniejszanie dużych obrazów `*.jpg` (>4MB) do 50% wymiaru (i wielokrotnie mniejszej pojemności) w aktualnie otwartym folderze i  jego wszystkich podfolderach
    * (można ustawić `set DUZY=4000000` na inną wartość w `r.cmd`).

#### Instalacja

1. Potrzebne jest wcześniejsze zainstalowanie <https://www.irfanview.com/> (darmowy do użytku domowego i niekomercyjnego)
2. Wypakuj [**i_view_advancedbatch.zip**]({{ site.baseurl }}/assets/files/i_view_advancedbatch.zip) i zamień/skopiuj plik [`r.txt`]({{ site.baseurl }}/assets/files/r.cmd.txt) na `r.cmd`.
3. Umieść pliki `r.cmd` i `i_view32.ini` oraz/lub `i_view64.ini` gdzieś, gdzie wskazuje PATH (w menu START zacznij pisać "Edytuj zmienne środowiskowe dla konta")  
 ... albo w folderze z obrazami *.jpg lub folderze nadrzędnym, z którego będziemy uruchamiali skrypt.

Plik `i_view...ini` jest gotowy, ale można go też utworzyć z innymi, swoimi ustawieniami w IfranView:

     Plik \ Przetwarzanie wsadowe (seryjne) \ Opcja zaawansowane... \ 
       opcjonalnie - [Ładuj ustawienia]
       [Zapisz ustawienia]

![i_view_ini.png]({{ site.baseurl }}/assets/img/i_view_ini.png "i_view_ini.png"){:style="float:right;width:77%;"} 
Załadowanie ustawień pozwala na podgląd tego co jest wpisane w `i_view...ini` ->

#### Użytkowanie

**Uwaga - wypróbuj najpierw działanie na kopii danych!**

Wpisz

    r.cmd

w pasku eksploratora plików w aktualnie otwartym folderze w którym lub poniżej którego są obrazy `*.jpg` i naciśnij [Enter].
Nastąpi automatyczne zmniejszenie wszystkich dużych `*.jpg`, także w podfolderach - poczekaj i na zakończenie naciśnij dowolny klawisz.
![cmd-exe.png]({{ site.baseurl }}/assets/img/cmd-exe.png "cmd-exe.png"){:style="float:right;width:33%;"} 
![r-cmd.png ]({{ site.baseurl }}/assets/img/r-cmd.png  "r-cmd.png "){:style="float:right;width:22%;"} 

<br>

- - - -

### Problem ogromnego rozmiaru plików RTF i DOC

... po wstawieniu grafiki PNG, GIF lub JPEG w programie MS Word.

![ExportPictureWithMetafile-0.png ]({{ site.baseurl }}/assets/img/ExportPictureWithMetafile-0.png  "ExportPictureWithMetafile-0.png "){:style="float:right;width:66%;"} 
Zapisanie dokumentu programu Microsoft Word z grafiką EMF, PNG, GIF lub JPEG w innym formacie pliku (tj. nie docx), na przykład formacie programu Word 6.0/95 (*.doc) lub Tekst sformatowany RTF (*.rtf)), może znacznie zwiększyć rozmiar pliku dokumentu, gdyż powstaje dodatkowa, niespakowana kopia grafiki.
Aby zapobiec zapisywaniu przez program Word dwóch kopii grafiki w dokumencie i zmniejszyć rozmiar pliku dokumentu należy dodać nową wartość ciągu **ExportPictureWithMetafile=0** w rejestrze systemu Microsoft Windows (uwaga - działaj z ostrożnościową w programie "regedit.exe" = Edytor rejestru):

`HKEY_CURRENT_USER\Software\Microsoft\Office\xx.x\Word\Options`

**xx.x** to aktualny numer wersji MS Office (na ogół najwyższy, jeśli jest kilka).
 
