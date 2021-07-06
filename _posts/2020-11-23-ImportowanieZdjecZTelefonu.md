---
layout: post
title:  "Importowanie zdjęć i filmów z telefonu"
date:   2020-11-23 07:00:00 +0100
categories: Programowanie
---

Skrypt Powershell "importCameraRoll.ps1"


1. Importuje multimedia z telefonów / apartów kilku domowników.
2. Uwzględnia tylko nowsze dane od ostatniego importu.
3. Zmienia nazwy plików na "yyyy-MM-dd_hh.mm.ss..." i umieszcza je w bibliotekach Obrazy albo Wideo w folderach jak rok i podfolderach jak data dnia albo miesiąca.
4. Wymaga jednorazowej konfiguracji dla każdego telefonu / aparatu na podstawie danych wyświetlanych w eksploratorze Windows po podłączeniu urządzenia kablem USB.

Plik do pobrania [**importCameraRoll.ps1**(.zip)]({{ site.baseurl }}/assets/files/importCameraRoll.zip "importCameraRoll.zip") 

<small>
Jeśli uruchamiasz Powershel po raz pierwszy to przeczytaj początkowe 2 zdania w 
["Hybrydowy skrypt CMD-PowerShell"]({% if jekyll.environment == "production" %}{{ site.baseurl }}{% endif %}{% post_url 2021-03-22-Hybrydowy_skrypt_CMD-Powershell %})
.</small>

Początkowy fragment skryptu:
````powershell
$phoneCameraFolder = @{ 
# nazwę aparatu i właściwy folder DCIM należy odczytać w eksploratorze Windows
  'A40'  = '\Card\DCIM\Camera'
  'Mi 9T'= '\Wewnętrzna pamięć współdzielona\DCIM\Camera'
}
$phonePostfix = @{ #dopisek tuż przed rozszerzeniem nazwy pliku
  'A40'  = '_a'
  'Mi 9T'= ''
}
$tmp='.tmp'
# - tymczasowe miejsce kopiowania z aparatu (względem folderu skryptu) 
# - powinno to być na tym samym dysku co Obrazy i Wideo
            # poniżej podwójne tablice $iv = 0..1 dla _img, _vid
$filterImgVid=@( '(.jpg)|(.jpeg)|(.png)|(.heic)|(.heif)$',
                 '(.mp4)|(.mpeg)|(.mpg)|(.hevc)$' )
````
URUCHAMIANIE: `powershell.exe -noexit -File "importCameraRoll.ps1"`  
[![IKONA-Zgrywanie_zdjec_i_filmow.png]({{ site.baseurl }}/assets/img/IKONA-Zgrywanie_zdjec_i_filmow.png "IKONA-Zgrywanie_zdjec_i_filmow.png"){:style="float:right;width:88px;"}]({{ site.baseurl }}/assets/files/Zgrywanie_zdjec_i_filmow.zip "Zgrywanie_zdjec_i_filmow.zip ")
<small> Możesz sobie zrobić na pulpicie skrót z takim poleceniem w polu "Element docelowy:" i z "Rozpocznij w:" <_folder, w krórym jest skrypt_>. Warto też dobrać stosowną nazwę i ikonkę tego skrótu. Możesz go wypakować z pliku ZIP (ikona po prawej) tylko we właściwościach musisz wpisać poprawną  ścieżkę "Rozpocznij w:" do foldera w któym jest plik "importCameraRoll.ps1". </small>


Więcej informacji:

1. Kopiowanie plików z DCIM na podstawie nazwy z pominiętymi początkowymi nie-cyframi, 
która jest większa od maksymalnej takiej nazwy ostatnio skopiowanej - zapamiętanej w pliku json.
Tu nie jest ważne co zawierają ciągi cyfr - ważne, żeby nowsze pliki dawały wyższą wartość podczas 
porównywania łańcuchów znaków.
2. Pliki z DCIM są kopiowane do foldera ".tmp". Tam można także wrzucić ręcznie jakieś pliki.
3. Zakładamy, że ciąg cyfr w nazwie w DCIM- pomijając wszelkie nie-cyfry - zawiera yyyyMMddhhmmss...
Będzie to generowało nazwę pliku "yyyy-MM-dd_hh.mm.ss...", gdzie w "..." będzie zachowana 
oryginalna końcówka nazwy oryginalnej, np. "_1_HDR.jpg".  
Jeśli nie ma takich cyfr, to pobierana jest data modyfikacji, a gdy i jej brak to data aktualna.
4. Zdjęcia są docelowo kopiowane do biblioteki "Obrazy" do foldera "yyyy\yyyy-MM-dd".  
Filmy są kopiowane do biblioteki "Wideo" do foldera "yyyy\yyyy-MM".
5. Gdyby plik docelowy o wygenerowanej nazwie "yyyy-MM-dd_hh.mm.ss..." już istniał, to 
    - jeśli ma różną treść, dopisywana jest "_<liczba>" poczynając od "_7" w górę. 
    - jeśli oba są o identycznej treści, to kopiowanie jest pomijane:
        - wstępnie sprawdzany jest rozmiar w px i wielkość w bajtach itp.
        - jeśli te są identyczne, to plik nie jest kopiowany, a na końcu, po porównaniu binarnym jest usuwany z ".tmp". Na koniec folder ".tmp" powinien być pusty.

