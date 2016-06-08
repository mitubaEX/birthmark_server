import os
import glob
import commands
import codecs
import os

cvfv = codecs.open("class_cvfv.csv","w",'utf-8')
fmc = codecs.open("class_fmc.csv","w",'utf-8')
fuc = codecs.open("class_fuc.csv","w",'utf-8')
kgram = codecs.open("class_kgram.csv","w",'utf-8')
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
    elif "kgram" in i:
        birthmark = "kgram"
    elif "smc" in i:
        birthmark = "smc"
    elif "uc" in i:
        birthmark = "uc"
    elif "wsp" in i:
        birthmark = "wsp"
    for row in reader:
        if count == 0:
            class_line = row.split(",")
            count += 1
        elif count >= 1:
            compare = row.split(",")
            classname = compare[0]
            del compare[0]
            for index,l in enumerate(compare):
                if l >= 0.75 and classname != class_line[index + 1]:
                    if birthmark == "cvfv":
                        cvfv.write(classname+","+class_line[index + 1]+"\n")
                    elif birthmark == "fmc":
                        fmc.write(classname+","+class_line[index + 1]+"\n")
                    elif birthmark == "fuc":
                        fuc.write(classname+","+class_line[index + 1]+"\n")
                    elif birthmark == "kgram":
                        kgram.write(classname+","+class_line[index + 1]+"\n")
                    elif birthmark == "smc":
                        smc.write(classname+","+class_line[index + 1]+"\n")
                    elif birthmark == "uc":
                        uc.write(classname+","+class_line[index + 1]+"\n")
                    elif birthmark == "wsp":
                        wsp.write(classname+","+class_line[index + 1]+"\n")



