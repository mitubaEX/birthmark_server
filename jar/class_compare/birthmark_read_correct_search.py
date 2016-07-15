import os
import glob
import commands
import codecs
import os
from decimal import *
import math

cvfv = codecs.open("class_cvfv.csv","w",'utf-8')
fmc = codecs.open("class_fmc.csv","w",'utf-8')
fuc = codecs.open("class_fuc.csv","w",'utf-8')
twogram = codecs.open("class_2gram.csv","w",'utf-8')
trigram = codecs.open("class_3gram.csv","w",'utf-8')
smc = codecs.open("class_smc.csv","w",'utf-8')
uc = codecs.open("class_uc.csv","w",'utf-8')
wsp = codecs.open("class_wsp.csv","w",'utf-8')

tmp = glob.glob("*.csv")
for i in tmp:
    count = 0
    reader = open(i).read().split("\n")
    if "cvfv" in i:
        birthmark = "cvfv"
    elif "fmc" in i:
        birthmark = "fmc"
    elif "fuc" in i:
        birthmark = "fuc"
    elif "2gram" in i:
        birthmark = "2gram"
    elif "3gram" in i:
        birthmark = "3gram"
    elif "smc" in i:
        birthmark = "smc"
    elif "uc" in i:
        birthmark = "uc"
    elif "wsp" in i:
        birthmark = "wsp"
    for row in reader:
        if count == 0:
            class_line = row.split(",")
            print class_line
            print
            count += 1
        elif count >= 1:
            compare = row.split(",")
            classname = compare[0]
            del compare[0]
            for index,l in enumerate(compare):
                print "error:"+str(l)
                if l and math.isnan(float(l)) is False:
                    if Decimal(str(l)) >= Decimal('0.75'):
                        print "l: "+str(l)
                        print
                        if birthmark == "cvfv":
                            cvfv.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "fmc":
                            fmc.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "fuc":
                            fuc.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "2gram":
                            twogram.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "3gram":
                            trigram.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "smc":
                            smc.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "uc":
                            uc.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "wsp":
                            wsp.write(classname+","+class_line[index + 1]+"\n")



