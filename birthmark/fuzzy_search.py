import os
import glob
import commands
import codecs
import time
import solr
import pydeep

cvfv_count = 0
fmc_count = 0
fuc_count = 0
kgram_count = 0
smc_count = 0
uc_count = 0
wsp_count = 0

cvfv_fault_count = 0
fmc_fault_count = 0
fuc_fault_count = 0
kgram_fault_count = 0
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
    global kgram_count
    global smc_count
    global uc_count
    global wsp_count

    global cvfv_fault_count
    global fmc_fault_count
    global fuc_fault_count
    global kgram_fault_count
    global smc_fault_count
    global uc_fault_count
    global wsp_fault_count
    start = time.time()
    con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    quely = pydeep.hash_buf(str(quely))
    print
    print "classname: "+classname
    print "quely: "+quely.replace("\)",")").replace("\(","(")
    print
    global correct_count
    global fault_count
    response = con.select("\""+str(quely)+"\"")
    print "data: "+birthmark
    for hit in response.results:
        print hit['filename'],hit['value']
        # print type(hit['value']);
        print pydeep.compare(str(quely),str(hit['value'][0]))
        if pydeep.compare(str(quely),str(hit['value'][0])) >= 75:
            if "cvfv" in str(birthmark):
                cvfv_count += 1
            elif "fmc" in str(birthmark):
                fmc_count += 1
            elif "fuc" in str(birthmark):
                fuc_count += 1
            elif "kgram" in str(birthmark):
                kgram_count += 1
            elif "smc" in str(birthmark):
                smc_count += 1
            elif "uc" in str(birthmark):
                uc_count += 1
            elif "wsp" in str(birthmark):
                wsp_count += 1
            # correct_count += 1
        else:
            if "cvfv" in str(birthmark):
                cvfv_fault_count += 1
            elif "fmc" in str(birthmark):
                fmc_fault_count += 1
            elif "fuc" in str(birthmark):
                fuc_fault_count += 1
            elif "kgram" in str(birthmark):
                kgram_fault_count += 1
            elif "smc" in str(birthmark):
                smc_fault_count += 1
            elif "uc" in str(birthmark):
                uc_fault_count += 1
            elif "wsp" in str(birthmark):
                wsp_fault_count += 1
            # fault_count += 1
    elapsed_time = time.time() - start
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    # print "correct"
    # print correct_count
    # print "fault"
    # print fault_count
    print cvfv_count
    print fmc_count
    print fuc_count
    print kgram_count
    print smc_count
    print uc_count
    print wsp_count
    print
    print cvfv_fault_count
    print fmc_fault_count
    print fuc_fault_count
    print kgram_fault_count
    print smc_fault_count
    print uc_fault_count
    print wsp_fault_count

tmp = glob.glob("*.csv")
print "fuzzy_start"
for i in tmp:
    if "jar" in str(i):
        print i
        reader = open(i).read().split("\n")
        for row in reader:
            row.replace("<","&lt;").replace(">","&gt;").replace("&","&amp;").replace("\"","&quot;").replace("\'","&apos;")
            fuzzy_split = row.split(" ")
            # print
            # print "fuzzy_split"
            # print fuzzy_split
            # print
            # print
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
