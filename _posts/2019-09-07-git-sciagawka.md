---
layout: post
title:  "git - ściągawka"
date:   2019-09-07 08:08:39 +0100
categories: Programowanie
---

Ściągawka **git** - na razie brudnopis... 

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


# gałąź śledząca zdalne repo

git remote add aabbcc https://github.com/aabbcc/abc.git
git fetch aabbcc

git remote -v
git remote -vv

#lista plików do rozw. konfliktów:

git diff --name-only --diff-filter=U --relative

git config --global core.eol lf
git config --global core.autocrlf false

git config merge.tool tortoisemerge

git status


-------------------

git config --global core.autocrlf false
git config --global core.eol lf



````
* [Pro GIT wyd.2](https://git-scm.com/book/pl/v2) >> git-scm.com/book/pl/v2
* [git - prosty przewodnik](http://rogerdudler.github.io/git-guide/index.pl.html) >>  rogerdudler.github.io
* [Managing remote repositories](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories?utm_source=pocket_mylist) >> docs.github.com
