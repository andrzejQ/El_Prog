---
layout: post
title:  "C# - ściągawka"
date:   2019-09-08 08:08:55 +0100
categories: Programowanie
---

[Prawie uniwersalne odczytanie łańcucha data-czas]({{ site.url }}{{ site.baseurl }}{{ page.url }}#prawie-uniwersalne-odczytanie-łańcucha-data-czas) &nbsp; *


### Prawie uniwersalne odczytanie łańcucha data-czas

`DateTime.TryParse()` interpretuje czas zapisany w lokalnym (dla systemu) formacie, ale też dobrze sobie radzi z datą i czasem, gdy łańcuch zaczyna się od 4 cyfr roku. Po po dodaniu w kolejnym kroku opcji dla daty rozpoczynającej się od cyfr dnia, mamy załatwione prawie wszystkie przypadki.


````cs
using System;
using System.Globalization;

CultureInfo ddMMyyyCI = new CultureInfo("da-DK", false);
// "da-DK" or any other culture with dd at the beginning (Denmark: dd-MM-yyyy)
// false = without the user-selected culture settings. 
// Separator sign is not important.
// "pl-PL" now has dd.MM.yyyy, but in Win7 it was yyyy-MM-dd !

if (DateTime.TryParse(dateString, out dateValue)) 
    // local culture with user-selected culture settings in the system
    // yyyy MM dd are also parsed
    Console.WriteLine("  Converted -> '{0}' to {1} ({2}).", dateString, dateValue, dateValue.Kind);
else if (DateTime.TryParse(dateString, ddMMyyyCI // dd at the beginning case
    , DateTimeStyles.AssumeLocal | DateTimeStyles.AllowWhiteSpaces, out dateValue))
    Console.WriteLine("  Converted dd.MM.yyyy '{0}' to {1} ({2}).", dateString, dateValue, dateValue.Kind);
else
    Console.WriteLine("  Unable to parse '{0}'.", dateString);
````


Wypisanie uniwersalnej, sortowalnej postaci `yyyy-MM-dd hh:mm:ssZ` w czasie lokalnym (tzn. nie uniwersalnym), np.: `DateTime.Now.ToString("u") // 2023-02-15 08:48:18Z`. Można to sobie przyciąć do wymaganej dokładności.


* [DateTime1-test.zip]({{ site.baseurl }}/assets/files/DateTime1-test.zip)

<style> pre code {font-size: smaller;} </style>
