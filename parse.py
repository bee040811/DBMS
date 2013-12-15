#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    parse csv file to user
"""
import csv
import sys
import json
from pprint import pprint

def main(argv):
    type = sys.argv[1].split(".")
    if(type[1] == "csv"):
        spamreader= csv.reader(open(sys.argv[1], 'rU'), dialect=csv.excel_tab)
        for row in spamreader:
            print row[0].split(',')
    elif(type[1] == "json"):
        file = open(sys.argv[1])
        data = json.load(file)
        for row in data:
            print row,data[row]
if __name__ == "__main__" :
    main(sys.argv)
