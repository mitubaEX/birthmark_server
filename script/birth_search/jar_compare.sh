first=`basename $2`
secound=`basename $3`
java -jar ../../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "$1" compare "$2" "$3" >> ../../data/birth_search_result/"$first"-"$secound"-"$1"-"$4"-compare.csv
