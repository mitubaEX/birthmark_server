#! /usr/bin/python

import pydeep
import csv
import sys
import argparse
import struct

def calculateBinaryHash(values):
    fp = open('tmp.dat', 'wb')
    for value in values:
        b1 = value % 16
        b2 = (value / 16) % 16
        b3 = (value / 256) % 16
        b4 = (value / 16 * 16 * 16) % 16
        fp.write(struct.pack('BBBB', b4, b3, b2, b1))
    fp.close()

    return pydeep.hash_file('tmp.dat')

def calculateHash(values):
    first = True
    string = ''
    for value in values:
        if not first:
            string = string + ','
        string = string + value
    return pydeep.hash_buf(string)

def performItem(row, dict, options):
    cols = row[3:]
    if options.sort:
        cols.sort()
    cols2 = []

    for column in cols:
        col = column
        if options.binary:
            if column not in dict:
                dict[column] = len(dict);
            col = dict[column]
        cols2.append(col)

    hash = '';
    if options.binary:
        hash = calculateBinaryHash(cols2)
    else:
        hash = calculateHash(cols2)

    return (row[0], hash)

def performFile(file, options):
    fp = open(file, 'r')
    reader = csv.reader(fp)
    csv.field_size_limit(1000000000)
    dict = {}
    count = 0
    for row in reader:
        tuple = performItem(row, dict, options)
        print tuple[0] + ' ' + tuple[1]
        count = count + 1
    fp.close()

def perform(options):
    result = {}
    for file in options.files:
        performFile(file, options)

def write(result):
    for k, v in result.iteritems():
        print k, v

class Options:
    sort = False
    binary = False
    files = []

def buildParser():
    parser = argparse.ArgumentParser(description="fuzzy hashing birthmark result")
    parser.add_argument('-s', '--sort', action='store_true',
                        help='sorting element')
    parser.add_argument('-b', '--binary', action='store_true',
                        help='change element to binary')
    parser.add_argument('FILE', nargs='+', action='append',
                        help='birthmark result as CSV files.')
    return parser

def parseOptions():
    parser = buildParser()
    args = parser.parse_args()
    options = Options()
    if args.sort:
        options.sort = True
    if args.binary:
        options.binary = True
    options.files = args.FILE[0]

    return options

if __name__ == '__main__':
    options = parseOptions()
    perform(options)
