---
layout: post
title:  "Szablon importu zakładek Firefox"
date:   2025-07-25 13:30:49 +0200
categories: Przeglądarka internetowa
---

To koniec POCKETa. Można wyeksportować odnośniki i przełożyć je jako folder zakładek w Firefox.

**Szablon EXCEL** - [pocket2bookmk_templ_FF.zip]({{site.baseurl}}/assets/files/pocket2bookmk_templ_FF.zip   "pocket2bookmk_templ_FF.zip")

Po wkopiowaniu danych do Excela:
1. Zauważ, że poniżej jest potrzebny wiersz `="</DL><p></DL><p></BODY></HTML>"`, który teraz jest w G2.
2. Całą kolumnę G skopiuj do pliku tekstowego z kodowaniem UTF-8 "Jakaś nazwa.HTML".
3. W Firefix: [Ctrl+Shift+O] (tj. Biblioteka) -> Importowanie i kopie zapasowe \ Importuj zakładki z pliku HTML...


<style> code {font-size: 85%;} </style>

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