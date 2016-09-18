#class_list_csv -> input correct_count -> output
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
fault_count = 0
correct_fault_count = 0
all_count = 0
all_hit_count = 0
birth_correct = [0,0,0,0,0,0,0,0]
birth_fault = [0,0,0,0,0,0,0,0]
hit_count = [0,0,0,0,0,0,0,0]
left_count = 0
right_count = 0
flags = []
flags_right = []
right_count_flag=[]
left_count_flag=[]
all_list_ = []

birthmark = ['cvfv', 'fmc', 'fuc', '2gram', '3gram', 'smc', 'uc','wsp']
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

def solr_serchclass(birthmark, first_class, secound_class):
    global correct_count
    global fault_count
    global all_count
    global birth_correct
    global birth_fault
    global hit_count
    global all_hit_count
    global correct_fault_count
    global left_count
    global right_count
    global flags
    global flags_right
    global right_count_flag
    global left_count_flag
    global all_list_
    secound_class = secound_class.split(",")
    numFound_value = 0
    if len(str(first_class)) <=5000:
        quely_tmp = first_class
        quely = str(first_class).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)")
        url_mae = "http://localhost:8983/solr/birth_"+ str(birthmark)+"/select?q="
        url_query = urllib.quote_plus(str(quely))
        url_query_tmp = urllib.quote_plus(str(quely_tmp))
        sort_ = urllib.quote_plus("strdist(data,"+str(quely)+",edit) desc")
        fl_ = urllib.quote_plus("*,data,score,lev:strdist(data,"+str(quely)+",edit)")
        url = url_query+"&sort=strdist(data,\""+url_query_tmp+"\",edit)+desc&rows=100&fl=*,data,score,lev:strdist(data,\""+url_query_tmp+"\",edit)&wt=python&indent=true"

        # response = con.select("strdist("+str(first_class).replace("[","\[").replace("]","\]").replace(":","\:").replace("<","\<").replace(">","\>").replace("(","\(").replace(")","\)")+",text,edit)")
        res = urllib.urlopen(str(url_mae)+str(url).replace(",","%2C").replace(":","%3A"))
        # print res.read()
        tmp_res = res.read()
        if tmp_res is not None and tmp_res:
            # print tmp_res
            response = eval(tmp_res)

            start = time.time()
            numFound_value = getnumFound(response,100,url,url_query_tmp,url_mae,url_query)
            elapsed_time = time.time() - start
            global all_time
            all_time += elapsed_time
            all_count += 1
            print all_count
            print "All_time:"+str(all_time)
            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


            if numFound_value is not None:
                for results in all_list_:
                    for hit in results['response']['docs']:
                        if Decimal(str(hit['lev'])) < Decimal("0.75"):
                            break
                        flags.append(str(hit['filename'].replace(".class","")))
                    for n in secound_class:
                        flags_right.append(str(n))
                all_list_ = []


if __name__ == "__main__":
    param = sys.argv
    del param[0]
    for i in param:
        reader = open(i).read().split("\n")
        count = 0
        for row in reader:
            #if count >= 500:
            #    break
            count += 1
            all_hit_count += 1
            print
            print "all_count"+str(count)
            print "all_hit_count"+str(all_hit_count)
            print
            class_line = row.split(",",1)
            if len(class_line) >= 2:
                first_class = class_line[0]
                del class_line[0]
                if class_line[0] != "":
                    secound_class = class_line[-1]
                    #print first_class
                    #print secound_class
                    #print class_line
                    # print "secound"
                    # print secound_class
                    # print
                    if "cvfv" in param[0]:
                        j = "cvfv"
                    elif "fmc" in param[0]:
                        j = "fmc"
                    elif "fuc" in param[0]:
                        j = "fuc"
                    elif "2gram" in param[0]:
                        j = "2gram"
                    elif "3gram" in param[0]:
                        j = "3gram"
                    elif "4gram" in param[0]:
                        j = "4gram"
                    elif "5gram" in param[0]:
                        j = "5gram"
                    elif "6gram" in param[0]:
                        j = "6gram"
                    elif "smc" in param[0]:
                        j = "smc"
                    elif "uc" in param[0]:
                        j = "uc"
                    elif "wsp" in param[0]:
                        j = "wsp"
                    result = commands.getoutput("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+str(j)+" extract ~/birthmark_server/data/jar/"+first_class.replace(".","/")+".class")
                    result_split = result.split(",",3)
                    if len(result_split) >= 4:
                        # print result_split[3]
                        # print secound_class[-1]
                        solr_serchclass(j, str(result_split[3]), secound_class)
                    else:
                        count -= 1
            # print flags
            # print flags_right
    list_ = []
    print len(flags),len(flags_right)
    for l in flags:
        flag = False
        for n in flags_right:
            if l == n:
                flag = True
                break
        if flag:
            correct_count += 1
        else:
            left_count += 1
        # list_.append(str(l))

    for m in flags_right:
        flag = False
        for k in flags:
            if k == m:
                pass
            else:
                flag = True
                break
        if flag and str(m) not in list_:
            right_count += 1

    print correct_count
    print left_count
    print right_count
