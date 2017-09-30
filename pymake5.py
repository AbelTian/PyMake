"""PyMake 5.0.

Usage:
  pymake5.py source [ --add | --del | --switch ] [ <config-file-name> ]
  pymake5.py source --mod <config-file-name> <new-config-file-name>
  pymake5.py source [ --show | --restore ]
  pymake5.py set value ( path | cmd | var | proj ) ( --add | --del | --mod ) <group> <name> [ <value> ]
  pymake5.py set current ( path | cmd | var | proj | exe ) ( --add | --del | --mod ) <name> [ <values> ... ]
  pymake5.py set working ( path | cmd | var | proj | exe ) <name>
  pymake5.py set store (--add | --del | --mod ) <name> [ <value> ]
  pymake5.py set stream (--add | --del | --mod ) <name> [ <values> ... ]
  pymake5.py list ( path | cmd | var | proj | store | exe ) [--raw] [<name>]
  pymake5.py exe [ <name> ]
  pymake5.py (-h | --help)
  pymake5.py --version

Command:
  source           switch to another source file
  set path         config work directory
  set cmd
  set var
  set proj         config project's pattern
  set current
  set working      switch to current env path project or stream
  set command
  set stream
  list             list configed values

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
import shutil
import time
import json
import copy
import types
from pycore.pycore import *
from pycore.docopt import docopt
from collections import OrderedDict

def main_function():

    d = {
        "path+": {
            "mac":{
                "dev-root": "/Users/abel/Develop"
            },

            "var-comm":{
                "src-root": "${dev-root}/a0-Developworkspace",
                "prod-root": "${dev-root}/b1-Product/a0-qqtbased/Application",
                "build-root": "${dev-root}/c0-buildstation",
                "tool-root": "${dev-root}/b0-toolskits",
                "test-root": "${dev-root}/a1-testspace",
                "webrc-root": "${dev-root}/b2-webrc"
            },

            "macOS": {
                "target-sdk": "${os-sdk}",
                "QtSDK": "${tool-root}/Libraries/QtLibraries/${QtVer}/${QtSDK}/bin",
                "cmake-path": "${tool-root}/compliers/${cmake-bin}",
                "make-and-toolchain-path": "${path-toolchain}"
            },

            "macJava":{
                "java-path":"${JAVA_HOME}/bin",
                "android-platform-tool":"${tool-root}/AndroidGroupLibraries/android-sdk-macosx/platform-tools",
                "ant-path":"${tool-root}/AndroidGroupLibraries/apache-ant-1.10.1/bin",
                "toolchain-path":"${tool-root}/AndroidGroupLibraries/android-ndk-r10/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/bin"
            },

            "mywin7":{

            }
        },

        "command":{
            "macgcc": {
                "mkdir": "mkdir -p",
                "cd": "cd",
                "deployqt": "macdeployqt",
                "make": "make"
            },
            "win-mingw32": {
                "cd": "cd /d",
                "make": "mingw32-make"
            }
        },

        "variable":{
            "PYCMD_MYNAME": "T.D.R",
            "a_special_var_const": "hello world",

            "mac":{
            },
            "var-comm":{
                "src-root": "${dev-root}/a0-Developworkspace",
                "prod-root": "${dev-root}/b1-Product/a0-qqtbased/Application",
                "build-root": "${dev-root}/c0-buildstation",
                "tool-root": "${dev-root}/b0-toolskits",
                "test-root": "${dev-root}/a1-testspace",
                "webrc-root": "${dev-root}/b2-webrc"
            },
            "ios": {
                "QtVer": "5.9.1",
                "QKIT": "iOS",
                "QtSDK": "ios",
                "QSYSNAME": "iOS",
                "BUILDTYPE": "Release",
                "QSYSNAME_BUILDTYPE": "${QSYSNAME}/${BUILDTYPE}",
                "os-sdk": "/Applications/Xcode.app/Contents/Developer/Platforms/xxxx.platform/Developer/SDKs/xxx.sdk/System/Library/Frameworks",
            },
            "macOS": {
                "QKIT": "macOS",
                "QtSDK": "clang_64",
                "QtVer": "5.9.1",
                "QSYSNAME": "MacOS",
                "BUILDTYPE": "Release",
                "cmake-bin": "CMake.app/Contents/bin",
                "path-toolchain": "/usr/bin",
                "QSYSNAME_BUILDTYPE": "${QSYSNAME}/${BUILDTYPE}",
                "QTDIR": "${tool-root}/Libraries/QtLibraries/${QtVer}/${QtSDK}",
                "os-sdk": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks",
            },
            "var-mac-comm":{
                "cmake-bin": "CMake.app/Contents/bin",
                "QSYSNAME_BUILDTYPE": "${QSYSNAME}/${BUILDTYPE}",
                "QTDIR": "${tool-root}/Libraries/QtLibraries/${QtVer}/${QtSDK}"
            },
            "macOS-Java":{
                "JAVA_HOME":"${dev-root}/b0-toolskits/AndroidGroupLibraries/java-macosx/Java/JavaVirtualMachines/jdk-9.jdk/Contents/Home",
                "CLASSPATH":".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar",
                "ANDROID_API_VERSION":"android-23",
                "ANDROID_SDK_ROOT":"${dev-root}/b0-toolskits/AndroidGroupLibraries/android-sdk-macosx",
                "ANDROID_NDK_ROOT":"${dev-root}/b0-toolskits/AndroidGroupLibraries/android-ndk-r13b",
                "ANDROID_NDK_HOST":"darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX":"arm-linux-androideabi",
                "ANDROID_NDK_TOOLCHAIN_VERSION":"4.9",
                "ANDROID_NDK_PLATFORM":"android-23",
                "NDK_TOOLCHAIN_PATH":"${dev-root}/b0-toolskits/AndroidGroupLibraries/android-ndk-r13b/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64",
                "NDK_TOOLS_PREFIX":"arm-linux-androideabi",
            },
            "a-group-0":{
                "app-bundle":"${prod-name}.app",
                "app-native":"${bin-path}/${app-bundle}/Contents/MacOS",
                "lib-native":"${bin-path}/${app-bundle}/Contents/Frameworks",
                "lib-bundle":"${prod-name}.framework"
            }
        },

        "project":{
            "qqt": {
                "prod-name": "QQt",
                "proj-name": "a0-qqtfoundation",
                "build-path": "${build-root}/${proj-name}/${QSYSNAME_BUILDTYPE}",
                "source-path": "${src-root}/${proj-name}",
                "qmake-file": "${proj-name}.pro",
                "bin-path": "${build-path}/src/bin"
            },
            "qqt-example":{
                "prod-name": "qqtframe",
                "proj-name": "a0-qqtfoundation",
                "source-path": "${src-root}/${proj-name}",
                "build-path": "${build-root}/${proj-name}/${QSYSNAME_BUILDTYPE}",
                "qmake-file": "${proj-name}.pro",
                "bin-path": "${build-path}/examples/${prod-name}/bin",
                "lib-dep":"${build-path}/src/bin/QQt.framework",
                "lib-dep-name":"QQt.framework/Versions/1/QQt"
            },
            "wiz": {
                "build-path": ""
            },
            "myfamily":{
                "":""
            },
            "android":{
                "install-path":"${tool-root}/AndroidGroupLibraries/android-sdk-macosx"
            },
            "QtOnAndroidProj":{
                "build-path":"${tool-root}/Libraries/QtLibraries/Source/qt5",
                "install-path":"${tool-root}/Libraries/QtLibraries/5.9.1/android6.0_armv7_mac"
            }
        },

        "store-command":{
            "current":{
                "path+":{
                    "mac":[
                        "mac",
                        "var-comm",
                        "macOS"
                    ],
                    "current":"mac"
                },
                "command":{
                    "a-group":[
                        "macgcc"
                    ],
                    "current":"a-group"
                },
                "env-variable":{
                    "a-group":[
                        "macOS"
                    ],
                    "current":"a-group"
                },
                "project":{
                    "a-group":[
                        "qqt-example"
                    ],
                    "current":"a-group"
                }
            },

            "why-to-set-these": "I'm not similar to these command, so list them here, rather than forgotten them",
            "here": "cl-command, sys-command",
            "here-1": "replace? no, append? easy!",

            "mk-build-path": "${mkdir} ${build-path}",
            "cd-build-path": "${cd} ${build-path}",
            "cd-prod-path": "${cd} ${prod-root}",
            "cd-bin-path":"${cd} ${bin-path}",
            "cd-install-path": "${cd} ${install-path}",

            "cmake": "cmake -G\"Unix Makefiles\" -DCMAKE_INSTALL_PREFIX=${prod-root} ${source-path}",
            "cmake-xcode": "cmake -GXCode -DCMAKE_INSTALL_PREFIX=${prod-root} ${source-path}",
            "cmake-rmcache": "rm -f CMakeCache.txt",

            "qmake": "qmake ${source-path}/${qmake-file} -spec macx-g++ CONFIG+=x86_64 && ${make} qmake_all",
            "make": "${make} -j4",
            "make-clean": "${make} clean in ${build-path}",
            "make-install": "${make} install",

            "deployqt": "${deployqt} ${bin-path}/${app-bundle} -verbose=1",
            "deployqt-dmg": "${deployqt} -dmg",
            "deployqt-help": "${deployqt} --help",

            "cp-dep": "cp -fr ${lib-dep} ${lib-native}",
            "install_name_tool": "install_name_tool -change ${lib-dep-name} @rpath/${lib-dep-name} ${app-native}/${prod-name} ",

            "pwd": "pwd",
            "var": "echo 'qtdir:' $QTDIR ",
            "var2": "echo 'qtdir:' ${QTDIR} ",
            "msg": "echo 'work complete!'"
        },

        "store-stream":{
            "t": [
                  "pwd",
                "pwd",
                "var",
                "var2",
                "pwd",
                "msg",
                "var2",
                "set ${build-path}",
                "macdeployqt --help"
            ],
            "build": [
                "mk-build-path",
                "cd-build-path",
                "qmake",
                "make",
                "msg"
            ],
            "macdeploy-qqt":[
                "cd-build-path",
                "deployqt",
                "cp-dep",
                "install_name_tool",
                "msg"
            ],
            "rebuild": [
                "mk-build-path",
                "cd-build-path",
                "qmake",
                "make-clean",
                "make",
                "deployqt",
                "cp-dep",
                "install_name_tool",
                "msg"
            ],
            "install": [
                "cd-build-path"
            ],
            "test-android":[
                "cd-install-path",
                "pwd",
                "which java",
                "java --version",
                "adb version",
                "ant"
            ],
            "qt-creator":[
                "\"/Applications/Qt Creator.app/Contents/MacOS/Qt Creator\""
            ],
            "QtOnAndroid":[
                "cd-build-path",
                "echo ./configure -prefix ${install-path} -hostprefix ${install-path} -xplatform android-g++ -release -nomake tests -nomake examples -android-ndk $ANDROID_NDK_ROOT -android-sdk $ANDROID_SDK_ROOT -android-ndk-host darwin-x86_64 -android-toolchain-version 4.9 -skip qtwebkit-examples -no-warnings-are-errors",
                "make",
                "make install"
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

    args = docopt(__doc__, version='pymake5.py v5.0')
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

    #set
    while (True):
        if (args['set'] == True):
            if( args['value'] is True):
                if (args['path'] is True):
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            config['path+'][args['<group>']][args['<name>']] = args["<value>"]
                            print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['path+'][args['<group>']].__contains__(args['<name>'])):
                                config['path+'][args['<group>']].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['path+'][args['<group>']].__contains__(args['<name>'])):
                                config['path+'][args['<group>']][args['<name>']] = args["<value>"]
                                print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['cmd'] is True):
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            config['command'][args['<group>']][args['<name>']] = args["<value>"]
                            print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['command'][args['<group>']].__contains__(args['<name>'])):
                                config['command'][args['<group>']].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['command'][args['<group>']].__contains__(args['<name>'])):
                                config['command'][args['<group>']][args['<name>']] = args["<value>"]
                                print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['var'] is True):
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            config['variable'][args['<group>']][args['<name>']] = args["<value>"]
                            print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['variable'][args['<group>']].__contains__(args['<name>'])):
                                config['variable'][args['<group>']].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['variable'][args['<group>']].__contains__(args['<name>'])):
                                config['variable'][args['<group>']][args['<name>']] = args["<value>"]
                                print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['proj'] is True):
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            config['project'][args['<group>']][args['<name>']] = args["<value>"]
                            print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['project'][args['<group>']].__contains__(args['<name>'])):
                                config['project'][args['<group>']].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['project'][args['<group>']].__contains__(args['<name>'])):
                                config['project'][args['<group>']][args['<name>']] = args["<value>"]
                                print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
            elif ( args['current'] is True ):
                if (args['path'] is True):
                    if (args['--add'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            config["store-current"]["path+"][args['<name>']] = args["<values>"]
                            print ( "successed %s:%s" % (args['<name>'],args[ "<values>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args["<name>"] is not None):
                            if (config["store-current"]["path+"].__contains__(args['<name>'])):
                                config["store-current"]["path+"].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            if (config["store-current"]["path+"].__contains__(args['<name>'])):
                                config["store-current"]["path+"][args['<name>']] = args["<values>"]
                                print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['cmd'] is True):
                    if (args['--add'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            config["store-current"]["command"][args['<name>']] = args["<values>"]
                            print ( "successed %s:%s" % (args['<name>'],args[ "<values>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args["<name>"] is not None):
                            if (config["store-current"]["command"].__contains__(args['<name>'])):
                                config["store-current"]["command"].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            if (config["store-current"]["command"].__contains__(args['<name>'])):
                                config["store-current"]["command"][args['<name>']] = args["<values>"]
                                print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['var'] is True):
                    if (args['--add'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            config["store-current"]["variable"][args['<name>']] = args["<values>"]
                            print ( "successed %s:%s" % (args['<name>'],args[ "<values>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args["<name>"] is not None):
                            if (config["store-current"]["variable"].__contains__(args['<name>'])):
                                config["store-current"]["variable"].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            if (config["store-current"]["variable"].__contains__(args['<name>'])):
                                config["store-current"]["variable"][args['<name>']] = args["<values>"]
                                print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['proj'] is True):
                    if (args['--add'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            config["store-current"]["project"][args['<name>']] = args["<values>"]
                            print ( "successed %s:%s" % (args['<name>'],args[ "<values>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args["<name>"] is not None):
                            if (config["store-current"]["project"].__contains__(args['<name>'])):
                                config["store-current"]["project"].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            if (config["store-current"]["project"].__contains__(args['<name>'])):
                                config["store-current"]["project"][args['<name>']] = args["<values>"]
                                print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                elif (args['exe'] is True):
                    if (args['--add'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            config["store-current"]["execute"][args['<name>']] = args["<values>"]
                            print ( "successed %s:%s" % (args['<name>'],args[ "<values>"]))
                        else:
                            ''
                    elif (args['--del'] == True):
                        if (args["<name>"] is not None):
                            if (config["store-current"]["execute"].__contains__(args['<name>'])):
                                config["store-current"]["execute"].__delitem__(args['<name>'])
                                print ("successed %s" % (args['<name>']))
                            else:
                                ''
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<name>'] and args["<values>"] is not None):
                            if (config["store-current"]["execute"].__contains__(args['<name>'])):
                                config["store-current"]["execute"][args['<name>']] = args["<values>"]
                                print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                            else:
                                ''
                        else:
                            ''
                    else:
                        ''
                else:
                    ''
            elif ( args['working'] is True ):
                if (args['path'] is True):
                    config["store-current"]["path+"]['current'] = args["<name>"]
                    print ("successed %s" % (args['<name>']))
                elif (args['cmd'] is True):
                    config["store-current"]["command"]['current'] = args["<name>"]
                    print ("successed %s" % (args['<name>']))
                elif (args['var'] is True):
                    config["store-current"]["variable"]['current'] = args["<name>"]
                    print ("successed %s" % (args['<name>']))
                elif (args['proj'] is True):
                    config["store-current"]["project"]['current'] = args["<name>"]
                    print ("successed %s" % (args['<name>']))
                elif (args['exe'] is True):
                    config["store-current"]["execute"]['current'] = args["<name>"]
                    print ("successed %s" % (args['<name>']))
                else:
                    ''
            elif (args['store'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config['store-command'][args['<name>']] = args["<value>"]
                        print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['store-command'].__contains__(args['<name>'])):
                            config['store-command'].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['store-command'].__contains__(args['<name>'])):
                            config['store-command'][args['<name>']] = args["<value>"]
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
                        config["store-stream"][args['<name>']] = args["<values>"]
                        print ("successed %s:%s" % (args['<name>'],args["<values>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['store-stream'].__contains__(args['<name>'])):
                            config["store-stream"].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["store-stream"][args['<name>']] = args["<values>"]
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

    ### config -> raw config
    rawconfig = copy.deepcopy(config)
    # print ( config )
    # print ( rawconfig )

    # replace path+ 's ${...}
    # path+
    current_vars = rawconfig["store-current"]['path+']["current"]
    for ( name ) in rawconfig['store-current']['path+'][current_vars]:
        for (key, value) in rawconfig["path+"][name].items():
            #print (key) #...

            startpos = 0
            while (True):
                #print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                #print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                #print ( key1 ) #...

                # find in up of this name and self
                for ( finding ) in rawconfig['store-current']["path+"][current_vars]:
                    if(rawconfig["path+"][finding].has_key(key_from)):
                        rawconfig["path+"][name][key] = rawconfig["path+"][name][key].replace(key_replace, rawconfig["path+"][finding][key_from])
                    if( finding == name ):
                        break;

    # replace command 's ${...}
    # command
    current_vars = rawconfig["store-current"]['command']["current"]
    for ( name ) in rawconfig['store-current']['command'][current_vars]:
        for (key, value) in rawconfig["command"][name].items():
            #print (key) #...

            startpos = 0
            while (True):
                #print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                #print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                #print ( key1 ) #...

                # find in up of this name and self
                for ( finding ) in rawconfig['store-current']["command"][current_vars]:
                    if(rawconfig["command"][finding].has_key(key_from)):
                        rawconfig["command"][name][key] = rawconfig["command"][name][key].replace(key_replace, rawconfig["command"][finding][key_from])
                    if( finding == name ):
                        break;

    # replace variable 's ${...}
    # variable
    current_vars = rawconfig["store-current"]['variable']["current"]
    for ( name ) in rawconfig['store-current']['variable'][current_vars]:
        for (key, value) in rawconfig["variable"][name].items():
            #print (key) #...

            startpos = 0
            while (True):
                #print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                #print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                #print ( key1 ) #...

                # find in up of this name and self
                for ( finding ) in rawconfig['store-current']["variable"][current_vars]:
                    if(rawconfig["variable"][finding].has_key(key_from)):
                        rawconfig["variable"][name][key] = rawconfig["variable"][name][key].replace(key_replace, rawconfig["variable"][finding][key_from])
                    if( finding == name ):
                        break;

    # replace project 's ${...}
    # project
    current_vars = rawconfig["store-current"]['project']["current"]
    for ( name ) in rawconfig['store-current']['project'][current_vars]:
        for (key, value) in rawconfig["project"][name].items():
            #print (key) #...

            startpos = 0
            while (True):
                #print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                #print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                #print ( key1 ) #...

                # find in up of this name and self
                for ( finding ) in rawconfig['store-current']['project'][current_vars]:
                    if(rawconfig["project"][finding].has_key(key_from)):
                        rawconfig["project"][name][key] = rawconfig["project"][name][key].replace(key_replace, rawconfig["project"][finding][key_from])
                    if( finding == name ):
                        break;

    # replace store-command's ${...}
    # path+ command variable project store-command
    for (key, value) in rawconfig["store-command"].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key_replace = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key_from = key_replace.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...

            # find in path+
            current_vars = rawconfig["store-current"]['path+']["current"]
            for ( finding ) in rawconfig['store-current']['path+'][current_vars]:
                if(rawconfig["path+"][finding].has_key(key_from)):
                    rawconfig["store-command"][key] = rawconfig['store-command'][key].replace(key_replace, rawconfig["path+"][finding][key_from])

            # find in command
            current_vars = rawconfig["store-current"]['command']["current"]
            for ( finding ) in rawconfig['store-current']['command'][current_vars]:
                if(rawconfig["command"][finding].has_key(key_from)):
                    rawconfig["store-command"][key] = rawconfig['store-command'][key].replace(key_replace, rawconfig["command"][finding][key_from])

            # find in variable
            current_vars = rawconfig["store-current"]['variable']["current"]
            for ( finding ) in rawconfig['store-current']['variable'][current_vars]:
                if(rawconfig["variable"][finding].has_key(key_from)):
                    rawconfig["store-command"][key] = rawconfig['store-command'][key].replace(key_replace, rawconfig["variable"][finding][key_from])

            # find in project
            current_vars = rawconfig["store-current"]['project']["current"]
            for ( finding ) in rawconfig['store-current']['project'][current_vars]:
                if(rawconfig["project"][finding].has_key(key_from)):
                    rawconfig["store-command"][key] = rawconfig['store-command'][key].replace(key_replace, rawconfig["project"][finding][key_from])

            # self
            if(rawconfig["store-command"].has_key(key_from)):
                rawconfig["store-command"][key] = rawconfig["store-command"][key].replace(key_replace, rawconfig["store-command"][key_from])

    # replace store-stream's ${}
    # path+ command variable project command
    for (cmd, stream) in rawconfig["store-stream"].items():
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

                key_replace = value[index:index2 + 1]
                #print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                #print ( key1 ) #...

                # find in path+
                current_vars = rawconfig["store-current"]['path+']["current"]
                for ( finding ) in rawconfig['store-current']['path+'][current_vars]:
                    if(rawconfig["path+"][finding].has_key(key_from)):
                        rawconfig['store-stream'][cmd][step] = rawconfig['store-stream'][cmd][step].replace(key_replace, rawconfig["path+"][finding][key_from])

                # find in command
                current_vars = rawconfig["store-current"]['command']["current"]
                for ( finding ) in rawconfig['store-current']['command'][current_vars]:
                    if(rawconfig["command"][finding].has_key(key_from)):
                        rawconfig['store-stream'][cmd][step] = rawconfig['store-stream'][cmd][step].replace(key_replace, rawconfig["command"][finding][key_from])

                # find in variable
                current_vars = rawconfig["store-current"]['variable']["current"]
                for ( finding ) in rawconfig['store-current']['variable'][current_vars]:
                    if(rawconfig["variable"][finding].has_key(key_from)):
                        rawconfig['store-stream'][cmd][step] = rawconfig['store-stream'][cmd][step].replace(key_replace, rawconfig["variable"][finding][key_from])

                # find in project
                current_vars = rawconfig["store-current"]['project']["current"]
                for ( finding ) in rawconfig['store-current']['project'][current_vars]:
                    if(rawconfig["project"][finding].has_key(key_from)):
                        rawconfig['store-stream'][cmd][step] = rawconfig['store-stream'][cmd][step].replace(key_replace, rawconfig["project"][finding][key_from])

            step += 1

    # expand store-stream's command
    # store-command
    for (cmd, stream) in rawconfig["store-stream"].items():
        #print (key) #...
        if (isinstance(stream, basestring)):
            continue
        step = 0
        for command in stream:
            if (rawconfig["store-command"].has_key(command)):
                rawconfig['store-stream'][cmd][step] = rawconfig['store-stream'][cmd][step].replace(command, rawconfig["store-command"][command])
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

            if( args['path'] == True):
                current_vars = list_config['store-current']['path+']['current']
                print ("group %s" % current_vars)
                for current_group in list_config['store-current']['path+'][current_vars]:
                    dict0 = copy.deepcopy(list_config['path+'][current_group])
                    for (k, v) in dict0.items():
                        print("%-24s %s" % (k, v) )

            elif( args['cmd'] == True):
                current_vars = list_config['store-current']['command']['current']
                print ("group %s" % current_vars)
                for current_group in list_config['store-current']['command'][current_vars]:
                    dict0 = copy.deepcopy(list_config['command'][current_group])
                    for (k, v) in dict0.items():
                        print("%-24s %s" % (k, v) )

            elif( args['var'] == True):
                current_vars = list_config['store-current']['variable']['current']
                print ("group %s" % current_vars)
                for current_group in list_config['store-current']['variable'][current_vars]:
                    dict0 = copy.deepcopy(list_config['variable'][current_group])
                    for (k, v) in dict0.items():
                        print("%-24s %s" % (k, v) )

            elif( args['proj'] == True):
                current_vars = list_config['store-current']['project']['current']
                print ("group %s" % current_vars)
                for current_group in list_config['store-current']['project'][current_vars]:
                    dict0 = copy.deepcopy(list_config['project'][current_group])
                    for (k, v) in dict0.items():
                        print("%-24s %s" % (k, v) )

            elif( args['store'] == True):
                dict0 = copy.deepcopy(list_config['store-command'])
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['exe'] == True):
                current_vars = list_config['store-current']["execute"]['current']
                if(args['<name>'] is not None):
                    current_vars = args['<name>']
                print ("group %s" % current_vars)
                list0 = []
                for current_group in list_config['store-current']['execute'][current_vars]:
                    list0.extend(copy.deepcopy(list_config['store-stream'][current_group]))
                step = 1
                for v1 in list0:
                    print("%-3s %s" % (step, v1))
                    step += 1

            return
        else:
            ''
        break

    # set into env
    env = os.environ
    # variable
    current_vars = rawconfig["store-current"]['variable']['current']
    for ( name ) in rawconfig["store-current"]['variable'][current_vars]:
        for (key, value) in rawconfig["variable"][name].items():
            env[key] = value

    for (key, value) in env.items():
        #print ("%-24s %s" % (key, value) )
        ''

    # path+
    current_vars = rawconfig["store-current"]['path+']['current']
    for ( name ) in rawconfig["store-current"]['path+'][current_vars]:
        for (key, value) in rawconfig["path+"][name].items():
            env["PATH"] = value + os.path.pathsep + env["PATH"]

    #print(env["PATH"].replace(os.path.pathsep, '\n'))

    while ( True ):
        if( args['exe'] == True):
            current_vars = rawconfig['store-current']["execute"]['current']
            if(args['<name>'] is not None):
                current_vars = args['<name>']
            #print ("group %s" % current_vars)
            list0 = []
            for current_group in rawconfig['store-current']['execute'][current_vars]:
                list0.extend(copy.deepcopy(rawconfig['store-stream'][current_group]))

            communicateWithCommandLine(list0)
            os._exit(0)
            return
        else:
            ''
        break

    return

if __name__ == '__main__':

    main_function()
