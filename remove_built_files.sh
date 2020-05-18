#!/bin/bash

git filter-branch --prune-empty --index-filter \
  'git rm -rf --cached --ignore-unmatch *.aux *.synctex.gz *.log *.toc *.bbl *~' \
  --tag-name-filter cat -- --all
