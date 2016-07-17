import sys
import codecs
import os
import commands
import time
import solr
import urllib,json
from decimal import *
all_time = 0
correct_count = 0
all_count = 0
all_hit_count = 0
birth_correct = [0,0,0,0,0,0,0,0]
birth_fault = [0,0,0,0,0,0,0,0]
hit_count = [0,0,0,0,0,0,0,0]
birthmark = ['cvfv', 'fmc', 'fuc', '2gram', '3gram', 'smc', 'uc','wsp']

def solr_serchclass(birthmark, first_class, secound_class):
    global correct_count
    global all_count
    global birth_correct
    global birth_fault
    global hit_count
    global all_hit_count
    start = time.time()
    print
    print first_class
    print
    print secound_class
    print
    con = solr.Solr('http://localhost:8983/solr/birth_'+ str(birthmark)+'')
    if len(str(first_class)) <=5000:
        quely_tmp = first_class
        quely = str(first_class).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)")
        url_mae = "http://localhost:8983/solr/birth_"+ str(birthmark)+"/select?q="
        url_query = urllib.quote_plus(str(quely))
        url_query_tmp = urllib.quote_plus(str(quely_tmp))
        sort_ = urllib.quote_plus("strdist(data,"+str(quely)+",edit) desc")
        fl_ = urllib.quote_plus("*,data,score,lev:strdist(data,"+str(quely)+",edit)")
        url = url_mae+url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&rows=1&fl=*,data,score,lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"

        # response = con.select("strdist("+str(first_class).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)")+",text,edit)")
        res = urllib.urlopen(str(url))
        # print res.read()
        tmp_res = res.read()
        if tmp_res is not None and tmp_res:
            # print tmp_res
            response = eval(tmp_res)
            url = url_mae+url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&"+ str(response['response']['numFound'])+"&fl=*,data,score,lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"
            res = urllib.urlopen(str(url))
            # print res.read()
            tmp_res = res.read()

            response = eval(tmp_res)
            results = response['response']['docs']
            if len(results) == 0:
                if "cvfv" in birthmark:
                    birth_correct[0] += 1
                elif "fmc" in birthmark:
                    birth_fault[1] += 1
                elif "fuc" in birthmark:
                    birth_fault[2] += 1
                elif "2gram" in birthmark:
                    birth_fault[3] += 1
                elif "3gram" in birthmark:
                    birth_fault[4] += 1
                elif "smc" in birthmark:
                    birth_fault[5] += 1
                elif "uc" in birthmark:
                    birth_fault[6] += 1
                elif "wsp" in birthmark:
                    birth_fault[7] += 1
            else:
                if "cvfv" in birthmark:
                    birth_correct[0] += len(results)
                    hit_count[0] += 1
                elif "fmc" in birthmark:
                    birth_correct[1] += len(results)
                    hit_count[1] += 1
                elif "fuc" in birthmark:
                    birth_correct[2] += len(results)
                    hit_count[2] += 1
                elif "2gram" in birthmark:
                    birth_correct[3] += len(results)
                    hit_count[3] += 1
                elif "3gram" in birthmark:
                    birth_correct[4] += len(results)
                    hit_count[4] += 1
                elif "smc" in birthmark:
                    birth_correct[5] += len(results)
                    hit_count[5] += 1
                elif "uc" in birthmark:
                    birth_correct[6] += len(results)
                    hit_count[6] += 1
                elif "wsp" in birthmark:
                    birth_correct[7] += len(results)
                    hit_count[7] += 1
            print
            print "birth_correct"
            for n in birth_correct:
                print n
            print
            print "birth_fault"
            for m in birth_fault:
                print m
            print
            print "hit_count"
            for o in hit_count:
                print o
            print
            # print results
            for hit in results:
                if Decimal(str(hit['lev'])) < Decimal(0.75):
                    break
                # for filename,place,barthmark in [(filename,place,barthmark) for filename in hit['filename'] for place in hit['place'] for barthmark in hit['barthmark']]:
                birth_class = hit['place'].split("!")
                place = birth_class[0].split(":")
                birth_kind = hit['barthmark'].split("_")
                #os.system("cp "+place[2]+" .")
                #os.system("jar xf "+os.path.basename(place[2])+" "+birth_class[1][1:])
                print
                print os.path.basename(birth_class[1]).replace(".class","")
                # print first_class
                print secound_class
                print hit['lev']
                print
                print
                print
                if secound_class == os.path.basename(birth_class[1]).replace(".class",""):
                    correct_count += 1
                    print
                    print "correct_count: "+str(correct_count)
                    print
                    break
    else:
        if "cvfv" in birthmark:
            birth_correct[0] += 1
        elif "fmc" in birthmark:
            birth_fault[1] += 1
        elif "fuc" in birthmark:
            birth_fault[2] += 1
        elif "2gram" in birthmark:
            birth_fault[3] += 1
        elif "3gram" in birthmark:
            birth_fault[4] += 1
        elif "smc" in birthmark:
            birth_fault[5] += 1
        elif "uc" in birthmark:
            birth_fault[6] += 1
        elif "wsp" in birthmark:
            birth_fault[7] += 1
        print
        print "birth_fault"
        for m in birth_fault:
            print m
        print

    # elapsed_time = time.time() - start
    # global all_time
    # all_time += elapsed_time
    # all_count += 1
    # print all_count
    # print "All_time:"+str(all_time)
    # print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == "__main__":
    param = sys.argv
    reader = open(param[1]).read().split("\n")
    count = 0
    for row in reader:
        if count >= 500:
            break
        count += 1
        all_hit_count += 1
        print
        print "all_count"+str(count)
        print "all_hit_count"+str(all_hit_count)
        print
        class_line = row.split(",")
        if len(class_line) >= 2:
            first_class = class_line[0].split(".")
            secound_class = class_line[1].split(".")
            # print "first"
            # print first_class
            # print "secound"
            # print secound_class
            # print
            if "cvfv" in param[1]:
                j = "cvfv"
            elif "fmc" in param[1]:
                j = "fmc"
            elif "fuc" in param[1]:
                j = "fuc"
            elif "2gram" in param[1]:
                j = "2gram"
            elif "3gram" in param[1]:
                j = "3gram"
            elif "smc" in param[1]:
                j = "smc"
            elif "uc" in param[1]:
                j = "uc"
            elif "wsp" in param[1]:
                j = "wsp"
            result = commands.getoutput("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+str(j)+" extract ~/birthmark_server/birthmark/class_list/"+first_class[-1]+".class")
            result_split = result.split(",",3)
            if len(result_split) >= 4:
                # print result_split[3]
                # print secound_class[-1]
                solr_serchclass(j, str(result_split[3]), str(secound_class[-1]))
            else:
                count -= 1

