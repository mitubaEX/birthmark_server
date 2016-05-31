import os
import glob
import commands
import codecs
import os

tmp = glob.glob("*.csv")
collect_count = 0
fault_count = 0
for i in tmp:
    count = 0
    reader = open(i).read().split("\n")
    for row in reader:
        count += 1
        if count == 2:
            compare = row.split(",")
            if len(compare) >= 3:
                if float(compare[2]) >= 0.75:
                    print i+"   "+compare[2]
                    collect_count += 1
                else:
                    fault_count += 1
print "collect:"+str(collect_count)
print "fault:"+str(fault_count)

