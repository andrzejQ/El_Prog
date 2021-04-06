---
layout: post
title:  "PowerShell ściągawka"
date:   2020-11-24 07:00:00 +0100
categories: Programowanie
---

Moja ściągawka (zapewne tylko do użytku własnego) ... 

... będzie miała poziomy - od najkrótszego przypomnienia, które się przyda po długim czasie nie-praktykowania po nieco bardziej rozbudowane przypominajki

0:

`($x='coś')` , `"2+3=$(2+3)"` , `@()`, `${a b}`



1:

`()` - wykonaj teraz, np. `($x='coś')` podstaw i wyświetl  
`$()` - wykonaj teraz i potraktuj jak zmienną, np. `"2+3=$(2+3)"`  
`@()` - potaktuj jako tablicę (także pustą lub 1-el.)  
`, `  - literał tablicy  
`&` - wykonaj  
`. `  - wykonaj skrypt ps1 zapamiętując jego zmienne (spacja po kropce)  
`..` - zakres liczb całk. np. `-5.1..1.9` -eq `-5..1`  
`${}` - nazwa zmiennej z użyciem znaków niedozwolonych w nazwach, np. `${a b}` (ale `$ąćę` jest ok)  

PSCustomObject  
`$myObj=[PSCustomObject]@{Nm='K'}` lub `$ht=@{Nm='K'};$myObj=[pscustomobject]$ht`  
`$myObj | ConvertTo-Json -depth 1 | Set-Content -Path $Path` - zapis do pliku  
`$myObj=Get-Content -Path $Path | ConvertFrom-Json` - odczyt z pliku  
`$myObj | Add-Member -MemberType NoteProperty -Name 'ID' -Value 'KMarquette'`  
wszystkie własności: `$myObj | Get-Member -MemberType NoteProperty | Select -ExpandProperty Name` ; czy wł. istnieje:  
`if( $null -ne $myObj.ID )` lub `if( $myObj.psobject.properties.match('ID').Count )`  
`$myObj.Nm` lub `$myObj.'Nm'` lub `$myObj.$prop` - odczytaj wartość  
`$b=$myObj.psobject.copy()` - prawdziwa kopia (a nie tylko referencja)  


2:

`$a -replace $b,$c` to .NET `Regex.Replace($a, $b, $c, RegexOptions.IgnoreCase)`; `$a.replace($b, $c)` - zwykła zamiana



Linki 01:

* [PowerShell – mini kompendium -> ](http://tymoteuszkestowicz.com/2013/11/powershell-mini-kompendium/) tymoteuszkestowicz.com
* [PowerShell Operators $( ) @( ) :: & -> ](https://ss64.com/ps/syntax-operators.html) ss64.com
* [Getting started with PowerShell -> ](https://riptutorial.com/powershell) riptutorial.com
* [Powershell: Everything you wanted to know about arrays -> ](https://powershellexplained.com/2018-10-15-Powershell-arrays-Everything-you-wanted-to-know/) powershellexplained.com
* [Everything you wanted to know about PSCustomObject -> ](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-pscustomobject?view=powershell-5.1) docs.microsoft.com
* [PowerShell Commands Every Developer Should Know -> ](https://stackify.com/powershell-commands-every-developer-should-know/) stackify.com

Linki 02:

* [Regular Expression Language - Quick Reference](https://docs.microsoft.com/pl-pl/dotnet/standard/base-types/regular-expression-language-quick-reference); [Regex.Replace(...)](https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.replace?view=net-5.0); [.NET Replace(String, String), Replace(String, String, StringComparison)](https://docs.microsoft.com/en-us/dotnet/api/system.string.replace?redirectedfrom=MSDN&view=net-5.0#System_String_Replace_System_String_System_String_), [StringComparison](https://docs.microsoft.com/en-us/dotnet/api/system.stringcomparison?view=net-5.0)



<style> pre code {font-size: smaller;} </style>
