---
layout: post
title:  "PowerShell - wyodrębnianie plików z XML"
date:   2020-11-24 09:55:00 +0100
categories: Programowanie
---

Szablon do wyodrębniania plików-załączników zakodowanych jako base64 w XML * [Hybrydowy plik CMD-PowerShell]({{ site.url }}{{ site.baseurl }}{{ page.url }}#hybrydowy-plik-cmd-powershell)

----


Czasem może się przydać wyodrębnianie plików binarnych zakodowanych w XML (base64). Tutaj szkic takiego skryptu o nazwie np. `base64inXML.ps1`:

````powershell
#nazwa pliku:
$xmlFName = "base64inXMLfile.xml"

[xml]$xmlElm = Get-Content -Path $xmlFName #teraz można będzie używac notacji kropkowej
      #/Dokument/TrescDokumentu/Zalaczniki/Zalacznik (skopiowne w N++: XML Tools / Current XML Path)
$xmlElm.Dokument.TrescDokumentu.Zalaczniki.Zalacznik | ForEach-Object {
  $nazwaPliku = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String( $_.nazwaPliku ))
  "Zapis do pliku: $nazwaPliku    (poczekaj ...)" #, $_.DaneZalacznika
  [System.Convert]::FromBase64String($_.DaneZalacznika) | Set-Content $nazwaPliku -Encoding Byte
}
"koniec."
````

### Hybrydowy plik CMD-PowerShell

Można podczas wywoływania Powershell można skorzystać hybrydowego pliku CMD-Powershell, tj. pliku *.CMD, który nie wymaga odblokowania uruchamiania skryptu `*.ps1` - po prostu zadziała u każdego. Np.: 

````powershell
@chcp 65001>nul&@findstr/v "^@chcp.* -&goto:eof$" "%~f0"|powershell -&goto:eof
<#
Tu jest komentarz powershell
#>

# Nie wiem dlaczego po `#>` lub `"@` czy `}` musi być pusty wiersz...
${ąćę} = "ĄĆŁĘŃÓŚŹŻ ąćłęńóśźż €" 
"polskie literki (kodowanie pliku: utf-8 bez BOM) - ${ąćę}" 
"test@chcp ... -&goto:eof"
@"
===
Uwaga - w nowej wersji konsoli Win10 - czcionka `"Consolas`" jakoś przełącza 
się na mikroczcionkę rastrową po wywołaniu Powershell. Ale np. 
`"Source Code Pro Medium`" działa dobrze. Już nie trzeba włączać czcionki 
w Default. Pamiętane jest ostatnie ustawienie właściwości.
"@

"==="
````

Pierwszy wiersz przekazuje zawartość pliku - tego który jest właśnie uruchomiony (`"%~f0"`), jako strumień do `|powershell` z pominięciem pierwszego wiersza (`findstr/v ...`). 

Nasz skrypt o przykładowej nazwie `base64inXML.ps1.cmd` wyodrębniający pliki z XML może wyglądać tak:

````powershell
@chcp 65001>nul&@findstr/v "^@chcp.* -&goto:eof$" "%~f0"|powershell -&goto:eof

#nazwa pliku:
$xmlFName = "base64inXMLfile.xml"
 
[xml]$xmlElm = Get-Content -Path $xmlFName #teraz można będzie używac notacji kropkowej
      #/Dokument/TrescDokumentu/Zalaczniki/Zalacznik (skopiowne w N++: XML Tools / Current XML Path)
$xmlElm.Dokument.TrescDokumentu.Zalaczniki.Zalacznik | ForEach-Object {
  $nazwaPliku = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String( $_.nazwaPliku ))
  "Zapis do pliku: $nazwaPliku    (poczekaj ...)"
  [System.Convert]::FromBase64String($_.DaneZalacznika) | Set-Content $nazwaPliku -Encoding Byte
}

"koniec."
````

<style> code {font-size: smaller;} </style>