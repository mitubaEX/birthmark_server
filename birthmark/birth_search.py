import glob
import commands
import csv
import pysolr
import solr
import os
import time
import subprocess
from decimal import *

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
    start = time.time()
    con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    print str(quely)
    print len(quely)
    if(len(quely) <= 4000 and len(quely) != 0):
        response = con.select('data:'+str(quely).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)"),rows=1)
        # print len(response.results)
        # print response.numFound
        # response = con.select("strdist("+str(quely).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)")+",text,edit)",rows=response.numFound)
        print "birhtmark"+birthmark
        # hit_count
        if len(response.results) == 0:
            if "cvfv" in birthmark:
                birthmark_count_fault[0] += 1
            elif "fmc" in birthmark:
                birthmark_count_fault[1] += 1
            elif "fuc" in birthmark:
                birthmark_count_fault[2] += 1
            elif "2gram" in birthmark:
                birthmark_count_fault[3] += 1
            elif "3gram" in birthmark:
                birthmark_count_fault[4] += 1
            elif "smc" in birthmark:
                birthmark_count_fault[5] += 1
            elif "uc" in birthmark:
                birthmark_count_fault[6] += 1
            elif "wsp" in birthmark:
                birthmark_count_fault[7] += 1
            none_count += 1
        elif len(response.results) != 0:
            if "cvfv" in birthmark:
                birthmark_count[0] += len(response.results)
                hit_count[0] += 1
            elif "fmc" in birthmark:
                birthmark_count[1] += len(response.results)
                hit_count[1] += 1
            elif "fuc" in birthmark:
                birthmark_count[2] += len(response.results)
                hit_count[2] += 1
            elif "2gram" in birthmark:
                birthmark_count[3] += len(response.results)
                hit_count[3] += 1
            elif "3gram" in birthmark:
                birthmark_count[4] += len(response.results)
                hit_count[4] += 1
            elif "smc" in birthmark:
                birthmark_count[5] += len(response.results)
                hit_count[5] += 1
            elif "uc" in birthmark:
                birthmark_count[6] += len(response.results)
                hit_count[6] += 1
            elif "wsp" in birthmark:
                birthmark_count[7] += len(response.results)
                hit_count[7] += 1
            is_count += len(response.results)
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

        # result_annalysys
        for hit in response.results:
            for filename,place,barthmark in [(filename,place,barthmark) for filename in hit['filename'] for place in hit['place'] for barthmark in hit['barthmark']]:
                birth_class = place.split("!")
                place = birth_class[0].split(":")
                birth_kind = birthmark.split("_")
                print "birth_kind"+birth_kind[1]
                print "score"+str(hit['score'])
                if "CharUtils" not in os.path.basename(birth_class[1]) and "CharUtils" not in os.path.basename(classname):
                    subprocess.call("sh ~/birthmark_server/birthmark/class_list/jar_compare.sh "+birth_kind[1]+" "+os.path.basename(birth_class[1])+" "+os.path.basename(classname)+" "+str(hit['score']),shell=True)
                elif "CharUtils" not in os.path.basename(birth_class[1]):
                    subprocess.call("sh ~/birthmark_server/birthmark/class_list/jar_compare.sh "+birth_kind[1]+" "+os.path.basename(birth_class[1])+" CharUtils.class"+" "+str(hit['score']),shell=True)
                elif "CharUtils" not in os.path.basename(classname):
                    subprocess.call("sh ~/birthmark_server/birthmark/class_list/jar_compare.sh "+birth_kind[1]+" "+"CharUtils.class "+os.path.basename(classname)+" "+str(hit['score']),shell=True)

                # else:
                #     if "cvfv" in birthmark:
                #         birthmark_count[0] -= 1
                #         compare_fault[0] += 1
                #     elif "fmc" in birthmark:
                #         birthmark_count[1] -= 1
                #         compare_fault[1] += 1
                #     elif "fuc" in birthmark:
                #         birthmark_count[2] -= 1
                #         compare_fault[2] += 1
                #     elif "2gram" in birthmark:
                #         birthmark_count[3] -= 1
                #         compare_fault[3] += 1
                #     elif "3gram" in birthmark:
                #         birthmark_count[4] -= 1
                #         compare_fault[4] += 1
                #     elif "smc" in birthmark:
                #         birthmark_count[5] -= 1
                #         compare_fault[5] += 1
                #     elif "uc" in birthmark:
                #         birthmark_count[6] -= 1
                #         compare_fault[6] += 1
                #     elif "wsp" in birthmark:
                #         birthmark_count[7] -= 1
                #         compare_fault[7] += 1
                #     print "compare_fault"
                #     for k in compare_fault:
                #         print k
                #     print
                #     print "birthmark_count"
                #     for n in birthmark_count:
                #         print n
                #     print

                    # compare_fault += 1
                    # print "compare_fault: "+str(compare_fault)
        elapsed_time = time.time() - start
        global all_time
        all_time += elapsed_time
        print "All_time:"+str(all_time)
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


if __name__ == "__main__":
    tmp = glob.glob("*.csv")
    for i in tmp:
         reader = open(i).read().split("\n")
         if '\0' not in open(i).read():
            if reader is not None:
                for row in reader:
                    row = row.split(",",3)
                    if len(row) >= 4:
                        print "hello:"+str(row[3])
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
                        elif "smc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_smc",str(row[3]))
                        elif "uc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_uc",str(row[3]))
                        elif "wsp" in row[2]:
                            solr_serchpy(search_class_[1],"birth_wsp",str(row[3]))



    os.chdir("/Users/mituba/birthmark_server/birthmark/class_list/")
    os.system("python ~/birthmark_server/birthmark/class_list/birth_compare.py")
