# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyPaths 1.0.

Usage:
  pypaths.py list [ <abs-path> ] [ -d <deeps> ]
  pypaths.py (-h | --help)
  pypaths.py --version

Command:
  list              list all directory in a abs path.

Options:
  -h --help     Show this screen.
  --version     Show version.
  -d            restrict deeps.
"""

import os
import re
import sys
import uuid
import shutil
import time
import json
import copy
import types
from pycore.pycore import *

def main_function():

    args = docopt(__doc__, version='pypaths.py v1.0')
    #print(args)

    pypathsworkpath = os.getcwd()

    def level_depath(path0, deep = 0):
        tuple_path = []
        positon = 0
        for path1 in os.listdir(path0):
            if(os.path.isdir(path1)):
                positon += 1
                tuple_path = level_depath(path1, positon)
                return tuple_path

        return tuple_path

    # list
    while (True):
        if (args['list'] == True):
            ''

            localabspath = args['<abs-path>']
            if(args['<abs-path>'] is None):
                localabspath = os.getcwd()

            if(args['<abs-path>'] is '.'):
                localabspath = os.getcwd()

            if(args['<abs-path>'] is '..'):
                localabspath = os.getcwd() + os.path.sep + ".."

            if (not os.path.isdir(localabspath)
                #or os.path.islink(localabspath)
                or not os.path.isabs(localabspath)):
                print("please input a legal abspath.")
                return

            deeps = 0
            if(args['<deeps>'] is not None):
                deeps = int(args['<deeps>'])

            positon = 0
            for (dirpath, dirnames, filenames) in os.walk(localabspath, topdown=True):
                #for name in filenames:
                #    print(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                #    #keylist1.append(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                for name in dirnames:
                    str0 = os.path.relpath(os.path.join(dirpath, name), os.getcwd())
                    if(str0.startswith('.')):
                        continue
                    if(str0.count(os.path.sep) > deeps):
                        continue
                    #print(dirpath, name)
                    print(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))
                    #keylist1.append(os.path.relpath(os.path.join(dirpath, name), os.getcwd()))

                print(positon)
                if(positon > deeps):
                    break
                positon += 1


        else:
            ''
        break

    return

if __name__ == '__main__':
    main_function()
