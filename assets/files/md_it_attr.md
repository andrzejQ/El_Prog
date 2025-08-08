Zob.
* <https://github.com/arve0/markdown-it-attrs>


| E                       | F   | G   | H    |
| ----------------------- | --- | --- | ---- |
| 1                       | 11  | 111 | 1111 |
| 2 {colspan=2}                 | 222 | 2222 | 
| 3 {colspan=3}                       | 3333 |


Tu dokładane są dodatkowe komórki pomimo `colspan`. HTML:

<table>
<thead>
<tr><th>E</th><th>F</th><th>G</th><th>H</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>11</td><td>111</td><td>1111</td></tr>
<tr><td colspan="2">2</td><td>222</td><td>2222</td><td></td></tr>
<tr><td colspan="3">3</td><td>3333</td><td></td><td></td></tr>
</tbody>
</table>

Można by ich nie wyświetlać za pomocą stylu `{display: none;}` dla komórek sąsiednich ` ~ td` względem `td.c0`. 

```html
<style>
.c0, .test {color:fuchsia;} td.c0 ~ td,  th.c0 ~ th {display: none;} 
/*ale to usuwanie nie zadziała dla nagłówka i pierwszego wiersza*/
</style>
```
<style>
.c0, .test {color:fuchsia;}
td.c0 ~ td,  th.c0 ~ th {display: none;} 
/*ale to usuwanie nie zadziała dla nagłówka i pierwszego wiersza*/
</style>

| J                       | K   | L   | M{.test}   |
| ----------------------- | --- | --- | ---------- |
| 1                       | 11  | 111 | 1111 {.c0} |
| 2 {colspan=2}                 | 222 | 2222 {.c0} | 
| 3 {colspan=3}                       | 3333 {.c0} |

{border=2}

Jest prawie dobrze, tylko nie wiadomo dlaczego niektóre atrybuty dla ostatniej komórki są rzutowane na cały wiersz. HTML:

<table border="2">
<thead class="test">
<tr><th>J</th><th>K</th><th>L</th><th>M</th></tr>
</thead>
<tbody>
<tr class="c0"><td>1</td><td>11</td><td>111</td><td>1111</td></tr>
<tr><td colspan="2">2</td><td>222</td><td class="c0">2222</td><td></td></tr>
<tr><td colspan="3">3</td><td class="c0">3333</td><td></td><td></td></tr>
</tbody>
</table>

Można zadawać klasę w przedostatniej kolumnie i nie wyświetlać komórek `td.c1+td ~ td`. To działa.

```html
<style>
td.c1+td, .test1+th {color:blue;}
td.c1+td ~ td {display: none;} 
/*klasa wstawiana dla komórek w przedostatniej kolumnie*/
</style>
```
<style>
td.c1+td, .test1+th {color:blue;}
td.c1+td ~ td {display: none;} 
/*klasa wstawiana dla komórek w przedostatniej kolumnie*/
</style>


| N                       | O   | P {.test1}| Q    |
| ----------------------- | --- | --------- | -----|
| 1                       | 11  | 111 {.c1} | 1111 |
| 2 {colspan=2}                 | 222 {.c1} | 2222 | 
| 3 {colspan=3 .c1}                         | 3333 |

{border=2}


Albo można dodać sztuczną dodatkową kolumnę, która nie będzie wyświetlana.

| A                       | B   | C   | D              {.c0} | |
| ----------------------- | --- | --- | ---------------- | --- |
| 1                       | 11  | 111 | 1111 {rowspan=3 .c0} | |
| 2 {colspan=2 rowspan=2}       | 222                  {.c0} | |
|                                 333                  {.c0} | |

{border=1}


W markdown pipe-table nagłówek musi mieć pełną, docelową liczbę kolumn. Można scalić komórki pierwszego wiersza, a pusty nagłówek usunąć.

```html
<style>
.tab3 > thead {display: none;}
</style>
```
<style>
.tab3 > thead {display: none;}
</style>


|                         |     |     |               |
| ----------------------- | --- | --- | ------------- |
| **Tytuł przez 4 kolumny**           {colspan=4 .c0} |
| 1                       | 11  | 111 | 1111          |
| 2 {colspan=2}                 | 222 | 2222    {.c0} | 
| 3 {colspan=3}                       | 3333    {.c0} |

{border=4 .tab3}

<style> pre {font-size: 90% !important; } </style>