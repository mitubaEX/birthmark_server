import sys
import glob
import commands
import time

param = sys.argv

tmp = glob.glob("../../data/jar/*.jar")
all_time = 0
start = time.time()
for i in tmp:
    commands.getoutput("java -jar ../../stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+ param[1] +" compare "+param[2]+" "+i)
    # print t
    elapsed_time = time.time() - start
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
