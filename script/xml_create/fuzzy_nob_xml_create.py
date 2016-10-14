import os
import glob
import commands
import codecs
import sys

cvfv = codecs.open("../../data/fuzzy_nob_xml/zcvfv.xml","w",'utf-8')
fmc = codecs.open("../../data/fuzzy_nob_xml/zfmc.xml","w",'utf-8')
fuc = codecs.open("../../data/fuzzy_nob_xml/zfuc.xml","w",'utf-8')
smc = codecs.open("../../data/fuzzy_nob_xml/zsmc.xml","w",'utf-8')
uc = codecs.open("../../data/fuzzy_nob_xml/zuc.xml","w",'utf-8')
wsp = codecs.open("../../data/fuzzy_nob_xml/zwsp.xml","w",'utf-8')
_2gram = codecs.open("../../data/fuzzy_nob_xml/z2gram.xml","w",'utf-8')
_3gram = codecs.open("../../data/fuzzy_nob_xml/z3gram.xml","w",'utf-8')
_4gram = codecs.open("../../data/fuzzy_nob_xml/z4gram.xml","w",'utf-8')
_5gram = codecs.open("../../data/fuzzy_nob_xml/z5gram.xml","w",'utf-8')
_6gram = codecs.open("../../data/fuzzy_nob_xml/z6gram.xml","w",'utf-8')
cvfv.write("<add>\n")
cvfv.write("<doc>\n")
fmc.write("<add>\n")
fmc.write("<doc>\n")
fuc.write("<add>\n")
fuc.write("<doc>\n")
smc.write("<add>\n")
smc.write("<doc>\n")
uc.write("<add>\n")
uc.write("<doc>\n")
wsp.write("<add>\n")
wsp.write("<doc>\n")
_2gram.write("<add>\n")
_2gram.write("<doc>\n")
_3gram.write("<add>\n")
_3gram.write("<doc>\n")
_4gram.write("<add>\n")
_4gram.write("<doc>\n")
_5gram.write("<add>\n")
_5gram.write("<doc>\n")
_6gram.write("<add>\n")
_6gram.write("<doc>\n")

tmp = glob.glob("../../data/fuzzy/*.csv")
#tmp = sys.argv
#del tmp[0]
for i in tmp:
    reader = open(i).read().split("\n")
    for row in reader:
        #row.replace("<","&lt;").replace(">","&gt;").replace("&","&amp;").replace("\"","&quot;").replace("\'","&apos;")
        fuzzy_split = row.split(" ")
        print fuzzy_split
        if len(fuzzy_split) >= 2:
            print "before:  "+fuzzy_split[1]
            fuzzy_split[0] = fuzzy_split[0].replace('\n',"").replace('<','&lt;').replace(">",'&gt;').replace("&",'&amp;').replace("\"",'&quot;').replace("\'",'&apos;')
            print "fuzzy_split[1]:  "+fuzzy_split[1]
            if "cvfv" in str(i):
                cvfv.write("</doc>\n")
                cvfv.write("<doc>\n")
                cvfv.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                cvfv.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "fmc" in str(i):
                fmc.write("</doc>\n")
                fmc.write("<doc>\n")
                fmc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                fmc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "fuc" in str(i):
                fuc.write("</doc>\n")
                fuc.write("<doc>\n")
                fuc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                fuc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "2gram" in str(i):
                _2gram.write("</doc>\n")
                _2gram.write("<doc>\n")
                _2gram.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                _2gram.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "3gram" in str(i):
                _3gram.write("</doc>\n")
                _3gram.write("<doc>\n")
                _3gram.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                _3gram.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "4gram" in str(i):
                _4gram.write("</doc>\n")
                _4gram.write("<doc>\n")
                _4gram.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                _4gram.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "5gram" in str(i):
                _5gram.write("</doc>\n")
                _5gram.write("<doc>\n")
                _5gram.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                _5gram.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "6gram" in str(i):
                _6gram.write("</doc>\n")
                _6gram.write("<doc>\n")
                _6gram.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                _6gram.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "smc" in str(i):
                smc.write("</doc>\n")
                smc.write("<doc>\n")
                smc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                smc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "uc" in str(i):
                uc.write("</doc>\n")
                uc.write("<doc>\n")
                uc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                uc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            elif "wsp" in str(i):
                wsp.write("</doc>\n")
                wsp.write("<doc>\n")
                wsp.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
                wsp.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
cvfv.write("</doc>\n")
cvfv.write("</add>\n")
fmc.write("</doc>\n")
fmc.write("</add>\n")
fuc.write("</doc>\n")
fuc.write("</add>\n")
smc.write("</doc>\n")
smc.write("</add>\n")
uc.write("</doc>\n")
uc.write("</add>\n")
wsp.write("</doc>\n")
wsp.write("</add>\n")
_2gram.write("</doc>\n")
_2gram.write("</add>\n")
_3gram.write("</doc>\n")
_3gram.write("</add>\n")
_4gram.write("</doc>\n")
_4gram.write("</add>\n")
_5gram.write("</doc>\n")
_5gram.write("</add>\n")
_6gram.write("</doc>\n")
_6gram.write("</add>\n")
