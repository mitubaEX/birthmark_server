#!/bin/bash
cwd=`dirname "${0}"`
echo $cwd
cd $cwd
echo `pwd`
array=()
while read -r file
do
    array+=("$file")
done < <(find ../../data/search_birthmark -maxdepth 1 -name "*.csv")
# echo ${array[@]}
python ./fuzzy_search.py ${array[@]}
python ./fuzzy_nob_search.py ${array[@]}

# str_result=()
# while read -r file
# do
#     str_result+=($file)
# done < <(find ../../data/birth_search_result -maxdepth 1 -name "*.csv")
# python birth_compare.py ${str_result[@]}

