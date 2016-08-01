import sys
import glob
import commands
import time

param = sys.argv

tmp = glob.glob("../../data/jar/*.jar")
all_time = 0
start = time.time()
for i in tmp:
    t = commands.getoutput("java -Xmx4g -jar ../../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+ param[1] +" compare "+param[2]+" "+i)
    t = t.split("\n")
    elapsed_time = int(t[0].replace(" ns",""))
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[ns]")
