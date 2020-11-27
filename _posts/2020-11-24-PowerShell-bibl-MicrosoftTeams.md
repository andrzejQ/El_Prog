---
layout: post
title:  "Moduł MicrosoftTeams PowerShell w praktyce"
date:   2020-11-24 10:00:00 +0100
categories: Programowanie
---

[Instrukcja instalacji modułu MicrosoftTeams PowerShell]({{ site.url }}{{ site.baseurl }}{{ page.url }}#szczegółowa-instrukcja-instalacji--modułu-microsoftteams-powershell) * [Pobieranie listy członków zespołów]({{ site.url }}{{ site.baseurl }}{{ page.url }}#pobieranie-listy-członków-swoich-zespołów">Pobieranie listy członków swoich zespołów)  * [Automatyczne dodawanie członków do swoich zespołów]({{ site.url }}{{ site.baseurl }}{{ page.url }}#automatyczne-dodawanie-członków-do-swoich-zespołów) 

Szczegółowy opis instalacji modułu MicrosoftTeams PowerShell na podstawie  
<https://docs.microsoft.com/en-us/microsoftteams/teams-powershell-install>

"  
... Te instrukcje działają na platformach Azure Cloud Shell, Linux, macOS i Windows.  
... Domyślnie Galeria programu PowerShell (PSGallery) nie jest skonfigurowana jako zaufane repozytorium ... Odpowiedz "Yes", aby kontynuować instalację...  
"

![Win_X.png]({{ site.baseurl }}/assets/img/Win_X.png "Win_X.png"){:style="float:right;width:35%;"} 

### Szczegółowa instrukcja instalacji  modułu MicrosoftTeams PowerShell

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

![PowerShell_ISE.png]({{ site.baseurl }}/assets/img/PowerShell_ISE.png "PowerShell_ISE.png"){:style="float:right;width:188px;"} 
Wypakuj i otwórz skrypt [**Connect-MicrosoftTeams.ps1**(.zip)]({{ site.baseurl }}/assets/files/Connect-MicrosoftTeams.zip "Connect-MicrosoftTeams.zip")
 w `PowerShell ISE`. 
 Po uruchomieniu (F5) należy zalogować się na swoje konto Office365. Zostaną wyświetlone Twoje zespoły i członkowie pierwszego zespołu. <small> Można następnie testować inne [funkcje modułu](https://docs.microsoft.com/en-us/powershell/module/teams/?view=teams-ps).</small>

Można też skopiować poniższy skrypt i uruchomić.

````powershell
$ConnectTeams = Connect-MicrosoftTeams
$ConnectTeams #: Account ... TenantDomain
# Lista zespołów - Get-Team bez parametrów się zawiesza, więc coś trzeba podać...
$Team = Get-Team -User $ConnectTeams.Account
$Team | Format-Table
$Team[0].DisplayName
# $Team[0] | Get-TeamChannel
$Team[0] | Get-TeamUser
Write-Host 'Wypróbuj: Get-Team -DisplayName "..." | Get-TeamChannel'
````

### Pobieranie listy członków swoich zespołów

Skrypt [**GetUsers-Teams.ps1**(.zip)]({{ site.baseurl }}/assets/files/GetUsers-Teams.zip "GetUsers-Teams.zip") pobiera listę zespołów użytkownika Office365 i dla każdego z zespołów pobiera kanały i listę członków zespołu. Wynik zapisuje do pliku CSV (który jest automatycznie otwierany): 
![Credential.png]({{ site.baseurl }}/assets/img/Credential.png "Credential.png"){:style="float:right;width:344px;position: relative; top: 33px;"} 


User      | Name        | Role
:--------:|-------------|-------
..        | Mój zespół1 | 
.         |             | Kanał 1
.         |             | Kanał 2
uż.1@o365 | Imię Nazw.1 | owner
uż.2@o365 | Imię Nazw.1 | member
{:style="width:auto;font-size: smaller;"}

Po jednorazowym zapytaniu o login i hasło zapamiętuje je zaszyfrowane w pliku "...!o365.cred" 

<small> Jest to wersja dla modułu MicrosoftTeams - General Availability (GA) v.1.1.6, która pozawala zarządzać 
 członkami zespołów. Zarządzanie członkami kanałów jest obecnie (2020r) możliwe tylko w wersji 
 MicrosoftTeams Public Preview (np. v.1.1.7), która wymaga osobnej instalacji.
<https://docs.microsoft.com/en-us/microsoftteams/teams-powershell-install></small>



### Automatyczne dodawanie członków do swoich zespołów

1. Utwórz zespół/zespoły ręcznie (z wybranych szablonów).
2. Zapisz plik `CSV` z wyeksportowanymi zespołami, uruchamiając skrypt `GetUsers-Teams.ps1`.
3. Na podstawie tego pliku stwórz nowy, zachowując nagłówek `User;Name;Role` i sekcję dla modyfikowanego zespołu <small>(może być więcej zespołów, ale wystarczy jeden)</small>.  
<small>Możesz też dopisać nowe kanały do automatycznego dodania w tym zespole.</small>
4. Dopisz członków zespołu do dodania z rolą "owner" (właściciel) lub "member"(członek). Zapisz plik `CSV`.
5. W `PowerShell ISE` uruchom skrypt `AddUsers-Teams.ps1`.
6. Zmiany są (raczej) natychmiast widoczne w aplikacji MS Teams.

![csvFileDialog.png]({{ site.baseurl }}/assets/img/csvFileDialog.png "csvFileDialog.png"){:style="float:right;width:477px;"} 
Skrypt [**AddUsers-Teams.ps1**(.zip)]({{ site.baseurl }}/assets/files/AddUsers-Teams.zip "AddUsers-Teams.zip") Odczytuje plik CSV o formacie jak w skrypcie `GetUsers-Teams.ps1`.

Gdy napotka wiersz  
`..;<nazwa zespołu>;`  
uaktualnia istniejący zespół zalogowanego użytkownika 
<small>(albo tworzy nowy, gdy potrzeba - ale raczej powinno się tworzyć zespoły ręcznie korzystając z szablonów)</small>.

Dodaje kanały jeśli są nowe, wg. wierszy w CSV `.;;<nazwa kanału>`.

Dodaje członków wg. odczytywanej listy członków zespołu w CSV, ale tylko jeśli są nowi.  
2-ga kolumna ("Name") jest pomijana podczas operacji dodawania (nie da się w ten sposób zmodyfikować 
imienia i nazwiska użytkownika).  
W 3-ciej kolumnie ("Role") w przypadku dodawania użytkownika ważny jest wpis "owner", a każdy inny 
jest zamieniany na "member".

Może być wiele sekcji zespół-kanały-użytkownicy.

Skrypt nie usuwa członków, których brak na liście CSV.

Po jednorazowym zapytaniu o login i hasło zapiętuje je zaszyfrowane w pliku "...!o365.cred", wspólnym dla tej rodziny skryptów.


<style> pre code {font-size: smaller;} </style>
