---
layout: post
title:  "MarkDown - zastosowania"
date:   2024-03-11 12:00:00 +0100
categories: Programowanie
---

[1. System wielo-plikowej dokumentacji MarkDown]({{site.url}}{{site.baseurl}}{{page.url}}#1system-wielo-plikowej-dokumentacji-markdown) * 
[2. pandoc -> MD]({{site.url}}{{site.baseurl}}{{page.url}}#2pandoc---md) 


<style>.date{font-size: smaller;color:#828282;}</style>

### 1. System wielo-plikowej dokumentacji MarkDown 

Przykład systemu dokumentacji tworzonej w polikach lokalnych MarkDown z ilustracjami i wzajemnie linkowanymi plikami.

Założenia:
1. Edytor tekstowy, który ułatwia otwieranie plików wspomnianych w tekście.  
   Tu **Notepad++** (N++), który po zaznaczeniu w tekście ścieżki/nazwy  ma opcję p.kl.myszy: "Otwórz plik". N++ z opcjonalnie zainstalowaną wtyczką "MarkdownPanel".
2. Przeglądarka www z wtyczką interpretującą pliki MarkDown.  
   Tu [**Markdown Viewer**](https://github.com/simov/markdown-viewer).
3. Dodatkowo warto mieć w przeglądarce wtyczkę, która generuje MarkDown na podstawie zaznaczonego fragmentu strony www (w tym zaznaczenia fragmentu przetłumaczonego).  
   Tu [**MarkDownload**](https://github.com/deathau/markdownload).
4. Po zakończonym okresie częstego edytowania dokumentacji można wyeksportować wszystkie "*.md" do "*.html" (skrypt?) i linkujące się dokumenty będą działały w przeglądarkach www bez zainstalowanych wtyczek MarkDown.

Tak jak obrazy `![]()` tak i pliki linkowane `➔📎 [** **]( )` wstawiam ze ścieżkami względnymi w takiej składni:

```md
➔📎 [**./inny_plik.md**](./inny_plik.md ) 
```
co dla HTML daje link:

➔📎 [**./inny_plik.md**](./inny_plik.md ) 

Po jego kliknięciu w przeglądarce www, gdy był oglądany (i interpretowany) w niej aktualny plik "*.md" otwierany jest "./inny_plik.md" i od razu interpretowany przez wtyczkę "Markdown Viewer".

Działając natomiast w pliku "*.md" w N++ zaznaczam ścieżkę do pliku, p.kl.myszy "Otórz plik".

Najwygodniej jest, gdy nazwy są bez spacji. Inaczej trzeba je zamienić w linku na `%20`:  
```md
➔📎 [**./kolejny plik.md**](./kolejny%20plik.md )
```
a w N++ zaznaczać ścieżkę z lewej strony - tu: `./kolejny plik.md`. Spacja przy końcowym nawiasie `␣)` nie przeszkadza w interpretacji linku, a jest pomocna podczas zamieniania wcześniejszych na `%20`.

W ten sposób można dołączać też inne pliki, np. tekstowe, czy takie jak PDF, które w edytorze tekstowym się nie otworzą, ale nieźle zadziałają w przeglądarce.

----
.

#### Moja konfiguracja wtyczek MarkDown

Obie wtyczki wymagają zezwolenia na pracę z plikami lokalnymi - co jest opisane w ich instrukcjach.

**Markdown Viewer**:

Włączyłem sobie dodatkowo -> opcje COMPILER (po kliknięciu w ikonę wtyczki): 
* `attr` (Custom attributes using `{}`), 
* `sub` (`~a~`), 
* `sup` (`^a^`), 
* `tasklists` (`- [x]`)

.

**MarkDownload**

Po kliknięciu w ikonę wtyczki mamy ⚙️ w prawym górnym rogu. Można zapisać swoje ustwienia i porównać z moimi:

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

### 2. pandoc -> MD

* Konfiguracja TotalCommander [pandoc -> MD]({% if jekyll.environment == "production" %}{{site.baseurl}}{% endif %}{% post_url 2019-09-07-Notepad++.config %}) - TotalCommnder \ pandoc -> MD


<style> code {font-size: 0.93em;}  div.zmniejsz code {font-size: 0.88em;}  </style>
