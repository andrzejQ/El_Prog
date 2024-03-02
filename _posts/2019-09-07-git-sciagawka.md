---
layout: post
title:  "git - ściągawka"
date:   2019-09-07 08:08:39 +0100
categories: Programowanie
---

_+ 02.03.2024_{: .date} | Ściągawka **git** - na razie brudnopis... 
<style>.date{font-size: smaller;color:#828282;}</style>

````bash
git init

git add .
git commit

git push

git fetch
git merge
git pull

git log --oneline --decorate
git log --oneline --decorate --graph --all

git branch -v
git branch -vv
git branch --no-merged
````


#### poprawka commit
````bash
git commit --amend --no-edit
git push -f
````

#### synchronizacja
````bash
git pull --verbose
# =
git fetch
git merge

# na ostro!
git fetch
git reset --hard
````


#### gałąź śledząca zdalne repo
````bash
git remote add aabbcc https://github.com/aabbcc/abc.git
git fetch aabbcc

git remote -v
git remote -vv
````

#### różne działania na repo zdalnym:
````bash
git push ...
# uaktualnienie wszystkich lokalnych gałęzi śledzących
git fetch --all -v --progress
````

#### lista plików do rozw. konfliktów:
````bash
git diff --name-only --diff-filter=U --relative

git config --global core.eol lf
git config --global core.autocrlf false

git config merge.tool tortoisemerge

git status
````
#### konfig.
````bash
git config --global core.autocrlf false
git config --global core.eol lf
````


#### differences: Newlines

Po przeniesieniu na inny komputer zdarzyło mi się, że wszystkie pliki `UTF-8 CrLf` zostały uznane za zmienione podczas próby wypchnięcia `commit` - zresztą trwającej bardzo długo (związane z inna konfiguracją CrLf Git na tamtym komputerze).  
Po sprawdzeniu co się zmieniło dostałem:
```
TortoiseGitMerge 
----------------
The text is identical, but the files do not match! 
The following differences were found: 
     Newlines
                  [OK]
```
W mojej konfiguracji oba `autocrlf=false`

Jakoś magicznie pomogło wydanie na chwilę polecenia
```bash
git config core.autocrlf true
```
i ponowny `commit` (lub tylko zamiar), po czym można było na powrót wyczyścić (tzn. <nic>) opcję TortoiseGit: Git \ Local \ AutoCrLf: [____]
i kolejne wypychanie było już sensowne. (A global AutoCrLf = false)



* [Pro GIT wyd.2](https://git-scm.com/book/pl/v2) >> git-scm.com/book/pl/v2
* [git - prosty przewodnik](http://rogerdudler.github.io/git-guide/index.pl.html) >>  rogerdudler.github.io
* [Managing remote repositories](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories?utm_source=pocket_mylist) >> docs.github.com
