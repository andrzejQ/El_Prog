---
layout: post
title:  "WinInst Error 0x800707E7-0x3000D first_boot migrate_data"
date:   2022-03-22 12:08:59 +0100
categories: Systemy
---

Podczas uaktualnienia Windows zdarzyło mi się, że na koniec instalator cofa zmiany i pojawia się komunikat: ... wystąpił błąd MIGRATE_DATA.

![21H2-error_MigrateData.png ]({{ site.baseurl }}/assets/img/21H2-error_MigrateData.png "21H2-error_MigrateData.png"){:style="float:right;width:66%;margin-right:15px;"}

<small>Instalator systemu Windows 10 </small>

**Nie mogliśmy zainstalować systemu Windows 10**


<small>Komputer został przywrócony do stanu sprzed rozpoczęcia instalacji systemu Windows 10.</small>  
  
<small>0x800707E7 - 0x3000D  
Instalacja nie powiodła się w fazie FIRST_BOOT — podczas operacji wystąpił błąd MIGRATE_DATA</small>


Szczegółowe informacje o błędach można znaleźć w ogromnym pliku logu (kilkadziesiąt MB):  
`"c:\$WINDOWS.~BT\Sources\Panther\setupact.log"`  
Przy końcu tego pliku mogą pojawić się informacje:
```
  Warning SP User profile suffix mismatch: upgrade asked for "usr1",actual suffix is:"usr1.000"
  Info    SP Conflicting profile folder content (C:\Users\usr1):
...          
  Error   SP User profile suffix mismatch, upgrade cannot continue.[gle=0x00000012]
  Info       Entering MigCloseCurrentStore method
 
  Error   SP pSPExecuteApply: Migration phase caught exception: Win32Exception: User profile 
  suffix mismatch, upgrade cannot continue: Określony profil jest przeznaczony dla 
  urządzenia innego typu niż określone urządzenie. [0x000007E7] 
...          
  Info    SP SPExecuteFirstBootApply: End run. Result: 0x00000004
  Error   SP Apply (first boot apply, online phase): Migration phase failed. Result: 4, 
             specific error: 0x800707E7[gle=0x00000002]
```

Po sprawdzeniu gałęzi rejestru  
`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`  
u mnie okazało się, że zdarzają się podwójne wpisy wskazujące na ten sam folder, np. `C:\Users\usr1`. 
Żeby odkryć który z wpisów jest starszy warto wyeksportować tą gałąź do pliku tekstowego (eksport do pliku *.reg nie daje wglądu w czas zapisu). 
Można też uruchomić skrypt jak w ramce poniżej, 
albo uruchomić skrypt

* [infProfileList_regWrTm.ps1 (html)]({{ site.baseurl }}/assets/files/infProfileList_regWrTm.ps1.html ) [(.zip)]({{ site.baseurl }}/assets/files/infProfileList_regWrTm.zip "infProfileList_regWrTm.zip"), 

który daje najwięcej informacji o czasach zdarzeń związanych z profilami.

Gdy usunąłem stare wpisy w rejestrze (a wcześniej wpisy usuniętych użytkowników, którzy nie mieli już folderów ze swoimi profilami), to aktualizacja Windows się powiodła.

````powershell
function fTime { param( [System.UInt32]$timeHigh, [System.UInt32]$timeLow )
  if ($timeHigh -or $timeLow) {
    [datetime]::FromFileTime((([long]$timeHigh -shl 32) -bor $timeLow)).
      ToString("yyyy'-'MM'-'dd' 'HH'.'mm'.'ss")
  } else {'0'}
}
function oTime { param( [PSCustomObject] $o, [string]$tName )
  fTime $o.($tName+'High') $o.($tName+'Low')
}
#------------------------------
$RegParentPath = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"
$Profiles = Get-ChildItem -Path Registry::$RegParentPath | 
  foreach {
    $a = $_ | Get-ItemProperty
    foreach ($tName in 'LocalProfileLoadTime', 'LocalProfileUnloadTime', 
                       'ProfileAttemptedProfileDownloadTime', 'ProfileLoadTime'){
      if( $null -ne $a.($tName+'Low') ) { # exists ...TimeLow
        $a | Add-Member @{$tName=(oTime $a $tName)}
        $a.psobject.properties.remove($tName+'High')
        $a.psobject.properties.remove($tName+'Low')
      }
    }
    $a
}
Write-Host "`n  " $RegParentPath "`n" -ForegroundColor Cyan
$Profiles | foreach{
  Write-Host $_.PSChildName  -ForegroundColor Magenta
  Write-Host ($_ | Format-List | Out-String)
}
````

<style> pre code {font-size: smaller;} </style>
