---
layout: post
title:  "Hybrydowy skrypt CMD-PowerShell"
date:   2021-03-22 08:45:00 +0100
categories: Programowanie
---


(`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned` - albo skrypt CMD).
{:style="font-size: smaller;"}

Gdy chcemy uruchamiać skrypty PowerShell `*.ps1` na swoim komputerze, to jednorazowo trzeba wpisać w oknie Powershell (Adminstrator):  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

Podobno ma to być jakieś zabezpieczenie. Chyba nie jest, zwłaszcza, że [można to obejść na 15 sposobów](https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/).

Generalnie można wklejać treść skryptu do konsoli Powershell bez powyższego zezwolenia. 

Można też wykonać polecenie Powershell w jedno-wierszowym skrypcie CMD, np. pliku `c.cmd`:  

````bat
Powershell -NoExit -c "$c=Get-Culture; $c.DateTimeFormat"
````
`-NoExit` - gdy nie chcemy abo po wykonaniu `c.cmd` okno się zamykało; wewnątrz `"..."` wygodnie jest używać `'...'`.
{:style="font-size: smaller;"}


Można także skorzystać z **hybrydowego pliku CMD-Powershell**, tj. pliku `*.CMD`, który nie wymaga odblokowania uruchamiania skryptów `*.ps1` - po prostu zadziała u każdego. Jest to skrypt PowerShell z dodatkowym wierszem poleceń CMD na początku, np.: 

````powershell
@chcp 1250>nul&more +1 "%~f0"|powershell -&pause&goto:eof
<#
Tu jest komentarz powershell
Pamiętaj - `more` - nie więcej niż 65536 wierszy.
#>

'Wygląda na to, że po `#>` lub `"@` czy `}` powinien być pusty wiersz lub #...'
${ąćę} = "ĄĆŁĘŃÓŚŹŻ ąćłęńóśźż €" 
"TEST-polskie literki (kodowanie pliku: utf-8 bez BOM) - ${ąćę}" 
@"
===
Uwaga - Ten plik "cmd" należy zapisać w kodowaniu ANSI (cp1250, Central European (Windows)).
"@

"==="
````

Pierwszy wiersz  pliku `cmd` przekazuje zawartość pliku - tego który jest właśnie uruchomiony (`"%~f0"`), jako strumień poleceń PowerShell (`|powershell -`) z pominięciem pierwszego wiersza (`more +1`). Na koniec są wywoływane jeszcze polecenia `pause` i `goto:eof`. Początkowe `chcp 1250` włącza kodowanie ANSI.

Taki skrypt np. o nazwie `1.cmd` można uruchomić wprost z eksploratora plików:


![FileExplorer-1.cmd.png]({{ site.baseurl }}/assets/img/FileExplorer-1.cmd.png "FileExplorer-1.cmd.png"){:style="float:right;width:242px;"} 
1. W wybranym folderze utwórz plik `1.cmd` o treści jak powyżej (np. użyj notatnika, zapisz jako, zmień kodowanie z `UTF-8` na `ANSI`).
2. W pasku adresu, gdzie zwykle znajduje się zapis ścieżki do foldera wpisz `1.cmd` i naciśnij `[Enter]`. Plik `1.cmd` można umieścić w folderze dodanym do ścieżki PATH i wtedy powyższa metoda zadziała w dowolnym folderze. Zamiast tego wpisywania `1.cmd` można też 2x kliknąć na tym pliku, choć czasem trzeba przejść jednorazowo przez kilka ostrzeżeń.
3. Po wykonaniu skryptu naciśnij `[Enter]` albo zamknij okno wyników.

#### Kodowanie "utf-8", czcionka raczej inna niż "Consolas"

Obecnie Notatnik Windows przyjmuje domyślnie kodowanie tekstu "utf-8" - i bardzo dobrze.
Dla takiego kodowania właściwe jest przełączenie strony kodowej skryptu na `utf-8` tj. `chcp 65001`:

````powershell
@chcp 65001>nul&more +1 "%~f0"|powershell -&pause&goto:eof
<#
Tu jest komentarz powershell
Pamiętaj - `more` - nie więcej niż 65536 wierszy.
#>

'Wygląda na to, że po `#>` lub `"@` czy `}` powinien być pusty wiersz lub #...'
${ąćę} = "ĄĆŁĘŃÓŚŹŻ ąćłęńóśźż €" 
"TEST-polskie literki (kodowanie pliku: utf-8 bez BOM) - ${ąćę}" 
@"
===
Uwaga - w nowej wersji konsoli Win10 - czcionka `"Consolas`" jakoś przełącza się 
na mikroczcionkę rastrową po wywołaniu Powershell przy chcp 65001 (=utf-8).
Ale np. `"Source Code Pro Medium`" działa dobrze.
Wystarczy jednorazowo zmienić na taką czcionkę "Właściwości" tego okna konsoli 
(lewy, górny róg) zanim się go zamknie. Taka zmiana jest pamiętana w przyszłości.
"@

"==="
````

Pojawiają się drobne problemy z czcionką konsoli, które można zlikwidować zmieniając czcionkę np. na "Source Code Pro Medium" jak opisano powyżej.

Można też włączyć domyślne kodowanie UTF-8 dla wszyskich plików bez początkowego BOM - które dotąd były traktowane jako kodowanew ANSI lub OEM:
<https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window>
(nie testowałem).

Nowa aplikacja terminala Microsoft [Windows Terminal](https://www.microsoft.com/pl-pl/p/windows-terminal-preview/9n0dx20hk701)
obsługuje domyślnie UTF-8. W Windows 10 trzeba ją zainstalować. 

W Win 11 ten terminal jest domyślnie instalowany i domyślnie uruchamia się powershell, czcionka "Cascadia Mono". A jednak domyślnie ma ustawione archaiczne kodowanie OEM (chcp -> 852). 
Można zmienić [konfigurację startową powershell](https://stackoverflow.com/questions/49476326/displaying-unicode-in-powershell/49481797) wpisując 
```powershell
$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding
```

Nazwa pliku konfiguracji jest w zmiennej `$PROFILE`, która ma typowo wartość: `<moje dokumenty>\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`.

Podobno wersja PowerShell 7 nie ma tej wady z podmianą czcionki.

#### Polecenie zapisane w skrócie *.LNK

Polecenie 1-wierszowe, które mogło by być w pliku `*.CMD` można też zapisywać w ramach skrótu `*.LNK`. Musi to być 1 wiersz ograniczony do 260 znaków.

Przykład:
````powershell
powershell.exe -NoExit -c "polecenie1 -ErrorAction SilentlyContinue;...;'Zrobione.'"
````
Takie polecenie może mieć maksymalnie 260-43 znaków (-43, bo i tak automatycznie dopisane będzie na początku 
`C:\Windows\system32\WindowsPowerShell\v1.0\`). Na zewnątrz ciągu poleceń oddzielonych `;` musi być `"`, więc w środku warto używać `'` dla łańcuchów.
{:style="font-size: smaller;"}

Tu może się przydać używanie krótszych poleceń PowerShell - lista: `get-alias`
{:style="font-size: smaller;"}





<style> code {font-size: smaller;} </style>