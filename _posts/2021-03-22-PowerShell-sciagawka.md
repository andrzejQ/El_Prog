---
layout: post
title:  "PowerShell ściągawka"
date:   2021-03-22 07:00:00 +0100
categories: Programowanie
---

Moja ściągawka (zapewe tylko do użytku własnego) ... 

... będzie miała poziomy - od najkrótszego przypomnienia, które się przyda po długim czasie nie-praktykowania po nieco bardziej rozbudowane przypominajki

0:

`($x='coś')` , `"2+3=$(2+3)"` , `@()`



1:

`()` - wykonaj teraz, np. `($x='coś')` podstaw i wyświetl  
`$()` - wykonaj teraz i potraktuj jak zmienną, np. `"2+3=$(2+3)"`  
`@()` - potaktuj jako tablicę (także pustą lub 1-el.)  
` , ` - literał tablicy  
`&` - wykonaj  
`.` - wykonaj skrypt ps1 zapamiętując jego zmienne  
`..` - zakres liczb całk. np. `-5.1..1.9` -eq `-5..1`

Linki 01:

* [PowerShell – mini kompendium -> ](http://tymoteuszkestowicz.com/2013/11/powershell-mini-kompendium/) tymoteuszkestowicz.com
* [PowerShell Operators $( ) @( ) :: & -> ](https://ss64.com/ps/syntax-operators.html) ss64.com
* [Getting started with PowerShell -> ](https://riptutorial.com/powershell) riptutorial.com
* [Powershell: Everything you wanted to know about arrays -> ](https://powershellexplained.com/2018-10-15-Powershell-arrays-Everything-you-wanted-to-know/) powershellexplained.com
* [Everything you wanted to know about PSCustomObject -> ](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-pscustomobject?view=powershell-5.1) docs.microsoft.com
* [PowerShell Commands Every Developer Should Know -> ](https://stackify.com/powershell-commands-every-developer-should-know/) stackify.com

Linki 02:

...

<style> pre code {font-size: smaller;} </style>
