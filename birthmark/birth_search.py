import glob
import commands
import csv
import pysolr
import solr
import os
import time
all_time = 0.0

def solr_serchpy(classname,birthmark, quely):
    start = time.time()
    con = solr.Solr('http://localhost:8983/solr/'+ str(birthmark)+'')
    response = con.select("\""+str(quely)+"\"")
    for hit in response.results:
        for filename,place,barthmark in [(filename,place,barthmark) for filename in hit['filename'] for place in hit['place'] for barthmark in hit['barthmark']]:
            birth_class = place.split("!")
            place = birth_class[0].split(":")
            birth_kind = barthmark.split("_")
            output = commands.getoutput("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+birth_kind[0]+" compare ~/birthmark_server/birthmark/class_list/"+os.path.basename(birth_class[1])+" ~/birthmark_server/birthmark/class_list/"+os.path.basename(classname)+" > ~/birthmark_server/birthmark/class_list/"+birth_class[1].replace("/","_")+"-"+classname.replace("/","_")+"-"+birth_kind[0]+"-compare.csv")
            print
            print output
            print
    elapsed_time = time.time() - start
    global all_time
    all_time += elapsed_time
    print "All_time:"+str(all_time)
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


if __name__ == "__main__":
    tmp = glob.glob("*.csv")
    for i in tmp:
         reader = csv.reader(open(i, 'rU'),delimiter = ',')
         if '\0' not in open(i).read():
            if reader is not None:
                for row in reader:
                    if len(row) >= 4:
                        search_class = row[1].split(":")
                        search_class_ = search_class[2].split("!")
                        print search_class_
                        print
                        print
                        print
                        if "cvfv" in row[2]:
                            solr_serchpy(search_class_[1],"birth_cvfv",str(row[3]))
                        elif "fmc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_fmc",str(row[3]))
                        elif "fuc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_fuc",str(row[3]))
                        elif "kgram" in row[2]:
                            solr_serchpy(search_class_[1],"birth_kgram",str(row[3]))
                        elif "smc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_smc",str(row[3]))
                        elif "uc" in row[2]:
                            solr_serchpy(search_class_[1],"birth_uc",str(row[3]))
                        elif "wsp" in row[2]:
                            solr_serchpy(search_class_[1],"birth_wsp",str(row[3]))



    os.system("python ./class_list/birth_compare.py")
