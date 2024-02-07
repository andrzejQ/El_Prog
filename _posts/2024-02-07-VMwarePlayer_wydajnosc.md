---
layout: post
title:  "VMWare Player i S0 - poprawianie wydajności"
date:   2024-02-06 15:00:00 +0100
categories: Systemy
---

Zebrałem tu kilka porad dotyczących niepełnego wykorzystania możliwości Intel Turbo Boost Technology
podczas pracy VMWare Player, w przypadku, gdy system wykorzystuje nowoczesny tryb gotowości `S0`.

Jest sporo porad dla starszych trybów gotowości `S3`, gdzie trzeba skorzystać z przełączania wydajności w klasycznym panelu sterowania. Ale w przypadku nowoczesnego trybu `S0` w klasycznym panelu mamy tylko 1 tryb "Zrównoważony" i zmiana jego konfiguracji zaawansowanej nic nie daje.
Dodatkowo [są ostrzeżenia](https://answers.microsoft.com/pl-pl/windows/forum/all/modern-standby-s0-tryb-wstrzymania-bez-zachowania/25abf8c6-077e-4737-8c4a-2da115762813) 
przed wymuszaniem starszych trybów `S1`..`S3` na nowym sprzęcie. (To się daje zrobić, ale np. wtedy u mnie system nie wchodził w tryb uśpienia)


#### 1. Przypadek trybu `S0`


Generalnie ustalanie trybu wstrzymania można zacząć od 
```bat
cmd:
powercfg /a
```
Dla trybu `S0` dostajemy:
```
The following sleep states are available on this system:
    Standby (S0 Low Power Idle) Network Connected
    Hibernate
    Fast Startup
```

Najważniejszą poradą w tym przypadku był dla mnie:

[Poor VM performance on Core i9 CPU 12th gen](https://communities.vmware.com/t5/VMware-Workstation-Player/Poor-VM-performance-on-Core-i9-CPU-12th-gen/m-p/2988384#M40912):

1. `cmd` [Ctrl+Shift+Enter], czyli `cmd` w trybie adm.

```bat
powercfg /powerthrottling disable /path "c:\Program Files (x86)\VMware\VMware Player\vmplayer.exe"
powercfg /powerthrottling disable /path "C:\Program Files (x86)\VMware\VMware Player\x64\vmware-vmx.exe"
powercfg /powerthrottling list
```

- to polecenie, aby wyłączyć dławienie zasilania na maszynie wirtualnej  
  (z jakiegoś powodu Windows chce uruchamiać wirtualne procesory maszyn wirtualnych na E-Cores, a nie P-Cores)  
  P-core są podobne do tradycyjnych projektów procesorów, z dużą prędkością zegara i możliwościami Hyper-Threading,   
  E-cores są mniejsze i zużywają znacznie mniej energii. 

Po tym WMware zaczyna wykorzystywać rdzenie P procesora

2. Znaczące przyśpieszenie daje też wyłączenie korzystania z technologii Hyper-V przez Windows w celu wymuszenia użycia hipernadzorcy VMware, a nie Hyper-V:

Upewnij się, że wszystko, co związane z Hyper-V jest odinstalowane w systemie Windows - "funkcje systemu Windows"
[_] Hyper-V
[_] Platforma funkcji Hypervisor systemu Windows
[_] Platforma maszyny wirtualnej
			(restart)


Są porady dotyczące wyłączenia ustawienia integralności pamięci  
    Windows Security -> Device Security -> Core Isolation then turn off the "Memory Integrity"  
			(restart)

Dodatkowo `cmd` [Ctrl+Shift+Enter], czyli `cmd` w trybie adm.

```bat
bcdedit /set hypervisorlaunchtype off
            (restart)
```

To, że funkcje Hyper-V nie są zainstalowane, nie oznacza, że Windows ich nie używa. Jeśli spojrzysz na plik vmware.log generowany w folderze zawierającym wszystkie pliki w maszynie wirtualnej, poszukaj linii rozpoczynającego się od trybu Monitora. Jeśli jest to ustawione na ULM, Workstation nadal używa Hyper-V.
- sprawdź plik vmware.log ponownie i powinieneś zobaczyć, że tryb monitora jest ustawiony na CPL0 - wskazując, że hipernadzorca VMware jest uruchomiony VM, a nie Hyper-V.  
Nie  
`vmx Monitor Mode: ULM`  
ale powinno być  
`vmx Monitor Mode: CPL0`

Sprawdź też
Wydajność [Ctrl+Shift+Esc] - wydajność - wirtualizacja: włączone!


**Konfiguracja VMWare Player**

Możesz napotkać problem podczas uruchamiania maszyny wirtualnej z systemem Windows 11 w programie VMWare Player. Oprogramowanie ostrzeże Cię o potencjalnym spadku wydajności podczas korzystania z maszyny wirtualnej z "czynnikami kanału  bocznego" (side-channel mitigations).

[\<maszyna\>.vmx](https://winaero.com/how-to-disable-side-channel-mitigations-in-vmware-player/) - dodaj:  
`ulm.disableMitigations="TRUE"` - ale może to jest ważne tylko dla trybu ULM.

Wyłączenie VM-Display-3D nieco pomaga (bardzo nieco)  
Defragmentacja VMWare - w opcjach maszyny w VMware  
Wykluczenie VM folderu z antywirusa  
Wył. CD-ROM, wył. A:  
Enter Full Scr. on start


#### 2. Przypadek trybu `S1`..`S3`

```bat
cmd
powercfg /a
The following sleep states are available on this system:
    Standby (S3)
    Hibernate
    Hybrid Sleep
```

Tu jest sporo porad. Gdy brakuje do wyboru trybu zasilania "najwyższa wydajność" to można go dodać i to nawet na 
[okres ograniczony](https://www.elevenforum.com/t/question-about-windows-power-plan.10813/)
 (nie sprawdzałem skuteczności skryptu):  
Plik "power_conf.cmd":
```bat
@echo off
for /f "tokens=4 delims= " %%f in ('powercfg /GETACTIVESCHEME') do (
  set ACTIVE_SCHEME=%%f
  set ACTIVE_SCHEME
)
:: VMWare Player
"c:\Program Files (x86)\VMware\VMware Player\vmplayer.exe"
powercfg /setactive %ACTIVE_SCHEME%
```


<style> pre code {font-size: smaller;} </style>
