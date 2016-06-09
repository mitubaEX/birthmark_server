import glob
import os

tmp = glob.glob("*.jar")
birthmark = ['cvfv', 'fmc', 'fuc', 'kgram', 'smc', 'uc', 'wsp']
for i in range(0,len(tmp)):
    ans = tmp[0]
    del tmp[0]
    print ans
    for j in tmp:
        for l in birthmark:
            os.system("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+l+" compare "+ans+" "+j+" > class_compare/"+ans+"-"+j+"-"+l+".csv")
os.chdir("./class_compare");
os.system("python ~/birthmark_server/jar/class_compare/birthmark_read_correct_search.py")
for i in birthmark:
    os.system("python ./class_compare/class_search.py ./class_compare/class_"+i+".csv > class_"+i+"_out.txt")


