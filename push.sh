#!/bin/bash

if [ -z "$1" ]; then
  echo "What are you calling this"
  read TITLE
else
  TITLE="$1"
fi

d=date
f=+'%y%m%d'
da=$($d $f)
echo "$TITLE$da.py"
cat > "$TITLE$da.py"

echo "Git Message"
read MSG

git add .
git commit -a -m "$MSG"
git push origin master

git status




