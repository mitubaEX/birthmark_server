import glob
import os
import csv

csv.field_size_limit(1000000000)
# -*- coding: utf-8 -*-
import codecs
cvfv = codecs.open("barth_cvfv.xml","w",'utf-8')
fmc = codecs.open("barth_fmc.xml","w",'utf-8')
fuc = codecs.open("barth_fuc.xml","w",'utf-8')
kgram = codecs.open("barth_kgram.xml","w",'utf-8')
smc = codecs.open("barth_smc.xml","w",'utf-8')
uc = codecs.open("barth_uc.xml","w",'utf-8')
wsp = codecs.open("barth_wsp.xml","w",'utf-8')
cvfv.write("<add>\n")
cvfv.write("<doc>\n")
fmc.write("<add>\n")
fmc.write("<doc>\n")
fuc.write("<add>\n")
fuc.write("<doc>\n")
kgram.write("<add>\n")
kgram.write("<doc>\n")
smc.write("<add>\n")
smc.write("<doc>\n")
uc.write("<add>\n")
uc.write("<doc>\n")
wsp.write("<add>\n")
wsp.write("<doc>\n")
tmp = glob.glob("*.csv")
count = 0
for i in tmp:
    reader = open(i).read().split('\n')
    if '\0' not in open(i).read():
        if reader is not None:
            for row in reader:
                row = row.split(',',3)
                print row
                if len(row) >= 4:
                    if "cvfv" in row[2]:
                        cvfv.write("</doc>\n")
                        cvfv.write("<doc>\n")
                        cvfv.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        cvfv.write("<field name=\"place\">"+row[1]+"</field>\n")
                        cvfv.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        cvfv.write("<field name=\"data\">"+row[3].decode('utf-8')+"</field>\n")
                    elif "fmc" in row[2]:
                        fmc.write("</doc>\n")
                        fmc.write("<doc>\n")
                        fmc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        fmc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        fmc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        row[3] = row[3].replace("<","   &lt;").replace(">","&gt;")
                        fmc.write("<field name=\"data\">"+row[3].decode('utf-8')+"</field>\n")
                    elif "fuc" in row[2]:
                        fuc.write("</doc>\n")
                        fuc.write("<doc>\n")
                        fuc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        fuc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        fuc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        fuc.write("<field name=\"data\">"+row[3].decode('utf-8')+"</field>\n")
                    elif "kgram" in row[2]:
                        kgram.write("</doc>\n")
                        kgram.write("<doc>\n")
                        kgram.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        kgram.write("<field name=\"place\">"+row[1]+"</field>\n")
                        kgram.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        kgram.write("<field name=\"data\">"+row[3].decode('utf-8')+"</field>\n")
                    elif "smc" in row[2]:
                        smc.write("</doc>\n")
                        smc.write("<doc>\n")
                        smc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        smc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        smc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        row[3] = row[3].replace("<","   &lt;").replace(">","&gt;")
                        smc.write("<field name=\"data\">"+row[3].decode('utf-8')+"</field>\n")
                    elif "uc" in row[2]:
                        uc.write("</doc>\n")
                        uc.write("<doc>\n")
                        uc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        uc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        uc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        uc.write("<field name=\"data\">"+row[3].decode('utf-8')+"</field>\n")
                    elif "wsp" in row[2]:
                        wsp.write("</doc>\n")
                        wsp.write("<doc>\n")
                        wsp.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        wsp.write("<field name=\"place\">"+row[1]+"</field>\n")
                        wsp.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        wsp.write("<field name=\"data\">"+row[3].decode('utf-8')+"</field>\n")


cvfv.write("</doc>\n")
cvfv.write("</add>\n")
fmc.write("</doc>\n")
fmc.write("</add>\n")
fuc.write("</doc>\n")
fuc.write("</add>\n")
kgram.write("</doc>\n")
kgram.write("</add>\n")
smc.write("</doc>\n")
smc.write("</add>\n")
uc.write("</doc>\n")
uc.write("</add>\n")
wsp.write("</doc>\n")
wsp.write("</add>\n")
