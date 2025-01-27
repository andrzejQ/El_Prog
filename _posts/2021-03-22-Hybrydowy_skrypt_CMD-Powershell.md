---
layout: post
title:  "Hybrydowy skrypt CMD-PowerShell"
date:   2021-03-22 08:45:00 +0100
categories: Programowanie
---

_+ 16.10.2024_{: .date}  
(`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned` - albo skrypt CMD).
<style>.date{font-size: smaller;color:#828282;}</style>

Gdy chcemy uruchamiać skrypty PowerShell `*.ps1` na swoim komputerze, to jednorazowo trzeba wpisać w oknie Powershell (Adminstrator):  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

Podobno ma to być jakieś zabezpieczenie. Chyba nie jest, skoro [można je obejść na 15 sposobów](https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/).

Generalnie można wklejać treść skryptu do konsoli Powershell bez powyższego zezwolenia. 

Można też wykonać polecenie Powershell w jedno-wierszowym skrypcie CMD, np. pliku `c.cmd`:  

````bat
Powershell -NoExit -c "$c=Get-Culture; $c.DateTimeFormat"
````
`-NoExit` - gdy nie chcemy abo po wykonaniu `c.cmd` okno się zamykało;  
po `-c` wewnątrz polecenia  `"..."` można używać napisów `'...'`.
{: style="font-size: smaller;"}


W pliku `cmd` można wyłączyć `-ExecutionPolicy`
````bat
powershell -noexit -ExecutionPolicy Bypass -File MyScript.ps1
````

--------

2024-10-16: W Windows 11 jakoś znika ścieżka do `PowerShell.exe` w zmiennej środowiskowej `PATH` (ale nie na pewno...).  
Czyli prawdopodobnie trzeba ją dodać: `c:\Windows\System32\WindowsPowerShell\v1.0\`
{: style="font-size: smaller;"}

A na pewno trzeba dodać, gdy pojawia się komunikat:  
**'powershell' is not recognized** as an internal or external command, operable program or batch file.
{: style="font-size: smaller;"}

--------
&nbsp;



Można także skorzystać z **hybrydowego pliku CMD-Powershell**, tj. pliku `*.CMD`, który nie wymaga odblokowania uruchamiania skryptów `*.ps1` - po prostu zadziała u każdego. Jest to skrypt PowerShell z dodatkowym wierszem poleceń CMD na początku, np.: 

````powershell
@set pwsh=c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
@chcp 65001>nul&more +2 "%~f0"|%pwsh% -&pause&goto:eof
<#
Tu jest komentarz powershell
Pamiętaj - `more` - nie więcej niż 65536 wierszy.
#>

'Wygląda na to, że po `#>` lub `"@` czy `}` powinien być pusty wiersz lub #...'
${ąćę} = "ĄĆŁĘŃÓŚŹŻ ąćłęńóśźż €" 
"TEST-polskie literki (kodowanie pliku: utf-8 bez BOM) - ${ąćę}" 
@"
===
Uwaga - Ten plik "cmd" należy zapisać w kodowaniu UTF-8.
"@

"==="
````
Pierwszy wiersz to skrót do pełnej ścieżki `PowerShell.exe`.  
Drugi wiersz  pliku `cmd` przekazuje zawartość pliku - tego który jest właśnie uruchomiony (`"%~f0"`), jako strumień poleceń PowerShell (`|powershell -`) z pominięciem pierwszego i drugiego wiersza (`more +2`). Na koniec są wywoływane jeszcze polecenia `pause` i `goto:eof`. Początkowe `chcp 65001` włącza kodowanie UTF-8 i w takim właśnie kodowaniu należy zapisać plik `*.cmd`.  
<small>Wygląda na to, że w Win11 może to być też kodowanie UTF-8 z BOM.</small>

Taki skrypt np. o nazwie `1.cmd` można uruchomić wprost z eksploratora plików:


![FileExplorer-1.cmd.png]({{site.baseurl}}/assets/img/FileExplorer-1.cmd.png "FileExplorer-1.cmd.png"){: style="float:right;width:242px;"} 
1. W wybranym folderze utwórz plik `1.cmd` o treści jak powyżej (np. użyj notatnika, zapisz jako, kodowanie `UTF-8`).
2. W pasku adresu, gdzie zwykle znajduje się zapis ścieżki do foldera wpisz `1.cmd` i naciśnij `[Enter]`. Plik `1.cmd` można umieścić w folderze dodanym do ścieżki PATH i wtedy powyższa metoda zadziała w dowolnym folderze. Zamiast tego wpisywania `1.cmd` można też 2x kliknąć na tym pliku, choć czasem trzeba przejść jednorazowo przez kilka ostrzeżeń.
3. Po wykonaniu skryptu naciśnij `[Enter]` albo zamknij okno wyników.

W **Win11** przed 2024r w domyślnym terminalu czasem nie działały niektóre funkcje w pliku hybrydowym "*.cmd", np. przeskakiwane bywa okienko uwierzytelniania (nie wyskakiwało). Można wtedy użyć "starszej" wersji terminala "**conhost.exe**", czyli wtedy w pasku adresu wpisać
`conhost 1.cmd`
{: style="font-size: smaller;"}

----


#### Polecenie zapisane w skrócie *.LNK

Polecenie 1-wierszowe, które mogło by być w pliku `*.CMD` można też zapisywać w ramach skrótu `*.LNK`. Musi to być 1 wiersz ograniczony do 260 znaków.

Przykład:
````powershell
powershell.exe -NoExit -c "polecenie1 -ErrorAction SilentlyContinue;...;'Zrobione.'"
````
Takie polecenie może mieć maksymalnie 260-43 znaków (-43, bo i tak automatycznie dopisane będzie na początku  
`C:\Windows\system32\WindowsPowerShell\v1.0\`). Na zewnątrz ciągu poleceń oddzielonych `;` musi być `"`, więc w środku warto używać `'` dla łańcuchów.
{: style="font-size: smaller;"}

Tu może się przydać używanie krótszych poleceń PowerShell - lista: `get-alias`
{: style="font-size: smaller;"}




--------
&nbsp;

**Informacja sprzed 2024r - mam nadzieję, że już mało potrzebna:**

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

W **Win11** w domyślnym terminalu czasem nie działały niektóre funkcje w pliku hybrydowym "*.cmd", np. przeskakiwane bywa okienko uwierzytelniania (nie wyskakuje). Można wtedy użyć "starszej" wersji terminala "**conhost.exe**", czyli wtedy w pasku adresu należy wpisać:
`conhost 1.cmd`

----

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

-------
.

* zob. też [PowerShell-sciągawka]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2020-11-24-PowerShell-sciagawka %})

<style> code {font-size: smaller;} </style>

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
