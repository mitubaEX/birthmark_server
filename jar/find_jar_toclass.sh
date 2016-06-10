find . -maxdepth 1 -name "*.jar" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    jar -xvf "$abs/$filename"
done


find . -name "*.class" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    cp "$abs/$filename" ~/birthmark_server/birthmark/class_list/
done


