#!/bin/sh

for i in "$@"
do
    find . -name "*.jar" |
    while read -r file;
    do
        echo ${file}
        abs=$(cd $(dirname ${file});pwd)
        echo $abs
        filename=`basename ${file}`
        echo "$filename-$i.csv"
        java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b $i extract "$abs/$filename" > "birthmark/$filename-$i.csv" ;
        java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b $i extract "$abs/$filename" > "fuzzy/$filename-$i.csv" ;
    done
    echo $i
done
echo "hello"
