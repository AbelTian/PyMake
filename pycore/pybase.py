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

class DiffDict(object):
    """get diff between two dicts"""

    def __init__(self, current, last):
        self.current = current
        self.last = last
        self.set_current = set(current)
        self.set_last = set(last)
        self.intersect_keys = self.set_current & self.set_last

    def get_added(self):
        """current - mixed = added key"""
        added_keys = self.set_current - self.intersect_keys
        return {key : self.current.get(key) for key in added_keys}

    def get_removed(self):
        """last - mixed = removed key"""
        removed_keys = self.set_last - self.intersect_keys
        return {key : self.current.get(key) for key in removed_keys}

    def get_mixed(self):
        return { key: self.current.get(key) for key in self.intersect_keys }, { key: self.last.get(key) for key in self.intersect_keys }

    def get_changed(self):
        """not equal keys in mixed"""
        changed_keys = set(o for o in self.intersect_keys if self.current.get(o) != self.last.get(o))
        return { key: self.current.get(key) for key in changed_keys }, { key: self.last.get(key) for key in changed_keys }

class DiffList(object):
    """get diff between two lists"""

    def __init__(self, current, last):
        self.current = current
        self.last = last
        self.set_current = set(current)
        self.set_last = set(last)
        self.intersect_keys = self.set_current & self.set_last

    def get_added(self):
        """current - mixed = added key"""
        added_keys = self.set_current - self.intersect_keys
        return [key for key in added_keys]

    def get_removed(self):
        """last - mixed = removed key"""
        removed_keys = self.set_last - self.intersect_keys
        return [key for key in removed_keys]

    def get_mixed(self):
        return [key for key in self.intersect_keys]

    def get_changed(self):
        """not equal keys"""
        return [key for key in self.set_current.difference(self.set_last)], [key for key in self.set_last.difference(self.current)]

#include inherret
def instanceof(variate):
    type1=""
    if (isinstance(variate,int)):
        type1 = "int"
    elif (isinstance(variate,str)):
        type1 = "str"
    elif (isinstance(variate,float)):
        type1 = "float"
    elif (isinstance(variate,list)):
        type1 = "list"
    elif (isinstance(variate,tuple)):
        type1 = "tuple"
    elif (isinstance(variate,dict)):
        type1 = "dict"
    elif (isinstance(variate,set)):
        type1 = "set"
    else:
        type1 = "valid"
    return type1

def typeof(variate):
    type1 = ""
    if (type(variate) == type(1)):
        type1 = "int"
    elif (type(variate) == type("str")):
        type1 = "str"
    elif (type(variate) == type(12.3)):
        type1 = "float"
    elif (type(variate) == type([1])):
        type1 = "list"
    elif (type(variate) == type(())):
        type1 = "tuple"
    elif (type(variate) == type({"key1":"123"})):
        type1 = "dict"
    elif (type(variate) == type({"key1"})):
        type1 = "set"
    else:
        type1 = "valid"
    return type1

#def getType(variate):
#    arr = {"int":"整数","float":"浮点","str":"字符串","list":"列表","tuple":"元组","dict":"字典","set":"集合","valid":"未知类型"}
#    vartype = typeof(variate)
#    if not (vartype in arr):
#        return "未知类型"
#    return arr[vartype]

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
    #if(sysstr =="Darwin"):
    #    print ("Call Darwin tasks")
    #elif(sysstr == "Linux"):
    #    print ("Call Linux tasks")
    #else:
    #    print ("Other System tasks")
    return sysstr

def getplatform_release():
    sysstr = platform.release()
    #7
    #XP
    #17.4.0
    #3.10.84-14528008
    return sysstr

def getcmd_codec():
    if (sys.version_info[0] == 2):
        return None
    else:
        if(getplatform() == "Windows"):
            if(getplatform_release() == "XP"):
                return None
            else:
                return "ansi"
        else:
            return 'utf8'
    return 'utf8'

def myopen(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True): # known special case of open
    if (sys.version_info[0] == 2):
        return open(name=file, mode=mode)
    else:
        if(getplatform() == "Windows"):
            if(getplatform_release() == "XP"):
                encoding = None
        return open(file=file, mode=mode, encoding=encoding)
    return open(file=file, mode=mode, encoding=encoding)

def getuserroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        #root = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
        root = os.environ["USERPROFILE"]
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
    with open(file, 'r', encoding='utf8') as json_file:
        for line in json_file.readlines():
            datas += line
    data = json.loads(datas, encoding='utf-8', object_pairs_hook=OrderedDict);


    #with open(file, 'r') as json_file:
    #    data = json.load(json_file)

    return data

def writeJsonData(file, data):

    with open(file, 'w', encoding='utf8') as json_file:
        json_file.write(json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False))


    #with open(file, 'w') as json_file:
    #    json.dump(data, json_file, indent=4)


