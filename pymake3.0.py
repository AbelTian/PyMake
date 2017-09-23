"""PyMake 3.0.

Usage:
  pymake3.py source [ --add | --del | --switch ] [ <config-file-name> ]
  pymake3.py source --mod <config-file-name> <new-config-file-name>
  pymake3.py source [ --show | --restore ]

  pymake3.py list [ --var | --path | --command | --stream ] [--raw]
  pymake3.py set ( env-var | env-path | project | cmd ) ( --add | --del | --mod ) <name> [ <value> ]
  pymake3.py set stream (--add | --del | --mod ) <name> [ <values> ... ]
  pymake3.py switch [ --env | --path | --command | --project | --stream ] <name>

  pymake3.py exec [ <stream-names> ... ]
  pymake3.py (-h | --help)
  pymake3.py --version

Command:
  source           switch to another source file
  set env-path     config work directory
  set env-var
  set cmd
  set project      config project's pattern
  list             list configed values
  switch           switch to current env path project or stream

Options:
  -h --help     Show this screen.
  --version     Show version.
  --add
  --del
  --mod         add or delete or modify a config or path
  --switch      switch to another source
  --var
  --path
  --command
  --stream        list info params
  --show        display haved stream config files
  --restore     reset to pymake3.json stream config file
"""

# -*- coding: utf-8 -*-

import os
import re
import sys
import pwd
import shutil
import time
import json
import types
import locale
import codecs
import threading
import subprocess
from pycore.pycore import *
from pycore.docopt import docopt

def main_function():

    d = {
        "environ":{
            "PYCMD_MYNAME": "T.D.R",
            "a_special_var_const":"hello world",

            "ios":{

            },
            "macOS":{
                "QKIT": "macOS",
                "QTDIR": "/Users/abel/Develop/b0-toolskits/Libraries/QtLibraries/5.9.1/clang_64",
            },
            "current":"macOS",

            "path+":{
                "mymac":{
                    "cc-path":"/usr/bin/ccddeef",
                    "qt5.9-clang64": "/Users/abel/Develop/b0-toolskits/Libraries/QtLibraries/5.9.1/clang_64/bin",
                    "cmake-path": "/Users/abel/Develop/b0-toolskits/compliers/CMake.app/Contents/bin",
                    "macosx-sdk": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks",
                    "make-and-toolchain-path": "/usr/bin",
                    "qqt-framework-path": "/Users/abel/Develop/c0-buildstation/qqt-mac/src/bin"
                },
                "mymac-ios":{
                    "cc-path":"/..."
                },
                "current":"mymac"
            }

        },

        "project":{
            "qqt":{
                "product-name": "QQt",
                "build-path": "/Users/abel/Develop/c0-buildstation/qqt-mac",
                "source-path": "/Users/abel/Develop/a0-Developworkspace/a0-qqtfoundation",
                "source-pro": "a0-qqtfoundation.pro"
            },
            "wiz":{
                "build-path":""
            },
            "current":"qqt"
        },

        "command":{
            "macClang":{
                "cd":"cd",
                "CC":"clang++"
            },
            "gcc":{
                "CC":"g++",
                "cd":"cd"
            },
            "win-mingw32": {
                "cd":"cd /d",
                "make":"mingw32-make"
            },
            "win-msvc": {
                "cd":"cd /d",
                "make":"nmake"
            },
            "current":"gcc"
        },

        "store-named-variable":{
            "cd":"${cd}",
            "now-make":"${make}",
            "now-app-bundle":"${product-name}.app",
            "now-framework-bundle":"${product-name}.framework",
            "now-product-name": "${product-name}",
            "now-install-path": "/Users/abel/Develop/b1-Product/a0-qqtbased/Application",
            "now-qmake-pro": "${source-pro}",
            "now-source-path": "${ source-path }",
            "now-build-path": "${build-path}"
        },

        "store-named-command": {
            "why-to-set-these":"I'm not similar to these command, so list them here, rather than forgotten them",
            "mkdir-build-path": "mkdir -p ${now-build-path}",
            "cd-build-path": "${cd} ${now-build-path}",
            "cd-product-path": "cd ${now-install-path}",
            "qmake": "qmake ${now-source-path}/${now-qmake-pro} -spec macx-g++ CONFIG+=x86_64 && /usr/bin/make qmake_all",
            "qmake-macdeployqt": "macdeployqt examples/qqtframe/bin/qqtframe.app -verbose=1",
            "make": "${make} -j4",
            "make-clean": "${make} clean in ${now-build-path}",
            "make-install": "${now-make} install",
            "cmake": "cmake -G\"Unix Makefiles\" -DCMAKE_INSTALL_PREFIX=${now-install-path} ${now-source-path}",
            "cmake-xcode": "cmake -GXCode -DCMAKE_INSTALL_PREFIX=${now-install-path} ${now-source-path}",
            "cmake-rmcache": "rm -f CMakeCache.txt",
            "test-pwd": "pwd",
            "test-var": "echo 'qtdir:' $QTDIR ",
            "test-msg": "echo 'work complete!'"
        },

        "execute-stream": {
            "ss": [
                "test-pwd",
                "test-pwd",
                "test-pwd",
                "test-msg"
            ],
            "build": [
                "mkdir-build-path",
                "cd-build-path",
                "test-pwd",
                "qmake",
                "make",
                "qmake-macdeployqt",
                "test-msg"
            ],
            "install": [
                "cd-build-path",
                "test-pwd",
                "qmake-macdeployqt"
            ],
            "current":"ss"
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

    args = docopt(__doc__, version='pymake3.py v3.0')
    #print(args)

    exceptFile = ( 'pymake.ini', 'pymake.py', '.gitignore', '.git', 'pycore', 'README.md', '.idea')
    while (True):
        if(args['source'] is True):
            if(args['--del'] is True):
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
            elif (args['--mod'] is True):
                if ( ( args['<config-file-name>'] and args['<new-config-file-name>']) is not None and not exceptFile.__contains__(args['<config-file-name>'])):

                    os.rename(args['<config-file-name>'],args['<new-config-file-name>'])

                    if (file == args['<config-file-name>']):
                        conf.set('pymake', 'config',args['<new-config-file-name>'])
                        conf.write(open('pymake.ini', 'w'))

                else:
                    print ('You can\'t mod pymake\'s file...')
            elif(args['--show'] is True):
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
                        print("switch to source config: %s" % args['<config-file-name>'])
                    else:
                        print("source file %s isn't exists" % args['<config-file-name>'])
                else:
                    print('You can\'t switch pymake\'s file...')
            else:
                print(file)
            return
        else:
            ''
        break

    config = readJsonData(file)
    #print(config)

    while (True):
        if (args['set'] == True):
            if (args['env-var'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):

                        current_vars = config['environ']['current']
                        config["environ"][current_vars][args['<name>']] = args["<value>"]
                        print ( "successed %s:%s" % (args['<name>'],args[ "<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):

                        current_vars = config['environ']['current']
                        if (config['environ'][current_vars].__contains__(args['<name>'])):
                            config['environ'][current_vars].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        current_vars = config['environ']['current']

                        if (config['environ'][current_vars].__contains__(args['<name>'])):
                            config['environ'][current_vars][args['<name>']] = args["<value>"]
                            print ("successed %s:%s" % (args['<name>'],args["<value>"]))
                        else:
                            ''
                    else:
                        ''
                else:
                    ''
            elif (args['env-path'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):

                        current_vars = config['environ']['path+']['current']

                        config['environ']['path+'][args['<name>']] = args["<value>"]
                        print ( "successed %s:%s" % (args['<name>'],args[ "<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):

                        current_vars = config['environ']['path+']['current']

                        if (config['environ']['path+'].__contains__(args['<name>'])):
                            config['environ']['path+'].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):

                        current_vars = config['environ']['path+']['current']

                        if (config['environ']['path+'].__contains__(args['<name>'])):
                            config['environ']['path+'][args['<name>']] = args["<value>"]
                            print ("successed %s:%s" % (args['<name>'],args["<value>"]))
                        else:
                            ''
                    else:
                        ''
                else:
                    ''
            elif (args['cmd'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config["store-named-command"][args['<name>']] = args["<value>"]
                        print ( "successed %s:%s" % (args['<name>'],args[ "<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['store-named-command'].__contains__(args['<name>'])):
                            config["store-named-command"].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['store-named-command'].__contains__(args['<name>'])):
                            config["store-named-command"][args['<name>']] = args["<value>"]
                            print ("successed %s:%s" % (args['<name>'],args["<value>"]))
                        else:
                            ''
                    else:
                        ''
                else:
                    ''
            elif (args['stream'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["execute-stream"][args['<name>']] = args["<values>"]
                        print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['execute-stream'].__contains__(args['<name>'])):
                            config["execute-stream"].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["execute-stream"][args['<name>']] = args["<values>"]
                        print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                    else:
                        ''
                else:
                    ''
            else:
                ''
            # print(config)
            writeJsonData(file, config)
            return
        else:
            ''
        break

    while (True):
        if (args['switch'] == True):
            if (args['--env'] == True):
                if (args['<name>'] is not None):
                    config['environ']['current'] = args['<name>']
                    print ( "current %s" % (args['<name>']))
                else:
                    ''
            elif (args['--path'] == True):
                if (args['<name>'] is not None):
                    config['environ']['path+']['current'] = args['<name>']
                    print ("current %s" % (args['<name>']))
                else:
                    ''
            elif (args['--command'] == True):
                if (args['<name>'] is not None):
                    config['command']['current'] = args['<name>']
                    print ("current %s" % (args['<name>']))
                else:
                    ''
            elif (args['--stream'] == True):
                if (args['<name>'] is not None):
                    config['execute-stream']['current'] = args['<name>']
                    print ("current %s" % (args['<name>']))
                else:
                    ''
            # print(config)
            writeJsonData(file, config)
            return
        else:
            ''
        break

    ### config -> raw config
    rawconfig = config.copy()
    #print ( rawconfig )
    env = os.environ

    #replace env-variables's ${...}
    for (key, value) in rawconfig["environ"].items():
        #print (key) #...
        if(not isinstance( value, str)):
            continue

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...

            if (env.has_key(key1)):
                rawconfig["environ"][key] = rawconfig["environ"][key].replace(key0, env[key1])

            for (key2, value2) in config["environ"].items():

                if (not isinstance(value2, str)):
                    continue
                if (key2 == key1):
                    rawconfig["environ"][key] = rawconfig["environ"][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace env-variables current's ${...}
    current_vars = rawconfig["environ"]["current"]
    for (key, value) in rawconfig["environ"][current_vars].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...
            if (env.has_key(key1)):
                rawconfig["environ"][current_vars][key] = rawconfig["environ"][current_vars][key].replace(key0, env[key1])

            #env set
            for (key2, value2) in config["environ"].items():

                if (not isinstance(value2, str)):
                    continue

                if (key2 == key1):
                    rawconfig["environ"][current_vars][key] = rawconfig["environ"][current_vars][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''
            #current env-variable
            for (key2, value2) in config["environ"][current_vars].items():

                if (key2 == key1):
                    rawconfig["environ"][current_vars][key] = rawconfig["environ"][current_vars][key].replace(key0,rawconfig["environ"][current_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace path+'s ${}
    current_vars = rawconfig["environ"]['path+']["current"]
    for (key, value) in rawconfig["environ"]['path+'][current_vars].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...
            if (env.has_key(key1)):
                rawconfig["environ"]['path+'][current_vars][key] = rawconfig["environ"]['path+'][current_vars][key].replace(key0, env[key1])

            #env set
            for (key2, value2) in config["environ"].items():

                if (not isinstance(value2, str)):
                    continue

                if (key2 == key1):
                    rawconfig["environ"]['path+'][current_vars][key] = rawconfig["environ"]['path+'][current_vars][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            #current env-variable
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["environ"]['path+'][current_vars][key] = rawconfig["environ"]['path+'][current_vars][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            #current path
            for (key2, value2) in rawconfig["environ"]["path+"][current_vars].items():

                if (key2 == key1):
                    rawconfig["environ"]['path+'][current_vars][key] = rawconfig["environ"]['path+'][current_vars][key].replace(key0, rawconfig["environ"]["path+"][current_vars][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace project's ${}
    current_vars = rawconfig['project']["current"]
    for (key, value) in rawconfig["project"][current_vars].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...

            #env
            if (env.has_key(key1)):
                rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, env[key1])

            for (key2, value2) in config["environ"].items():

                if (not isinstance(value2, str)):
                    continue

                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            #current path+
            current_path_vars = rawconfig["environ"]['path+']['current']
            for (key2, value2) in config["environ"]['path+'][current_path_vars].items():

                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0,config["environ"]['path+'][current_path_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            #self
            for (key2, value2) in config["project"][current_vars].items():

                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0,rawconfig["project"][current_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''


    # replace command's ${}
    current_vars = rawconfig['command']["current"]
    for (key, value) in rawconfig["command"][current_vars].items():
        # print (key) #...

        startpos = 0
        while (True):
            # print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            # print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            # print ( key1 ) #...

            # env
            if (env.has_key(key1)):
                rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, env[key1])

            for (key2, value2) in config["environ"].items():

                if (not isinstance(value2, str)):
                    continue

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # current path+
            current_path_vars = rawconfig["environ"]['path+']['current']
            for (key2, value2) in config["environ"]['path+'][current_path_vars].items():

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, config["environ"]['path+'][current_path_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # self
            for (key2, value2) in config["command"][current_vars].items():

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["command"][current_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace store-named-variable's ${}
    # from env path+ command project
    for (key, value) in rawconfig["store-named-variable"].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...

            if (env.has_key(key1)):
                rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, env[key1])

            for (key2, value2) in config["environ"].items():

                if (not isinstance(value2, str)):
                    continue

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # current path+
            current_path_vars = rawconfig["environ"]['path+']['current']
            for (key2, value2) in config["environ"]['path+'][current_path_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, config["environ"]['path+'][current_path_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            current_command_vars = rawconfig["command"]['current']
            for (key2, value2) in rawconfig["command"][current_command_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["command"][current_command_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''
            current_project_vars = rawconfig["project"]['current']
            for (key2, value2) in rawconfig["project"][current_project_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["project"][current_project_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''
            # self
            for (key2, value2) in config["store-named-variable"].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["store-named-variable"][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace store-named-command's ${...}
    # store-named-variable
    for (key, value) in rawconfig["store-named-command"].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...
            if (env.has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, env[key1])

            for (key2, value2) in rawconfig["store-named-variable"].items():
                if (key2 == key1):
                    rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["store-named-variable"][key1])
                    #print ("%s:%s" % (key, rawconfig["store-named-command"][key]))
                else:
                    ''
            # self
            for (key2, value2) in config["store-named-command"].items():

                if (key2 == key1):
                    rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["store-named-command"][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    #list command
    while (True):
        if (args['list'] == True):
            if ( args['--raw'] == True ):
                list_config = rawconfig
            else:
                list_config = config

            if( args['--var'] == True):

                current_vars = list_config['environ']['current']
                dict0 = list_config['environ'][current_vars].copy()
                for (k, v) in list_config['environ']:
                    if(isinstance(v, str)):
                        dict0.update((k, v))

                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['--path'] == True):
                current_vars = list_config['environ']['path+']['current']
                dict0 = list_config['environ']['path+'][current_vars].copy()

                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['--command'] == True):
                dict0 = list_config['store-named-command'].copy()
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['--stream'] == True):
                dict0 = list_config['execute-stream'].copy()
                for (k,v) in dict0.items():
                    print("%-24s %s" % (k,v) )
            return
        else:
            ''
        break

    # set into env
    # env-varible
    for (key, value) in config["environ"].items():
        if (not isinstance(value, str)):
            continue
        env[key] = value
    # current env-variable
    current_env_vars = rawconfig["environ"]['current']
    for (key, value) in rawconfig["environ"][current_env_vars].items():
        env[key] = value
    for (key, value) in env.items():
        print ("%-24s %s" % (key, value) )
        ''

    # current path
    current_vars = rawconfig["environ"]['path+']['current']
    for (key, value) in rawconfig["environ"]["path+"][current_vars].items():
        env["PATH"] = path + os.path.pathsep + env["PATH"]
    print(env["PATH"].replace(os.path.pathsep, '\n'))

    def read_thread_function(p):
        ''
        code = (codecs.lookup(locale.getpreferredencoding()).name)
        while (True):
            l = p.stdout.readline().rstrip().decode(code)

            if (l is None):
                # print ('ddd')
                break

            if (p.poll() is not None):
                # print("eee")
                break

            print (l)
            # print (l)
            # stdout.flush()

    def read_stderr_thread_function(p):
        ''
        code = (codecs.lookup(locale.getpreferredencoding()).name)
        while (True):
            l = p.stderr.readline().rstrip().decode(code)

            if (l is None):
                # print ('ddd')
                break

            if (p.poll() is not None):
                # print("eee")
                break

            print (l)
            # print (l)
            # stdout.flush()

    def write_thread_function(list0):
        ''

    while ( True ):

        if( args['exec'] == True):
            if(args['<stream-names>'] is not None):
                list0 = []
                for stream in args['<stream-names>']:
                    if (rawconfig["execute-stream"].__contains__(stream)):
                        for cmd in rawconfig["execute-stream"][stream]:
                            if (rawconfig['store-named-command'].__contains__(cmd)):
                                # print("execute %s %s %s" % (stream, cmd, rawconfig['store-named-command'][cmd]))
                                list0.append( rawconfig['store-named-command'][cmd] )
                            else:
                                print ("can't find command %s" % cmd)
                    else:
                        print ("can't find stream %s" % stream)
                list0.append("exit 0")
                #print (list0)

                shell = pwd.getpwuid(os.getuid()).pw_shell
                if shell is None: shell = os.environ.get( 'SHELL'   )
                if shell is None: shell = os.environ.get( 'COMSPEC' )
                #print ( 'Running under', shell )

                p = subprocess.Popen(shell, shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                read_thread = threading.Thread(target=read_thread_function, args=(p,))
                read_thread.start()
                read_err_thread = threading.Thread(target=read_stderr_thread_function, args=(p,))
                read_err_thread.start()
                write_thread = threading.Thread(target=write_thread_function, args=(list0,))
                #write_thread.start()
                time.sleep(1)

                for cmd in list0:
                    #print  ("command:%s" % cmd)
                    p.stdin.write(cmd + '\n')
                    p.stdin.flush()
                    #p.stdin.write("ping 127.0.0.1 -c 2 \n")
                    #p.stdin.flush()

                p.wait()
                #read_thread.close()
                time.sleep(1)

                #return


            else:
                print ("stream-names is none")
        else:
            ''

        break

    return

if __name__ == '__main__':

    main_function()
