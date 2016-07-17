#!/bin/bash
cwd=`dirname "${0}"`
echo $cwd
cd $cwd
echo `pwd`
find ../../data/birth_search_result -name "*.csv" | xargs rm
array=()
while read -r file
do
    array+=("$file")
done < <(find ../../data/search_birthmark -maxdepth 1 -name "*.csv")
# echo ${array[@]}
python ./once_birht_searcher.py ${array[@]}
python ./once_fuzzy_searcher.py ${arrary[@]}
python ./once_fuzzy_searcher_nob.py ${arrary[@]}

# str_result=()
# while read -r file
# do
#     str_result+=($file)
# done < <(find ../../data/birth_search_result -maxdepth 1 -name "*.csv")
# python birth_compare.py ${str_result[@]}
#
