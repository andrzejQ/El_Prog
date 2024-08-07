---
layout: post
title:  "VMWare Player i S0 - poprawianie wydajności"
date:   2024-02-06 15:00:00 +0100
categories: Systemy
---

Zebrałem tu kilka porad dotyczących problemu niepełnego wykorzystania możliwości Intel Turbo Boost Technology 12-gen.+
podczas pracy VMWare Player w przypadku, gdy system wykorzystuje 
[1.&nbsp;nowoczesny tryb gotowości `S0`;]({{site.url}}{{site.baseurl}}{{page.url}}#1-przypadek-trybu-s0) &nbsp; * 
[2.&nbsp;przypadek trybu `S1`..`S3`.]({{site.url}}{{site.baseurl}}{{page.url}}#2-przypadek-trybu-s1s3) &nbsp; * 
_+ 08.05.2024_{: .date} [3.&nbsp;Spowolnione Visual Studio.]({{site.url}}{{site.baseurl}}{{page.url}}#3-spowolnione-visual-studio) 

<style>.date{font-size: smaller;color:#828282;}</style>

Jest sporo porad dla starszych trybów gotowości `S3`, gdzie trzeba skorzystać z przełączania wydajności w klasycznym panelu sterowania. Ale w przypadku nowoczesnego trybu `S0` w klasycznym panelu mamy tylko jeden tryb: "Zrównoważony" i zmiana jego konfiguracji zaawansowanej (chyba) nic nie daje jak chodzi o wydajność.
Dodatkowo [są ostrzeżenia](https://answers.microsoft.com/pl-pl/windows/forum/all/modern-standby-s0-tryb-wstrzymania-bez-zachowania/25abf8c6-077e-4737-8c4a-2da115762813) 
przed wymuszaniem starszych trybów `S1`..`S3` na nowym sprzęcie. (To się daje zrobić, ale np. wtedy u mnie system nie wchodzi w tryb uśpienia)


#### 1. Przypadek trybu `S0`


Sprawdzanie, czy w moim systemie działa tryb "S0 Low Power Idle":
```bat
cmd:
powercfg /a
```
Dla trybu `S0` dostajemy:
```
The following sleep states are available on this system:
    Standby (S0 Low Power Idle) Network Connected
    ...
```

Najważniejszą poradą w tym przypadku był dla mnie:

[Poor VM performance on Core i9 CPU 12th gen](https://communities.vmware.com/t5/VMware-Workstation-Player/Poor-VM-performance-on-Core-i9-CPU-12th-gen/m-p/2988384#M40912):

1.
`cmd` w trybie adm., czyli `cmd` [`Ctrl` + `⇧` + `↵`], <span>tj. `cmd` [`Ctrl` + `⇧ Shift` + `↵ Enter`]</span>{: style="font-size:0.85em;"}


{: .zmniejsz}
```bat
powercfg /powerthrottling disable /path "C:\Program Files (x86)\VMware\VMware Player\x64\vmware-vmx.exe"
```

{: style="font-size: 0.86em;"}
* To polecenie **wyłącza obniżanie taktowania dla "vmware-vmx.exe"**. Przy pracy na zasilaczu 
[powinno to być wyłączane](https://www.nextofwindows.com/enable-or-disable-power-throttling-windows-11)
na skutek wybrania opcji w nowym panelu ustawień Win 11:  
[`⊞ Win` + `i`] \ System \ Zasilanie i bateria \ Tryb zasilania \ Najwyższa wydajność.  
Ale z jakiegoś powodu Windows chce uruchamiać wirtualne procesory maszyn wirtualnych na rdzeniach E-Cores, a nie P-Cores:
   * P-cores (Performance-cores) są podobne do tradycyjnych projektów procesorów, z dużą prędkością zegara i możliwościami Hyper-Threading,   
   * E-cores (Efficient-cores) są mniejsze i zużywają znacznie mniej energii. 

Przy takiej konfiguracji WMware zaczyna wydajnie (i elastycznie!) wykorzystywać rdzenie P. Mój procesor ma 2 rdzenie P i 8 rdzeni E. Mam wrażenie, że udostępnianie systemowi gościa więcej niż 2 procesorów nic u mnie nie daje. Również porady, aby przydzielać jak najwięcej RAMu u mnie się nie sprawdzają. Dużo RAMu powyżej optymalnej wartości nie tylko nic się nie poprawia, ale wręcz daje pogorszenie wydajności (nie rozumiem dlaczego).

* Zawsze można 
[sprawdzić](https://www.windowscentral.com/how-manage-power-throttling-windows-10)
stan: `powercfg /powerthrottling list`

2.
Znaczące przyśpieszenie daje też wyłączenie korzystania z technologii Hyper-V przez Windows w celu wymuszenia użycia hipernadzorcy VMware, a nie Hyper-V:

Upewnij się, że wszystko, co związane z Hyper-V jest odinstalowane w systemie Windows - "funkcje systemu Windows"  
 ▢ Microsoft Defender Application Guard  
 ▢ Hyper-V  
 ▢ Platforma funkcji Hypervisor systemu Windows  
 ▢ Platforma maszyny wirtualnej  
			(restart)


Są porady dotyczące wyłączenia ustawienia integralności pamięci  
    Windows Security -> Device Security -> Core Isolation then turn off the "Memory Integrity"  
			(+restart)
Choć może to dotyczyć raczej słabszych komputerów

Dodatkowo  `cmd` [`Ctrl` + `⇧` + `↵`]:

```bat
bcdedit /set hypervisorlaunchtype off
            (+restart)
```

To, że funkcje Hyper-V nie są zainstalowane, nie oznacza, że Windows ich nie używa. Jeśli spojrzysz na plik vmware.log generowany w folderze zawierającym wszystkie pliki w maszynie wirtualnej, poszukaj wiersza `Monitor Mode:`. Jeśli jest to  
`vmx Monitor Mode: ULM`,  
to nadal używany jest Hyper-V, a nie hipernadzorca VMware. Powinno być  
`vmx Monitor Mode: CPL0`

Sprawdź też, że w BIOS włączona jest wirtualizacja. W Win11:
* Wydajność = [`Ctrl` + `⇧` + `Esc`] \ wydajność \ wirtualizacja: włączone!

Zob. też
* [Windows 11, VirtualBox, NativeAPI](https://mirekgab.pl/windows-11-virtualbox-nativeapi/) »

**Konfiguracja VMWare Player**

Można napotkać problem podczas uruchamiania maszyny wirtualnej z systemem Windows 11 w programie VMWare Player w trybie `UML`. Pojawia się ostrzeżenie o potencjalnym spadku wydajności podczas korzystania z maszyny wirtualnej z "side-channel mitigations".
W pliku konfiguracji [\<maszyna\>**.vmx** - dodaj wiersz](https://winaero.com/how-to-disable-side-channel-mitigations-in-vmware-player/): 
`ulm.disableMitigations="TRUE"`

Usprawnienia:
* Wyłączenie VM-Display-3D; VMware jako gra, a może wył. trybu gry hosta (podobno można sprawdzić, czy to coś daje - u mnie nie widać różnic).
* Defragmentacja VMWare - w opcjach maszyny w VMware (nie w systemie gościa).
* Wykluczenie z antywirusa przeszukiwania VM folderu z plikami maszyny gościa.
* Wył. `CD-ROM`, wył. `A:`
* Enter Full Scr. on start


#### 2. Przypadek trybu `S1`..`S3`

```bat
cmd:
powercfg /a
The following sleep states are available on this system:
    Standby (S3)
    ...
```

Tu jest sporo porad, które sprowadzają się do wybru trybu zasilania "najwyższa wydajność" w klasycznym panelu sterowania:
Sprzęt i dźwięk \ Opcje zasilania.  
Jeśli tego trybu nie widać, to 
[można go włączyć](https://www.elevenforum.com/t/question-about-windows-power-plan.10813/)
poleceniem  
```
cmd:
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```
Nie trzeba uruchamiać `cmd` w trybie administratora. Zmiana jest od razu widoczna w klasycznym panelu sterowania \ 
Sprzęt i dźwięk \ Opcje zasilania.  
Widać też (nieaktywny w tym momencie) tryb normalny, który można kliknąć w przyszłości.

Po zapamiętaniu GUID trybu normalnego: `powercfg /getactivescheme`  
można zrobić sobie skróty przełączające tryby na pulpicie.


#### 3. Spowolnione Visual Studio

Niekiedy powodem użycia systemu wirtualnego jest potrzeba pracy w izolowanym od sieci środowisku. 
Wtedy wybieram opcję sieciową "Host only" i wymieniam dane poprzez "Shared folders" udostępniając folder hosta.  
Można by też włączyć dla systemu gościa kartę sieciową i widzieć jego udostępnione foldery na hoście Windows. 
I tu może nas spotkać bardzo nieprzyjemne zaskoczenie. Aplikacje jak np. Visual Studio potrafią wtedy zamrażać się po starcie, czy po powrocie z debugowania na kilkanaście sekund (to zapewne nieudane próby nawiązania połączenia sieciowego) i ogólnie doznają znaczącego spowolnienia - nie wiem czy w każdym przypadku. 

![VM_Net_conf.png]({{site.baseurl}}/assets/img/VM_Net_conf.png "VM_Net_conf.png"){: style="float:left;width:49%;margin-bottom:14px;"} 
W takim wypadku może pomóc wyłączenie wirtualnych kart sieciowych w konfiguracji sprzętu gościa, 
a może alternatywnie też wyłączenie sieci w panelu sterowania systemu gościa - zob. 
<https://stackoverflow.com/questions/31383348/how-is-visual-studio-performance-linked-to-enable-disable-network-connection>

Uruchom: `ncpa.cpl` aby szybko otworzyć "Panel sterowania (klasyczny) \ Sieć i Internet \ Połączenia sieciowe"

Przy takiej konfiguracji sieci w systemie gościa, nadal działają "Shared folders".

![Bez_kart_sieci.png]({{site.baseurl}}/assets/img/Bez_kart_sieci.png "Bez_kart_sieci.png"){: style="float:right;width:49%;margin-bottom:6px;"} 

<style> code {font-size: 0.93em;}  div.zmniejsz code {font-size: 0.88em;}  </style>



#### 4. Koligacja procesorów

![VMware-wmx_koligacje.png]({{site.baseurl}}/assets/img/VMware-wmx_koligacje.png "VMware-wmx_koligacje.png"){: style="float:right;width:62%;"} 
Może można próbować przypisać procesory P do vmware-vmx.exe. Ale u mnie nie widać zmiany wydajności (przy war. jak w p.1). 

Można też jakoś na trwałe przypisać rdzenie:

* [How to launch a process with CPU affinity set](https://learn.microsoft.com/pl-pl/archive/blogs/santhoshonline/how-to-launch-a-process-with-cpu-affinity-set)


ale mi się to nie udaje. 

Np. przy 

`cmd /c START "" /HIGH /AFFINITY 03 "xyz.vmx"`

maszyna wirtualna `xyz.vmx`, tj. `vmware-vmx.exe` bierze wszystkie rdzenie. 

Polecenie poniżej otwiera co prawda `vmplayer.exe` z przypisaniem do rdzeni 1 i 2, ale nadal maszyna wirtualna `xyz.vmx` bierze wszystkie rdzenie:

`cmd /c START "" /HIGH /AFFINITY 03 "C:\Program Files (x86)\VMware\VMware Player\vmplayer.exe" "xyz.vmx"`






<!-- {% unless jekyll.environment %} -->
<script>

(function() {
  const images = document.getElementsByTagName('img'); 
  for(let i = 0; i < images.length; i++) {
    images[i].src = images[i].src.replace('%7B%7Bsite.baseurl%7D%7D','..');
  } //{{site.baseurl}} - without spaces!  
})();

</script>
<!-- {% endunless %} -->