---
layout: post
title:  "PowerShell - wyodrębnianie plików z XML"
date:   2021-03-22 08:55:00 +0100
categories: Programowanie
---

Wyodrębnianie plików-załączników zakodowanych jako base64 w XML * [Hybrydowy skrypt 1.CMD (CMD-PowerShell)]({{ site.url }}{{ site.baseurl }}{{ page.url }}#hybrydowy-skrypt-1cmd-cmd-powershell)

----


Niekiedy może się przydać wyodrębnianie plików binarnych zakodowanych w XML (base64). Tutaj szkic takiego skryptu o nazwie np. `b64xml.ps1`, który przetwarza wszystkie pliki XML z bieżącego foldera:

````powershell
$i=0;                                                  Set-StrictMode -Version 3
ForEach ($plikXml in Get-ChildItem '.' -Filter *.XML) {
  ++$i; "`n$i.$($plikXml.FullName)"
  "==================== (poczekaj ...)"
  $xmlElm = New-Object -TypeName XML; $xmlElm.Load($plikXml.FullName) 
  #$xmlElm # teraz można będzie używac notacji kropkowej
        #/Dokument/TrescDokumentu/Zalaczniki/Zalacznik (skopiowne w N++: XML Tools / Current XML Path)
  $xmlElm.Dokument.TrescDokumentu.Zalaczniki.Zalacznik | ForEach-Object {
    ($nazwaPliku = "$i."+[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String( $_.nazwaPliku )))
    [System.Convert]::FromBase64String($_.DaneZalacznika) | Set-Content $nazwaPliku -Encoding Byte
  }
}

"`n==koniec=="
````

Ten skrypt działa na pliki XML podpisane profilem zaufanym - zob.:  
-> <https://www.gov.pl/web/gov/podpisz-dokument-elektronicznie-wykorzystaj-podpis-zaufany>

Na tej stronie www można też sprawdzić podpis i wyodrębnić podpisane dokumenty - ale chyba tylko z pojedynczego pliku XML, więc powyższy skrypt może się przydać, gdy jest więcej plików XML (zob. też `1.cmd` poniżej).

### Hybrydowy plik CMD-PowerShell

Można podczas wywoływania Powershell można skorzystać hybrydowego pliku CMD-Powershell, tj. pliku *.CMD, który nie wymaga odblokowania uruchamiania skryptu `*.ps1` - po prostu zadziała u każdego. Np.: 

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

Pierwszy wiersz przekazuje zawartość pliku - tego który jest właśnie uruchomiony (`"%~f0"`), jako strumień do (`|powershell -`) z pominięciem pierwszego wiersza (`findstr/v ...`). Na koniec są wywoływane jeszcze polecenia `pause` i `goto:eof`.

#### Hybrydowy skrypt 1.CMD (CMD-PowerShell)

Skrypt o przykładowej nazwie `1.cmd` wyodrębniający pliki wewnętrzne z wszystkich  `*.xml` może wyglądać tak:

````powershell
@chcp 65001>nul&@findstr/v "^@chcp.*&goto:eof$" "%~f0"|powershell -&pause&goto:eof
$i=0;                                                  Set-StrictMode -Version 3
ForEach ($plikXml in Get-ChildItem '.' -Filter *.XML) {
  ++$i; "`n$i.$($plikXml.FullName)"
  "==================== (poczekaj ...)"
  $xmlElm = New-Object -TypeName XML; $xmlElm.Load($plikXml.FullName) 
        #/Dokument/TrescDokumentu/Zalaczniki/Zalacznik (skopiowne w N++: XML Tools / Current XML Path)
  $xmlElm.Dokument.TrescDokumentu.Zalaczniki.Zalacznik | ForEach-Object {
    ($nazwaPliku = "$i."+[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String( $_.nazwaPliku )))
    [System.Convert]::FromBase64String($_.DaneZalacznika) | Set-Content $nazwaPliku -Encoding Byte
  }
}

"`n==koniec=="
````

Osoby, które nie mają doświadczenia z uruchamianiem takich skryptów mogą skorzystać z przepisu:

![FileExplorer-1.cmd.png]({{ site.baseurl }}/assets/img/FileExplorer-1.cmd.png "FileExplorer-1.cmd.png"){:style="float:right;width:242px;"} 
1. W pustym folderze utwórz plik `1.cmd` o treści jak powyżej (np. użyj notatnika). <sup>*)</sup>
2. Do tego foldera skopiuj pliki XML z których mają być wyodrębnione pliki wewnętrzne. 
3. W pasku adresu, gdzie zwykle znajduje się zapis ścieżki do foldera wpisz `1.cmd` i naciśnij `[Enter]`.
4. Poczekaj dłuższą chwilę, aż pojawi się napis `==koniec==` i naciśnij `[Enter]`.
5. W folderze powinny pojawić się wyodrębnione pliki wewnętrzne.


<sup>*)</sup> <small>Jeszcze lepszym sposobem jest umieszczenie pliku `1.cmd` w jednej ze ścieżek Path (w menu START zacznij pisać “Edytuj zmienne środowiskowe dla konta” aby zobaczyć/edytować listę ścieżek). Wtedy krok 1 jest zbędny.</small> 

- - - -

Odnośniki:
* <https://www.powershellmagazine.com/2013/08/19/mastering-everyday-xml-tasks-in-powershell/>
* <https://dotnet-helpers.com/powershell/reading-xml-files-with-powershell/>
* <https://andrzejq.github.io/Office_S_Tips/pki/2019/09/19/Podpisy_cyfrowe.html>


<style> code {font-size: smaller;} </style>