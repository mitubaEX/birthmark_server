# birthmark search hit_count -> output
import glob
import commands
import csv
import pysolr
import solr
import os
import time
import subprocess
from decimal import *
import urllib,json
import sys

all_comparison_time = 0
kaisuu = 0
all_time = 0.0
none_count = 0
is_count = 0
compare_fault = [0,0,0,0,0,0,0,0]
birthmark_count = [0,0,0,0,0,0,0,0]
hit_count = [0,0,0,0,0,0,0,0]
birthmark_count_fault = [0,0,0,0,0,0,0,0]
csv.field_size_limit(1000000000)
all_list_ = []

def getnumFound(response,count,url,url_query_tmp,url_mae,url_query):
    global all_list_
    if response['response']['numFound'] == 0:
        return 0
    if len(response['response']['docs']) < 100:
        all_list_.append(response)
        return count
    if Decimal(str(response['response']['docs'][100-1]['lev'])) >= Decimal("0.75"):
        all_list_.append(response)
        url = url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&start="+str(count)+"&rows=100&fl=filename,data,lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"
        res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2C").replace(":","%3A"))
        tmp_res = res.read()
        if tmp_res is not None and tmp_res:
            response = eval(tmp_res)
            count = getnumFound(response,count + 100,url,url_query_tmp,url_mae,url_query)
            return count
    else:
        for i in reversed(response['response']['docs']):
            all_list_.append(response)
            if Decimal(i['lev']) >= Decimal("0.75"):
                return count
            count -= 1




def solr_serchpy(classname,birthmark, quely):
    global all_comparison_time
    global none_count
    global is_count
    global birthmark_count
    global compare_fault
    global kaisuu
    global all_list_

    #### query set
    quely_tmp = quely
    quely = str(quely).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)").replace("+","\+").replace("-","\-").replace("&&","\&&").replace("||","\||").replace("{","\{").replace("}","\}").replace("^","\^").replace("?","\?")
    print quely
    url_mae = "http://localhost:8983/solr/"+ str(birthmark)+"/select?q=data%3A"
    url_query = urllib.quote_plus(str(quely))
    url_query_tmp = urllib.quote_plus(str(quely_tmp))
    url = url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&rows=100&fl=filename,place,barthmark,data,lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"

    numFound_value = 0
    if(len(quely) <= 4000 and len(quely) != 0):
        res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2C").replace(":","%3A"))
        tmp_res = res.read()

        if tmp_res is not None and tmp_res:
            response = eval(tmp_res)


            #### search start
            start = time.time()
            numFound_value = getnumFound(response,100,url,url_query_tmp,url_mae,url_query)
            elapsed_time = time.time() - start
            global all_time
            all_time += elapsed_time
            print "All_time:"+str(all_time)
            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


            if numFound_value is not None:
                for results in all_list_:

                    # result_annalysys
                    for hit in results['response']['docs']:
                        print hit['lev']
                        if Decimal(str(hit['lev'])) < Decimal('0.75'):
                            break
                        birth_class = hit['filename'].replace(".","/")
                        place = birth_class[0].split(":")
                        birth_kind = birthmark.split("_")
                        print "lev"+ str(hit['lev'])
                        print hit['place']
                        print birth_class
                        print classname
                        if os.path.isfile("../../data/birth_search_result/"+birth_class+"-"+classname+"-"+str(hit['lev'])+".csv") == False:
                            t = commands.getoutput("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+birth_kind[1]+" compare ../../data/jar/"+birth_class.replace(".","/").replace("$","\$")+".class ../../data/jar/"+classname.replace(".","/").replace("$","\$")+".class 2>&1 | tee ../../data/birth_search_result/"+birth_class.replace("/",".")+"-"+classname+"-"+str(hit['lev'])+".csv")
                            t = t.split("\n")
                            print t
                            # print str(int(t[0].replace(" ns","")))
                            all_comparison_time += int(t[0].replace(" ns",""))
                            kaisuu += 1
                            print "comparison_time"
                            print all_comparison_time
                            print kaisuu
                all_list_ = []


if __name__ == "__main__":
    args = sys.argv
    del args[0]
    print args
    #tmp = glob.glob("*.csv")
    for i in args:
        reader = open(i).read().split("\n")
        if '\0' not in open(i).read():
            if reader is not None:
                for row in reader:
                    row = row.split(",",3)
                    if len(row) >= 4:
                        # print "hello:"+str(row[3])
                        search_class = row[1].split(":")
                        search_class_ = search_class[2].split("!")
                        birthmarks = i.split("-")
                        birthmarks[-1] = birthmarks[-1].replace(".csv","")
                        solr_serchpy(row[0],"birth_"+birthmarks[-1],str(row[3]))
