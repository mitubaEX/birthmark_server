import glob
import os
import sys
import csv

count = 0
file_count = 1

csv.field_size_limit(1000000000)
# -*- coding: utf-8 -*-
import codecs
files = []
cvfv = codecs.open("../../data/birth_xml/birth_cvfv.xml", "w", 'utf-8')
fmc = codecs.open("../../data/birth_xml/birth_fmc.xml", "w", 'utf-8')
fuc = codecs.open("../../data/birth_xml/birth_fuc.xml", "w", 'utf-8')
_2gram = codecs.open("../../data/birth_xml/birth_2gram.xml", "w", 'utf-8')
_3gram = codecs.open("../../data/birth_xml/birth_3gram.xml", "w", 'utf-8')
_4gram = codecs.open("../../data/birth_xml/birth_4gram.xml", "w", 'utf-8')
_5gram = codecs.open("../../data/birth_xml/birth_5gram.xml", "w", 'utf-8')
_6gram = codecs.open("../../data/birth_xml/birth_6gram.xml", "w", 'utf-8')
smc = codecs.open("../../data/birth_xml/birth_smc.xml", "w", 'utf-8')
uc = codecs.open("../../data/birth_xml/birth_uc.xml", "w", 'utf-8')
wsp = codecs.open("../../data/birth_xml/birth_wsp.xml", "w", 'utf-8')

files = [cvfv, fmc, fuc, _2gram, _3gram, _4gram, _5gram, _6gram, smc, uc, wsp]

_2gram_list = []
_3gram_list = []
_4gram_list = []
_5gram_list = []
_6gram_list = []
uc_list = []


def init(filename):
    filename.write("<add>\n")
    filename.write("<doc>\n")


def get_hex_row(row_birthmark):
    if row_birthmark == "data" or row_birthmark == "":
        return row_birthmark
    hex_row = ""
    for j in row_birthmark.split(','):
        for i in j.split(' '):
            try:
                hex_row += hex(int(i)).replace('0x', '')
            except:
                return row_birthmark
        hex_row += ','
    return hex_row


def writer(filename, row):

    if uc == filename:
        filename.write("</doc>\n")
        filename.write("<doc>\n")
        filename.write("<field name=\"filename\">" +
                       unicode(row[0], 'utf-8')+"</field>\n")
        filename.write("<field name=\"place\">" +
                       unicode(row[1], 'utf-8')+"</field>\n")
        filename.write("<field name=\"barthmark\">" +
                       unicode(row[2], 'utf-8')+"</field>\n")
        if len(row[3]) <= 30000:
            filename.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<', '&lt;').replace(">", '&gt;').replace(
                "&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;').replace("&quot;", "")+"</field>\n")
    else:
        encode_row = get_hex_row(row[3].replace("&quot;", ""))
        filename.write("</doc>\n")
        filename.write("<doc>\n")
        filename.write("<field name=\"filename\">"+row[0]+"</field>\n")
        filename.write("<field name=\"place\">"+row[1]+"</field>\n")
        filename.write("<field name=\"barthmark\">"+row[2]+"</field>\n")
        if len(row[3]) <= 30000:
            filename.write("<field name=\"encode_data\">"+encode_row.decode('utf-8').replace('<', '&lt;').replace(">", '&gt;').replace(
                "&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;').replace("&quot;", "").replace("&amp;", "")+"</field>\n")
            filename.write("<field name=\"data\">"+row[3].decode('utf-8').replace('<', '&lt;').replace(">", '&gt;').replace(
                "&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;').replace("&quot;", "").replace("&amp;", "")+"</field>\n")


def finish_writer(filename):
    filename.write("</doc>\n")
    filename.write("</add>\n")


for j in files:
    init(j)


tmp = glob.glob("../../data/birthmark/*"+sys.argv[1]+"*.csv")

all_list_ = []
#tmp = sys.argv
#del tmp[0]
# print tmp
for i in tmp:
    reader = open(i).read().split('\n')
    if '\0' not in open(i).read():
        if reader is not None:
            for row in reader:
                if "2-gram" in str(i):
                    _2gram_list.append(row)
                elif "3-gram" in str(i):
                    _3gram_list.append(row)
                elif "4-gram" in str(i):
                    _4gram_list.append(row)
                elif "5-gram" in str(i):
                    _5gram_list.append(row)
                elif "6-gram" in str(i):
                    _6gram_list.append(row)
                elif "uc" in str(i):
                    uc_list.append(row)


all_ = [_2gram_list, _3gram_list, _4gram_list,
        _5gram_list, _6gram_list, uc_list, ]

list_ = []

for index, i in enumerate(all_):
    count = 0
    file_count = 1
    for l in i:
        row = l.split(',', 3)
        # print row
        if len(row) >= 4:
            if row[0] not in list_:
                list_.append(row[0])
                row[0] = row[0].replace('\n', "").replace('<', '&lt;').replace(
                    ">", '&gt;').replace("&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;')
                row[1] = row[1].replace('\n', "").replace('<', '&lt;').replace(
                    ">", '&gt;').replace("&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;')
                row[2] = row[2].replace('\n', "").replace('<', '&lt;').replace(
                    ">", '&gt;').replace("&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;')
                row[3] = row[3].replace('\n', "").replace('<', '&lt;').replace(
                    ">", '&gt;').replace("&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;')
                if index == 0:
                    if len(row[3].split(',')) <= 15:
                        continue
                    writer(_2gram, row)
                elif index == 1:
                    if len(row[3].split(',')) <= 24:
                        continue
                    writer(_3gram, row)
                elif index == 2:
                    if len(row[3].split(',')) <= 31:
                        continue
                    writer(_4gram, row)
                elif index == 3:
                    if len(row[3].split(',')) <= 37:
                        continue
                    writer(_5gram, row)
                elif index == 4:
                    if len(row[3].split(',')) <= 41:
                        continue
                    writer(_6gram, row)
                elif index == 5:
                    if len(row[3].split(',')) <= 2:
                        continue
                    writer(uc, row)
                count += 1
                if count == 2000:
                    count = 0
                    if index == 0:
                        finish_writer(_2gram)
                        _2gram.close()
                        _2gram = codecs.open(
                            "../../data/birth_xml/birth_2gram"+str(file_count)+".xml", "w", 'utf-8')
                    if index == 1:
                        finish_writer(_3gram)
                        _3gram.close()
                        _3gram = codecs.open(
                            "../../data/birth_xml/birth_3gram"+str(file_count)+".xml", "w", 'utf-8')
                    if index == 2:
                        finish_writer(_4gram)
                        _4gram.close()
                        _4gram = codecs.open(
                            "../../data/birth_xml/birth_4gram"+str(file_count)+".xml", "w", 'utf-8')
                    if index == 3:
                        finish_writer(_5gram)
                        _5gram.close()
                        _5gram = codecs.open(
                            "../../data/birth_xml/birth_5gram"+str(file_count)+".xml", "w", 'utf-8')
                    if index == 4:
                        finish_writer(_6gram)
                        _6gram.close()
                        _6gram = codecs.open(
                            "../../data/birth_xml/birth_6gram"+str(file_count)+".xml", "w", 'utf-8')
                    if index == 5:
                        finish_writer(uc)
                        uc.close()
                        uc = codecs.open(
                            "../../data/birth_xml/birth_uc"+str(file_count)+".xml", "w", 'utf-8')

                    if index == 0:
                        init(_2gram)
                    if index == 1:
                        init(_3gram)
                    if index == 2:
                        init(_4gram)
                    if index == 3:
                        init(_5gram)
                    if index == 4:
                        init(_6gram)
                    if index == 5:
                        init(uc)
                    file_count += 1
    if index == 0:
        finish_writer(_2gram)
    if index == 1:
        finish_writer(_3gram)
    if index == 2:
        finish_writer(_4gram)
    if index == 3:
        finish_writer(_5gram)
    if index == 4:
        finish_writer(_6gram)
    if index == 5:
        finish_writer(uc)


# for j in files:
#     finish_writer(j)
