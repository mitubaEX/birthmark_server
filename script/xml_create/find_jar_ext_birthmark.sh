#!/bin/sh
# birthmark_extarct

for i in "$@"
do
    find ../../data/jar/ -name "*.jar" |
    while read -r file;
    do
        echo ${file}
        abs=$(cd $(dirname ${file});pwd)
        echo $abs
        filename=`basename ${file}`
        echo "$filename-$i.csv"
        echo $i
        #echo "java -jar ../../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b $i extract "$abs/$filename" > "../../data/birthmark/$filename-$i.csv" ;"
        java -jar ../../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b $i extract "$abs/$filename" > "../../data/birthmark/$filename-$i.csv" ;
        # java -jar ../../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b $i extract "$abs/$filename" > "../../data/fuzzy/$filename-$i.csv" ;
    done
    #echo $i
done
echo "hello"
# python ~/birthmark_server/jar/barthmark/bathmark_xml_create.py
# sh ~/birthmark_server/jar/fuzzy/find_csv_tofuzzy.sh
# python ~/birthmark_server/jar/fuzzy/fuzzy_csv/fuzzy_xml_create.py
#
