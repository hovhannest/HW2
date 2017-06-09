#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import re
import requests
import json
import types
import sys
import matplotlib.pyplot as plt

def task_1():
    # generate links
    urls = []
    for i in range(7):
        urls.append("http://rate.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/0" + str(i+1) + "/11-45")
    #print urls
    for url in urls:
        data = pd.read_html(url)
        data = data[2] # we need this table
        data = data[2:19] # drop columns 0, 1 and row 20
        del data[0]
        del data[2]
        del data[3]
        del data[4]
        data.columns = ["name", "USD_Առք", "USD_Վաճ", "EUR_Առք", "EUR_Վաճ", "RUB_Առք", "RUB_Վաճ", "GBF_Առք", "GBF_Վաճ"]
        print(data)

def task_2():
    url = "https://www.bloomberg.com/quote/SPX:IND"
    response = requests.get(url)
    data = response.text
    output = re.findall('(<\s*div\s+class\s*=\s*"price"\s*>\s*)(\S+)(\s*<\s*/div\s*>)',data)
    tstr = output[0][1]
    tstr = tstr.replace(",", "")
    return float(tstr)

def task_3_dict(input, depth):
    for key, data in input.iteritems():
        # we can print offset depending on depth
        sys.stdout.write(key)
        sys.stdout.write(":")
    
        if(isinstance(data, types.ListType)):
            task_3_list(data, depth + 1)
        elif((isinstance(data, types.DictionaryType))):
            task_3_dict(data, depth + 1)
        else:
            sys.stdout.write(data)
            sys.stdout.write("\n")
    sys.stdout.write("\n")


def task_3_list(input, depth):
    for data in input:
        if(isinstance(data, types.ListType)):
            task_3_list(data, depth + 1)
        elif((isinstance(data, types.DictionaryType))):
            task_3_dict(data, depth + 1)

def task_3(input):
    data = json.loads(input)
    depth = 0
    if(isinstance(data, types.ListType)):
        task_3_list(data, depth + 1)
    elif((isinstance(data, types.DictionaryType))):
        task_3_dict(data, depth + 1)


def task_4():
    data = pd.read_csv("AirPassengers.csv")
    plt.plot(data["Passengers"])
    plt.show()
    print(data)


def task_5():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    data = response.text
    output = re.findall('(<\s*li.*class\s*=\s*"next"\s*>\s*<\s*a\s*href\s*=\s*")(\S*)(")',data)
    tstr = output[0][1]
    return tstr

input = '''[
    {
    "Movie":"Game of Thrones",
    "Actor":"Peter Dinklage",
    "Role":"Tyrion Lannister"
    },
    {
    "Movie":"Vikings",
    "Actor":"Travis Fimmel",
    "Role":"Ragnar Lothbrok"
    },
    {
    "Movie":"The last Kingdom",
    "Actor":{
    "Young Uhtred":"Tom Taylor",
    "Not that young Uhtred":"Alexander Dreymon"
    },
    "Role":"Uhtred of Bebbanburg"
    }
    ]'''

input1 = '''[
    {
    "Movie":{
    "Movie":"Vikings",
    "Actor":"Travis Fimmel",
    "Role":"Ragnar Lothbrok"
    },
    "Actor":"Peter Dinklage",
    "Role":"Tyrion Lannister"
    },
    {
    "Movie":"Vikings",
    "Actor":"Travis Fimmel",
    "Role":"Ragnar Lothbrok"
    },
    {
    "Movie":"The last Kingdom",
    "Actor":{
    "Young Uhtred":"Tom Taylor",
    "Not that young Uhtred":"Alexander Dreymon"
    },
    "Role":"Uhtred of Bebbanburg"
    }
    ]'''
