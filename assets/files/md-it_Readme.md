# `markdown-it` z opcjami i dodatkami w wierszu pleceń.

Wersja CLI (linia poleceń/skrypt) dla `node` `markdown-it` dająca wynik podobny do tego, który daje wtyczka `markdown-it viewer`.
Można konfigurować opcje i dodatki.

Sposób instalacji:

1. `nvm`, dla Windows <https://github.com/coreybutler/nvm-windows>  
   * nvm-setup.exe 
     * podaję foder do instalacji pakietów (nie musi być C:)
     * akceptuję folder dla skrótu dla "nodejs": `C:\nvm4w\nodejs`
2. W oknie terminala:
   ```batch
   nvm install latest
   nvm use latest
   npm install -g  markdown-it markdown-it-task-lists markdown-it-attrs markdown-it-footnote 
   npm install -g markdown-it-container markdown-it-anchor markdown-it-prism
   ```
3. W folderze "c:\nvm4w\nodejs\" (który już jest w PATH) umieszczam rozpakowany ZIP, czyli plik "md-it.cmd" i folder "usr" z zawartością.

Od tego momentu można gdziekolwiek uruchamiać polecenie `md-it.cmd "plik źródłowy.md"` i będzie powstawał `plik źródłowy.html`. Plik HTML będzie używał arkusza stylów z foldera "c:\nvm4w\nodejs\usr\css"

Można następnie użyć także `embed-img.cmd` aby do podanego pliku HTML tekstowo wbudować obrazki lokalne.

<style> pre code { font-size: 90% !important; } pre {line-height: 1.2 !important; border: 1px lightgrey solid;}
.token.variable { color: #905; } .token.string { color: green; } .token.key.attr-name { color: darkgreen; }</style>
