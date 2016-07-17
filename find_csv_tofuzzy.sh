#!/bin/sh

find . -maxdepth 1 -name "*.csv" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    echo "fuzzy-$filename"
    # cd ~/birthmark_server/jar/fuzzy
    python ~/yamamoto15scis/prog/fuzzyhashing.py "$abs/$filename" > "fuzzy_csv/fuzzy-$filename" ;
done
echo "hello"
