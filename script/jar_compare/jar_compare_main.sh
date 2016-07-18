#!/bin/bash
cwd=`dirname "${0}"`
echo $cwd
cd $cwd
echo `pwd`

str_result=()
while read -r file
do
    str_result+=($file)
done < <(find ../../data/class_compare_before -maxdepth 1 -name "*.csv")
python ./birthmark_read_correct_search.py ${str_result[@]}

array=()
while read -r file
do
    array+=("$file")
done < <(find ../../data/class_compare -maxdepth 1 -name "*.csv")
# echo ${array[@]}
python ./class_search.py ${array[@]}


