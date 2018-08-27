#!/bin/bash

if [ -z "$1" ]; then
  echo "Please pass in git message"
  exit
else
  GIT_MESSAGE="$1"
fi

git add .
git commit -a -m "$GIT_MESSAGE"
git push origin master