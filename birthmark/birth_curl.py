import glob
import commands
import csv
import pysolr
import solr
import os
import time
all_time = 0.0

def solr_curl(classname,birthmark, quely):
    start = time.time()
    quely = quely.replace("[","").replace("]","").replace("/","%2").replace(";=", "%3B%253D").replace("(","\(").replace(")","\)").replace(" ", "")
    quely = quely.replace("&","\&")

    #print
    #print quely
    #print
    search = commands.getoutput("curl --globoff http://localhost:8983/solr/"+birthmark+"/select?q="+str(quely)+"&wt=json&indent=true")
    #print search
    elapsed_time = time.time() - start
    #print elapsed_time
    #print type(elapsed_time)
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print search
    #search = commands.getoutput("http http://localhost:8983/solr/"+birthmark+"/select?q="+str(quely)+"&wt=json&indent=true")
    #print search
    #os.system("http http://localhost:8983/solr/"+birthmark+"/select?q="+str(quely)+"&wt=json&indent=true")

def solr_serchpy(classname,birthmark, quely):
    start = time.time()
    #quely = quely.replace("[","").replace("]","").replace("/","%2").replace(";=", "%3B%253D").replace("(","\(").replace(")","\)").replace(" ", "")
    #quely = quely.replace("&","\&")
    con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    #print
    #print "quely: "+quely.replace("\)",")").replace("\(","(")
    #print
    #response = con.select("\""+str(quely.replace("\)",")").replace("\(","("))+"\"")
    response = con.select("\""+str(quely)+"\"")
    for hit in response.results:
#        print hit['filename'],hit['place'],hit['barthmark'],hit['data']
        for filename,place,barthmark in [(filename,place,barthmark) for filename in hit['filename'] for place in hit['place'] for barthmark in hit['barthmark']]:
            birth_class = place.split("!")
            place = birth_class[0].split(":")
            birth_kind = barthmark.split("_")
            os.system("cp "+place[2]+" .")
            os.system("jar xf "+os.path.basename(place[2])+" "+birth_class[1][1:])

            output = commands.getoutput("java -jar ~/barthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+birth_kind[1]+" compare ~/birthmark_server/birthmark"+birth_class+" ~/birthmark_server/birthmark"+classname+" > "+birth_class+"-"+classname+"compare.csv")
            print
            print output
            print
    #print
    #print quely
    #print
    #print search
    elapsed_time = time.time() - start
    #print elapsed_time
    #print type(elapsed_time)
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

def solr_search(birthmark, quely):
    solr = pysolr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    results = solr.search(str(quely))
    print
    print results.hits
    print
    for i in results:
        for j in i:
            print i[j]

if __name__ == "__main__":
    tmp = glob.glob("*.csv")
    for i in tmp:
         reader = csv.reader(open(i, 'rU'),delimiter = ',')
         if '\0' not in open(i).read():
            if reader is not None:
                for row in reader:
                    if len(row) >= 4:
                        if "cvfv" in row[2]:
                            #del row[0:3]
                            #for j in row:
                                #solr_search("barth_cvfv",str(j))
                            search_class = row[1].split("!")
                            solr_serchpy(search_class[1][1:],"birth_cvfv",str(row[3]))
                        elif "fmc" in row[2]:
                            #del row[0:3]
                            #for j in row:
                                #solr_search("barth_fmc",str(j))
                            search_class = row[1].split("!")
                            solr_serchpy(search_class[1][1:],"birth_fmc",str(row[3]))
                        elif "fuc" in row[2]:
                            #del row[0:3]
                            #for j in row:
                                #solr_search("barth_fuc",str(j))
                            search_class = row[1].split("!")
                            solr_serchpy(search_class[1][1:],"birth_fuc",str(row[3]))
                        elif "kgram" in row[2]:
                            #del row[0:3]
                            #for j in row:
                                #solr_search("barth_kgram",str(j))
                            search_class = row[1].split("!")
                            solr_serchpy(search_class[1][1:],"birth_kgram",str(row[3]))
                        elif "smc" in row[2]:
                            #del row[0:3]
                            #for j in row:
                                #solr_search("barth_smc",str(j))
                            search_class = row[1].split("!")
                            solr_serchpy(search_class[1][1:],"birth_smc",str(row[3]))
                        elif "uc" in row[2]:
                            #del row[0:3]
                            #for j in row:
                                #solr_search("barth_uc",str(j))
                            search_class = row[1].split("!")
                            solr_serchpy(search_class[1][1:],"birth_uc",str(row[3]))
                        elif "wsp" in row[2]:
                            #del row[0:3]
                            #for j in row:
                                #solr_search("barth_wsp",str(j))
                            search_class = row[1].split("!")
                            solr_serchpy(search_class[1][1:],"birth_wsp",str(row[3]))




