"""PyMake 3.0.

Usage:
  pymake3.py source [ --add | --del | --switch ] [ <config-file-name> ]
  pymake3.py source --mod <config-file-name> <new-config-file-name>
  pymake3.py source [ --show | --restore ]
  pymake3.py set ( env-var | env-path | proj | cmd ) ( --add | --del | --mod ) <name> [ <value> ]
  pymake3.py set stream (--add | --del | --mod ) <name> [ <values> ... ]
  pymake3.py set comm ( env-var | env-path ) ( --add | --del | --mod ) <name> [ <value> ]
  pymake3.py switch [ --env | --path | --cmd | --proj | --stream ] <name>
  pymake3.py list [ --var | --path | --project | --command | --value | --cmd | --stream ] [--raw]
  pymake3.py exec [ <stream-names> ... ]
  pymake3.py (-h | --help)
  pymake3.py --version

Command:
  source           switch to another source file
  set env-path     config work directory
  set env-var
  set cmd
  set proj         config project's pattern
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
  --cmd
  --stream      show cmd list
  --show        display haved stream config files
  --restore     reset to pymake.json stream config file
"""

# -*- coding: utf-8 -*-

import os
import re
import sys
import pwd
import shutil
import time
import json
import copy
import types
import locale
import codecs
import threading
import subprocess
from pycore.pycore import *
from pycore.docopt import docopt
from collections import OrderedDict

def main_function():

    d = {
        "environ": {
            "PYCMD_MYNAME": "T.D.R",
            "a_special_var_const": "hello world",

            "ios": {
                "QKIT": "iOS"
            },
            "macOS": {
                "QKIT": "macOS",
                "QtSDK": "clang_64",
                "QtVer": "5.9.1",
                "QSYSNAME": "MacOS",
                "BUILDTYPE": "Release",
                "cmake-bin": "CMake.app/Contents/bin",
                "path-toolchain": "/usr/bin",
                "dev-root": "/Users/abel/Develop",
                "QSYSNAME_BUILDTYPE": "${QSYSNAME}/${BUILDTYPE}",
                "os-sdk": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks"
            },
            "current": "macOS",

            "src-root": "${dev-root}/a0-Developworkspace",
            "prod-root": "${dev-root}/b1-Product/a0-qqtbased/Application",
            "build-root": "${dev-root}/c0-buildstation",
            "tool-root": "${dev-root}/b0-toolskits",
            "test-root": "${dev-root}/a1-testspace",
            "webrc-root": "${dev-root}/b2-webrc",
            "QTDIR": "${tool-root}/Libraries/QtLibraries/${QtVer}/${QtSDK}",

            "path+": {
                "dev-?": {
                    "cc-path": "ee/ff"
                },
                "develop-mac": {
                    "target-sdk": "${os-sdk}"
                },
                "current": "develop-mac",

                "QtSDK": "${tool-root}/Libraries/QtLibraries/${QtVer}/${QtSDK}/bin",
                "cmake-path": "${tool-root}/compliers/${cmake-bin}",
                "make-and-toolchain-path": "${path-toolchain}"
            }
        },
        "project": {
            "qqt": {
                "prod-name": "QQt",
                "prod-major-version": "1",
                "app-name": "qqtframe",
                "proj-name": "a0-qqtfoundation",
                "build-path": "${build-root}/${proj-name}/${QSYSNAME_BUILDTYPE}",
                "source-path": "${src-root}/${proj-name}",
                "qmake-pro": "${proj-name}.pro",
                "release-path": "${build-path}/src/bin",
                "app-release-path": "${build-path}/examples/${app-name}/bin"
            },
            "wiz": {
                "build-path": ""
            },
            "current": "qqt"
        },
        "command": {
            "macgcc": {
                "mkdir": "mkdir -p",
                "cd": "cd",
                "deployqt": "macdeployqt",
                "make": "make"
            },
            "win-mingw32": {
                "cd": "cd /d",
                "make": "mingw32-make"
            },
            "current": "macgcc"
        },
        "store-named-variable": {
            "tips": "put your any common & special variables here, you worn it",
            "cd": "${cd}",
            "mkdir": "${mkdir}",
            "make": "${make}",
            "deployqt": "${deployqt}",
            "prod-name": "${prod-name}",
            "app-bundle": "${app-name}.app",
            "app": "${app-bundle}",
            "app-native": "${app-bundle}/Contents/MacOS",

            "framework-bundle": "${prod-name}.framework",
            "app-dep": "${app-release-path}/${app-bundle}/Contents/Frameworks",
            "dep-lib-qqt": "${release-path}/${framework-bundle}",
            "dep-lib": "${dep-lib-qqt}",
            "dep-lib-qqt-native": "${framework-bundle}/Versions/${prod-major-version}/${prod-name}",
            "install-path": "${prod-root}/a0-qqtbased/Application",
            "qmake-pro": "${qmake-pro}",
            "source-path": "${ source-path }",
            "build-path": "${build-path}",
            "release-path": "${release-path}",
            "app-release-path": "${app-release-path}"
        },
        "store-named-command": {
            "why-to-set-these": "I'm not similar to these command, so list them here, rather than forgotten them",
            "here": "cl-command, sys-command",
            "here-1": "replace? no, append? easy!",

            "mk-build-path": "${mkdir} ${build-path}",
            "cd-build-path": "${cd} ${build-path}",
            "cd-release-path": "${cd} ${release-path}",
            "cd-app-release-path": "${cd} ${app-release-path}",
            "cd-prod-path": "${cd} ${install-path}",

            "cmake": "cmake -G\"Unix Makefiles\" -DCMAKE_INSTALL_PREFIX=${install-path} ${source-path}",
            "cmake-xcode": "cmake -GXCode -DCMAKE_INSTALL_PREFIX=${install-path} ${source-path}",
            "cmake-rmcache": "rm -f CMakeCache.txt",

            "qmake": "qmake ${source-path}/${qmake-pro} -spec macx-g++ CONFIG+=x86_64 && ${make} qmake_all",
            "make": "${make} -j4",
            "make-clean": "${make} clean in ${build-path}",
            "make-install": "${make} install",

            "deployqt": "${deployqt} ${app-release-path}/${app} -verbose=1",
            "deployqt-dmg": "${deployqt} -dmg",
            "deployqt-help": "${deployqt} --help",

            "cp-dep": "cp -fr ${dep-lib} ${app-dep}",
            "install_name_tool": "install_name_tool -change ${dep-lib-qqt-native} @rpath/${dep-lib-qqt-native} ${app-release-path}/${app-native}/${app-name} ",

            "pwd": "pwd",
            "var": "echo 'qtdir:' $QTDIR ",
            "var2": "echo 'qtdir:' ${QTDIR} ",
            "msg": "echo 'work complete!'"
        },
        "execute-stream": {
            "t": [
                "pwd",
                "pwd",
                "var",
                "var2",
                "pwd",
                "msg",
                "set ${build-path}",
                "macdeployqt --help"
            ],
            "build": [
                "mk-build-path",
                "cd-build-path",
                "qmake",
                "make",
                "deployqt",
                "cp-dep",
                "install_name_tool",
                "msg"
            ],
            "rebuild": [
                "mk-build-path",
                "cd-build-path",
                "qmake",
                "make",
                "deployqt",
                "cp-dep",
                "msg"
            ],
            "install": [
                "cd-build-path",
                "pwd",
                "qdeployqt"
            ],
            "current": "build"
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

    #create store-named-variable

    while (True):
        if (args['set'] == True):
            if( args['comm'] is True):
                if (args['env-var'] is True):
                    if (args['--add'] == True):
                        if (args['<name>'] and args["<value>"] is not None):

                            config["environ"][args['<name>']] = args["<value>"]
                            print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args["<name>"] is not None):

                            if (config['environ'].__contains__(args['<name>'])):
                                config['environ'].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<name>'] and args["<value>"] is not None):

                            if (config['environ'].__contains__(args['<name>'])):
                                config['environ'][args['<name>']] = args["<value>"]
                                print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['env-path'] is True):
                    if (args['--add'] == True):
                        if (args['<name>'] and args["<value>"] is not None):

                            config['environ']['path+'][args['<name>']] = args["<value>"]
                            print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args["<name>"] is not None):

                            if (config['environ']['path+'].__contains__(args['<name>'])):
                                config['environ']['path+'].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<name>'] and args["<value>"] is not None):

                            if (config['environ']['path+'].__contains__(args['<name>'])):
                                config['environ']['path+'][args['<name>']] = args["<value>"]
                                print ("successed %s:%s" % (args['<name>'], args["<value>"]))
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

            elif (args['env-var'] is True):
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

                        config['environ']['path+'][current_vars][args['<name>']] = args["<value>"]
                        print ( "successed %s:%s" % (args['<name>'],args[ "<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):

                        current_vars = config['environ']['path+']['current']

                        if (config['environ']['path+'][current_vars].__contains__(args['<name>'])):
                            config['environ']['path+'][current_vars].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):

                        current_vars = config['environ']['path+']['current']

                        if (config['environ']['path+'][current_vars].__contains__(args['<name>'])):
                            config['environ']['path+'][current_vars][args['<name>']] = args["<value>"]
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
            elif (args['--cmd'] == True):
                if (args['<name>'] is not None):
                    config['command']['current'] = args['<name>']
                    print ("current %s" % (args['<name>']))
                else:
                    ''
            elif (args['--proj'] == True):
                if (args['<name>'] is not None):
                    config['project']['current'] = args['<name>']
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
    rawconfig = copy.deepcopy(config)
    # print ( config )
    # print ( rawconfig )

    # maybe not env, it is env's variable dict
    # yeah, it is env, env is a dict, not a platform based variable
    # ${...} is ok to use, it will find variable in env
    env = os.environ

    # replace env-variables current's ${...}
    # env env-current
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

            #env
            if (env.has_key(key1)):
                rawconfig["environ"][current_vars][key] = rawconfig["environ"][current_vars][key].replace(key0, env[key1])

            #current env-variable
            for (key2, value2) in rawconfig["environ"][current_vars].items():

                if (key2 == key1):
                    rawconfig["environ"][current_vars][key] = rawconfig["environ"][current_vars][key].replace(key0,rawconfig["environ"][current_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace env-variables's ${...}
    # env env-current env-comm
    for (key, value) in rawconfig["environ"].items():
        # print (key) #...
        if (not isinstance(value, basestring)):
            continue

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
                rawconfig["environ"][key] = rawconfig["environ"][key].replace(key0, env[key1])

            # env-current
            current_env_vars = rawconfig["environ"]["current"]
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (not isinstance(value2, basestring)):
                    continue
                if (key2 == key1):
                    rawconfig["environ"][key] = rawconfig["environ"][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # env comm
            for (key2, value2) in rawconfig["environ"].items():

                if (not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["environ"][key] = rawconfig["environ"][key].replace(key0, rawconfig["environ"][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace path+'s current ${}
    # env env-comm env-current path-current
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

            # env
            if (env.has_key(key1)):
                rawconfig["environ"]['path+'][current_vars][key] = rawconfig["environ"]['path+'][current_vars][key].replace(key0, env[key1])

            # current env-variable
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["environ"]['path+'][current_vars][key] = rawconfig["environ"]['path+'][current_vars][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # env comm
            for (key2, value2) in rawconfig["environ"].items():

                if (not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["environ"]['path+'][current_vars][key] = rawconfig["environ"]['path+'][current_vars][key].replace(key0, rawconfig["environ"][key1])
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

    # replace path+ comm's ${}
    # env env-comm env-current path-current path-comm
    for (key, value) in rawconfig["environ"]['path+'].items():
        #print (key) #...

        if(not isinstance(value, basestring)):
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

            # env
            if (env.has_key(key1)):
                rawconfig["environ"]['path+'][key] = rawconfig["environ"]['path+'][key].replace(key0, env[key1])

            # current env-variable
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["environ"]['path+'][key] = rawconfig["environ"]['path+'][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # env comm
            for (key2, value2) in rawconfig["environ"].items():

                if (not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["environ"]['path+'][key] = rawconfig["environ"]['path+'][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            #current path
            current_path_vars = rawconfig["environ"]['path+']["current"]
            for (key2, value2) in rawconfig["environ"]["path+"][current_path_vars].items():

                if (key2 == key1):
                    rawconfig["environ"]['path+'][key] = rawconfig["environ"]['path+'][key].replace(key0, rawconfig["environ"]["path+"][current_path_vars][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # comm path
            for (key2, value2) in rawconfig["environ"]["path+"].items():

                if (not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["environ"]['path+'][key] = rawconfig["environ"]['path+'][key].replace(key0, rawconfig["environ"]["path+"][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace project's ${}
    # env env-comm env-current path-current path-comm project
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

            # env
            if (env.has_key(key1)):
                rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, env[key1])

            # env current
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():
                #print (key0, key1, key2, isinstance(value2, basestring), key2==key1)
                if (key2 == key1):

                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, rawconfig["environ"][current_env_vars][key1])

                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # env comm
            for (key2, value2) in rawconfig["environ"].items():

                if (not isinstance(value2, basestring)):
                    continue
                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, rawconfig["environ"][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # current path+
            current_path_vars = rawconfig["environ"]['path+']['current']
            for (key2, value2) in rawconfig["environ"]['path+'][current_path_vars].items():
                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, rawconfig["environ"]["path+"][current_path_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # comm path+
            for (key2, value2) in rawconfig["environ"]['path+'].items():

                if (not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0, rawconfig["environ"]['path+'][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            #self
            for (key2, value2) in rawconfig["project"][current_vars].items():

                if (key2 == key1):
                    rawconfig["project"][current_vars][key] = rawconfig["project"][current_vars][key].replace(key0,rawconfig["project"][current_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''


    # replace command's ${}
    # env env-comm env-current path-current path-comm command
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

            # env current
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # env comm
            for (key2, value2) in rawconfig["environ"].items():

                if (not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # current path+
            current_path_vars = rawconfig["environ"]['path+']['current']
            for (key2, value2) in rawconfig["environ"]['path+'][current_path_vars].items():

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["environ"]['path+'][current_path_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # comm path+
            for (key2, value2) in rawconfig["environ"]['path+'].items():

                if (not isinstance(value2, basestring)):
                    continue


                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["environ"]['path+'][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # self
            for (key2, value2) in rawconfig["command"][current_vars].items():

                if (key2 == key1):
                    rawconfig["command"][current_vars][key] = rawconfig["command"][current_vars][key].replace(key0, rawconfig["command"][current_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace store-named-variable's ${}
    # env env-comm env-current path-current path-comm command project
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

            # env
            if (env.has_key(key1)):
                rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, env[key1])

            # env current
            current_env_vars = rawconfig["environ"]['current']
            for (key2, value2) in rawconfig["environ"][current_env_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["environ"][current_env_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # env comm
            for (key2, value2) in rawconfig["environ"].items():

                if (not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["environ"][key1])
                    #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''


            # current path+
            current_path_vars = rawconfig["environ"]['path+']['current']
            for (key2, value2) in rawconfig["environ"]['path+'][current_path_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["environ"]['path+'][current_path_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # comm path+
            for (key2, value2) in rawconfig["environ"]['path+'].items():

                if(not isinstance(value2, basestring)):
                    continue

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["environ"]['path+'][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # current command
            current_command_vars = rawconfig["command"]['current']
            for (key2, value2) in rawconfig["command"][current_command_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["command"][current_command_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # current project
            current_project_vars = rawconfig["project"]['current']
            for (key2, value2) in rawconfig["project"][current_project_vars].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["project"][current_project_vars][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

            # self
            for (key2, value2) in rawconfig["store-named-variable"].items():

                if (key2 == key1):
                    rawconfig["store-named-variable"][key] = rawconfig["store-named-variable"][key].replace(key0, rawconfig["store-named-variable"][key1])
                    # print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                else:
                    ''

    # replace store-named-command's ${...}
    # env env-current env-comm path+-current path+comm project command store-named-variable
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

            # env
            if (env.has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, env[key1])

            # env current
            current_vars = rawconfig["environ"]['current']
            if(rawconfig["environ"][current_vars].has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["environ"][current_vars][key1])

            # env comm
            if(rawconfig["environ"].has_key(key1)):
                if( isinstance(rawconfig["environ"][key1], basestring) ):
                    rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["environ"][key1])

            # path+ current
            current_vars = rawconfig["environ"]['path+']['current']
            if(rawconfig["environ"]['path+'][current_vars].has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["environ"]['path+'][current_vars][key1])

            # path+ comm
            if(rawconfig["environ"]['path+'].has_key(key1)):
                if( isinstance(rawconfig["environ"]['path+'][key1], basestring) ):
                    rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["environ"]['path+'][key1])

            # project
            current_vars = rawconfig["project"]['current']
            if(rawconfig["project"][current_vars].has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["project"][current_vars][key1])

            # command
            current_vars = rawconfig["command"]['current']
            if(rawconfig["command"][current_vars].has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["command"][current_vars][key1])

            # store-named-variable
            if(rawconfig["store-named-variable"].has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["store-named-variable"][key1])

            # self
            if(rawconfig["store-named-command"].has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["store-named-command"][key1])

    # replace execute-stream's ${}
    # env env-current env-comm path-current path-comm project command store-named-variable store-named-command
    for (cmd, stream) in rawconfig["execute-stream"].items():
        #print (key) #...
        if (isinstance(stream, basestring)):
            continue

        step = 0
        for value in stream:
            startpos = 0
            while (True):
                # print (startpos)
                # print (value)

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
                    rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, env[key1])

                # env current
                current_vars = rawconfig["environ"]['current']
                if(rawconfig["environ"][current_vars].has_key(key1)):
                    rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["environ"][current_vars][key1])
                # env comm
                if(rawconfig["environ"].has_key(key1)):
                    if( isinstance(rawconfig["environ"][key1], basestring) ):
                        rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["environ"][key1])
                # path+ current
                current_vars = rawconfig["environ"]['path+']['current']
                if(rawconfig["environ"]['path+'][current_vars].has_key(key1)):
                    rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["environ"]['path+'][current_vars][key1])
                # path+ comm
                if(rawconfig["environ"]['path+'].has_key(key1)):
                    if( isinstance(rawconfig["environ"]['path+'][key1], basestring) ):
                        rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["environ"]['path+'][key1])
                # project
                current_vars = rawconfig["project"]['current']
                if(rawconfig["project"][current_vars].has_key(key1)):
                    rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["project"][current_vars][key1])

                # command
                current_vars = rawconfig["command"]['current']
                if(rawconfig["command"][current_vars].has_key(key1)):
                    rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["command"][current_vars][key1])

                # store-named-variable
                if(rawconfig["store-named-variable"].has_key(key1)):
                    rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["store-named-variable"][key1])

                # store-named-command
                if(rawconfig["store-named-command"].has_key(key1)):
                    rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig["store-named-command"][key1])

                # stream current
                key_pos = 0
                for key2 in stream:
                    if ( key2 == key1 ):
                        rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(key0, rawconfig['execute-stream'][cmd][key_pos])
                    key_pos+=1

            step += 1

    # expand execute-stream's command
    # store-named-command
    for (cmd, stream) in rawconfig["execute-stream"].items():
        #print (key) #...
        if (isinstance(stream, basestring)):
            continue
        step = 0
        for command in stream:
            if (rawconfig["store-named-command"].has_key(command)):
                rawconfig['execute-stream'][cmd][step] = rawconfig['execute-stream'][cmd][step].replace(command, rawconfig["store-named-command"][command])
            else:
                ''
                #print ("can't find command %s:%s" % ( cmd, command ))
            step += 1

    #list command
    while (True):
        if (args['list'] == True):

            if ( args['--raw'] == True ):
                list_config = rawconfig
            else:
                list_config = config


            if( args['--var'] == True):

                current_vars = list_config['environ']['current']
                dict0 = copy.deepcopy(list_config['environ'][current_vars])
                for (k, v) in list_config['environ'].items():
                    if(isinstance(v, basestring)):
                        dict0[k] = v

                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['--path'] == True):
                current_vars = list_config['environ']['path+']['current']
                dict0 = copy.deepcopy(list_config['environ']['path+'][current_vars])
                for (k, v) in list_config['environ']['path+'].items():
                    if(isinstance(v, basestring)):
                        if(k == "current"):
                            continue
                        dict0[k] = v

                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['--project'] == True):
                current_project_vars = list_config['project']['current']
                dict0 = copy.deepcopy(list_config['project'][current_project_vars])
                print ("current %s" % current_project_vars)
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )


            elif( args['--command'] == True):
                current_command_vars = list_config['command']['current']
                dict0 = copy.deepcopy(list_config['command'][current_command_vars])
                print ("current %s" % current_command_vars)
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['--value'] == True):
                dict0 = copy.deepcopy(list_config['store-named-variable'])
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )


            elif( args['--cmd'] == True):
                dict0 = copy.deepcopy(list_config['store-named-command'])
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['--stream'] == True):
                current_cmd_vars = list_config['execute-stream']['current']
                list0 = copy.deepcopy(list_config['execute-stream'][current_cmd_vars])
                print ("current %s" % current_cmd_vars)
                step = 1
                for v1 in list0:
                    print("%s: %s" % (step, v1))
                    step += 1

            return
        else:
            ''
        break

    # set into env
    # current env-variable
    current_env_vars = rawconfig["environ"]['current']
    for (key, value) in rawconfig["environ"][current_env_vars].items():
        env[key] = value

    # env-varible
    for (key, value) in config["environ"].items():
        if (not isinstance(value, basestring)):
            continue
        if (key == "current"):
            continue
        env[key] = value

    for (key, value) in env.items():
        #print ("%-24s %s" % (key, value) )
        ''

    # current path
    current_vars = rawconfig["environ"]['path+']['current']
    for (key, value) in rawconfig["environ"]["path+"][current_vars].items():
        env["PATH"] = value + os.path.pathsep + env["PATH"]

    # comm path
    for (key, value) in rawconfig["environ"]["path+"].items():
        if (not isinstance(value, basestring)):
            continue
        env["PATH"] = value + os.path.pathsep + env["PATH"]

    #print(env["PATH"].replace(os.path.pathsep, '\n'))

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
                            list0.append(cmd)
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
                #write_thread = threading.Thread(target=write_thread_function, args=(list0,))
                #write_thread.start()
                #time.sleep(1)

                for cmd in list0:
                    #print  ("command:%s" % cmd)
                    p.stdin.write(cmd + '\n')
                    p.stdin.flush()
                    #p.stdin.write("ping 127.0.0.1 -c 2 \n")
                    #p.stdin.flush()

                p.wait()
                #read_thread.close()
                #time.sleep(1)

                #return


            else:
                print ("stream-names is none")
        else:
            ''

        break

    return

if __name__ == '__main__':

    main_function()
