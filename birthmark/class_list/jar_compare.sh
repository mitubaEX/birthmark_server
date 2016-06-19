

java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "$1" compare ~/birthmark_server/birthmark/class_list/"$2" ~/birthmark_server/birthmark/class_list/"$3" > ~/birthmark_server/birthmark/class_list/"$2"-"$3"-"$1"-compare.csv
