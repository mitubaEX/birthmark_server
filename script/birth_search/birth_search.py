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

def getnumFound(response,count,url,url_query_tmp,url_mae,url_query):
    if response['response']['numFound'] == 0:
        return 0
    print count
    # print response['response']['docs']
    print len(response['response']['docs'])
    if len(response['response']['docs']) < 100:
        return count
    if Decimal(str(response['response']['docs'][100-1]['lev'])) >= Decimal("0.75"):
        url = url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&start="+str(count)+"&rows=100&fl=lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"
        res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2C").replace(":","%3A"))
        tmp_res = res.read()
        if tmp_res is not None and tmp_res:
            response = eval(tmp_res)
            count = getnumFound(response,count + 100,url,url_query_tmp,url_mae,url_query)
            print "hello"
            print count
            print
            return count
    else:
        for i in reversed(response['response']['docs']):
            if Decimal(i['lev']) >= Decimal("0.75"):
                return count
            count -= 1



def counter(results,birthmark):
    global none_count
    global is_count
    global birthmark_count
    global compare_fault
    if len(results) == 0:
        if "cvfv" in birthmark:
            birthmark_count_fault[0] += 1
        elif "fmc" in birthmark:
            birthmark_count_fault[1] += 1
        elif "fuc" in birthmark:
            birthmark_count_fault[2] += 1
        elif "2gram" in birthmark:
            birthmark_count_fault[3] += 1
        elif "5gram" in birthmark:
            birthmark_count_fault[4] += 1
        elif "smc" in birthmark:
            birthmark_count_fault[5] += 1
        elif "uc" in birthmark:
            birthmark_count_fault[6] += 1
        elif "wsp" in birthmark:
            birthmark_count_fault[7] += 1
        none_count += 1
    elif len(results) != 0:
        if "cvfv" in birthmark:
            birthmark_count[0] += len(results)
            hit_count[0] += 1
        elif "fmc" in birthmark:
            birthmark_count[1] += len(results)
            hit_count[1] += 1
        elif "fuc" in birthmark:
            birthmark_count[2] += len(results)
            hit_count[2] += 1
        elif "2gram" in birthmark:
            birthmark_count[3] += len(results)
            hit_count[3] += 1
        elif "5gram" in birthmark:
            birthmark_count[4] += len(results)
            hit_count[4] += 1
        elif "smc" in birthmark:
            birthmark_count[5] += len(results)
            hit_count[5] += 1
        elif "uc" in birthmark:
            birthmark_count[6] += len(results)
            hit_count[6] += 1
        elif "wsp" in birthmark:
            birthmark_count[7] += len(results)
            hit_count[7] += 1
        is_count += len(results)
    print "is_count"+str(is_count)
    print "none_count:"+str(none_count)
    print
    print "birthmark_count"
    for n in birthmark_count:
        print n
    print
    print "birthmark_count_fault"
    for m in birthmark_count_fault:
        print m
    print
    print "hit_count"
    for o in hit_count:
        print o
    print
    print "compare_fault"
    for k in compare_fault:
        print k
    print
    print "birthmark_count"
    for n in birthmark_count:
        print n
    print

def solr_serchpy(classname,birthmark, quely):
    global all_comparison_time
    global none_count
    global is_count
    global birthmark_count
    global compare_fault
    global kaisuu
    start = time.time()

    #### query set
    quely_tmp = quely
    quely = str(quely).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)").replace("+","\+").replace("-","\-").replace("&&","\&&").replace("||","\||").replace("{","\{").replace("}","\}").replace("^","\^").replace("?","\?")
    print quely
    url_mae = "http://localhost:8983/solr/"+ str(birthmark)+"/select?q=data%3A"
    url_query = urllib.quote_plus(str(quely))
    url_query_tmp = urllib.quote_plus(str(quely_tmp))
    # sort_ = "strdist(data,"+str(quely)+",edit)+desc"
    # fl_ = urllib.quote_plus("*,data,score,lev:strdist(data,"+str(quely)+",edit)")
    url = url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&rows=100&fl=filename,place,barthmark,data,lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"

    numFound_value = 0
    #### search start
    if(len(quely) <= 4000 and len(quely) != 0):
        #### search again
        res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2C").replace(":","%3A"))
        tmp_res = res.read()
        if tmp_res is not None and tmp_res:
            response = eval(tmp_res)
            print response
            numFound_value = getnumFound(response,100,url,url_query_tmp,url_mae,url_query)
            print
            print numFound_value
            if numFound_value is not None:
                url = url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&rows="+str(numFound_value)+"&fl=filename,place,barthmark,data,lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"
                res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2C").replace(":","%3A"))
                tmp_res = res.read()
                if tmp_res is not None and tmp_res:
                    response = eval(tmp_res)
                    results = response['response']['docs']

                    counter(results,birthmark)

                    count = 0
                    # result_annalysys
                    for hit in results:
                        print hit['lev']
                        if Decimal(str(hit['lev'])) < Decimal('0.75'):
                            break
                        # print hit
                        # for filename,place,barthmark in [(filename,place,barthmark) for filename in hit['filename'] for place in hit['place'] for barthmark in hit['barthmark']]:
                        # for filename,place,barthmark in zip(hit['filename'],hit['place'],hit['barthmark']):
                        birth_class = hit['filename'].replace(".","/")
                        place = birth_class[0].split(":")
                        birth_kind = birthmark.split("_")
                        # print "birth_kind"+birth_kind[1]
                        # print "score"+str(hit['score'])
                        print "lev"+ str(hit['lev'])
                        # print "score"+str(hit['score'])
                        # count += 1
                        print count
                        print hit['place']
                        print birth_class
                        print classname
                        # subprocess.call("sh ./jar_compare.sh "+birth_kind[1]+" ~/birthmark_server/data/jar/"+birth_class.replace(".","/").replace("$","\$")+".class ~/birthmark_server/data/jar/"+classname.replace(".","/").replace("$","\$")+".class "+str(hit['lev']),shell=True)
                        if os.path.isfile(birth_class+"-"+classname+"-"+str(hit['lev'])+".csv") == False:
                            t = commands.getoutput("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+birth_kind[1]+" compare ~/birthmark_server/data/jar/"+birth_class.replace(".","/").replace("$","\$")+".class ~/birthmark_server/data/jar/"+classname.replace(".","/").replace("$","\$")+".class 2>&1 | tee ~/birthmark_server/data/birth_search_result/"+birth_class.replace("/",".")+"-"+classname+"-"+str(hit['lev'])+".csv")
                            t = t.split("\n")
                            print t
                            # print str(int(t[0].replace(" ns","")))
                            all_comparison_time += int(t[0].replace(" ns",""))
                            kaisuu += 1
                            print "comparison_time"
                            print all_comparison_time
                            print kaisuu
        elapsed_time = time.time() - start
        global all_time
        all_time += elapsed_time
        print "All_time:"+str(all_time)
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


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
                        if "cvfv" in row[2]:
                            solr_serchpy(row[0],"birth_cvfv",str(row[3]))
                        elif "fmc" in row[2]:
                            solr_serchpy(row[0],"birth_fmc",str(row[3]))
                        elif "fuc" in row[2]:
                            solr_serchpy(row[0],"birth_fuc",str(row[3]))
                        elif "2gram" in str(i):
                            solr_serchpy(row[0],"birth_2gram",str(row[3]))
                        elif "3gram" in str(i):
                            solr_serchpy(row[0],"birth_3gram",str(row[3]))
                        elif "4gram" in str(i):
                            solr_serchpy(row[0],"birth_4gram",str(row[3]))
                        elif "5gram" in str(i):
                            solr_serchpy(row[0],"birth_5gram",str(row[3]))
                        elif "6gram" in str(i):
                            solr_serchpy(row[0],"birth_6gram",str(row[3]))
                        elif "smc" in row[2]:
                            solr_serchpy(row[0],"birth_smc",str(row[3]))
                        elif "uc" in row[2]:
                            solr_serchpy(row[0],"birth_uc",str(row[3]))
                        elif "wsp" in row[2]:
                            solr_serchpy(row[0],"birth_wsp",str(row[3]))



