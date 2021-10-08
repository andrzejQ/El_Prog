---
layout: post
title:  "PowerShell ściągawka"
date:   2020-11-24 07:00:00 +0100
categories: Programowanie
---

Moja ściągawka (zapewne tylko do użytku własnego) ...<br/>
[1: Podstawy                 ]({{ site.url }}{{ site.baseurl }}{{ page.url }}#1-podstawy) &nbsp; 
[2: RegExp                   ]({{ site.url }}{{ site.baseurl }}{{ page.url }}#2-regexp) &nbsp; 
[3: Ustawienia               ]({{ site.url }}{{ site.baseurl }}{{ page.url }}#3-ustawienia) &nbsp; 
[4: Array                    ]({{ site.url }}{{ site.baseurl }}{{ page.url }}#4-array) &nbsp; 
[5: Pliki                    ]({{ site.url }}{{ site.baseurl }}{{ page.url }}#5-pliki) &nbsp; 
[6: Właściwości mutim. plików]({{ site.url }}{{ site.baseurl }}{{ page.url }}#6-właściwości-mutim-plików) &nbsp; 
[# Nie będziesz używał!      ]({{ site.url }}{{ site.baseurl }}{{ page.url }}#-nie-będziesz-używał) &nbsp; 


### 0: <small> *skondensowana przypominajka bez objaśnień* </small>

`($x='coś')` , <code>"2+3=$(2+3)`n"</code> , `@()`, `${a b}`


### 1: Podstawy

`()` - wykonaj teraz, np. `($x='coś')` podstaw i wyświetl  
`$()` - wykonaj teraz i potraktuj jak zmienną, np. `"2+3=$(2+3)"`  
`@()` - potaktuj jako tablicę (także pustą lub 1-el.)  
`, `  - literał tablicy  
`&` - wykonaj  
`. `  - wykonaj skrypt ps1 zapamiętując jego zmienne (spacja po kropce)  
`..` - zakres liczb całk. np. `-5.1..1.9` -eq `-5..1`  
`${}` - nazwa zmiennej z użyciem znaków niedozwolonych w nazwach, np. `${a b}` (ale `$ąćę` jest ok)  
<code>`</code> = `\` w innych językach, choć w PowerShell RegExp jest normalnie `\`

PSCustomObject  
`$myObj=[PSCustomObject]@{Nm='K'}`, `$ht=[ordered]@{Nm='K'};$myObj=[pscustomobject]$ht`  
`$myObj | ConvertTo-Json -depth 10 | Set-Content -Path $Path` - zapis do pliku  
`$myObj=Get-Content -Path $Path | ConvertFrom-Json` - odczyt z pliku  
`$myObj | Add-Member -MemberType NoteProperty -Name 'ID' -Value 'KMarquette'`  
`$myObj | Add-Member @{ID='KMarquette'}` <small>(krótko, ale nie wiem, czy to to samo co powyżej)</small>  
<small>wszystkie własności:</small>  
`$myObj | Get-Member -MemberType NoteProperty | Select -ExpandProperty Name`  
<small>czy własność istnieje?:</small>  
`if( $null -ne $myObj.ID )` lub `if( $myObj.psobject.properties.match('ID').Count )`  
`$myObj.Nm` lub `$myObj.'Nm'` lub `$myObj.$prop` - odczytaj wartość  
`$b=$myObj.psobject.copy()` - prawdziwa kopia (a nie tylko referencja)  

* [PowerShell – mini kompendium](http://tymoteuszkestowicz.com/2013/11/powershell-mini-kompendium/)  -> tymoteuszkestowicz.com
* [PowerShell Operators $( ) @( ) :: &](https://ss64.com/ps/syntax-operators.html)  -> ss64.com
* [Getting started with PowerShell](https://riptutorial.com/powershell)  -> riptutorial.com
* [Powershell: Everything you wanted to know about arrays](https://powershellexplained.com/2018-10-15-Powershell-arrays-Everything-you-wanted-to-know/)  -> powershellexplained.com
* [Everything you wanted to know about PSCustomObject](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-pscustomobject?view=powershell-5.1)  -> docs.microsoft.com
* [PowerShell Commands Every Developer Should Know](https://stackify.com/powershell-commands-every-developer-should-know/)  -> stackify.com


### 2: RegExp

`$a -replace $b,$c` to .NET `Regex.Replace($a, $b, $c, RegexOptions.IgnoreCase)`; `$a.replace($b, $c)` - zwykła zamiana  

* [Regular Expression Language - Quick Reference](https://docs.microsoft.com/pl-pl/dotnet/standard/base-types/regular-expression-language-quick-reference); [Regex.Replace(...)](https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.replace?view=net-5.0); [.NET Replace(String, String), Replace(String, String, StringComparison)](https://docs.microsoft.com/en-us/dotnet/api/system.string.replace?redirectedfrom=MSDN&view=net-5.0#System_String_Replace_System_String_System_String_), [StringComparison](https://docs.microsoft.com/en-us/dotnet/api/system.stringcomparison?view=net-5.0)  -> docs.microsoft.com

### 3: Ustawienia

Przydatne ustawienia  
`Set-StrictMode -Version 3`  
`$ErrorActionPreference = "Stop"` - gdy chcemy na początku nie przeoczyć błędów  
`$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'` - inaczej UTF16 LE BOM, czyli UCS2 LE BOM - też nieźle.  

### 4: Array 

`$myArray = @(); $myArray += '...'` - bardzo powolne; za każdym `+=` kopiuje całą tablicę  
`$myArrList = [System.Collections.ArrayList]@(); [void]$myArrList.Add()` - lista dynamiczna; gdy brak `[void]` do drukuje liczbę elementów  
`$Arr.length` szybko dla tablicy, `$ArrList.count` powolniejsze, używaj dla kolekcji.

`$a=@(11,22,33,44); $a[0,2];`11,33 `@a[0,-1]`11,44 `$a[($a.Count-1)..0]`wspak `$b,$c=$a; $b`11 `$c`22,33,44  
`[string[]]$s3=@('')*3` `[string[][]]$s2x4=(,(@('x')*4))*2` `$s2x4[1][3]='13'`  

`$ArrayDeepCopy = $Array | foreach { $_ } # deep copy trick` to spłaszcza tablicę;  
dla wielowymiarowych: `$MultiDimShallowCopy = $Array | foreach { , $_ }`  `$MultiDimDeepCopy = $Array | foreach { , ($_ | foreach{ $_ }) }`

`$Obj | Export-Clixml -LiteralPath .\serialized.xml` `$ObjDeepCopy = Import-Clixml .\serialized.xml`  


* [PowerShell add or remove elements from an Array](https://pscustomobject.github.io/powershell/Add-Remove-Items-From-Array/) -> pscustomobject.github.io
* [Deep copying arrays and objects](https://www.powershelladmin.com/wiki/Deep_copying_arrays_and_objects_in_PowerShell) -> powershelladmin.com


### 5: Pliki

````powershell
$EnDefault = [System.Text.Encoding]::Default # gdy potrzeba ANSI, np. dla txt-CSV
[Console]::OutputEncoding = [System.Text.Encoding]::Unicode
Set-Location -Path $PSScriptRoot # gdy używam ścieżek względem położenia bieżącego skryptu
            # System.IO.Stream - szybko, ale mało intuicyjnie:
$fWe = new-object System.IO.StreamReader( (Resolve-Path ('we.txt')), $EnDefault) 
                                        #  ^-- Reader: koniecznie pełna ścieżka!
  try { while (($wiersz = $fWe.ReadLine()) -ne $null) { ... } finally { $fWe.Close() }
$fWy = new-object System.IO.StreamWriter( ('..\Wyniki\' + 'wy1.txt'), $false, $EnDefault) 
                                        # ^-- konieczny nawias, gdy "+"  ^--no-append
  try { ...; $fWy.WriteLine( $kolejnyWiersz )  } finally { $fWy.Close() }
````

* [The many ways to read and write to files](https://powershellexplained.com/2017-03-18-Powershell-reading-and-saving-data-to-files/)  -> powershellexplained.com


### 6: Właściwości mutim. plików

Odczyt rozszerzonych własności pliku  
````powershell
$shellFolder = $Shell.NameSpace("$($pwd.Path)\...\").self.GetFolder()
$shellFile   = $shellFolder.ParseName('abc.mp4')
$shellFile # m.in. Name ('abc.mp4'), Path, ModifyDate ('2021-04-08 19:11:27'), Size (bajty)
0..400 | where-object {($details=$shellFolder.GetDetailsOf($shellFile,$_))} | ForEach {
  " $($_.ToString('000')):$(($shellFolder.GetDetailsOf($null,$_)).PadLeft(40,'.')) : $details"
} #rozmiar np. w MB, czas bez sek.
                   # albo odczytaj wszystkie, także puste właściwości
0..400 | ForEach {
  " $($_.ToString('000')):$(($shellFolder.GetDetailsOf($null,$_)).PadLeft(40,'.')) " +
  ":  $($shellFolder.GetDetailsOf($shellFile,$_))"
}
````

<small>
Odczytywanie tekstów z językowych **DLL.MUI**, np. z `c:\Windows\System32\en-US\propsys.dll.mui` 
<br> 1. Dodaj na końcu rozszerzenie `.DLL`; 2. Otwórz w Visual Studio; 3. Zapisz jako `.RC`
</small>

* [Getting file metadata with PowerShell](https://evotec.pl/getting-file-metadata-with-powershell-similar-to-what-windows-explorer-provides/) -> evotec.pl



- - - - - -

&nbsp;

Różne odnośniki:

* [unicodeSupSub_test.ps1 (html)]({{ site.baseurl }}/assets/files/unicodeSupSub_test.ps1.html ) [(.zip)]({{ site.baseurl }}/assets/files/unicodeSupSub_test.zip "unicodeSupSub_test.zip") 


- - - - - -

&nbsp;

### # Nie będziesz używał!


`... | foreach { ...` ~~`continue`~~ ~~`break`~~  
`@a[`~~`0..-1`~~`]`



<style> 
  pre code {font-size: smaller;} 
  h3 small em {font-size: 14px;} 
  ul {font-size: smaller;} 
</style>


