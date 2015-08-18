#!/bin/bash

git filter-branch --prune-empty --index-filter \
  'git rm -rf --cached --ignore-unmatch *.pdf *.aux *.synctex.gz *.log *.toc *.bbl *~' \
  --tag-name-filter cat -- --all
