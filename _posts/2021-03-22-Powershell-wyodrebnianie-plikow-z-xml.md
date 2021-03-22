---
layout: post
title:  "PowerShell - wyodrębnianie plików z XML"
date:   2021-03-22 08:55:00 +0100
categories: Programowanie
---

Szablon do wyodrębniania plików-załączników zakodowanych jako base64 w XML * [Hybrydowy plik CMD-PowerShell]({{ site.url }}{{ site.baseurl }}{{ page.url }}#hybrydowy-plik-cmd-powershell)

----


Czasem może się przydać wyodrębnianie plików binarnych zakodowanych w XML (base64). Tutaj szkic takiego skryptu o nazwie np. `b64xml.ps1`:

````powershell
                       Set-StrictMode -Version 3
#nazwa pliku:
($xmlFName = "1.xml")
"==================== (poczekaj ...)"
$xmlElm = New-Object -TypeName XML; $xmlElm.Load($xmlFName) 
#$xmlElm # teraz można będzie używac notacji kropkowej
      #/Dokument/TrescDokumentu/Zalaczniki/Zalacznik (skopiowne w N++: XML Tools / Current XML Path)
$xmlElm.Dokument.TrescDokumentu.Zalaczniki.Zalacznik | ForEach-Object {
  ( $nazwaPliku = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String( $_.nazwaPliku )) )
  [System.Convert]::FromBase64String($_.DaneZalacznika) | Set-Content $nazwaPliku -Encoding Byte
}

"==koniec=="
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

Nasz skrypt o przykładowej nazwie `1.cmd` wyodrębniający pliki z `1.xml` może wyglądać tak:

````powershell
@chcp 65001>nul&@findstr/v "^@chcp.* -&goto:eof$" "%~f0"|powershell -&goto:eof
                      Set-StrictMode -Version 3
#nazwa pliku:
($xmlFName = "1.xml")
"==================== (poczekaj ...)"
$xmlElm = New-Object -TypeName XML; $xmlElm.Load($xmlFName) 
#$xmlElm # teraz można będzie używac notacji kropkowej
      #/Dokument/TrescDokumentu/Zalaczniki/Zalacznik (skopiowne w N++: XML Tools / Current XML Path)
$xmlElm.Dokument.TrescDokumentu.Zalaczniki.Zalacznik | ForEach-Object {
  ( $nazwaPliku = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String( $_.nazwaPliku )) )   
  [System.Convert]::FromBase64String($_.DaneZalacznika) | Set-Content $nazwaPliku -Encoding Byte
}

"==koniec=="
````

Dla osób, które nie mają doświadczenia z uruchamianiem takich skryptów można podać przepis:
![FileExplorer-1.cmd.png]({{ site.baseurl }}/assets/img/FileExplorer-1.cmd.png "FileExplorer-1.cmd.png"){:style="float:right;width:242px;"} 
1. W pustym folderze utwórz notatnikiem plik `1.cmd` o trześci jak powyżej.
2. Do tego foldera skopiuj plik XML i zmień jego nazwę na `1.xml`. 
3. W pasku adresu, gdzie zwykle znajduje się zapis ścieżki do foldera wpisz `1.cmd` i naciśnij `[Enter]`
4. Poczekaj dłuższą chwilę, aż zniknie czarne okienko z komunikatami wykonania skryptu.
5. W folderze powinny pojawić się rozpakowane pliki.

----
Odnośniki:
* <https://www.powershellmagazine.com/2013/08/19/mastering-everyday-xml-tasks-in-powershell/>
* <https://dotnet-helpers.com/powershell/reading-xml-files-with-powershell/>


<style> code {font-size: smaller;} </style>