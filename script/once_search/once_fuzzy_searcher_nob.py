import os
import sys
import glob
import commands
import codecs
import time
import solr
import pydeep
import editdistance
from decimal import *
import urllib,json
all_time = 0.0

def fuzzy_serchpy(classname, birthmark, quely):
    start = time.time()
    quely_tmp = quely
    quely = str(quely).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)")
    url_mae = "http://localhost:8983/solr/"+ str(birthmark)+"/select?q=value%3A"
    url_query = urllib.quote_plus(str(quely))
    url_query_tmp = urllib.quote_plus(str(quely_tmp))
    sort_ = urllib.quote_plus("strdist(value,"+str(quely)+",edit) desc")
    fl_ = urllib.quote_plus("*,value,score,lev:strdist(value,"+str(quely)+",edit)")
    url = url_query+"&sort=strdist(value,\""+url_query_tmp+"\",edit)+desc&rows=1&fl=*,value,score,lev:strdist(value,\""+url_query_tmp+"\",edit)&wt=python&indent=true"
    res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2c").replace(":","%3A"))
    response = eval(res.read())
    elapsed_time = time.time() - start
    global all_time
    all_time += elapsed_time
    print "birthmark: "+birthmark
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


# tmp = glob.glob("./birthmark/*.csv")
# print tmp
print "fuzzy_start"
tmp = sys.argv
del tmp[0]
for i in tmp:
    if "jar" in str(i):
        reader = commands.getoutput("python ~/yamamoto15scis/prog/fuzzyhashing.py -b "+i).split("\n");
        # reader = open(i).read().split("\n")
        for row in reader:
            # print "row:"+row
            # row.replace("<","&lt;").replace(">","&gt;").replace("&","&amp;").replace("\"","&quot;").replace("\'","&apos;")
            fuzzy_split = row.split(" ")
            if len(fuzzy_split) >= 2:
                class_name = fuzzy_split[0].split(".")
                # print "search_class"
                # print fuzzy_split[3]
                if "cvfv" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]), "fuzzy_cvfv", fuzzy_split[1])
                elif "fmc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]),"fuzzy_fmc", fuzzy_split[1])
                elif "fuc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]),"fuzzy_fuc", fuzzy_split[1])
                elif "2gram" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]),"fuzzy_2gram", fuzzy_split[1])
                elif "3gram" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]),"fuzzy_3gram", fuzzy_split[1])
                elif "smc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]),"fuzzy_smc", fuzzy_split[1])
                elif "uc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]),"fuzzy_uc", fuzzy_split[1])
                elif "wsp" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[-1]),"fuzzy_wsp", fuzzy_split[1])
                break
