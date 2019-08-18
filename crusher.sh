#!/bin/bash
if [ -z "$1" ]; then
  echo "what challenge are you crushing?"
  read TITLE
  echo "Crush It!"
else
  TITLE="$1" 
fi

if [ -z "$2" ]; then
  echo "what is your command for $TITLE"
  read COMMD
else
    COMMD="$2"
fi

if [ $COMMD == "--init" ]; then
  bash bash-pipe/initcpp.sh $TITLE

elif [ $COMMD == "--case" ]; then
  if [ -z "$3" ]; then
    bash bash-pipe/case.sh $TITLE
  else
    bash bash-pipe/case.sh $TITLE $3
  fi
elif [ $COMMD == "--test" ]; then
  if [ -z "$3" ]; then
    bash bash-pipe/testcpp.sh $TITLE
  else
    bash bash-pipe/testcpp.sh $TITLE $3
  fi
elif [ $COMMD == "--submitted" ]; then
  if [ -z "$3" ]; then
    bash bash-pipe/submitted.sh $TITLE
  else
    bash bash-pipe/submitted.sh $TITLE $3
  fi
else
  echo "Invalid Command"
fi

