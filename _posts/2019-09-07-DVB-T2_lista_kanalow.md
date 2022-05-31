---
layout: post
title:  "DVB-T2 lista kanałów"
date:   2019-09-07 08:08:59 +0100
categories: Programowanie
---

Gdy Twój nadawca TV zmienia listę kanałów, to można szybko sprawdzić aktualny stan.

Jeśli masz tuner TV podpięty do komputera, to można uruchomić program  
 **SichboPVR** -> <https://sichbopvr.com/pl-pl/>.  
Każdorazowo po wyszukaniu kanałów w **SichboPVR** powstaje plik  
`%ProgramData%\SichboPVR4\service-channels.json`  
z aktualną informacją o dostępnych kanałach DVB-T/T2.

Uruchamiając  [`py channels.py`]({{ site.baseurl }}/assets/files/channels.py) otrzymasz listę programów TV i kilka dodatkowych danych - wynik w `chInfo.csv`

Analogiczny skrypt w PowerShell: Uruchamiając [`channels.ps1`]({{ site.baseurl }}/assets/files/channels.ps1) otrzymasz listę programów TV i kilka dodatkowych danych - wynik w `chInfo_.csv`

<small>
Można też uruchomić skrypt, który daje listę częstotliwości kanałów w standardzie D/K (CCIR) - 
[`tvMHz.py`]({{ site.baseurl }}/assets/files/tvMHz.py)
lub
[`tvMHz.ps1`]({{ site.baseurl }}/assets/files/tvMHz.ps1).
</small>

<style> pre code {font-size: smaller;} </style>
