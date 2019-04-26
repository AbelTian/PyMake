from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import os
import sys
#import pwd
import time
import json
import platform
from collections import OrderedDict
from .colorama import init, Fore, Back, Style


init(autoreset=True)

if ( sys.version_info[0] == 2 ):
    import ConfigParser as PyConfigParser
else:
    import configparser as PyConfigParser

class MyConfigParser(PyConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        PyConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

class MyOrderedDict(OrderedDict):
    def prepend(self, key, value, dict_setitem=dict.__setitem__):
        root = self[0]
        first = root[1]
        if key in self:
            link = self[key]
            link_prev, link_next, _ = link
            link_prev[1] = link_next
            link_next[0] = link_prev
            link[0] = root
            link[1] = first
            root[1] = first[0] = link
        else:
            root[1] = first[0] = self[key] = [root, first, key]
            dict_setitem(self, key, value)

    def insert(self, index, key, value):
        self[key] = value
        for ii, k in enumerate(list(self.keys())):
            if ii >= index and k != key:
                self.move_to_end(k)

def TestPlatform( ):
    print ("----------Operation System--------------------------")
    #  Python Version
    print (platform.python_version())

    #   exe pe type (32bit, WindowsPE)
    print (platform.architecture())

    #   computer network name, acer-PC
    print (platform.node())

    # os name and version, Windows-7-6.1.7601-SP1
    print (platform.platform())

    # cpu info 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel'
    print (platform.processor())

    # Python build time
    print (platform.python_build())

    #  python compiler info
    print (platform.python_compiler())

    if platform.python_branch()=="":
        print (platform.python_implementation())
        print (platform.python_revision())
    print (platform.release())
    print (platform.system())

    #print platform.system_alias()
    #  os version
    print (platform.version())

    #  all of up
    print (platform.uname())

def getplatform( ):
    sysstr = platform.system()
    #print ( sysstr )
    #if(sysstr =="Windows"):
    #    print ("Call Windows tasks")
    #elif(sysstr == "Linux"):
    #    print ("Call Linux tasks")
    #else:
    #    print ("Other System tasks")
    return sysstr

def getuserroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        root = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
    else:
        root = os.environ["HOME"]
    return root

def getconfigroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        root = os.environ["APPDATA"]
    else:
        root = os.environ["HOME"]
    return root

def readJsonData(file):

    datas = ""
    with open(file, 'r') as json_file:
        for line in json_file.readlines():
            datas += line
    data = json.loads(datas, encoding='utf-8', object_pairs_hook=OrderedDict);


    #with open(file, 'r') as json_file:
    #    data = json.load(json_file)

    return data

def writeJsonData(file, data):

    with open(file, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4, sort_keys=False))


    #with open(file, 'w') as json_file:
    #    json.dump(data, json_file, indent=4)


