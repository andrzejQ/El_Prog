---
layout: post
title:  "Artefakty JPEG - Quant Smooth"
date:   2024-02-05 06:54:00 +0100
categories: Multimedia
---

_+ 27.05.2024_{: .date} JPEG Quant Smooth w IrfanView

<style>.date{font-size: smaller;color:#828282;}</style>


![Opcje_JPG.png]({{site.baseurl}}/assets/img/Opcje_JPG.png "Opcje_JPG.png"){: style="float:right;width:55%;"}

W programie IrfanView można właczyć opcję
"**Ładuj za pomocą metody [QuantSmooth](https://github.com/ilyakurdyukov/jpeg-quantsmooth)**",
która poprawia artefakty kompresji JPEG. 

Przykład:

![Opcje_JPG.png]({{site.baseurl}}/assets/img/JPG_QuantSmooth.png "JPG_QuantSmooth.png"){: style="width:64%;"}

W tak poprawionym obrazie można łatwiej stosować narzędzia edycyjne, np. zmianę tła. A na koniec można zapisać jako plik PNG.

![Opcje_JPG.png]({{site.baseurl}}/assets/img/zapis_OptiPNG.png "zapis_OptiPNG.png"){: style="float:right;width:33%;"}

Mam wrażenie, że także zapisywanie PNG z opcją "[OptiPNG](https://optipng.sourceforge.net/)" powoduje częściowo redukcję tych artefaktów - ale to wrażenie po wykonaniu niewielu prób.


<style> pre code {font-size: smaller;} </style>
<style> small code {font-size: smaller;} </style>

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