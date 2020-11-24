---
layout: post
title:  "Instalowanie modułu Teams PowerShell"
date:   2020-11-24 10:00:00 +0100
categories: Programowanie
---

Szczegółowy opis instalacji modułu Teams PowerShell na podstawie  
<https://docs.microsoft.com/en-us/microsoftteams/teams-powershell-install>

"  
... Te instrukcje działają na platformach Azure Cloud Shell, Linux, macOS i Windows.  
... Domyślnie Galeria programu PowerShell (PSGallery) nie jest skonfigurowana jako zaufane repozytorium ... Odpowiedz "Yes", aby kontynuować instalację...  
"

![Win_X.png]({{ site.baseurl }}/assets/img/Win_X.png "Win_X.png"){:style="float:right;width:35%;"} 

### Szczegółowa instrukcja instalacji  modułu Teams PowerShell

1. Uruchamiamy PowerShell w trybie administratora, np. [![WinKey]({{ site.baseurl }}/assets/img/WinKey.png "WinKey"){:style="width:18px;"}+**x**] \ `Program Windows PowerShell (Administrator)`
![(adm)PowerShell.png]({{ site.baseurl }}/assets/img/(adm)PowerShell.png "(adm)PowerShell.png"){:style="width:59%;"} 

2. [Zezwalamy](https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/) na pracę skryptów PowerShell  
<small>(jeśli nigdy wcześniej tego nie zrobiliśmy)</small>:  
`Set-ExecutionPolicy RemoteSigned`, `Y`

3. Instalujemy moduł:  
`Install-Module MicrosoftTeams`, `Y`  
(tu tryb administratora nie jest wymagany)

![InstallModule.png]({{ site.baseurl }}/assets/img/InstallModule.png "InstallModule.png")


### Testowanie modułu

Uruchom skrypt [Connect-MicrosoftTeams.ps1]({{ site.baseurl }}/assets/files/Connect-MicrosoftTeams.zip "Connect-MicrosoftTeams.zip") w `PowerShell ISE`, logując się na swoje konto Office365. Zostaną wyświetlone Twoje zespoły i członkowie pierwszego zespołu. Można następnie testować inne [funkcje modułu](https://docs.microsoft.com/en-us/powershell/module/teams/?view=teams-ps).


````powershell
$ConnectTeams = Connect-MicrosoftTeams
$ConnectTeams #: Account ... TenantDomain
# Lista zespołów - bez parametrów się zawiesza, więc coś trzeba podać...
$Team = Get-Team -User $ConnectTeams.Account
$Team | Format-Table
$Team[0].DisplayName
# $Team[0] | Get-TeamChannel
$Team[0] | Get-TeamUser
Write-Host 'Wypróbuj: Get-Team -DisplayName "..." | Get-TeamChannel'
````
<style> pre code {font-size: smaller;} </style>
