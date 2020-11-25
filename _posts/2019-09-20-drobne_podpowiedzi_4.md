---
layout: post
title:  "Kabel USB tylko do ładowania"
date:   2019-09-20 13:21:59 +0100
categories: Elektronika
---

Tu raczej nie ma nic ciekawego: [2-żyłowe kabelki USB tylko do ładowania]({{ site.url }}{{ site.baseurl }}{{ page.url }}#2-żyłowe-kabelki-usb-tylko-do-ładowania)

----

### 2-żyłowe kabelki USB tylko do ładowania 

Aby ładować urządzenia przez gniazdo mikro-USB lub USB-C prądem 1A i większym potrzeba kabla z odpowiednio grubymi żyłami. Jeśli chodzi tylko o ładowanie to wystarczyłby w zasadnie dobry kabel 2-żyłowy (pomijając system szybkiego ładowania napięciem wyższym niż 5V, bo wtedy potrzebny jest kabel co najmniej 4 żyłowy, a grubość żył nie jest tak krytyczna).

![Mikro-USB.png]({{ site.baseurl }}/assets/img/Mikro-USB.png "Mikro-USB.png"){:style="float:left;width:30%;"} Sam solidny kabel 2-żyłowy nie wystarcza - trzeba odpowiednio połączyć styki wtyku kabla. We wtyku mikro-USB trzeba zewrzeć nieużywane styki danych (3)D+ i (2)D- oraz styk (4) połączyć do (5) opornikiem R. ![Mikro-USB-wtyk-podlaczenie.png]({{ site.baseurl }}/assets/img/Mikro-USB-wtyk-podlaczenie.png "Mikro-USB-wtyk-podlaczenie.png"){:style="float:right;width:16%;"} Różni producenci mają swoje nominalne wartości, np. 130kΩ, 190kΩ, 200kΩ, 301kΩ.  Zdaje się, że dołączenie opornika o dowolnej z podanych wartości daje dobry efekt. Obraz po prawej to wyprowadzenie wtyku mikro-USB do lutowania. Uwaga - tanie wtyki mikro-USB i USB-C do lutowania mogą być źle wykonane, np. zbyt ciasne - lepiej takich nie używać.

W przypadku [kabla USB-C](https://masters.com.pl/pl/usb-typu-c/) konieczne jest (gdy chodzi o kabel 2 żyłowy) zwarcie niepodłączonych linii danych D+ i D- . Co ciekawe nawet w przypadku, gdy linie CC ([zob.](https://masters.com.pl/pl/usb-typu-c/) tabela 2) są podwieszone do +5V opornikiem 56kΩ, czyli dla przypadku domyślnej wartości mocy USB odbiornik jednak potrafi pobrać znacznie większy prąd, zgodnie z możliwościami zasilacza i możliwościami żył kabla. 

Takie właśnie podwieszenie, tj. 56kΩ jest stosowane w przejściówkach mikro-USB -> USB-C. Gdy więc zastosujemy niezły kabel 4-żyłowy z wtykiem mikro-USB + przejściówka, to z kolei odbiornik USB-C potrafi się dogadać z kompatybilnym zasilaczem i włączyć szybkie ładowanie z napięciem wyższym niż 5V, a w takim wypadku oporność żył kabla nie jest już tak krytyczna. (Oczywiście najlepszy jest mimo wszystko oryginalny kabel z wtykiem USB-C).

