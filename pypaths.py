# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyPaths 1.0.

Usage:
  pypaths.py list [ <abs-path> ] [ -d <deeps> ] [ --pymake ]
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

    def Depth_Ergodic_new(filepath, allpath_list, depth_value, sign=True):
        if (sign):
            depth_value -= 1
            if (depth_value >= 0):
                files = os.listdir(filepath)
                for fi in files:
                    fi_d = os.path.join(filepath, fi)
                    if (os.path.isdir(fi_d)):
                        if (os.path.relpath(fi_d, os.getcwd()).startswith('.')):
                            continue
                        #if (depth_value == 0):
                        allpath_list.append(fi_d)
                        Depth_Ergodic_new(fi_d, allpath_list, depth_value, sign)
                    else:
                        pass
                    #print (os.path.join(filepath,fi_d))
        else:
            files = os.listdir(filepath)
            for fi in files:
                fi_d = os.path.join(filepath, fi)
                if (os.path.isdir(fi_d)):
                    if (os.path.relpath(fi_d, os.getcwd()).startswith('.')):
                        continue
                    allpath_list.append(fi_d)
                    Depth_Ergodic_new(fi_d, allpath_list, depth_value, sign)
        return allpath_list

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

            os.chdir(localabspath)

            deeps = 1
            if(args['<deeps>'] is not None):
                deeps = int(args['<deeps>'])

            allpath_list = []
            all_path = Depth_Ergodic_new(localabspath, allpath_list, deeps, True)

            if(args['--pymake'] is True):
                pos = 1
                for path0 in all_path:
                    print("\"P%d\": \"%s\"," % (pos, path0))
                    pos += 1
            else:
                for path0 in all_path:
                    print(path0)

        else:
            ''
        break

    return

if __name__ == '__main__':
    main_function()
