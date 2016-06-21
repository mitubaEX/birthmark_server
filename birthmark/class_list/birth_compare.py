import os
import glob
import commands
import codecs
import os
from decimal import *
import math
# cvfv fmc fuc kgram smc uc wsp
middle_count = [0,0,0,0,0,0,0,0]

cvfv_count = 0
fmc_count = 0
fuc_count = 0
_2gram_count = 0
_3gram_count = 0
smc_count = 0
uc_count = 0
wsp_count = 0

cvfv_fault_count = 0
fmc_fault_count = 0
fuc_fault_count = 0
_2gram_fault_count = 0
_3gram_fault_count = 0
smc_fault_count = 0
uc_fault_count = 0
wsp_fault_count = 0

tmp = glob.glob("*.csv")
for i in tmp:
    count = 0
    reader = open(i).read().split("\n")
    for row in reader:
        count += 1
        if count == 2:
            compare = row.split(",")
            if len(compare) >= 3 and math.isnan(float(compare[2])) is False and compare[2]:
                if Decimal(str(compare[2])) >= Decimal('0.75'):
                    if "cvfv" in str(i):
                        cvfv_count += 1
                    elif "fmc" in str(i):
                        fmc_count += 1
                    elif "fuc" in str(i):
                        fuc_count += 1
                    elif "2gram" in str(i):
                        _2gram_count += 1
                    elif "3gram" in str(i):
                        _3gram_count += 1
                    elif "smc" in str(i):
                        smc_count += 1
                    elif "uc" in str(i):
                        uc_count += 1
                    elif "wsp" in str(i):
                        wsp_count += 1
                    print i+"   "+compare[2]
                elif Decimal(str(compare[2])) < Decimal('0.75') and Decimal(str(compare[2])) > Decimal('0.25'):
                    if "cvfv" in str(i):
                        middle_count[0] += 1
                    elif "fmc" in str(i):
                        middle_count[1] += 1
                    elif "fuc" in str(i):
                        middle_count[2] += 1
                    elif "2gram" in str(i):
                        middle_count[3] += 1
                    elif "3gram" in str(i):
                        middle_count[4] += 1
                    elif "smc" in str(i):
                        middle_count[5] += 1
                    elif "uc" in str(i):
                        middle_count[6] += 1
                    elif "wsp" in str(i):
                        middle_count[7] += 1

                elif Decimal(str(compare[2])) <= Decimal('0.25'):
                    if "cvfv" in str(i):
                        cvfv_fault_count += 1
                    elif "fmc" in str(i):
                        fmc_fault_count += 1
                    elif "fuc" in str(i):
                        fuc_fault_count += 1
                    elif "2gram" in str(i):
                        _2gram_fault_count += 1
                    elif "3gram" in str(i):
                        _3gram_fault_count += 1
                    elif "smc" in str(i):
                        smc_fault_count += 1
                    elif "uc" in str(i):
                        uc_fault_count += 1
                    elif "wsp" in str(i):
                        wsp_fault_count += 1

print "birth 0.75"
print
print cvfv_count
print fmc_count
print fuc_count
print _2gram_count
print _3gram_count
print smc_count
print uc_count
print wsp_count
print
print "birth 0.75~0.25"
for j in middle_count:
    print j
print
print "birth 0.25"
print cvfv_fault_count
print fmc_fault_count
print fuc_fault_count
print _2gram_fault_count
print _3gram_fault_count
print smc_fault_count
print uc_fault_count
print wsp_fault_count

