import sys
import codecs
import os
import commands
import time
import solr
all_time = 0
correct_count = 0
birthmark = ['cvfv', 'fmc', 'fuc', 'kgram', 'smc', 'uc','wsp']

def solr_serchclass(birthmark, first_class, secound_class):
    global correct_count
    start = time.time()
    con = solr.Solr('http://localhost:8983/solr/birth_'+ str(birthmark)+'')
    response = con.select("\""+str(first_class)+"\"")
    for hit in response.results:
        for filename,place,barthmark in [(filename,place,barthmark) for filename in hit['filename'] for place in hit['place'] for barthmark in hit['barthmark']]:
            birth_class = place.split("!")
            place = birth_class[0].split(":")
            birth_kind = barthmark.split("_")
            os.system("cp "+place[2]+" .")
            os.system("jar xf "+os.path.basename(place[2])+" "+birth_class[1][1:])
            print
            print os.path.basename(birth_class[1]).replace(".class","")
            print first_class
            print secound_class
            print
            print
            # print
            # print
            if secound_class == os.path.basename(birth_class[1]).replace(".class",""):
                correct_count += 1
                print "correct: "+str(correct_count)
                # print

    elapsed_time = time.time() - start
    global all_time
    all_time += elapsed_time
    # print "All_time:"+str(all_time)
    # print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == "__main__":
    param = sys.argv
    reader = open(param[1]).read().split("\n")
    count = 0
    for row in reader:
        count += 1
        print count
        class_line = row.split(",")
        if len(class_line) >= 2:
            first_class = class_line[0].split(".")
            secound_class = class_line[1].split(".")
            # print "first"
            # print first_class
            # print "secound"
            # print secound_class
            # print
            for j in birthmark:
                result = commands.getoutput("java -jar ~/birthmark_server/stigmata/target/stigmata-5.0-SNAPSHOT.jar -b "+str(j)+" extract ~/birthmark_server/birthmark/class_list/"+first_class[-1]+".class")
                result_split = result.split(",",3)
                if len(result_split) >= 4:
                    # print result_split[3]
                    solr_serchclass(j, str(result_split[3]), str(secound_class[-1]))


