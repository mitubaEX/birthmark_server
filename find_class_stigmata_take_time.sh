#!/bin/sh
# function setStarttime() {
#         start_time=`date +%s`
# }
#
# function getEndtime() {
#         end_time=`date +%s`
#
#         SS=`expr ${end_time} - ${start_time}`
#
#         HH=`expr ${SS} / 3600`
#         SS=`expr ${SS} % 3600`
#         MM=`expr ${SS} / 60`
#         SS=`expr ${SS} % 60`
#         MS=`expr ${SS} % 1000`
#
#         echo "${HH}:${MM}:${SS}:${MS}"
# }

# H:M:Sで表記
# setStarttime
find ~/birthmark_server/birthmark/class_list -name "*.class" |
while read -r file;
do
    for i in $@;
    do
        echo "helloworld"
        # java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b
    done

done
# getEndtime
