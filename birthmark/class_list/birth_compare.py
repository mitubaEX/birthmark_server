import os
import glob
import commands
import codecs
import os

cvfv_count = 0
fmc_count = 0
fuc_count = 0
kgram_count = 0
smc_count = 0
uc_count = 0
wsp_count = 0

cvfv_fault_count = 0
fmc_fault_count = 0
fuc_fault_count = 0
kgram_fault_count = 0
smc_fault_count = 0
uc_fault_count = 0
wsp_fault_count = 0

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
                    if "cvfv" in str(i):
                        cvfv_count += 1
                    elif "fmc" in str(i):
                        fmc_count += 1
                    elif "fuc" in str(i):
                        fuc_count += 1
                    elif "kgram" in str(i):
                        kgram_count += 1
                    elif "smc" in str(i):
                        smc_count += 1
                    elif "uc" in str(i):
                        uc_count += 1
                    elif "wsp" in str(i):
                        wsp_count += 1
                    print i+"   "+compare[2]
                    # collect_count += 1
                else:
                    if "cvfv" in str(i):
                        cvfv_fault_count += 1
                    elif "fmc" in str(i):
                        fmc_fault_count += 1
                    elif "fuc" in str(i):
                        fuc_fault_count += 1
                    elif "kgram" in str(i):
                        kgram_fault_count += 1
                    elif "smc" in str(i):
                        smc_fault_count += 1
                    elif "uc" in str(i):
                        uc_fault_count += 1
                    elif "wsp" in str(i):
                        wsp_fault_count += 1
                    # fault_count += 1
# print "collect:"+str(collect_count)
# print "fault:"+str(fault_count)

print cvfv_count
print fmc_count
print fuc_count
print kgram_count
print smc_count
print uc_count
print wsp_count
print
print cvfv_fault_count
print fmc_fault_count
print fuc_fault_count
print kgram_fault_count
print smc_fault_count
print uc_fault_count
print wsp_fault_count
