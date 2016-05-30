import os
import glob
import commands
import codecs
import time
import solr
all_time = 0.0

def fuzzy_serchpy(classname, birthmark, quely):
    start = time.time()
    con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    print
    print "quely: "+quely.replace("\)",")").replace("\(","(")
    print
    response = con.select("\""+str(quely)+"\"")
    for hit in response.results:
        print hit['filename'],hit['value']
    elapsed_time = time.time() - start
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


tmp = glob.glob("*.csv")
print "fuzzy"
for i in tmp:
    reader = open(i).read().split("\n")
    for row in reader:
        row.replace("<","&lt;").replace(">","&gt;").replace("&","&amp;").replace("\"","&quot;").replace("\'","&apos;")
        fuzzy_split = row.split(" ")
        print fuzzy_split
        #tmp = glob.glob("*.csv")
        if len(fuzzy_split) >= 2:
            fuzzy_split[1] = fuzzy_split[1].replace('\n',"")
            if "cvfv" in str(i):
                fuzzy_serchpy(fuzzy_split[0], "fuzzy_cvfv", fuzzy_split[1])
            elif "fmc" in str(i):
                fuzzy_serchpy(fuzzy_split[0],"fuzzy_fmc", fuzzy_split[1])
            elif "fuc" in str(i):
                fuzzy_serchpy(fuzzy_split[0],"fuzzy_fuc", fuzzy_split[1])
            elif "kgram" in str(i):
                fuzzy_serchpy(fuzzy_split[0],"fuzzy_kgram", fuzzy_split[1])
            elif "smc" in str(i):
                fuzzy_serchpy(fuzzy_split[0],"fuzzy_smc", fuzzy_split[1])
            elif "uc" in str(i):
                fuzzy_serchpy(fuzzy_split[0],"fuzzy_uc", fuzzy_split[1])
            elif "wsp" in str(i):
                fuzzy_serchpy(fuzzy_split[0],"fuzzy_wsp", fuzzy_split[1])
