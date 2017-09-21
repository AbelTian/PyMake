"""PyMake 1.0.

Usage:
  pymake.py source [ --delete | --add | --switch ] [ <config-file-name> ]
  pymake.py source [ --list | --restore ]
  pymake.py list-path [ --keys | --values ]
  pymake.py config ( --toolchain | --genmake | --make | --build ) <path>
  pymake.py other-bin ( --add | --del | --mod ) <name> [ <path> ]
  pymake.py (generate|build|install)
  pymake.py genmake <genmake-command>
  pymake.py (-h | --help)
  pymake.py --version

Command:
  source        switch to another config file
  genmake       execute genmake command after
  generate
  build
  install       pymake command
  config        config toolchain path
  list-path
  other-bin     modify the other bin path to env

Options:
  -h --help     Show this screen.
  --version     Show version.
  --add
  --del --delete
  --mod         add or delete or modify a config or path
  --switch      switch to another source
  --keys
  --values
  --toolchain   set toolchain path in source config file
  --build       set build directory in souce config file
  --genmake     set genmake directory in current souce
  --make        set make directory in current source config file
  --list        list haved source files
  --restore     reset to pymake.json source config file
"""

# -*- coding: utf-8 -*-

import os
import sys
import shutil
import time
import json

from pycore.pycore import *
from pycore.docopt import docopt

def main_function():

    d = {
        "add-custom-bin-path-to-env": {
            "qt5.9-win32": "C:/Users/Administrator/Qt/5.9.1/mingw53_32/bin"
        },
        "add-to-env": {
            'PYMAKE_TOOLCHAIN_PATH': "C:/Users/Administrator/Qt/Tools/mingw530_32/bin",
            'PYMAKE_MAKE_PATH': "C:/Users/Administrator/Qt/Tools/mingw530_32/bin",
            'PYMAKE_GENMAKE_PATH': "Z:/abel/Develop/b0-toolskits/compliers/cmake3.9.1_64/bin"
        },
        "source-to-build": {
            "PYMAKE_BUILD_PATH": "Z:/abel/Develop/c0-buildstation/mingw32-qqt",
            "PYMAKE_GENMAKE_COMMAND": "cmake -G\"MinGW Makefiles\" ../",
            "PYMAKE_MAKE_COMMAND": "mingw32-make",
            "PYMAKE_INSTALL_COMMAND": "mingw32-make install"
        }
    }
    if (not os.path.exists('pymake.json')):
        writeJsonData('pymake.json', d)

    """
    [pymake]
    config = pymake.json
    """
    file = 'pymake.json'
    conf = MyConfigParser()
    conf.read('pymake.ini')
    if(conf.has_section('pymake') ):
        if(conf.has_option('pymake', 'config')):
            if(conf.get('pymake', 'config')):
                file = conf.get('pymake', 'config')
                print("use source config: %s" % file)
            else:
                conf.set('pymake', 'config', 'pymake.json')
                conf.write(open('pymake.ini', 'w'))
                print('initial pymake.ini')
        else:
            conf.set('pymake', 'config', 'pymake.json')
            conf.write(open('pymake.ini', 'w'))
            print('initial pymake.ini')
    else:
        conf.add_section('pymake')
        conf.set('pymake', 'config', 'pymake.json')
        conf.write(open('pymake.ini', 'w'))
        print ( 'initial pymake.ini')

    args = docopt(__doc__, version='pymake.py 1.0')
    #print(args)
    config = readJsonData(file)
    #print(config)

    exceptFile = ( 'pymake.ini', 'pymake.py', '.gitignore', '.git', 'pycore', 'README.md', '.idea')
    while (True):
        if(args['source'] is True):
            if(args['--delete'] is True):
                if (args['<config-file-name>'] is not None and args['<config-file-name>'] == 'pymake.json'):
                    print('You can\'t remove pymake\'s file...')
                elif (args['<config-file-name>'] is not None and not exceptFile.__contains__(args['<config-file-name>']) ):
                    os.remove(args['<config-file-name>'])
                    conf.set('pymake', 'config', 'pymake.json')
                    conf.write(open('pymake.ini', 'w'))
                else:
                    print ( 'You can\'t remove pymake\'s file...')
            elif(args['--add'] is True):
                if (args['<config-file-name>'] is not None and not exceptFile.__contains__(args['<config-file-name>']) ):
                    if(file != args['<config-file-name>']):
                        shutil.copyfile(file, args['<config-file-name>'])
                        conf.set('pymake', 'config', args['<config-file-name>'])
                        conf.write(open('pymake.ini', 'w'))
                    else:
                        print('You can\'t add same named file...')
                else:
                    print ( 'You can\'t add pymake\'s file...')
            elif(args['--list'] is True):
                files = os.listdir(os.getcwd())
                for f in files:
                    if (not exceptFile.__contains__(f)):
                        print(f)
            elif(args['--restore'] is True):
                conf.set('pymake', 'config', 'pymake.json')
                conf.write(open('pymake.ini', 'w'))
            elif (args['--switch'] is True
                  or ( args['<config-file-name>'] is not None and args['<config-file-name>'] != '' )):
                if (args['<config-file-name>'] is not None and not exceptFile.__contains__(args['<config-file-name>']) ):
                    if (os.path.exists(args['<config-file-name>'])):
                        conf.set('pymake', 'config', args['<config-file-name>'])
                        conf.write(open('pymake.ini', 'w'))
                        print("switch source config: %s" % file)
                    else:
                        print("source file %s isn't exists" % args['<config-file-name>'])
                else:
                    print('You can\'t add pymake\'s file...')
            else:
                print(file)
        else:
            ''
        break


    while (True):
        if (args['list-path'] == True):
            dict0 = config['add-to-env'].copy()
            dict0.update(config['add-custom-bin-path-to-env'])
            dict0['PYMAKE_BUILD_PATH'] = config['source-to-build']['PYMAKE_BUILD_PATH']
            if(args["--keys"] is True) :
                for k in dict0.keys():
                    print(k)
            elif ( args["--values"]  is True ):
                for v in dict0.values():
                    print(v)
            else:
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )
        else:
            ''
        break

    while (True):
        if (args['config'] == True):
            if(args['--toolchain'] == True):
                if( args["<path>"] is not None):
                    config["add-to-env"]["PYMAKE_TOOLCHAIN_PATH"] = args["<path>"]
                else:
                    ''
            elif (args['--genmake'] == True):
                if (args["<path>"] is not None):
                    config["add-to-env"]["PYMAKE_GENMAKE_PATH"] = args["<path>"]
                else:
                    ''
            elif (args['--make'] == True):
                if (args["<path>"] is not None):
                    config["add-to-env"]["PYMAKE_MAKE_PATH"] = args["<path>"]
                else:
                    ''
            elif (args['--build'] == True):
                if (args["<path>"] is not None):
                    config["source-to-build"]["PYMAKE_BUILD_PATH"] = args["<path>"]
                else:
                    ''
            else:
                ''
        elif ( args['other-bin'] is True):
            if(args['--add'] == True):
                if( args['<name>'] and args["<path>"] is not None):
                    config["add-custom-bin-path-to-env"][args['<name>']] = args["<path>"]
                else:
                    ''
            elif (args['--del'] == True):
                if( args["<name>"] is not None):
                    if(config['add-other-bin-path-to-dev'].__contains__(args['<name>'])):
                        config["add-custom-bin-path-to-env"].__delitem__(args['<name>'])
                    else:
                        ''
                else:
                    ''
            elif (args['--mod'] == True):
                if (args['<name>'] and args["<path>"] is not None ):
                    if(config['add-other-bin-path-to-dev'].__contains__(args['<name>'])):
                        config["add-other-bin-path-to-dev"][args['<name>']] = args["<path>"]
                    else:
                        ''
                else:
                    ''
        else:
            ''
        #print(config)
        writeJsonData(file, config)
        break

    while ( True ):
        cmd = ""
        path = ""

        if( args['generate'] == True ):
            cmd = config["source-to-build"]["PYMAKE_GENMAKE_COMMAND"]
        elif (args['build'] == True):
            cmd = config["source-to-build"]["PYMAKE_MAKE_COMMAND"]
        elif (args['install'] == True):
            cmd = config["source-to-build"]["PYMAKE_INSTALL_COMMAND"]
        elif ( args['genmake'] == True ):
            cmd = args['<genmake-command>']
        else:
            ''

        env = os.environ
        path = config["add-to-env"]['PYMAKE_TOOLCHAIN_PATH']
        env["PATH"] = path + os.path.pathsep + env["PATH"]
        path = config["add-to-env"]['PYMAKE_MAKE_PATH']
        env["PATH"] = path + os.path.pathsep + env["PATH"]
        path = config["add-to-env"]['PYMAKE_GENMAKE_PATH']
        env["PATH"] = path + os.path.pathsep + env["PATH"]
        path = config["source-to-build"]['PYMAKE_BUILD_PATH']
        env["PATH"] = path + os.path.pathsep + env["PATH"]
        if ( not os.path.exists(path) ):
            os.makedirs(path)
        for path in config["add-custom-bin-path-to-env"].values():
            env["PATH"] = path + os.path.pathsep + env["PATH"]

        #print(env["PATH"].replace(os.path.pathsep, '\n'))
        path = config["source-to-build"]["PYMAKE_BUILD_PATH"]
        os.chdir(path)
        #print( cmd )
        os.system(cmd)
        break

    return

if __name__ == '__main__':

    main_function()
