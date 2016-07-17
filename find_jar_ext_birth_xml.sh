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
        java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b $i extract "$abs/$filename" > "barthmark/$filename-$i.csv" ;
        java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b $i extract "$abs/$filename" > "fuzzy/$filename-$i.csv" ;
    done
    echo $i
done
echo "hello"
python ~/birthmark_server/jar/barthmark/bathmark_xml_create.py
sh ~/birthmark_server/jar/fuzzy/find_csv_tofuzzy.sh
python ~/birthmark_server/jar/fuzzy/fuzzy_csv/fuzzy_xml_create.py

