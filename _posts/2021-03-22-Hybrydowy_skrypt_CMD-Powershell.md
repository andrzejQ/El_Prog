---
layout: post
title:  "Hybrydowy skrypt CMD-PowerShell"
date:   2021-03-22 08:45:00 +0100
categories: Programowanie
---


`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`, albo po prostu skrypt CMD.

Gdy chcemy uruchamiać skrypty PowerShell `*.ps1` na swoim komputerze, to jednorazowo trzeba wpisać w oknie Powershell (Adminstrator):  
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

Podobno ma to być jakieś zabezpieczenie. Chyba nie jest, zwłaszcza, że [można to obejść na 15 sposobów](https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/).

Generalnie można wklejać treść skryptu do konsoli Powershell bez powyższego zezwolenia. 

Można też wykonać polecenie Powershell w jedno-wierszowym skrypcie CMD, np. pliku `c.cmd`:  

````bat
Powershell -NoExit -c "$c=Get-Culture; $c.DateTimeFormat"
````
<small>`-NoExit` - gdy nie chcemy abo po wykonaniu `c.cmd` okno się zamykało; wewnątrz `"..."` wygodnie jest używać `'...'`.
</small>


Można także skorzystać z **hybrydowego pliku CMD-Powershell**, tj. pliku `*.CMD`, który nie wymaga odblokowania uruchamiania skryptów `*.ps1` - po prostu zadziała u każdego. Plik taki poza pierwszym wierszem to skrypt PoweShell. Np.: 

````powershell
@chcp 65001>nul&@findstr/v "^@chcp.*&goto:eof$" "%~f0"|powershell -&pause&goto:eof
<#
Tu jest komentarz powershell
#>

# Nie wiem dlaczego po `#>` lub `"@` czy `}` musi być pusty wiersz...
${ąćę} = "ĄĆŁĘŃÓŚŹŻ ąćłęńóśźż €" 
"polskie literki (kodowanie pliku: utf-8 bez BOM) - ${ąćę}" 
"test@chcp ... &goto:eof"
@"
===
Uwaga - w nowej wersji konsoli Win10 - czcionka `"Consolas`" jakoś przełącza 
się na mikroczcionkę rastrową po wywołaniu Powershell. Ale np. 
`"Source Code Pro Medium`" działa dobrze. Już nie trzeba włączać czcionki 
w Default. Pamiętane jest ostatnie ustawienie właściwości.
"@

"==="
````

Pierwszy wiersz przekazuje zawartość pliku - tego który jest właśnie uruchomiony (`"%~f0"`), jako strumień do (`|powershell -`) z pominięciem pierwszego wiersza (`findstr/v ...`). Na koniec są wywoływane jeszcze polecenia `pause` i `goto:eof`. Początkowe `chcp 65001` włącza kodowanie utf-8.

Taki skrypt np. o nazwie `1.cmd` można uruchomić wprost z eksploratora plików:


![FileExplorer-1.cmd.png]({{ site.baseurl }}/assets/img/FileExplorer-1.cmd.png "FileExplorer-1.cmd.png"){:style="float:right;width:242px;"} 
1. W wybranym folderze utwórz plik `1.cmd` o treści jak powyżej (np. użyj notatnika).
2. W pasku adresu, gdzie zwykle znajduje się zapis ścieżki do foldera wpisz `1.cmd` i naciśnij `[Enter]`.
3. Po wykonaniu skryptu naciśnij `[Enter]` albo zamknij okno wyników.


<style> code {font-size: smaller;} </style>