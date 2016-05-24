import os
import glob
import commands
import codecs
import time
import solr
all_time = 0.0

def fuzzy_curl(birthmark, quely):
    start = time.time()
    quely = quely.replace("[","").replace("]","").replace("/","%2").replace(";=", "%3B%253D").replace("(","\(").replace(")","\)").replace(" ", "")
    quely = quely.replace("&","\&")

    print
    print quely
    print
    search = commands.getoutput("curl --globoff http://localhost:8983/solr/"+birthmark+"/select?q="+str(quely)+"&wt=json&indent=true")
    #print search
    elapsed_time = time.time() - start
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print search


def fuzzy_serchpy(birthmark, quely):
    start = time.time()
    quely = quely.replace("[","").replace("]","").replace("/","%2").replace(";=", "%3B%253D").replace("(","\(").replace(")","\)").replace(" ", "")
    quely = quely.replace("&","\&")
    con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    print
    print "quely: "+quely.replace("\)",")").replace("\(","(")
    print
    response = con.select("\""+str(quely.replace("\)",")").replace("\(","("))+"\"")
    for hit in response.results:
        print hit['filename'],hit['value']
    #print
    #print quely
    #print
    #print search
    elapsed_time = time.time() - start
    #print elapsed_time
    #print type(elapsed_time)
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

cvfv = codecs.open("cvfv.xml","w",'utf-8')
fmc = codecs.open("fmc.xml","w",'utf-8')
fuc = codecs.open("fuc.xml","w",'utf-8')
kgram = codecs.open("kgram.xml","w",'utf-8')
smc = codecs.open("smc.xml","w",'utf-8')
uc = codecs.open("uc.xml","w",'utf-8')
wsp = codecs.open("wsp.xml","w",'utf-8')
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
pwd = commands.getoutput('pwd')
print
print "fuzzy"
print
for i in tmp:
    fuzzy = commands.getoutput("python /Users/nakamurajun/yamamoto15scis/prog/fuzzyhashing.py -b "+ pwd+"/"+i)
    fuzzy_split = fuzzy.split(" ")
    tmp = glob.glob("*.csv")
    pwd = commands.getoutput('pwd')
    if len(fuzzy_split) >= 2:
        fuzzy_split[1] = fuzzy_split[1].replace('\n',"")
        if "cvfv" in str(i):
            cvfv.write("</doc>\n")
            cvfv.write("<doc>\n")
            cvfv.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            cvfv.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            fuzzy_serchpy("cvfv", fuzzy_split[1])
            #search = commands.getoutput("curl http://localhost:8983/solr/cvfv/select?q=*"+fuzzy_split[1]+"*&wt=json&indent=true")
            #print search
        elif "fmc" in str(i):
            fmc.write("</doc>\n")
            fmc.write("<doc>\n")
            fmc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            fmc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            fuzzy_serchpy("fmc", fuzzy_split[1])
            #search = commands.getoutput("curl http://localhost:8983/solr/fmc/select?q=*"+fuzzy_split[1]+"*&wt=json&indent=true")
            #print search
        elif "fuc" in str(i):
            fuc.write("</doc>\n")
            fuc.write("<doc>\n")
            fuc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            fuc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            fuzzy_serchpy("fuc", fuzzy_split[1])
            #search = commands.getoutput("curl http://localhost:8983/solr/fuc/select?q=*"+fuzzy_split[1]+"*&wt=json&indent=true")
            #print search
        elif "kgram" in str(i):
            kgram.write("</doc>\n")
            kgram.write("<doc>\n")
            kgram.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            kgram.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            fuzzy_serchpy("kgram", fuzzy_split[1])
            #search = commands.getoutput("curl http://localhost:8983/solr/kgram/select?q=*"+fuzzy_split[1]+"*&wt=json&indent=true")
            #print search
        elif "smc" in str(i):
            smc.write("</doc>\n")
            smc.write("<doc>\n")
            smc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            smc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            fuzzy_serchpy("smc", fuzzy_split[1])
            #search = commands.getoutput("curl http://localhost:8983/solr/smc/select?q=*"+fuzzy_split[1]+"*&wt=json&indent=true")
            #print search
        elif "uc" in str(i):
            uc.write("</doc>\n")
            uc.write("<doc>\n")
            uc.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            uc.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            fuzzy_serchpy("uc", fuzzy_split[1])
            #search = commands.getoutput("curl http://localhost:8983/solr/uc/select?q=*"+fuzzy_split[1]+"*&wt=json&indent=true")
            #print search
        elif "wsp" in str(i):
            wsp.write("</doc>\n")
            wsp.write("<doc>\n")
            wsp.write("<field name=\"filename\">"+fuzzy_split[0]+"</field>\n")
            wsp.write("<field name=\"value\">"+fuzzy_split[1]+"</field>\n")
            fuzzy_serchpy("wsp", fuzzy_split[1])
            #search = commands.getoutput("curl http://localhost:8983/solr/wsp/select?q=*"+fuzzy_split[1]+"*&wt=json&indent=true")
            #print search
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
