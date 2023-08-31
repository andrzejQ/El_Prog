---
layout: post
title:  "PowerShell - wyodrębnianie plików z XML"
date:   2021-03-22 08:55:00 +0100
categories: Programowanie
---

Wyodrębnianie plików-załączników zakodowanych jako base64 w XML * [Hybrydowy skrypt 1.CMD (CMD-PowerShell)]({{site.url}}{{site.baseurl}}{{page.url}}#hybrydowy-skrypt-1cmd-cmd-powershell)

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

Na tej stronie www można też sprawdzić podpis i wyodrębnić podpisane dokumenty - ale chyba tylko z pojedynczego pliku XML, więc powyższy skrypt może się przydać, gdy jest więcej plików XML.

Powyższy skrypt wygodnie jest  używać jako ([_zob. objaśnienie_]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2021-03-22-Hybrydowy_skrypt_CMD-Powershell %})):

#### Hybrydowy skrypt 1.CMD (CMD-PowerShell)



Skrypt o przykładowej nazwie `1.cmd` wyodrębniający pliki wewnętrzne z wszystkich  `*.xml` może wyglądać tak:

````powershell
@chcp 65001>nul&more +1 "%~f0"|powershell -&pause&goto:eof
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

(zob. też [_problem małej czcionki w oknie konsoli_]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2021-03-22-Hybrydowy_skrypt_CMD-Powershell %}#kodowanie-utf-8-czcionka-raczej-inna-niż-consolas))
{: style="font-size: smaller;"}

Taki skrypt można uruchomić wprost z eksploratora plików:

![FileExplorer-1.cmd.png]({{site.baseurl}}/assets/img/FileExplorer-1.cmd.png "FileExplorer-1.cmd.png"){: style="float:right;width:242px;"} 
1. Przygotuj sobie pusty folder roboczy.
2. W tym folderze utwórz plik `1.cmd` o treści jak powyżej (np. użyj notatnika, kodowanie utf-8). <sup>*)</sup>
3. Do tego foldera skopiuj pliki XML z których mają być wyodrębnione pliki wewnętrzne. 
4. W pasku adresu, gdzie zwykle znajduje się zapis ścieżki do foldera wpisz `1.cmd` i naciśnij `[Enter]`.
5. Poczekaj dłuższą chwilę, aż pojawi się napis `==koniec==` i naciśnij `[Enter]`.
6. W folderze powinny pojawić się wyodrębnione pliki wewnętrzne.


<sup>*)</sup> <small>Jeszcze lepszym sposobem jest umieszczenie pliku `1.cmd` w jednej ze ścieżek Path (w menu START zacznij pisać “Edytuj zmienne środowiskowe dla konta” aby zobaczyć/edytować listę ścieżek). Wtedy krok 2 jest zbędny.</small> 

- - - -

Odnośniki:
* <https://www.powershellmagazine.com/2013/08/19/mastering-everyday-xml-tasks-in-powershell/>
* <https://dotnet-helpers.com/powershell/reading-xml-files-with-powershell/>
* <https://andrzejq.github.io/Office_S_Tips/pki/2019/09/19/Podpisy_cyfrowe.html>


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