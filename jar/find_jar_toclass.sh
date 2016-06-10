echo $1
find . -maxdepth 1 -name "*.jar" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    bool=$(jar -tf "$abs/$filename" | grep "$1")
    if [ -n "$bool" ]; then
        jar -xvf "$abs/$filename" "$1"
        break
    fi
done


find . -name "*.class" |
while read -r file;
do
    echo ${file}
    abs=$(cd $(dirname ${file});pwd)
    echo $abs
    filename=`basename ${file}`
    cp "$abs/$filename" ~/birthmark_server/birthmark/class_list/
    rm -rf "$abs/$filename"
done


