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
    stronie 1-szej, 2-giej i ostatniej. Raczej powinien to być tekst w białym kolorze (niewidoczny pod sygnaturką podpisu).
2.  Zapisz jako PDF
3.  Uruchom: `toSign.py "NAZWA PLIKU.PDF"`
4.  Wynik zostanie zapisany w "NAZWA PLIKU**_toSign.PDF**"

**Aby uruchomić \"toSign.py\":**

Przygotowanie

1.  Zainstaluj PYTHON v.3.8+ (a najlepiej najnowszy; testowałem to w v.3.12)
2.  Zainstaluj moduły (okno terminala, np. CMD): `python -m pip install pyHanko pdfplumber`
3.  Pobierz i rozpakuj w folderze twojego pliku PDF: 
	* [**toSign.py_test.zip**]({{site.baseurl}}/assets/files/toSign.py_test.zip  "toSign.py_test.zip ")

Uruchamianie

*  W oknie terminala (CMD) uruchamiaj: `python toSign.py "NAZWA PLIKU.PDF"` (lub w oknie eksploratora w pasku ścieżki do plików wpisz: `python -i toSign.py "NAZWA PLIKU.PDF"`).



<details markdown=1><summary markdown="span">src. **`toSign.py`** . . . </summary>

````py
import pdfplumber # pip install pdfplumber
import pyhanko    # pip install pyHanko
from pyhanko.sign.fields import SigFieldSpec, append_signature_field
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields
import shutil
import argparse

def cli_args():
  parser = argparse.ArgumentParser(
    usage='python toSign.py FILE.PDF',
    description=f'''Replace specific graphical objects with an empty signature fields.
  Objects like rectangles or table cell containig text starting with pattern.
  Loop on pages from list like [0,1,-1] i.e. first, second and last page.''',)
  parser.add_argument('input_file')
  parser.add_argument('-o', '--output',
                 help='or default FILE_toSign.PDF')
  parser.add_argument('-t', '--txt_pattern', default='signature field')
  parser.add_argument('-p', '--pages', nargs='+', type=int, default=[0,1,-1], 
                 help='as last param. Pages to analyse e.g.: --pages 0 1 -1')
  return parser.parse_args()

def main ():
  args=cli_args() ;print(f'{args=}') #$# py 3.8+
  out_suffix='_toSign' #to insert before last '.pdf' in output file of not --output
  output_file = args.output or f'{args.input_file[:-4]}{out_suffix}{args.input_file[-4:]}'
  print(f'{output_file=}') #$#
  shutil.copy(args.input_file, output_file)
  # # #
  num_added = addSignatureFields(output_file, args.txt_pattern, args.pages)
  print(f'{num_added=}')

def addSignatureFields(path, pattern, pages):
#  https://github.com/MatthiasValvekens/pyHanko/issues/8#issuecomment-803586088
#
#  Objects to place empty signature field on it are:
#  - Rectangles containing a string that starts with the string specificed in pattern
#  The rectangles may have any linecolor, linewidth (including 0 pts) and filling color
#  The string may have any color, font and font size. Even a white box with white text 
#  on white background should be sufficient. Cannot be used inside a table cell. 
#  - Table cells containing a string that starts with the string specificed in pattern
#  All four cell borders must be visible in the PDF file
#
# INPUT:
#   path: Path to PDF file to be processed. The file will be replaced with the resulting file
#   pattern: String to match (startwith, case insensitive) against cell/rect content
#   pages: Pages to analyse, e.g. [0, 1, -1] will analyze the first two and the last page 
#   if they exist. Use None for all pages.
#
# RETURN: 
#   Number of signature fields added to the PDF
#
  # inner function used for tables and rectangels:
  def appendSignField(iFieldCounter, occupied_boxes,   pattern, pg, wrPdf,
                      field_bbox, additional_info, sig_box):
    def intersects(box1, box2):
      return not (box1[2] <= box2[0] or box1[0] >= box2[2] or box1[3] <= box2[1] or box1[1] >= box2[3])
    try:
      field_text = page.crop(field_bbox).extract_text()
    except ValueError:
      print("Error. Perhaps a rect reaches outside of the page")
    if field_text and field_text.strip().lower().startswith(pattern):
      for t in occupied_boxes:
        if intersects(t, field_bbox): break
      else: # i.e. no intersects anywhere
        print(f"Placing signature field {iFieldCounter} {additional_info} on page {pg}")
        occupied_boxes.append(field_bbox)
        append_signature_field(wrPdf, SigFieldSpec(sig_field_name=f"Signature {iFieldCounter}", 
          on_page=pg, box=sig_box))
        iFieldCounter += 1
    return iFieldCounter, occupied_boxes
#
  pattern = pattern.lower()
  with pdfplumber.open(path) as inpdf:
    with open(path, 'rb+') as outpdf:
      iFieldCounter = 0
      wrPdf = IncrementalPdfFileWriter(outpdf)
      if not pages:
        page_selection = range(len(inpdf.pages))
      else:
        _max_page = len(inpdf.pages)
        page_selection = set([(p % _max_page) for p in pages if (p >=-_max_page and p < _max_page)])
      print(f'{page_selection=}') #$#
      for pg in page_selection:
        page =inpdf.pages[pg]
        occupied_boxes = [] # occupied_boxes contains a list of areas where no further field can be placed.
          #These areas include bounding boxes of fully analyzed tables and already placed signature fields.
        
        for table in page.find_tables():
          for c, cell in enumerate(table.cells):
            iFieldCounter, occupied_boxes = appendSignField(iFieldCounter, occupied_boxes, pattern,pg,wrPdf,
              field_bbox = [cell[0], cell[1], cell[2], cell[3]], 
              additional_info=f"in table cell {c}",
              sig_box=[1.01*cell[0], page.height - 1.01*cell[1], 0.99*cell[2], page.height - 0.99*cell[3]])
          occupied_boxes.append(table.bbox)
        
        for rect in page.rects:
          iFieldCounter, occupied_boxes = appendSignField(iFieldCounter, occupied_boxes, pattern,pg,wrPdf,
            field_bbox =[rect['x0'],rect['top'],rect['x1'],rect['bottom']], 
            additional_info=f"in box",
            sig_box=[rect['x0'],rect['y0'],rect['x1'],rect['y1']])
      #end for pg...
      wrPdf.write_in_place()
  return iFieldCounter # number of sign fields added

#----------------------------------

if __name__ == "__main__":
  main ()
````
</details>

. 
![toSign.png ]({{site.baseurl}}/assets/img/toSign.png  "toSign.png "){: style="float:right;width:71%;"}

.

.

* Przykład: 
  [test_docx.pdf]({{site.baseurl}}/assets/files/test_docx.pdf  "test_docx.pdf")   → 
  [test_docx_toSign.pdf]({{site.baseurl}}/assets/files/test_docx_toSign.pdf  "test_docx_toSign.pdf") 
  <small>(otwieraj w Adobe Reader!)</small>

- - - -

Odnośniki:
* <https://github.com/MatthiasValvekens/pyHanko/issues/8#issuecomment-803586088>
* [Podpisy cyfrowe](https://andrzejq.github.io/Office_S_Tips/pki/2019/09/19/Podpisy_cyfrowe.html)

<style> pre code {font-size: smaller;} </style>

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