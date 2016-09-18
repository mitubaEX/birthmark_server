# stigmata_similarity levenshtein birthmark_kind -> output
import os
import glob
import commands
import codecs
import os
from decimal import *
import sys
import math

args = glob.glob("../../data/birth_search_result/*.csv")
for i in args:
    tmpnum = 2
    count = 0
    reader = open(i).read().split("\n")
    for row in reader:
        if " ns" in row:
            continue
        count += 1
        if count == tmpnum:
            tmpnum += 3
            compare = row.split(",")
            score = i.split("-")
            if len(compare) >= 3 and math.isnan(float(compare[2])) is False and compare[2]:
                print str(compare[2]) +","+ score[3]+","+score[2]
            elif len(compare) == 2 and math.isnan(float(compare[1])):
                print str(compare[1]) +","+ score[3]+","+score[2]
                tmpnum -= 1
            elif len(compare) == 2 :
                tmpnum -= 1
                print str(compare[1]) +","+ str(score[3])+","+str(score[2])
            elif len(compare) >= 3 and math.isnan(float(compare[2])):
                print "NaN" +","+ score[3]+","+score[2]
