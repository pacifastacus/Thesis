#!/bin/bash

if [ -z $1 ]
then
  echo "Nem adtál meg fájlnevet!"
  exit 0
fi

newfile=$(basename -- "$1")
newfile="${filename%.*}"

echo 1 $1
echo newfile $newfile
#inkscape -D -z --file=$1 --export-pdf=$1.pdf --export-latex
