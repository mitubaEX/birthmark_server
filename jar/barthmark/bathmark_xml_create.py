import glob
import os
import csv

csv.field_size_limit(1000000000)
# -*- coding: utf-8 -*-
import codecs
files = []
cvfv = codecs.open("birth_cvfv.xml","w",'utf-8')
fmc = codecs.open("birth_fmc.xml","w",'utf-8')
fuc = codecs.open("birth_fuc.xml","w",'utf-8')
_2gram = codecs.open("birth_2gram.xml","w",'utf-8')
_3gram = codecs.open("birth_3gram.xml","w",'utf-8')
smc = codecs.open("birth_smc.xml","w",'utf-8')
uc = codecs.open("birth_uc.xml","w",'utf-8')
wsp = codecs.open("birth_wsp.xml","w",'utf-8')

files = [cvfv, fmc, fuc, _2gram, _3gram, smc, uc, wsp]

def init(filename):
    filename.write("<add>\n")
    filename.write("<doc>\n")

def writer(filename, row):
    filename.write("</doc>\n")
    filename.write("<doc>\n")
    filename.write("<field name=\"filename\">"+row[0]+"</field>\n")
    filename.write("<field name=\"place\">"+row[1]+"</field>\n")
    filename.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
    if len(row[3]) <= 30000:
        filename.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")

def finish_writer(filename):
    filename.write("</doc>\n")
    filename.write("</add>\n")


for j in files:
    init(j)
# fmc.write("<add>\n")
# fmc.write("<doc>\n")
# fuc.write("<add>\n")
# fuc.write("<doc>\n")
# kgram.write("<add>\n")
# kgram.write("<doc>\n")
# smc.write("<add>\n")
# smc.write("<doc>\n")
# uc.write("<add>\n")
# uc.write("<doc>\n")
# wsp.write("<add>\n")
# wsp.write("<doc>\n")


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
                    row[0] = row[0].replace('\n',"").replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')
                    row[1] = row[1].replace('\n',"").replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')
                    row[2] = row[2].replace('\n',"").replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')
                    row[3] = row[3].replace('\n',"").replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')
                    if "cvfv" in row[2]:
                        writer(cvfv, row)
                        # cvfv.write("</doc>\n")
                        # cvfv.write("<doc>\n")
                        # cvfv.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        # cvfv.write("<field name=\"place\">"+row[1]+"</field>\n")
                        # cvfv.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        # if len(row[3]) <= 30000:
                        #     cvfv.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")
                    elif "fmc" in row[2]:
                        writer(fmc, row)
                        # fmc.write("</doc>\n")
                        # fmc.write("<doc>\n")
                        # fmc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        # fmc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        # fmc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        # row[3] = row[3].replace("<","   &lt;").replace(">","&gt;")
                        # if len(row[3]) <= 30000:
                        #     fmc.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")
                    elif "fuc" in row[2]:
                        writer(fuc, row)
                        # fuc.write("</doc>\n")
                        # fuc.write("<doc>\n")
                        # fuc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        # fuc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        # fuc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        # if len(row[3]) <= 30000:
                        #     fuc.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")
                    elif "2gram" in str(i):
                        writer(_2gram, row)
                        # kgram.write("</doc>\n")
                        # kgram.write("<doc>\n")
                        # kgram.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        # kgram.write("<field name=\"place\">"+row[1]+"</field>\n")
                        # kgram.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        # if len(row[3]) <= 30000:
                        #     kgram.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")
                    elif "3gram" in str(i):
                        writer(_3gram, row)
                    elif "smc" in row[2]:
                        writer(smc, row)
                        # smc.write("</doc>\n")
                        # smc.write("<doc>\n")
                        # smc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        # smc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        # smc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        # row[3] = row[3].replace("<","   &lt;").replace(">","&gt;")
                        # if len(row[3]) <= 30000:
                        #     smc.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")
                    elif "uc" in row[2]:
                        writer(uc, row)
                        # uc.write("</doc>\n")
                        # uc.write("<doc>\n")
                        # uc.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        # uc.write("<field name=\"place\">"+row[1]+"</field>\n")
                        # uc.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        # if len(row[3]) <= 30000:
                        #     uc.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")
                    elif "wsp" in row[2]:
                        writer(wsp, row)
                        # wsp.write("</doc>\n")
                        # wsp.write("<doc>\n")
                        # wsp.write("<field name=\"filename\">"+row[0]+"</field>\n")
                        # wsp.write("<field name=\"place\">"+row[1]+"</field>\n")
                        # wsp.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
                        # if len(row[3]) <= 30000:
                        #     wsp.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')+"</field>\n")


for j in files:
    finish_writer(j)
