---
layout: post
title:  "Wstawianie pola podpisu w pliku PDF"
date:   2024-10-17 10:55:00 +0100
categories: Programowanie
---

Do pliku PDF utworzonego np. z DOCX można dodać pola podpisu, które ułatwiają wstawianie podpisów w Adobe Reader.

----
.


**Wstawianie pól podpisu w pliku PDF:**

1.  Przygotuj w swoim dokumencie DOCX miejsca na pola podpisu. Może to być pole tekstowe 
    z tekstem \"Signature field ...\" lub tabela z tekstem w komórce
    \"Signature field ...\". Domyślnie program szuka takich obiektów na
    stronie 1-szej, 2-giej i ostatniej.
2.  Zapisz jako PDF
3.  Uruchom: `python toSign.py "NAZWA PLIKU.PDF"`
4.  Wynik zostanie zapisany w "NAZWA PLIKU**_toSign.PDF**"

**Aby uruchomić \"toSign.py\":**

1.  Zainstaluj PYTHON v.3.8+
2.  Zainstaluj moduły (okno CMD): `python -m pip install pyHanko pdfplumber`
3.  Pobierz i rozpakuj w folderze twojego pliku PDF: 
	* [**toSign.py_test.zip**]({{site.baseurl}}/assets/files/toSign.py_test.zip  "toSign.py_test.zip ") 
4.  W oknie CMD uruchamiaj: `python toSign.py "NAZWA PLIKU.PDF"`



- - - -

Odnośniki:
* <https://github.com/MatthiasValvekens/pyHanko/issues/8#issuecomment-803586088>


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