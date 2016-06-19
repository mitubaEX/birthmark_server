import os
import glob
import commands
import codecs
import time
import solr
import pydeep
import editdistance
from decimal import *
fuzzy_count_correct = [0,0,0,0,0,0,0,0]
fuzzy_count_fault = [0,0,0,0,0,0,0,0]
hit_count = [0,0,0,0,0,0,0,0]
middle_count = [0,0,0,0,0,0,0,0]
search_count = 0

cvfv_count = 0
fmc_count = 0
fuc_count = 0
_2gram_count = 0
_3gram_count = 0
smc_count = 0
uc_count = 0
wsp_count = 0

cvfv_fault_count = 0
fmc_fault_count = 0
fuc_fault_count = 0
_2gram_fault_count = 0
_3gram_fault_count = 0
smc_fault_count = 0
uc_fault_count = 0
wsp_fault_count = 0
correct_count = 0
fault_count = 0
all_time = 0.0

def fuzzy_serchpy(classname, birthmark, quely):
    global cvfv_count
    global fmc_count
    global fuc_count
    global _2gram_count
    global _3gram_count
    global smc_count
    global uc_count
    global wsp_count

    global cvfv_fault_count
    global fmc_fault_count
    global fuc_fault_count
    global _2gram_fault_count
    global _3gram_fault_count
    global smc_fault_count
    global uc_fault_count
    global wsp_fault_count

    # start
    start = time.time()
    con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    quely = pydeep.hash_buf(str(quely))
    print
    print "classname: "+classname
    print "quely: "+quely.replace("\)",")").replace("\(","(")
    print
    global correct_count
    global fault_count
    global search_count
    response = con.select(str(quely.replace("[","\[").replace("]","\]").replace(":","\:")))

    if len(response.results) == 0:
        if "cvfv" in str(birthmark):
            fuzzy_count_fault[0] += 1
        elif "fmc" in str(birthmark):
            fuzzy_count_fault[1] += 1
        elif "fuc" in str(birthmark):
            fuzzy_count_fault[2] += 1
        elif "2gram" in str(birthmark):
            fuzzy_count_fault[3] += 1
        elif "3gram" in str(birthmark):
            fuzzy_count_fault[4] += 1
        elif "smc" in str(birthmark):
            fuzzy_count_fault[5] += 1
        elif "uc" in str(birthmark):
            fuzzy_count_fault[6] += 1
        elif "wsp" in str(birthmark):
            fuzzy_count_fault[7] += 1
        fault_count += 1
    else:
        if "cvfv" in str(birthmark):
            fuzzy_count_correct[0] += len(response.results)
            hit_count[0] += 1
        elif "fmc" in str(birthmark):
            fuzzy_count_correct[1] += len(response.results)
            hit_count[1] += 1
        elif "fuc" in str(birthmark):
            fuzzy_count_correct[2] += len(response.results)
            hit_count[2] += 1
        elif "2gram" in str(birthmark):
            fuzzy_count_correct[3] += len(response.results)
            hit_count[3] += 1
        elif "3gram" in str(birthmark):
            fuzzy_count_correct[4] += len(response.results)
            hit_count[4] += 1
        elif "smc" in str(birthmark):
            fuzzy_count_correct[5] += len(response.results)
            hit_count[5] += 1
        elif "uc" in str(birthmark):
            fuzzy_count_correct[6] += len(response.results)
            hit_count[6] += 1
        elif "wsp" in str(birthmark):
            fuzzy_count_correct[7] += len(response.results)
            hit_count[7] += 1
        correct_count += len(response.results)
    print "none_count:"+str(fault_count)
    print "is_count:"+str(correct_count)
    search_count += 1
    print search_count
    print
    print "fuzzy_count_correct"
    for n in fuzzy_count_correct:
        print n
    print
    print "fuzzy_count_fault"
    for m in fuzzy_count_fault:
        print m
    print
    print "hit_count"
    for o in hit_count:
        print o
    print "data: "+birthmark




    # result_annalysys
    for hit in response.results:
        print hit['filename'],hit['value']
        #print pydeep.compare(str(quely),str(hit['value'][0]))
        distance = editdistance.eval(str(quely),str(hit['value']))
        length = max(len(str(quely)), len(str(hit['value'])))
        ans = 1.0 - float(distance) / length
        print "ans:  "+str(ans)
        if Decimal(str(ans)) >= Decimal('0.75'):
            if "cvfv" in str(birthmark):
                cvfv_count += 1
            elif "fmc" in str(birthmark):
                fmc_count += 1
            elif "fuc" in str(birthmark):
                fuc_count += 1
            elif "2gram" in str(birthmark):
                _2gram_count += 1
            elif "3gram" in str(birthmark):
                _3gram_count += 1
            elif "smc" in str(birthmark):
                smc_count += 1
            elif "uc" in str(birthmark):
                uc_count += 1
            elif "wsp" in str(birthmark):
                wsp_count += 1
        elif Decimal(str(ans)) < Decimal('0.75') and Decimal(str(ans)) > Decimal('0.25'):
            if "cvfv" in str(birthmark):
                middle_count[0] += 1
            elif "fmc" in str(birthmark):
                middle_count[1] += 1
            elif "fuc" in str(birthmark):
                middle_count[2] += 1
            elif "2gram" in str(birthmark):
                middle_count[3] += 1
            elif "3gram" in str(birthmark):
                middle_count[4] += 1
            elif "smc" in str(birthmark):
                middle_count[5] += 1
            elif "uc" in str(birthmark):
                middle_count[6] += 1
            elif "wsp" in str(birthmark):
                middle_count[7] += 1
        else:
            if "cvfv" in str(birthmark):
                cvfv_fault_count += 1
            elif "fmc" in str(birthmark):
                fmc_fault_count += 1
            elif "fuc" in str(birthmark):
                fuc_fault_count += 1
            elif "2gram" in str(birthmark):
                _2gram_fault_count += 1
            elif "3gram" in str(birthmark):
                _3gram_fault_count += 1
            elif "smc" in str(birthmark):
                smc_fault_count += 1
            elif "uc" in str(birthmark):
                uc_fault_count += 1
            elif "wsp" in str(birthmark):
                wsp_fault_count += 1
    elapsed_time = time.time() - start
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print "fuzzy 0.75"
    print
    print cvfv_count
    print fmc_count
    print fuc_count
    print _2gram_count
    print _3gram_count
    print smc_count
    print uc_count
    print wsp_count
    print
    print "fuzzy 0.75-0.25"
    for l in middle_count:
        print l
    print
    print "fuzzy 0.25"
    print
    print cvfv_fault_count
    print fmc_fault_count
    print fuc_fault_count
    print _2gram_fault_count
    print _3gram_fault_count
    print smc_fault_count
    print uc_fault_count
    print wsp_fault_count




tmp = glob.glob("*.csv")
print tmp
print "fuzzy_start"
for i in tmp:
    if "jar" in str(i):
        reader = open(i).read().split("\n")
        for row in reader:
            print "row:"+row
            row.replace("<","&lt;").replace(">","&gt;").replace("&","&amp;").replace("\"","&quot;").replace("\'","&apos;")
            fuzzy_split = row.split(",",3)
            if len(fuzzy_split) >= 4:
                class_name = fuzzy_split[1].split("!")
                print "search_class"
                print fuzzy_split[3]
                if "cvfv" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]), "fuzzy_cvfv", fuzzy_split[3])
                elif "fmc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]),"fuzzy_fmc", fuzzy_split[3])
                elif "fuc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]),"fuzzy_fuc", fuzzy_split[3])
                elif "2gram" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]),"fuzzy_2gram", fuzzy_split[3])
                elif "3gram" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]),"fuzzy_3gram", fuzzy_split[3])
                elif "smc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]),"fuzzy_smc", fuzzy_split[3])
                elif "uc" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]),"fuzzy_uc", fuzzy_split[3])
                elif "wsp" in str(i):
                    fuzzy_serchpy(os.path.basename(class_name[1]),"fuzzy_wsp", fuzzy_split[3])
