#!/bin/sh

find . -name "*.csv" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    echo "fuzzy-$filename"
    python ~/yamamoto15scis/prog/fuzzyhashing.py -b "$abs/$filename" > "fuzzy_csv/fuzzy-$filename" ;
done
echo "hello"
