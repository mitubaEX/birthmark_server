#!/bin/sh
# birthmark to fuzzyhashing

find ../../data/birthmark -maxdepth 1 -name "*.csv" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    echo "fuzzy-$filename"
    # cd ~/birthmark_server/jar/fuzzy
    python ~/yamamoto15scis/prog/fuzzyhashing.py -b "$abs/$filename" > "../../data/fuzzy/fuzzy-$filename" ;
done

find ../../data/birthmark -maxdepth 1 -name "*.csv" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    echo "fuzzy-$filename"
    # cd ~/birthmark_server/jar/fuzzy
    python ~/yamamoto15scis/prog/fuzzyhashing.py "$abs/$filename" > "../../data/fuzzy_nob/fuzzy-$filename" ;
done
echo "hello"
