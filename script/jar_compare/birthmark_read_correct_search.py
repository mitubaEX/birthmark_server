# 0.75 class group -> output
import os
import glob
import commands
import codecs
import os
from decimal import *
import math
import sys


# tmp = glob.glob("*.csv")
tmp = sys.argv
del tmp[0]
for i in tmp:
    count = 0
    reader = open(i).read().split("\n")
    if "cvfv" in i:
        cvfv = codecs.open("../../data/class_compare/class_cvfv.csv","w",'utf-8')
        birthmark = "cvfv"
    elif "fmc" in i:
        fmc = codecs.open("../../data/class_compare/class_fmc.csv","w",'utf-8')
        birthmark = "fmc"
    elif "fuc" in i:
        fuc = codecs.open("../../data/class_compare/class_fuc.csv","w",'utf-8')
        birthmark = "fuc"
    elif "2gram" in i:
        twogram = codecs.open("../../data/class_compare/class_2gram.csv","w",'utf-8')
        birthmark = "2gram"
    elif "3gram" in i:
        trigram = codecs.open("../../data/class_compare/class_3gram.csv","w",'utf-8')
        birthmark = "3gram"
    elif "4gram" in i:
        _4gram = codecs.open("../../data/class_compare/class_4gram.csv","w",'utf-8')
        birthmark = "4gram"
    elif "5gram" in i:
        _5gram = codecs.open("../../data/class_compare/class_5gram.csv","w",'utf-8')
        birthmark = "5gram"
    elif "6gram" in i:
        _6gram = codecs.open("../../data/class_compare/class_6gram.csv","w",'utf-8')
        birthmark = "6gram"
    elif "smc" in i:
        smc = codecs.open("../../data/class_compare/class_smc.csv","w",'utf-8')
        birthmark = "smc"
    elif "uc" in i:
        uc = codecs.open("../../data/class_compare/class_uc.csv","w",'utf-8')
        birthmark = "uc"
    elif "wsp" in i:
        wsp = codecs.open("../../data/class_compare/class_wsp.csv","w",'utf-8')
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
                        elif birthmark == "4gram":
                            _4gram.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "5gram":
                            _5gram.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "6gram":
                            _6gram.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "smc":
                            smc.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "uc":
                            uc.write(classname+","+class_line[index + 1]+"\n")
                        elif birthmark == "wsp":
                            wsp.write(classname+","+class_line[index + 1]+"\n")



