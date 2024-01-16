---
layout: post
title:  "DVB-T2 lista kanałów"
date:   2019-09-07 06:08:59 +0100
categories: Programowanie
---

Gdy Twój nadawca TV zmienia listę kanałów, to można szybko sprawdzić aktualny stan.

Jeśli masz tuner TV podpięty do komputera, to można uruchomić program  
 **SichboPVR** -> <https://sichbopvr.com/pl-pl/>.  
Każdorazowo po wyszukaniu kanałów w **SichboPVR** powstaje plik  
`%ProgramData%\SichboPVR4\service-channels.json`  
z aktualną informacją o dostępnych kanałach DVB-T/T2.

Uruchamiając  [`py channels.py`]({{site.baseurl}}/assets/files/channels.py) 
(używa [`DTV_DK_CCIR.py`]({{site.baseurl}}/assets/files/DTV_DK_CCIR.py))
otrzymasz listę programów TV i kilka dodatkowych danych - wynik w `chInfo.csv`

Analogiczny skrypt w PowerShell: Uruchamiając [`channels.ps1`]({{site.baseurl}}/assets/files/channels.ps1) otrzymasz listę programów TV i kilka dodatkowych danych - wynik w `chInfo_.csv`

- - - - - 
<br>
Do tunera DTV USB [`MyGica T230A`](https://www.mygica.com/support/) załączany jest program `MyGicaHiDTV`.  
<small>Nie umiem znaleźć informacji o jego licencji i autorach.</small>  
Po wyszukaniu stacji także uzyskasz listę programów z inf. o częstotliwościach  
[`py xml_HiDTV.py`]({{site.baseurl}}/assets/files/xml_HiDTV.py) 
 <small>\- używa [`DTV_DK_CCIR.py`  (pobierz)]({{site.baseurl}}/assets/files/DTV_DK_CCIR.py), należy też zainstalować "xmltodict": `py -m pip install xmltodict`</small>

- - - - - 
<br>
<small>
Można też uruchomić skrypt, który daje listę częstotliwości kanałów w standardzie D/K (CCIR) - 
[`tvMHz.py`]({{site.baseurl}}/assets/files/tvMHz.py)
lub
[`tvMHz.ps1`]({{site.baseurl}}/assets/files/tvMHz.ps1).
</small>


- - - - - 
<br>
W urządzeniach AndroidTV z adapterem do TV naziemnej działa np. program LiveTV.  
Po wyszukaniu kanałów w programie LiveTV i zapisaniu danych na pendrive 
powstaje plik "\backup_user_databases\TvProviderChannels\tv_provider_db.json".
Po uruchomieniu w tym samym folderze  
[`py andr_tv_chn_db.py`]({{site.baseurl}}/assets/files/andr_tv_chn_db.py)  
powstaje "andrTVchInfo.csv" z aktualną informacją o dostępnych kanałach DVB-T/T2 

W tym samym folderze można uruchomić skrypt z [`andr_tv_chng_nr.zip`]({{site.baseurl}}/assets/files/andr_tv_chng_nr.zip)  
wcześniej przygotowując dane ze swoją numeracja w "andr_tv_chng_nr.csv".

<style> pre code {font-size: smaller;} small code {font-size:95%;} </style>

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