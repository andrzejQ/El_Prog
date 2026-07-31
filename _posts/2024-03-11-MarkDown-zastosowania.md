---
layout: post
title:  "MarkDown - zastosowania"
date:   2024-03-11 12:00:00 +0100
categories: Programowanie
---

_+ 31.07.2026_{: .date} _+ 07.03.2025_{: .date} _+ 05.08.2025_{: .date}  
[1. System wielo-plikowej dokumentacji MarkDown]({{site.url}}{{site.baseurl}}{{page.url}}#1system-wielo-plikowej-dokumentacji-markdown) * 
[2. Markdown it! -> HTML]({{site.url}}{{site.baseurl}}{{page.url}}#2markdown-it---html) *  
[3. pandoc MD -> HTML]({{site.url}}{{site.baseurl}}{{page.url}}#3pandoc-md---html) * 
[4. pandoc -> MD]({{site.url}}{{site.baseurl}}{{page.url}}#4pandoc---md) * 
[5. PowerToys -> MD]({{site.url}}{{site.baseurl}}{{page.url}}#5powertoys---md) *  
[6. MD-ściągawka]({{site.url}}{{site.baseurl}}{{page.url}}#6md-ściągawka) 

<style>.date{font-size: smaller;color:#828282;}</style>
### 1. System wielo-plikowej dokumentacji MarkDown 


Przykład systemu dokumentacji tworzonej w polikach lokalnych MarkDown z ilustracjami i wzajemnie linkowanymi plikami.

Założenia:
1. Edytor tekstowy, który ułatwia otwieranie plików wspomnianych w tekście.  
   Tu **Notepad++** (N++), który po zaznaczeniu w tekście ścieżki/nazwy  ma opcję p.kl.myszy: 
   "Otwórz plik". N++ z opcjonalnie zainstalowaną wtyczką "MarkdownPanel".  
   <small>Ta lekka wtyczka w wersji od 0.9 ma nowoczesną opcję renderowania HTML za pomocą **WebView2 Edge**.
   Dodatkowo kliknięcie  w oknie panelu w odnośnik do pliku, np. md, txt, itp. od razu otwiera ten plik w N++.</small>
   
2. Przeglądarka www z wtyczką interpretującą pliki MarkDown.  
   Tu [**Markdown Viewer**](https://github.com/simov/markdown-viewer) ![](https://raw.githubusercontent.com/simov/markdown-viewer/refs/heads/main/icons/default/19x19.png) .  
   Składnia w bloku kodu jest kolorowana z pomocą <https://prismjs.com/>. Dostępnych jest wiele języków programowania. Łatwo też można korygować kolory, dodając  w pliku `*.md` np. 
   ```css
   <style> pre code { font-size: 90% !important; } pre {line-height: 1.2 !important; border: 1px lightgrey solid;}
   .token.variable { color: #905; } .token.string { color: green; } .token.key.attr-name { color: darkgreen; }</style>
   ```
   <small>(30.07.2026 - zapewne po aktualizacjach wtyczka przestała działać dla lokalnych plików. Wymagało to wejścia do menu: Zarządzaj rozszerzeniem / Uprawnienia i dane / [x] Dostęp do lokalnych plików na tym komputerze)</small>
   
3. Dodatkowo warto mieć w przeglądarce wtyczkę, która generuje MarkDown na podstawie zaznaczonego fragmentu strony www (w tym zaznaczenia fragmentu przetłumaczonego).  
   Tu [**MarkDownload**](https://github.com/deathau/markdownload).
4. Po zakończonym okresie częstego edytowania dokumentacji można wyeksportować wszystkie "*.md" do "*.html" [z pomocą skryptu](#2markdown-it---html) i linkujące się dokumenty będą działały także w przeglądarkach www bez zainstalowanych wtyczek MarkDown.

Tak jak obrazy `![]()` tak i pliki linkowane `➔📎 [** **]( )` wstawiam ze ścieżkami względnymi w takiej składni:

```md
➔📎 [**./inny_plik.md**](./inny_plik.md ) 
```
co dla HTML daje link:

➔📎 [**./inny_plik.md**](./inny_plik.md ) 

Po jego kliknięciu w przeglądarce www, gdy był oglądany (i interpretowany) w niej aktualny plik "*.md" otwierany jest "./inny_plik.md" i od razu interpretowany przez wtyczkę "Markdown Viewer".

Działając natomiast w pliku "*.md" w N++ zaznaczam ścieżkę do pliku, p.kl.myszy "Otwórz plik" albo najlepiej - klikając na link w panelu MD N++

Najwygodniej jest, gdy nazwy są bez spacji. Inaczej trzeba je zamienić w linku na `%20`:  
```md
➔📎 [**./kolejny plik.md**](./kolejny%20plik.md )
```
a w N++ zaznaczać ścieżkę z lewej strony - tu: `./kolejny plik.md`. Spacja przy końcowym nawiasie `␣)` nie przeszkadza w interpretacji linku, a jest pomocna podczas zamieniania wcześniejszych na `%20`.

W ten sposób można dołączać też inne pliki, np. tekstowe, czy takie jak PDF, które w edytorze tekstowym się nie otworzą, ale nieźle zadziałają w przeglądarce.

----
.

#### Moja konfiguracja wtyczek MarkDown

Obie wtyczki wymagają zezwolenia na pracę z plikami lokalnymi (Advanced opt./Szczegóły - File Access) - co jest opisane w ich instrukcjach.

**Markdown Viewer**:

Uwaga! Aby zezwolić na auto-konwersję plików lokalnych Markdown trzeba [włączyć ustawienia](https://github.com/simov/markdown-viewer?tab=readme-ov-file#manage-origins)
 w nieco magicznej sekwencji (tu przykładowa sekwencja dla FF/Win):
1. `ADVANCED OPTIONS` (po kliknięciu na ikonę ***m***)
2. **File Access** `ALLOW ACCESS`
3. **Site Access** `ALLOW ALL`
4. Po tym przy **File Access** pojawia się `REFRESH` i po kliknięciu mamy okazję w wyskakującym okienku zezwolić na dostęp.

Włączyłem sobie dodatkowo -> opcje COMPILER (po kliknięciu w ikonę wtyczki) `MARKDOWN-IT`  
oprócz domyślnie zaznaczonych `html`, `linkify`:
* `attr` (Custom attributes using `{}`), 
* `footnote` (`[^1]: tekst`)
* `sub` (`~a~`), 
* `sup` (`^a^`), 
* `tasklists` (`- [x]`)

<small> A `linkify` zwykle odznaczam, bo linkuje również `m.in.`, a przecież zawsze poprawnie działają linki w `<...>`  
Warto też przeglądnąć opcje `CONTENT` i ich [**przykłady**](https://github.com/simov/markdown-syntax).</small>

Opis na stronie <https://github.com/arve0/markdown-it-attrs> dotyczący atrybutów wpisanych w `{...}` jest prawie zgodny z działaniem w tej wtyczce, choć w przypadku tabeli nie zawsze to się zgadza. Problemem są m.in. atrybuty zadawane w ostatniej komórce wiersza i nie udaje się scalanie komórek (wersja Markdown Viewer z 23.05.2024). Częściowo udaje się to obejść - zob. źródłowy plik
* [`md_it_attr.md`]({{site.baseurl}}/assets/files/md_it_attr.md)
.

.

**MarkDownload**

Po kliknięciu w ikonę wtyczki mamy ⚙️ w prawym górnym rogu. Można zapisać swoje ustawienia i porównać z moimi:

<details markdown=1><summary markdown="span"><u>MarkDownload-export-AK.json</u><br> . . .</summary>

```json
{
  "headingStyle": "atx",
  "hr": "---",
  "bulletListMarker": "*",
  "codeBlockStyle": "fenced",
  "fence": "```",
  "emDelimiter": "_",
  "strongDelimiter": "**",
  "linkStyle": "inlined",
  "linkReferenceStyle": "full",
  "imageStyle": "markdown",
  "imageRefStyle": "inlined",
  "frontmatter": "---\ncreated: {date:YYYY-MM-DD HH:mm:ss} (UTC {date:Z})\ntags: [{keywords}]\nsource: {baseURI}\nauthor: {byline}\n---\n\n# {pageTitle}\n\n> ## Excerpt\n> {excerpt}\n\n---",
  "backmatter": "",
  "title": "{pageTitle}",
  "includeTemplate": false,
  "saveAs": true,
  "downloadImages": true,
  "imagePrefix": "img/",
  "mdClipsFolder": "MarkDownload/{pageTitle}",
  "disallowedChars": "[]#^",
  "downloadMode": "downloadsApi",
  "turndownEscape": true,
  "contextMenus": true,
  "obsidianIntegration": false,
  "obsidianVault": "",
  "obsidianFolder": ""
}
```

</details>

.

### 2. Markdown it! -> HTML

Po zainstalowaniu [`Markdown it!`](https://github.com/markdown-it/markdown-it) dla `node.js` można konwertować  MD -> HTML za pomocą skryptu, wypakowanego z  
[`md-it_CLI.zip`]({{site.baseurl}}/assets/files/md-it_CLI.zip )  
Skrypt działa podobnie do wtyczki "Markdown Viewer" - z możliwością wyboru opcji i dodatków.

Parametrem skryptu jest nazwa pliku MD.

Więcej informacji i dokładna instrukcja jest w [`md-it_CLI.zip\doc\md-it_Readme.md`]({{site.baseurl}}/assets/files/md-it_Readme.md).

### 3. pandoc MD -> HTML

Wypakuj plik 
[`markdown-v.head.html.zip`]({{site.baseurl}}/assets/files/markdown-v.head.html.zip)
do foldera `%appdata%\pandoc\`  
<small>Jest to styl skopiowany z wtyczki "Markdown Viewer" dla Edge, który będzie wklejany do nagłówka HTML.</small>

Wszystko z MD w pojedynczym pliku HTML (łacznie z obrazami):
```bat
pandoc -i FROM.md -o 1_(__TO__).html --embed-resources -H %appdata%\pandoc\markdown-v.head.html -M lang=pl
```

HTML z obrazami na zewnątrz (ale markdown-v.head.html jest wklejone do wynikowego pliku):
```bat
pandoc -i FROM.md -o (__TO__).html --standalone -H %appdata%\pandoc\markdown-v.head.html -M lang=pl
```

Wskazówka: jeśli chcemy uzyskać w tabelach automatyczne ustawianie szerokości kolumn to w pliku `*.md` można wstawić:  
`<style> body > table > colgroup > col {width: unset!important;}</style>`
{: style="font-size:smaller;"}


.



### 4. pandoc -> MD

* Konfiguracja TotalCommander [pandoc -> MD]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2019-09-07-Notepad++.config %}) - TotalCommnder \ pandoc -> MD
  
* Skrypt `pipetable_align.py` spakowany w 
  [`pipetable_align.zip`]({{site.baseurl}}/assets/files/pipetable_align.zip)
  wyrównuje spacjami pionowe `|` po konwersji do Markdown w pandoc.  
  Skrypt można zapisać w folderze `%appdata%\pandoc\` i dodać menu w TotalCommander:  
  cmd=`cmd` param=`/k %%AppData%%/pandoc/pipetable_align.py %N`

.


### 5. PowerToys -> MD

* W [**PowerToys**](https://learn.microsoft.com/pl-pl/windows/powertoys/) - narzędzie "Wklejanie zaawansowane" ("Advanced Paste") `[ ⊞ Win + ⇧ Shift + V ]` pozwala m.in. na przekonwertowanie zawartości schowka na tekst markdown.


### 6. MD-ściągawka

_To nie jest przegląd reguł - tylko wybrane przypominajki._

 1. Przy korzystaniu z list warto kolejne wiersze punktu wcinać na tyle spacji ile jest do pierwszego znaku nie-spacji w punkcie, bo to jest pozycja od której liczą się dalsze wcięcia np. dla pod-listy czy bloku kodu. Można to wykorzystać także do oddzielania punktów wierszami z pustymi spacjami - tu spacje są oznaczone jako "∙":
    
        ∙1.∙abc
        ∙∙∙∙
        ∙2.∙def
        ∙∙∙∙
        ∙∙∙∙∙∙∙∙blok kodu w p.2. (4 spacje wiodące)
        ∙∙∙∙∙∙*∙podpunkt w p.2. (ma 2 spacje wiodące)
        ∙∙∙∙
        ∙3.∙ghi∙∙
        ∙∙∙∙złamany wiersz w p.3.
    
    W listach obowiązuje też zasada ręcznego łamania wiersza,␣␣  
    np. 2 spacje na końcu.
    
    Jeśli potrzebujemy własnego znakowania punktów zagnieżdżonych list można użyć stylu, np.:
    ````html
    <style> 
      :root ol ol {list-style-type: lower-alpha;}
      :root ol ol ol {list-style-type: lower-roman;}
    </style>
    ````
    , z tym, że w źródłowym MD należy nadal w zagnieżdżonych listach używać 1. 2. 3. ...
    
 2. Zwinięty tekst:
    
    ```html
    <details markdown=1><summary markdown="span">Rozwiń . . . </summary>
    Zwinięty tekst
    </details>
    ```
    
    <details markdown=1><summary markdown="span">Rozwiń . . . </summary>
    Zwinięty tekst
    </details>
    

 3. Kotwica:
    
    ```html
    Kotwica:
    <span id="anchorName"></span>
    Odnośnik:
    [Idź do...](#anchorName)
    ```
    <span id="anchorName">Podobno lepiej</span> `name=` niż `id=`, bo dla `id` są generowane zmienne globalne javascript, ale jakoś to u mnie nie działa.  
    {: style="font-size:smaller;"}
    
    [Idź do...-test](#anchorName)
    
 4. We wtyczce "Markdown Viewer" nie działa kod zdefiniowany w bloku `<script>`
    
    ... to znaczy prawie nie działa, bo blok `<script>` jest dołączany do HTML, tylko nie jest wykonywany. Ale gdy się wynikowy HTML zapisze jako plik, to `<script>` działa. 
    
    Natomiast jest wykonywany kod javascript inicjowany ręcznie po załadowaniu strony, np.: 
    ````html
    <label style="border:1px solid aqua; padding:2px 6px;" title="Pokaż spis treści">
    <input type="checkbox" 
      onchange="document.querySelector('#toc').style.display=this.checked ? 'block' : 'none';
      if (this.checked) {
        //może być wiele wierszy, tylko nie może być wiersza pustego, ani `"`.
      };"
    >
     📑 Pokazuj spis treści </label>
    
    <div id="toc" style="display:none;"> ... </div>
    ````


----
 

* [Basic writing and formatting syntax - GitHub » ](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
  

<style> code {font-size: 0.93em;}  div.zmniejsz code {font-size: 0.88em;}  
 ol li div.language-plaintext > div > pre {background: linear-gradient(to right, 
 transparent 0em, transparent 2.9em, aqua 2.9em, 
 transparent 3.2em) !important;}
</style>
