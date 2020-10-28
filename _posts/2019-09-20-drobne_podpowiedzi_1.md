---
layout: post
title:  "Drobne podpowiedzi 1 (system)"
date:   2019-09-20 09:21:59 +0100
categories: System
---

[Ostatnio używane foldery]({{ site.url }}{{ site.baseurl }}{{ page.url }}#ostatnio-używane-foldery) * [Zwalnianie miejsca na dysku C:]({{ site.url }}{{ site.baseurl }}{{ page.url }}#zwalnianie-miejsca-na-dysku-c) * [Hurtowa zmiana daty folderów]({{ site.url }}{{ site.baseurl }}{{ page.url }}#hurtowa-zmiana-daty-folderów) * [Hurtowa zmiana daty, a także nazwy zdjęć/filmów]({{ site.url }}{{ site.baseurl }}{{ page.url }}#hurtowa-zmiana-daty-zdjęć-i-filmów-na-podstawie-metadanych)

----

### Ostatnio używane foldery 

.. to trochę co innego niż *często używane foldery*, które pojawiają się po włączeniu (Win+E) eksploratora plików.

![Przypnij_do_szybki_dostep.png]({{ site.baseurl }}/assets/img/Przypnij_do_szybki_dostep.png "Przypnij_do_szybki_dostep.png"){:style="float:right;width:35%;"}
Kroki w celu dodania do paska "szybki dostęp":

1. Win+R, wklej  
   `shell:::{22877a6d-37a1-461a-91b0-dbda5aaebc99}`   `[OK]`
2. Menu: "Przypnij do paska szybki dostęp".
3. Inne własne ważne foldery też wato tak przypiąć.

<br>

----
### Zwalnianie miejsca na dysku C:

W Win 10 jest wbudowanych kilka ciekawych opcji zwalniania miejsca na dysku C:

<https://support.microsoft.com/pl-pl/help/12425/windows-10-free-up-drive-space>

![Start-ustawienia.png]({{ site.baseurl }}/assets/img/Start-ustawienia.png "Start-ustawienia.png"){:style="float:left;width:8%;margin-right:3%;"}
* [Win + i]  albo Start \ Ustawienia
    * System \ Pamięć \

1. ![Zwolnij_miejsce_teraz.png]({{ site.baseurl }}/assets/img/Zwolnij_miejsce_teraz.png "Zwolnij_miejsce_teraz.png"){:style="float:right;width:45%;"} Skonfiguruj Czujnik pamięci lub uruchom go teraz <small>(albo: Zmień sposób zwalniania miejsca)</small> \ Zwolnij miejsce teraz \ Oczyść teraz
2. 

![Zmien_lok_zapisywania.png]({{ site.baseurl }}/assets/img/Zmien_lok_zapisywania.png "Zmien_lok_zapisywania.png"){:style="width:50%;"}


Można tu też wspomnieć o możliwości przesuwania foldera na inny dysk z dysku systemowego (np. gdy mamy mały dysk SSD) i [tworzeniu dowiązania](https://leniwy.eu/news,10,Linki-symboliczne-w-Windowsie.html#Windows-a-linki) udającego, że folder jest na dysku systemowym 

Przykład w linii poleceń Windows (uruchom CMD)
````bat
C:\mklink /j "C:\NazwaPseudoFoldera" "D:\Scieżka\NazwaIstniejącegoFoldera"
````

<br>

----

### Hurtowa zmiana daty folderów

Podczas kopiowania zawartości dysku, np. po zakupie nowego komputera, na ogół wszystkie foldery uzyskują datę z momentu kopiowania. Na nasze szczęście pliki mają prawdziwe daty, ale gubienie faktycznych dat dla folderów jest kłopotliwe. Przecież nie raz chcemy coś przeszukać i nie musielibyśmy zaglądać do folderów, które nie mają dat w interesującym nas zakresie.

![Touch32.gif]({{ site.baseurl }}/assets/img/Touch32.gif "Touch32.gif"){:style="float:right;width:55%;"}

Można do tego wykorzystać aplikację, która potrafi ustawiać datę folderu na na podstawie dat plików/folderów wewnętrznych. Przykładem jest mój programik [**Touch32.exe**](https://pei.prz.edu.pl/~kubaszek/freeware/index_pl.html).

Aby dopasować daty folderów do plików i folderów wewnętrznych należy w jednej ze ścieżek **Path**  <small>(w menu START zacznij pisać "Edytuj zmienne środowiskowe dla konta" aby zobaczyć listę ścieżek)</small> umieścić plik `Touch32.exe` oraz [`dt.cmd`]({{ site.baseurl }}/assets/files/dt.cmd.txt) o zawartości jak poniżej (dla wygody nazwa powinna być dość krótka). W Eksploratorze plików 
![Eksplorator_dt.png]({{ site.baseurl }}/assets/img/Eksplorator_dt.png "Eksplorator_dt.png"){:style="float:left;width:40%;"}
ustawiamy się w folderze dla którego (i dla podfolderów) chcemy zmienić datę. W pasku adresu 
(tam gdzie jest "Ten komputer") wpisujemy `dt.cmd 0` albo krócej `dt 0` i następuje wykonanie skryptu. (Jednak lepiej nie pomijać `.cmd`). Najpierw podfoldery są ustawiane na datę 1980-01-01, a potem na datę jak najnowszy wewnętrzny plik lub folder.

````bat
@echo off & chcp 1250
:: Set date and time for folder like it newest file or folder
if [%1] EQU [0] for /D /r %%G in (*.*) do Touch32.exe "%%G" 1980-01-01
if [%1] NEQ [1] for /D /r %%G in (*.*) do call :DirLastFile "%%G"
call :DirLastFile "."
goto:eof
:DirLastFile
  for /f "tokens=*" %%i in ('dir "%~1\*.*" /b/o-d') do (
    Touch32.exe "%~1" /f "%~1\%%~i" & exit /b )
  Touch32.exe "%~1" 1980-01-01
````

W tym skrypcie przeglądane są foldery wewnętrzne oraz bieżący i wykonywana jest dla nich procedura `DirLastFile`.
* W procedurze `DirLastFile` odbywa się zamiana daty folderu na 
	* datę najnowszego pliku/folderu wewnętrznego
	* albo 1980-01-01, gdy dany folder jest pusty
	* Pętla `for /f` przebiega po liście plików/folderów posortowanych od daty najnowszej `/o-d` i jest przerywana przy pierwszym elemencie `& exit /b`. Ten element jest referencją dla daty folderu podanego jako parametr tej procedury. 
* Jeśli trzeba podglądnąć co się dzieje to należy zamienić  `goto:eof` na `pause&goto:eof`. Można też pominąć `& chcp 1250`. 
* Gdy w ramach folderu są tylko podfoldery i nie ma plików, to w zależności od kolejności przeglądania folderów data aktualnego folderu może pozostać nie uaktualniona. Można wtedy wykonać ponownie skrypt  `dt.cmd` (bez parametru 0 - który jest używany jednorazowo na początek). A najlepiej wejść do wewnątrz foldera, który nie skorygował daty i tam wykonać ten skrypt `dt.cmd`. 
* `dt.cmd 1` wykona szybkie działanie nierekurencyjne - tylko dla bieżącego folderu dostosuje jego datę dla najnowszego pliku lub folderu wewnętrznego.

<small>
Uwaga - program *Touch32* nie jest gruntownie przetestowany – używasz go na własną odpowiedzialność  (nie ma zbyt wielu użytkowników, choć jeden używa go od wielu lat). Sprawdź jego działanie na początek na niewielkiej na kopii danych. Proszę o kontakt w przypadku zauważenia błędów.
</small>

<small>
Aplikacja _Attribute Changer_ (<https://www.petges.lu/>) pozwala zdaje się na hurtową zmianę czasu modyfikacji folderów na podstawie dat wewnętrznych plików/folderów. Podobno także pozwala na zmianę dat zdjęć na podstawie metadanych. Można monitorować stan tej aplikacji, bo wygląda na to, że jest aktualnie rozwijana. </small>

**Notatki**
{:style="font-size: smaller;"}

<small>1. Zamiast daty początkowej 1980-01-01 można by brać datę z jakiegoś napotkanego pliku wewnątrz folderów ...</small>  
`set "_AnyFile=" & call :FindAnyFile "%CD%"`{:style="font-size: smaller;"}  
`::... use "%_AnyFile%"`{:style="font-size: smaller;"}  
`goto:eof`{:style="font-size: smaller;"}  
`:FindAnyFile`{:style="font-size: smaller;"}  
`for /R %1 %%G in (*.*) do (set "_AnyFile=%%G" & exit /b)`{:style="font-size: smaller;"}


<small>2. Gdyby pobierać tylko listę plików 'dir /a-d' to dla pustego folderu pojawia się napis 'File Not Found', który można przekierować do NUL: '2>NUL', [np.](https://ss64.com/nt/syntax-esc.html#escape):</small>  
`@for /f "tokens=*" %%i in ('dir "EmptyFolder\*.*" /b/o-d/a-d 2^>NUL') do (@echo %%i)`{:style="font-size: smaller;"}

.

### Hurtowa zmiana daty zdjęć i filmów na podstawie metadanych

* [**ExifTool** by Phil Harvey](https://exiftool.org/) to trochę surowo wyglądające narzędzie, ale korzystając z poniższych porad da się go wygodnie używać. Pobieram ZIP, umieszczam zawartość w jednej ze ścieżek **Path**  <small>(w menu START zacznij pisać "Edytuj zmienne środowiskowe dla konta" aby zobaczyć listę ścieżek)</small>. Plik `exiftool(-k).exe`. Kopiuję go na `exiftool.exe`. 
* Tam też tworzę plik [**`et.cmd`**]({{ site.baseurl }}/assets/files/et.cmd.txt) o zawartości jak poniżej (dla wygody nazwa powinna być dość krótka). Będę go używał w  Eksploratorze plików - podobnie jak plik **dt.cmd** powyżej. Wywołanie **et.cmd** w folderze ze zdjęciami/filmami spowoduje, że daty modyfikacji tych plików staną się takie jak w metadanych np. exif.
````bat
exiftool.exe -k "-exif:DateTimeOriginal>FileModifyDate" -if "$exif:DateTimeOriginal" .
````
Opcja `-k` powoduje, że okienko z podsumowaniem działania pocenia nie znika samoczynnie. Należy wypróbować działanie na niewielkiej liczbie plików testowych i potem można usunąć `-k`.  
Polecenie pobiera zapisaną w metadanych datę zdjęcia/filmu (`exif:DateTimeOriginal`) i zapisuje ją (`>`) jako datę modyfikacji pliku (`FileModifyDate`) tylko wtedy (`-if`), gdy taka dana jest dostępna.  
Na końcu polcenia jest kropka `.`, która tu oznacza aktualny folder. Przetwarzaniu będą podlegać pliki znane [ExifTool](https://exiftool.org/) z tego foldera.
Można tu użyć  dowolnej wyliczanki folderów a także plików, np. `*.jpg *.jpeg *.mov *.mp*`. 
* Warto jeszcze wspomnieć o innych przełącznikach [ExifTool](https://exiftool.org/): `-r` operacja dotyczy także podfolderów; `-P` przy operacjach zapisu zachowywana jest pierwotna data modyfikacji pliku.
* Za pomocą [ExifTool](https://exiftool.org/) można skorygować czas pliku, np. przesunąć o +1 godzinę: `exiftool.exe -alldates+=1 -FileModifyDate+=1 .`

### Hurtowa zmiana nazwy zdjęć i filmów

* Można też zmienić nazwę pliku [np. na taką jak data/czas](https://exiftool.org/filename.html#ex0) wykonania zdjęcia/filmu:  
`exiftool.exe -k -P -d "%Y-%m-%d %H-%M-%S%%+c.%%e" "-TestName<DateTimeOriginal" .`{:style="font-size: smaller;"}  
Tutaj dla plików multimedialnych z foldera aktualnego `.` (pamiętaj, że można tu wstawić dowolną listę folderów i plików) jest wytwarzana nazwa pliku/foldera wg. wzorca podanego w `-d` - np. `'2020-03-27 10-44-55.jpg'`. Przy końcu wzorca jest `%%+c`, co poduje dodanie `_1, _2, ...` do nazwy pliku o ile istnieje inny plik o nazwie jak data/czas (właściwie to powinno być `%%-c`, co daje `-1, -2, ...`, ale tutaj `_` jest lepsze). `.%%e` odtwarza oryginalne rozszerzenie pliku. Można tu też sobie dodać `_%%f.%%e`, żeby po dacie wystąpiła oryginalna nazwa pliku. `TestName` to taka testowa nazwa, która pozwala wypróbować działanie bez efektu końcowego. Gdy już przetestujemy działanie to zamieniamy to na `FileName`. We wzorcu można użyć `/`, co spowoduje, że w `FileName` znajdzie się i ścieżka i nazwa pliku. (W Windows do rozdzielania folderów jest używany `\`, ale może być używany`/`, co jest tutaj najwygodniejsze). Aby zapisać takie polecenie w pliku np. [**`fnt.cmd`**]({{ site.baseurl }}/assets/files/fnt.cmd.txt) należy [podwoić znaki `%`](https://ss64.com/nt/syntax-esc.html#escape): 
`exiftool.exe -k -P -d "%%Y-%%m-%%d %%H-%%M-%%S%%%%+c.%%%%e" "-TestName<DateTimeOriginal" .`
* Podobną zmianę nazwy pliku można przeprowadzić na podstawie daty ostatniej modyfikacji pliku; np. [**`fnft.cmd`**]({{ site.baseurl }}/assets/files/fnft.cmd.txt): 
`exiftool.exe -k -ext "*" --ext . -P -d "%%Y-%%m-%%d %%H-%%M-%%S%%%%+c.%%%%e" "-TestName<FileModifyDate" .`  
Użyte tutaj przełączniki `-ext "*" --ext . `  oznaczają [uwzględnianie wszystkich plików](https://exiftool.org/exiftool_pod.html) - nie tylko multimedialnych, choć z pominięciem tych, które nie mają żadnego rozszerzenia.

Powyższe operacje z _ExifTool_ można wpisać w _Total Commander_ do listy poleceń [Start]. Ostatnią kropkę zastępujemy przez `%S` - co będzie oznaczało wykonanie polecenia dla zaznaczonych plików/folderów w oknie _Total Commander_. `exiftool.exe` wpisujemy jako polecenie, a dalsze elementy jako parametry.

Inną pomocą w zapamiętaniu tych kilku poleceń `*.cmd` może być uruchomienie pliku [**`-.cmd`**]({{ site.baseurl }}/assets/files/-.cmd.txt)

- - - -

Przykład - import zdjęć/filmów z telefonu/aparatu z automatyczną zmianą nazwy zdjęcia jak data:

W programie "Zdjęcia" ustawiam import zdjęć/filmów do foldera "Moje obrazy\Camera Roll", który jest w Win10 PL pokazywany jako Moje "obrazy\z aparatu".
* Uruchamiam [**`import-.cmd`**]({{ site.baseurl }}/assets/files/import-.cmd.txt)
* podłączam telefon do komputera i importuję zdjęcia/filmy
* naciskam jakiś klawisz np. SPACJA i następuje automatyczna zmiana nazwy plików na nazwę jak data wykonania np. "2020-03-20 19-44-55.jpg" z przeniesieniem ich do foldera powyżej o nazwie jak rok i dzień np. "../2020/2020-03-20/".




