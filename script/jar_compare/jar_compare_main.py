#!/bin/bash
cwd=`dirname "${0}"`
echo $cwd
cd $cwd
echo `pwd`
array=()
while read -r file
do
    array+=("$file")
done < <(find ../../data/class_compare -maxdepth 1 -name "*.csv")
# echo ${array[@]}
python ./class_search.py ${array[@]}

# str_result=()
# while read -r file
# do
#     str_result+=($file)
# done < <(find ../../data/birth_search_result -maxdepth 1 -name "*.csv")
# python birth_compare.py ${str_result[@]}
#
