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
