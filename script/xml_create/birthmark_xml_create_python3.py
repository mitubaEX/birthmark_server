import glob
import csv
import sys

# python3 ./birthmark_xml_create_python3.py <birthmark> <threshold>


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


def calcThreshold(birthmark):
    sum_num = 0
    count = 0
    for i in glob.glob('../../data/birthmark/*' + birthmark + '*.csv'):
        with open(i, 'r') as f:
            import csv
            for row in csv.reader(f):
                if len(row) <= 1:
                    continue
                sum_num += len(row[3:])
                count += 1
    return int(sum_num / count / 3)


threshold = int(calcThreshold(sys.argv[1]))
print(threshold)
output = open("../../data/birth_xml/birth_" + sys.argv[1] + ".xml", "w")
output.write("<add>\n")
output.write("<doc>\n")

for filename in glob.glob("../../data/birthmark/*" + sys.argv[1] + "*.csv"):
    with open(filename, 'r') as f:
        for row in csv.reader(f):
            if len(row[3:]) >= threshold:

                # over threshold

                if sys.argv[1] != "uc":
                    encode_data = get_hex_row(','.join(row[3:]))
                    output.write("</doc>")
                    output.write("<doc>\n")
                    output.write("<field name=\"output\">"+row[0]+"</field>\n")
                    output.write("<field name=\"place\">"+row[1]+"</field>\n")
                    output.write("<field name=\"barthmark\">" +
                                 row[2]+"</field>\n")
                    output.write("<field name=\"encode_data\">"+encode_data.replace('<', '&lt;').replace(">", '&gt;').replace(
                        "&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;').replace("&quot;", "").replace("&amp;", "")+"</field>\n")
                    output.write("<field name=\"data\">"+','.join(row[3:]).replace('<', '&lt;').replace(">", '&gt;').replace(
                        "&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;').replace("&quot;", "").replace("&amp;", "")+"</field>\n")
                else:
                    # encode_data = get_hex_row(','.join(row[3:]))
                    output.write("</doc>")
                    output.write("<doc>\n")
                    output.write("<field name=\"output\">"+row[0]+"</field>\n")
                    output.write("<field name=\"place\">"+row[1]+"</field>\n")
                    output.write("<field name=\"barthmark\">" +
                                 row[2]+"</field>\n")
                    output.write("<field name=\"data\">"+','.join(row[3:]).replace('<', '&lt;').replace(">", '&gt;').replace(
                        "&", '&amp;').replace("\"", '&quot;').replace("\'", '&apos;').replace("&quot;", "").replace("&amp;", "")+"</field>\n")

output.write("</doc>\n")
output.write("</add>\n")
