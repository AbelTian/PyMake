from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import os,sys
import pickle
import re
import platform

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    import Tkinter as tk
    import tkFont as tkFont
    import ttk as ttk
    import tkMessageBox as tkMessageBox

    # Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    # Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    # import tkFileDialog
    # import tkSimpleDialog

else:  # Python 3.x
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
    import tkinter.messagebox as tkMessageBox
    # import tkinter.filedialog as tkFileDialog
    # import tkinter.simpledialog as tkSimpleDialog    #askstring()

if ( sys.version_info[0] == 2 ):
    import ConfigParser as PyConfigParser
else:
    import configparser as PyConfigParser

class MyConfigParser(PyConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        PyConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

def getuserroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        #root = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
        root = os.environ["USERPROFILE"]
    else:
        root = os.environ["HOME"]
    return root

pipini = ''
if(platform.system() == "Windows"):
    piproot = getuserroot() + os.path.sep + 'pip'
    if(not os.path.exists(piproot)):
        os.mkdir(piproot)
    pipini = piproot + os.path.sep + 'pip.ini'
else:
    piproot = getuserroot() + os.path.sep + '.pip'
    if(not os.path.exists(piproot)):
        os.mkdir(piproot)
    pipini = piproot + os.path.sep + 'pip.ini'

conf = MyConfigParser()
conf.read(pipini)
if( not conf.has_section('global') ):
    conf.add_section('global')
    conf.write(open(pipini, 'w'))
if( not conf.has_section('install') ):
    conf.add_section('install')
    conf.write(open(pipini, 'w'))
if( not conf.has_option('global', 'index-url') ):
    conf.set('global', 'index-url', 'https://pypi.tuna.tsinghua.edu.cn/simple')
    conf.write(open(pipini, 'w'))
if(not conf.has_option('install', 'trusted-host')):
    conf.set('install', 'trusted-host', 'mirrors.aliyun.com')
    conf.write(open(pipini, 'w'))


try:
    import requests
except ModuleNotFoundError:
    os.system("pip3 install requests")
    import requests

try:
    import itchat
except ModuleNotFoundError:
    os.system("pip3 install itchat")
    import itchat

try:
    import jieba
except ModuleNotFoundError:
    os.system("pip3 install jieba")
    import jieba

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    os.system("pip3 install Matplotlib")
    import matplotlib.pyplot as plt

try:
    from wordcloud import WordCloud, ImageColorGenerator
except ModuleNotFoundError:
    os.system("pip3 install wordcloud")
    from wordcloud import WordCloud, ImageColorGenerator

try:
    import numpy as np
except ModuleNotFoundError:
    os.system("pip3 install numpy")
    import numpy as np

try:
    import PIL.Image as Image
except ModuleNotFoundError:
    os.system("pip3 install PIL")
    import PIL.Image as Image

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    os.system("pip3 install bs4")
    from bs4 import BeautifulSoup

try:
    from pymongo import MongoClient
except ModuleNotFoundError:
    os.system("pip3 install pymongo")
    from pymongo import MongoClient
