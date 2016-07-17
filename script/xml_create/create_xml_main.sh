#!/bin/bash
cwd=`dirname "${0}"`
echo $cwd
cd $cwd
echo `pwd`
# find ../../data/birthmark -name "*.csv" | xargs rm
bash ./find_jar_ext_birthmark.sh 2gram 3gram cvfv fmc fuc smc uc wsp
bash ./find_csv_tofuzzy.sh 2gram 3gram cvfv fmc fuc smc uc wsp

birth_str=()
while read -r file
do
    birth_str+=("$file")
done < <(find ../../data/birthmark -maxdepth 1 -name "*.csv")
# echo ${birth_str[@]}
python ./birthmark_xml_create.py ${birth_str[@]}



fuzzy_str=()
while read -r file
do
    fuzzy_str+=($file)
done < <(find ../../data/fuzzy -maxdepth 1 -name "*.csv")
python ./fuzzy_xml_create.py ${fuzzy_str[@]}



fuzzy_str_nob=()
while read -r file
do
    fuzzy_str_nob+=($file)
done < <(find ../../data/fuzzy_nob -maxdepth 1 -name "*.csv")
python ./fuzzy_nob_xml_create.py ${fuzzy_str_nob[@]}

