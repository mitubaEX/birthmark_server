#jar_compare_main
import glob
import os

tmp = glob.glob("*.jar")
birthmark = ['cvfv', 'fmc', 'fuc', '2gram', '3gram', 'smc', 'uc', 'wsp']
for i in range(0,1):
    ans = tmp[0]
    del tmp[0]
    print ans
    #for j in tmp:
    j = tmp[1]
    for l in birthmark:
        os.system("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+l+" compare "+ans+" "+j+" > class_compare/"+ans+"-"+j+"-"+l+".csv")
os.chdir("./class_compare");
os.system("python ~/birthmark_server/jar/class_compare/birthmark_read_correct_search.py")
for i in birthmark:
    os.system("python ~/birthmark_server/jar/class_compare/class_search.py ~/birthmark_server/jar/class_compare/class_"+i+".csv > ~/birthmark_server/jar/class_compare/class_"+i+"_out.txt")


