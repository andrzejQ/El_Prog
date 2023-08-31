---
layout: post
title:  "PowerShell 5.1 - wiersz CSV z cudzysłowami, gdy potrzeba"
date:   2020-11-24 09:00:00 +0100
categories: Programowanie
---

Funkcja PowerShell 5.1 - konwersja do wiersza CSV z opcjonalnym otaczaniem cudzysłowami.

Standardowo w PowerShell 5.1 konwersja do CSV powoduje zawsze otaczanie każdej komórki cudzysłowami. Nie działa -UseQuotes AsNeeded z v.7.

Plik [**convToCsvRow.ps1**(.zip)]({{site.baseurl}}/assets/files/convToCsvRow.zip "convToCsvRow.zip") zawiera funkcję do scalania tablicy łańcuchów w wiersz CSV.

````powershell
function encCsvRow {param( [string[]]$strArr ) #dodaje okalające cudzysłowy, gdy trzeba i łączy wiersz CSV
  ($strArr | foreach {$s = $_ -replace '"','""'; if ($s -match '[;"\r\n]') {$s = "`"$s`""}; $s}) -join ";" 
}#encCsvRow @("abc","`"ab`"c;ą`r`nć",'ef"g','h,i','j;k') 
#        ->     abc;"""ab""c;ą`r`nć";"ef""g";h,i;"j;k"  , gdzie `r`n = nowy wiersz
````

Czasem może się też przydać usuwanie znaków wymuszających cudzysłowy:

````powershell
function clrCsv { param( [string[]]$strArr ) 
# usuwa znaki wymuszające cudzysłowy; gdy '"' nie jest na pocz. to wchodzi dobrze w Excelu
  ($strArr | foreach {$_ -replace ';',',' -replace '[\r\n]','   ' -replace '^"',' "'}) -join ";"
}#clrCsv @("abc","`"ab`"c;ą`r`nć",'ef"g','h,i','j;k') 
#     ->      abc; "ab"c,ą      ć;ef"g;h,i;j,k
````
![FileExplorer.png]({{site.baseurl}}/assets/img/FileExplorer.png "FileExplorer.png"){: style="float:right;width:50%;"} 
<small>
Wskazówka - aby uruchomić PowerShell w folderze, w którym znajduje się skrypt - przejdź w Eksploratorze Plików do tego foldera i w pasku adresu wpisz `powershell_ise` lub `powershell.exe` [Enter].
</small>


<style> pre code {font-size: smaller;} </style>

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
