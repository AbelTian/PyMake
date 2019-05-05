# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyPaths 1.1.

Usage:
  pypaths.py list [ <abs-path> ] [ -d <deeps> ] [ --path+ ] [ --pymake=<substitute>:<substitute-value> ... ] [ --ignore=<ignore-keywords> ... ] [ --filter=<keywords> ... ]
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

    args = docopt(__doc__, version='pypaths.py v1.1')
    #print(args)
    #return

    pypathsworkpath = os.getcwd()

    def Depth_Ergodic_new(filepath, allpath_list, depth_value, sign=True, keywords = [], ignore_keywords = []):
        if (sign):
            depth_value -= 1
            if (depth_value >= 0):
                files = os.listdir(filepath)
                for fi in files:
                    fi_d = os.path.join(filepath, fi)
                    if (os.path.isdir(fi_d)):
                        ignore_path = os.path.relpath(fi_d, os.getcwd())
                        if (ignore_path.startswith('.')):
                            continue
                        if(ignore_path.__contains__('.git')):
                            continue
                        if(ignore_path.__contains__('.idea')):
                            continue

                        ignore = 1
                        if (keywords == []):
                            ignore = 0
                        for keyword in keywords:
                            if (fi_d.__contains__(keyword) is True):
                                ignore = 0
                                break
                        if (ignore == 1):
                            continue

                        ignore = 0
                        for keyword in ignore_keywords:
                            if (fi_d.__contains__(keyword) is True):
                                ignore = 1
                                break
                        if (ignore == 1):
                            continue
                        #print(ignore , ignore_keywords)
                        #continue

                        #if (depth_value == 0):
                        allpath_list.append(fi_d)
                        Depth_Ergodic_new(fi_d, allpath_list, depth_value, sign, keywords, ignore_keywords)
                    else:
                        pass
                    #print (os.path.join(filepath,fi_d))
        else:
            files = os.listdir(filepath)
            for fi in files:
                fi_d = os.path.join(filepath, fi)
                if (os.path.isdir(fi_d)):
                    ignore_path = os.path.relpath(fi_d, os.getcwd())
                    if (ignore_path.startswith('.')):
                        continue
                    if (ignore_path.__contains__('.git')):
                        continue
                    if (ignore_path.__contains__('.idea')):
                        continue

                    ignore = 1
                    if (keywords == []):
                        ignore = 0
                    for keyword in keywords:
                        if (fi_d.__contains__(keyword) is True):
                            ignore = 0
                            break
                    if (ignore == 1):
                        continue

                    ignore = 0
                    for keyword in ignore_keywords:
                        if (fi_d.__contains__(keyword) is True):
                            ignore = 1
                            break
                    if (ignore == 1):
                        continue

                    allpath_list.append(fi_d)
                    Depth_Ergodic_new(fi_d, allpath_list, depth_value, sign, keywords, ignore_keywords)
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

            all_keywords = []
            if(args['--filter'] != []):
                key_list = []
                for key in args['--filter']:
                    key_list.extend(str(key).split(' '))
                if(key_list.__contains__('')):
                    key_list.remove('')
                all_keywords = key_list
            #print(all_keywords)
            #return

            all_ignore_keywords = []
            if(args['--ignore'] != []):
                key_list = []
                for key in args['--ignore']:
                    key_list.extend(str(key).split(' '))
                if(key_list.__contains__('')):
                    key_list.remove('')
                all_ignore_keywords = key_list
            #print(all_ignore_keywords)
            #return

            allpath_list = []
            all_path = Depth_Ergodic_new(localabspath, allpath_list, deeps, True, all_keywords, all_ignore_keywords)

            #print(args['--pymake'])
            if(args['--pymake'] != []):
                all_new_path = copy.deepcopy(all_path)

                for item in args['--pymake']:
                    sub0 = str(item).split(':')[0]
                    sub1 = ':'.join(str(item).split(':')[1:])
                    #print(item)
                    #print(sub0,sub1)
                    if(sub0 != ''):
                        sub0 = sub0.replace('\\', '/')
                    if(sub1 != ''):
                        sub1 = sub1.replace('\\', '/')

                    for (i, path0) in enumerate(all_path):
                        str0 = str(all_new_path[i]).replace('\\', '/')
                        if (sub1 != ''):
                            str0 = str(str0).replace(sub1, "${%s}" % sub0)
                        all_new_path[i] = str0

                if(args['--path+'] is True):
                    pos = 1
                    for path0 in all_new_path:
                        print("\"P%d\": \"%s\"," % (pos, path0))
                        pos += 1
                    return

                for path0 in all_new_path:
                    print(path0)
            else:
                for path0 in all_path:
                    print(path0)

        else:
            ''
        break

    return

if __name__ == '__main__':
    main_function()
