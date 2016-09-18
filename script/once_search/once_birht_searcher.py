import glob
import sys
import commands
import csv
import pysolr
import solr
import os
import time
import subprocess
from decimal import *
import urllib,json

all_time = 0.0
none_count = 0
is_count = 0
compare_fault = [0,0,0,0,0,0,0,0]
birthmark_count = [0,0,0,0,0,0,0,0]
hit_count = [0,0,0,0,0,0,0,0]
birthmark_count_fault = [0,0,0,0,0,0,0,0]
csv.field_size_limit(1000000000)

def solr_serchpy(classname,birthmark, quely):
    global none_count
    global is_count
    global birthmark_count
    global compare_fault
    # con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    quely_tmp = quely
    # print quely
    quely = str(quely).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)").replace("+","\+").replace("-","\-").replace("&&","\&&").replace("||","\||").replace("{","\{").replace("}","\}").replace("^","\^").replace("?","\?")
    url_mae = "http://localhost:8983/solr/"+ str(birthmark)+"/select?q=data%3A"
    url_query = urllib.quote_plus(str(quely))
    url_query_tmp = urllib.quote_plus(str(quely_tmp))
    sort_ = urllib.quote_plus("strdist(data,"+str(quely)+",edit) desc")
    fl_ = urllib.quote_plus("*,data,score,lev:strdist(data,"+str(quely)+",edit)")
    url = url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&fl=*,data,score,lev:strdist(data,\""+url_query_tmp+"\",edit)&rows=1&wt=json&indent=true"
    # print str(quely)
    # print len(quely)
    if(len(quely) <= 4000 and len(quely) != 0):
        # print
        # print quely
        # print str(url)

        start = time.time()
        res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2C").replace(":","%3A").replace("\"","%22"))
        elapsed_time = time.time() - start
        global all_time
        all_time += elapsed_time
        print "All_time:"+str(all_time)
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

        # print str(url_mae)+str(url).replace(",","%2C").replace(":","%3A")
        tmp_res = res.read()


if __name__ == "__main__":
    # tmp = glob.glob("./birthmark/*.csv")
    tmp = sys.argv
    del tmp[0]
    for i in tmp:
         reader = open(i).read().split("\n")
         if '\0' not in open(i).read():
            if reader is not None:
                for row in reader:
                    row = row.split(",",3)
                    if len(row) >= 4:
                        # print "hello:"+str(row[3])
                        search_class = row[1].split(":")
                        search_class_ = search_class[2].split("!")
                        if "cvfv" in row[2]:
                            solr_serchpy(search_class_[1],"birth_cvfv",str(row[3]))
                        elif "fmc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_fmc",str(row[3]))
                        elif "fuc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_fuc",str(row[3]))
                        elif "2gram" in str(i):
                            solr_serchpy(search_class_[1],"birth_2gram",str(row[3]))
                        elif "3gram" in str(i):
                            solr_serchpy(search_class_[1],"birth_3gram",str(row[3]))
                        elif "4gram" in str(i):
                            solr_serchpy(search_class_[1],"birth_4gram",str(row[3]))
                        elif "6gram" in str(i):
                            solr_serchpy(search_class_[1],"birth_6gram",str(row[3]))
                        elif "5gram" in str(i):
                            solr_serchpy(search_class_[1],"birth_5gram",str(row[3]))
                        elif "smc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_smc",str(row[3]))
                        elif "uc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_uc",str(row[3]))
                        elif "wsp" in row[2]:
                            solr_serchpy(search_class_[1],"birth_wsp",str(row[3]))


