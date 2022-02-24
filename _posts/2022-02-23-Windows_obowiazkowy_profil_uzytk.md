---
layout: post
title:  "Windows - obowiązkowy profil użytkownika"
date:   2022-02-23 10:00:00 +0100
categories: Systemy
---

Konto użytkownika z obowiązkowym profilem może się przydać na współdzielonym komputerze - kiosku, sali konferencyjnej itp. Jakiekolwiek modyfikacje profilu nie są zapamiętywane po wylogowaniu. 

#### 1. Lusrmgr.msc <small>(Użytkownicy i grupy lokalne)</small>

* Nowe konto, np. `ktokolwiek`
* i na dysku nowy folder `C:\ktokolwiek.V6`

#### 2. SystemPropertiesAdvanced.exe <small>(Właściwości systemu \ Zaawansowane)</small>
* Profile użytkownika  
	Ustawienia pulpitu związane z logowaniem \ [Ustawienia...]
* `Profil domyślny` [Kopiuj do...] 
	* `C:\ktokolwiek.V6` (lub do jakiejś ścieżki UNC `\\serwer\...`)
	* Pozwolenie na używanie \ [Zmień]  
		Użytkownicy uwierzytelnieni (=ZARZĄDANIE NT\Użytkownicy uwierzytelnieni)
	* [_] Profil obowiązkowy <small>(gdy zaznaczone - użytkownicy z tym profilem nie będą mogli się zalogować, jeśli serwer, na którym przechowywany jest profil, jest niedostępny)</small>

#### 3. Lusrmgr.msc <small>(ponownie - Użytkownicy i grupy lokalne)</small>

* Użytkownicy \ `ktokolwiek` \ Profil
	* Profil użytkownika - Ścieżka profilu: `C:\ktokolwiek.V6`
	* Folder macierzysty - (●) Ścieżka lokalna
	
#### 4. 

Wylogowanie Adm

Zalogowanie `ktokolwiek` \ Ustawianie wyglądu, skrótów, aplikacji \ Wylogowanie `ktokolwiek`

Zalogowanie Adm  
`RENAME "C:\ktokolwiek.V6\NTuser.dat" NTuser.man`  
Adm zmienia nazwę pliku NTuser.dat (zawiera klucz rejestru użytkownika `ktokolwiek` HKEY_CURRENT_USER) na NTuser.man. System traktuje ​​profil NTuser.man jako tylko do odczytu i nie zapisuje w nim zmian.

#### 5. 

* Jeśli wystąpi błąd podczas próby zalogowania się użytkownika `ktokolwiek` - "... Profil użytkownika nie może zostać załadowany.":
	* Upewnij się, że następujące uprawnienia są przypisane do katalogu profilu (z wyłączonymi uprawnieniami dziedziczenia):
		* WSZYSTKIE PAKIETY APLIKACJI - pełna kontrola (bez tego menu start nie działa poprawnie)
		* Użytkownicy uwierzytelnieni - odczytywanie i wykonywanie
		* SYSTEM - pełna kontrola
		* Administratorzy - pełna kontrola







<style> pre code {font-size: smaller;} </style>
