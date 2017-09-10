from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import os
import sys
import json

if ( sys.version_info[0] == 2 ):
    import ConfigParser as PyConfigParser
else:
    import configparser as PyConfigParser

class MyConfigParser(PyConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        PyConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

def readJsonData(file):

    datas = ""
    with open(file, 'r') as json_file:
        for line in json_file.readlines():
            datas += line
    data = json.loads(datas, encoding='utf-8')
    """
    with open(file, 'r') as json_file:
        data = json.load(json_file)
    """
    return data

def writeJsonData(file, data):

    with open(file, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))

    """
    with open(file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    """