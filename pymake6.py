# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyMake 6.0.

Usage:
  pymake6.py source
  pymake6.py source root [ <source-root-path> ]
  pymake6.py source config [ --add | --del | --mod | --switch | --restore | --show ] [ <config-file-name> ] [<new-config-file-name>]
  pymake6.py set env cur <name>
  pymake6.py set env [ path ] ( --add | --del | --mod ) <group> <name> [ <value> ]
  pymake6.py set cmd (--add | --del | --mod ) <name> [ <values> ... ]
  pymake6.py set ( path | var ) ( --add | --del | --mod ) <name> [ <value> ]
  pymake6.py list ( path | var | env | cmd ) [--raw]
  pymake6.py j <name>
  pymake6.py (-h | --help)
  pymake6.py --version

Command:
  source           switch to another source file
  set path         path assessblage
  set var          var assessblage
  set env          env set
  set cmd          set cmd stream
  list             list configed values

Options:
  -h --help     Show this screen.
  --version     Show version.
  --add
  --del
  --mod         add or delete or modify a config or path
  --switch      switch to another source
  --show        display haved stream config files
  --restore     reset to pymake.json stream config file
  --raw         absolute the config values
"""

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
from colorama import init, Fore, Back, Style

def main_function():
    init(autoreset=True)

    d = {
        "path-assemblage":{
            "root":"/Users/abel/Develop",
            "root.src": "${root}/a0-develop",
            "root.prod": "${root}/b1-product",
            "root.tool": "${root}/b0-toolskits",
            "root.build": "${root}/c0-buildstation",
            "root.test": "${root}/c1-test",
            "root.webrc": "${root}/c2-webrc",
            "root.c":"${root.tool}/compiler",
            "root.qt":"${root.tool}/macLibraries/Qt",
            "root.android": "${root.tool}/macAndroidLibraries",
            "root.android.sdk": "${root.android}/android-sdk-macosx/platform-tools",
            "root.android.ndk": "${root.android}/android-ndk-r13b",
            "root.android.ant": "${root.android}/apache-ant-1.10.1",
            "root.android.java": "${root.android}/java-macosx/Java/JavaVirtualMachines",
            "cmake": "${root.c}/CMake.app/Contents",

            "qt5.9.clang": "${root.qt}/5.9.1/clang_64",
            "qt5.8.android_x86": "${root.qt}/5.8/android_x86",
            "qt5.8.android_arm": "${root.qt}/5.8/android_armv7",
            "qt5.8.clang": "${root.qt}/5.8/clang_64",
            "qt5.8.ios": "${root.qt}/5.8/ios",
            "qt4.8.clang": "${root.qt}/4.8.7/clang_64",

            "qt5.9.clang.bin":"${qt5.9.clang}/bin",
            "qt5.8.android_x86.bin": "${qt5.8.android_x86}/bin",
            "qt5.8.android_arm.bin": "${qt5.8.android_arm}/bin",
            "qt5.8.clang.bin": "${qt5.8.clang}/bin",
            "qt5.8.ios.bin": "${qt5.8.ios}/bin",
            "qt4.8.clang.bin": "${qt4.8.clang}/bin",

            "java1.7.home": "${root.android.java}/jdk1.7.0_79.jdk/Contents/Home",
            "java1.8.home": "${root.android.java}/jdk1.8.0_111.jdk/Contents/Home",
            "java1.9.home": "${root.android.java}/jdk9.jdk/Contents/Home",
            "java1.7.bin": "${java1.7.home}/bin",
            "java1.8.bin": "${java1.8.home}/bin",
            "java1.9.bin": "${java1.9.home}/bin",
            "ant.bin": "${root.android.ant}/bin",
            "ndk.arm": "${root.android.ndk}/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64",
            "ndk.x86": "${root.android.ndk}/toolchains/x86-4.9/prebuilt/darwin-x86_64",
            "ndk.x86_64": "${root.android.ndk}/toolchains/x86_64-4.9/prebuilt/darwin-x86_64",
            "ndk.arm.bin": "${ndk.arm}/bin",
            "ndk.x86.bin": "${ndk.x86}/bin",
            "ndk.x86_64.bin": "${ndk.x86_64}/bin",
            "mac.sdk.lib": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks"
        },
        "variable-assemblage":{
            "qt.sys.mac":"MacOS",
            "qt.sys.android.x86_64":"Android-x86_64",
            "qt.sys.android.x86":"Android",
            "qt.sys.android.arm":"Android-arm",
            "build.debug":"Debug",
            "build.release":"Release",

            "qqt.prod.name": "QQt",
            "qqt.proj.name": "a0-qqtfoundation",
            "qqt.build.path": "${root.build}/${qqt.proj.name}/${qt.sys.mac}/${build.release}",
            "qqt.source.path": "${root.src}/${qqt.proj.name}",
            "qqt.proj.qmake": "${qqt.proj.name}.pro",
            "qqt.prod.path": "${qqt.build.path}/src/bin",
            "qqt.install.path": "${root.prod}/QQt",

            "qqtframe.prod.name":"qqtframe",
            "qqtframe.bin.path": "${qqt.build.path}/examples/${qqtframe.prod.name}/bin",
            "qqtframe.dep1": "${qqt.build.path}/src/bin/QQt.framework",
            "qqtframe.dep1.name": "QQt.framework/Versions/1/QQt",

            "qt5.source": "${root.tool}/Source/qt5",

            "mac.app": "${prod.name}.app",
            "mac.app.content": "${mac.app}/Contents",
            "mac.app.macos": "${mac.app.content}/MacOS",
            "mac.app.framework": "${mac.app.content}/Frameworks",
            "mac.app.res": "${mac.app.content}/Resources",
            "mac.app.plugin": "${mac.app.content}/PlugIns",
            "mac.framework": "${prod.name}.framework",
            "mac.framework.ver": "${prod.name}.framework/Versions",
            "mac.framework.res": "${prod.name}.framework/Resources",
            "qt.deploy.android":"androiddeployqt",
            "qt.deploy.mac":"macdeployqt"
        },
        "command-assemblage": [
            "I'm not similar to these command, so list them here, rather than forgotten them",
            "cl-command, sys-command",
            "replace? no, append? easy!",
            "help you to remeber these command."
            "mkdir -p ${qqt.build.path}",
            "cd ${build-path}",
            "cmake -G\"Unix Makefiles\" -DCMAKE_INSTALL_PREFIX=${prod-root} ${source-path}",
            "cmake -GXCode -DCMAKE_INSTALL_PREFIX=${prod-root} ${source-path}",
            "rm -f CMakeCache.txt",
            "qmake ${source-path}/${qmake-file} -spec ${QTSPEC} CONFIG+=${QTCONFIG} && make qmake_all",
            "make -j4",
            "make clean in ${build-path}",
            "make install",
            "${deployqt} ${bin-path}/${app-bundle} -verbose=1",
            "${deployqt} -dmg",
            "${deployqt} --help",
            "cp -fr ${lib-dep} ${lib-native}",
            "install_name_tool -change ${lib-dep-name} @rpath/${lib-dep-name} ${app-native}/${prod-name} ",
            "install_name_tool -change $LibDep @rpath/$LibDep ${app-native}/${prod-name} ",
            "${source-path}/configure -prefix ${install-path} -hostprefix ${install-path} -xplatform android-g++ -release -nomake tests -nomake examples -android-ndk $ANDROID_NDK_ROOT -android-sdk $ANDROID_SDK_ROOT -android-ndk-host $ANDROID_NDK_HOST -android-toolchain-version $ANDROID_NDK_TOOLCHAIN_VERSION -skip qtwebkit-examples -no-warnings-are-errors"
        ],
        "environ": {
            "qt.android.mobile":{
                "path+": [
                    "${cmake.bin}",
                    "${qt5.8.android_arm.bin}",
                    "$(mac.java1.8.bin)",
                    "${mac.android.sdk}",
                    "${mac.ant.bin}",
                    "${mac.ndk.arm.bin}"
                ],
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_SDK_ROOT": "${mac.android.sdk}",
                "ANDROID_NDK_ROOT": "${mac.ndk.root}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "arm-linux-androideabi",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_PLATFORM": "android-23",
                "NDK_TOOLCHAIN_PATH": "${mac.ndk.arm.bin}",
                "NDK_TOOLS_PREFIX": "arm-linux-androideabi",

                "PYCMD_MYNAME": "T.D.R",
                "a_special_var_const": "hello world",
                "QKIT": "Android",
                "QTDIR": "${qt5.8.android_arm}",
                "QTSPEC": "android-g++",
                "QTCONFIG": "arm",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar"

            },
            "qt.android":{
                "path+": [
                    "${cmake.bin}",
                    "${qt5.8.android_x86.bin}",
                    "$(mac.java1.8.bin)",
                    "${mac.android.sdk}",
                    "${mac.ant.bin}",
                    "${mac.ndk.arm.bin}"
                ],
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_SDK_ROOT": "${mac.android.sdk}",
                "ANDROID_NDK_ROOT": "${mac.ndk.root}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "arm-linux-androideabi",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_PLATFORM": "android-23",
                "NDK_TOOLCHAIN_PATH": "${mac.ndk.arm.bin}",
                "NDK_TOOLS_PREFIX": "arm-linux-androideabi",

                "PYCMD_MYNAME": "T.D.R",
                "a_special_var_const": "hello world",
                "QKIT": "Android",
                "QTDIR": "${qt5.8.android_arm}",
                "QTSPEC": "android-g++",
                "QTCONFIG": "arm",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar"

            },
            "current":"qt.android.mobile"
        },
        "command":{
            "qqt.build":[
                "mkdir -p ${qqt.path.build}",
                "cd ${qqt.path.build}",
                "qmake ${qqt.path.source}/${qqt.qmake} -spec ${QTSPEC} CONFIG+=${QTCONFIG} && make qmake_all",
                "make -j4"
            ],
            "qqt.rebuild":[
                "cd ${qqt.path.build}",
                "make clean",
                "${build.qqt}"
            ],
            "qqt.clean":[
                "cd ${qqt.path.build}",
                "make clean",
                "echo success"
            ],
            "qqt.install":[
                "cd ${qqt.path.build}",
                "make install",
                "echo success"
            ],
            "qqtframe.deploy":[
                "cd-build-path",
                "deployqt",
                "cp-dep",
                "install_name_tool",
                "msg"
            ],
            "qt-creator": [
                "\"/Applications/Qt Creator.app/Contents/MacOS/Qt Creator\""
            ],
            "build-qt5-android": [
                "mk-build-path",
                "cd-build-path",
                "configure-qt5-android",
                "make",
                "make install"
            ]
        }
    }


    """
    [pymake]
    [source]
    root = ~/.pymake
    config = pymake.json
    """
    userroot = getuserroot()
    pymakeroot = userroot + os.path.sep + '.pymake'
    if (not os.path.exists(pymakeroot)):
        os.makedirs(pymakeroot)

    #initial pymake.ini
    pymakeini = pymakeroot + os.path.sep + 'pymake.ini'
    conf = MyConfigParser()
    conf.read(pymakeini)
    if( not conf.has_section('pymake') ):
        conf.add_section('pymake')
        conf.write(open(pymakeini, 'w'))
    if( not conf.has_section('source') ):
        conf.add_section('source')
        conf.write(open(pymakeini, 'w'))
    if( not conf.has_option('source', 'root') ):
        conf.set('source', 'root', pymakeroot)
        conf.write(open(pymakeini, 'w'))
    if(not conf.has_option('source', 'config')):
        conf.set('source', 'config', 'pymake.json')
        conf.write(open(pymakeini, 'w'))

    sourceroot = conf.get('source', 'root')
    os.chdir(sourceroot)
    if (os.path.abspath(sourceroot) == os.path.abspath(pymakeroot)):
        print("I checked you use pymakeroot to be sourceroot, suggest you use source command changing one.")

    args = docopt(__doc__, version='pymake6.py v6.0')
    #print(args)

    pymakesuffix = '.json'
    while (True):
        if(args['source'] is True):
            if(args['root'] is True):
                if ( args['<source-root-path>'] is not None):
                    conf.set('source', 'root', args['<source-root-path>'])
                    conf.write(open(pymakeini, 'w'))
                    print ("success root: %s" % args['<source-root-path>'])
                else:
                    print ("root: %s" % sourceroot)
            elif(args['config'] is True):
                if(args['--del'] is True):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'] == 'pymake.json'):
                        print('You can\'t remove pymake\'s file...')
                    elif (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix)):
                        os.remove(args['<config-file-name>'])
                        conf.set('source', 'config', 'pymake.json')
                        conf.write(open(pymakeini, 'w'))
                        print ("success: %s" % args['<config-file-name>'])
                    else:
                        print ('You can\'t remove pymake.json and un.json\'s file...')
                elif(args['--add'] is True):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix) and args['<config-file-name>'] != 'pymake.json'):
                        f = conf.get('source', 'config')
                        if( f != args['<config-file-name>']):
                            shutil.copyfile(f, args['<config-file-name>'])
                            conf.set('source', 'config', args['<config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                            print ("success: %s" % args['<config-file-name>'])
                        else:
                            print('You can\'t add same named file...')
                    else:
                        print ('You can\'t add pymake.json and un.json\'s file...')
                elif (args['--mod'] is True):
                    if ( ( args['<config-file-name>'] and args['<new-config-file-name>']) is not None and args['<config-file-name>'].endswith(pymakesuffix)):
                        os.rename(args['<config-file-name>'],args['<new-config-file-name>'])
                        f = conf.get('source', 'config')
                        if (f == args['<config-file-name>']):
                            conf.set('source', 'config',args['<new-config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                        print ("success: %s" % args['<new-config-file-name>'])
                    else:
                        print ('You can\'t mod pymake.json and un.json\'s file...')
                elif(args['--show'] is True):
                    files = os.listdir(os.getcwd())
                    for f in files:
                        if (f.endswith(pymakesuffix)):
                            print(f)
                elif(args['--restore'] is True):
                    conf.set('source', 'config', 'pymake.json')
                    conf.write(open(pymakeini, 'w'))
                    print ("success: %s" % 'pymake.json')
                elif (args['--switch'] is True or ( args['<config-file-name>'] is not None )):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix) ):
                        if (os.path.exists(args['<config-file-name>'])):
                            conf.set('source', 'config', args['<config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                            print("switch to source config: %s" % args['<config-file-name>'])
                        else:
                            print("source file %s isn't exists, please --add it" % args['<config-file-name>'])
                    else:
                        print ('You can\'t switch pymake.json and un.json\'s file...')
                else:
                    print ("conf: %s" % conf.get("source", "config"))
            else:
                r = conf.get('source', 'root')
                f = conf.get('source', 'config')
                print ("root: %s" % (r))
                print ("conf: %s" % (f))
            return
        else:
            ''
        break

    file = conf.get('source', 'config')
    #print ("root: %s config: %s" % (sourceroot, file))
    print("use source config: %s/%s" % (sourceroot, file) )

    if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)):
        if (not os.path.exists('pymake.json')):
            writeJsonData('pymake.json', d)
        if(not os.path.exists(file)):
            return

    config = readJsonData(file)
    #print(config)

    #set
    while (True):
        if (args['set'] == True):
            if (args['env'] is True):
                if (args['cur'] == True):
                    if (args["<name>"] is not None):
                        config["environ"]["current"] = args["<name>"]
                        print("successed %s" % (args['<name>']))
                    else:
                        ""
                elif (args["path"] is True):
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] is not None):
                            config['environ'][args['<group>']]["path+"].append(args["<name>"])
                            print ("successed %s:%s" % (args['<group>'], args['<name>']))
                        else:""
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['environ'][args['<group>']]["path+"].__contains__(args['<name>'])):
                                config['environ'][args['<group>']]["path+"].__delitem__(args['<name>'])
                                print("successed %s:%s" % (args['<group>'], args['<name>']))
                            else:
                                print("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['variable'][args['<group>']]["path+"].__contains__(args['<name>'])):
                                index = config['variable'][args['<group>']]["path+"].index(args['<name>'])
                                config['variable'][args['<group>']]["path+"][index] = [args['<name>']]
                                print("successed %s:%s" % (args['<group>'], args['<name>']))
                            else:
                                print("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                else:
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            config['environ'][args['<group>']][args['<name>']] = args["<value>"]
                            print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            print ("failed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['variable'][args['<group>']].__contains__(args['<name>'])):
                                config['variable'][args['<group>']].__delitem__(args['<name>'])
                                print ("successed %s:%s" % (args['<group>'], args['<name>']))
                            else:
                                print ("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['variable'][args['<group>']].__contains__(args['<name>'])):
                                config['variable'][args['<group>']][args['<name>']] = args["<value>"]
                                print ("successed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                print ("failed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            ''
                    else:
                        ''
            elif (args['cmd'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["command"][args['<name>']] = args["<values>"]
                        print("successed %s:%s" % (args['<name>'], args["<values>"]))
                    else:
                        print("failed %s:%s" % (args['<name>'], args["<values>"]))
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['command'].__contains__(args['<name>'])):
                            config["command"].__delitem__(args['<name>'])
                            print("successed %s" % (args['<name>']))
                        else:
                            print("failed %s" % (args['<name>']))
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["command"][args['<name>']] = args["<values>"]
                        print("successed %s:%s" % (args['<name>'], args["<values>"]))
                    else:
                        print("failed %s:%s" % (args['<name>'], args["<values>"]))
                else:
                    ''
            elif (args['path'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config['path-assemblage'][args['<name>']] = args["<value>"]
                        print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                    else:
                        print ("failed %s:%s" % (args['<name>'], args["<value>"]))
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['path-assemblage'].__contains__(args['<name>'])):
                            config['path-assemblage'].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            print ("failed %s" % (args['<name>']))
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['path-assemblage'].__contains__(args['<name>'])):
                            config['path-assemblage'][args['<name>']] = args["<value>"]
                            print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                        else:
                            print ("failed %s:%s" % (args['<name>'], args["<value>"]))
                    else:
                        ''
                else:
                    ''
            elif (args['var'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config['variable-assemblage'][args['<name>']] = args["<value>"]
                        print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                    else:
                        print ("failed %s:%s" % (args['<name>'], args["<value>"]))
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['variable-assemblage'].__contains__(args['<name>'])):
                            config['variable-assemblage'].__delitem__(args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            print ("failed %s" % (args['<name>']))
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['variable-assemblage'].__contains__(args['<name>'])):
                            config['variable-assemblage'][args['<name>']] = args["<value>"]
                            print ("successed %s:%s" % (args['<name>'], args["<value>"]))
                        else:
                            print ("failed %s:%s" % (args['<name>'], args["<value>"]))
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

    #replace path
    for (key, value) in rawconfig["path-assemblage"].items():
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

            for (find_key, find_value) in rawconfig["path-assemblage"].items():
                if (key == find_key):
                    break
                if (find_key == key_from):
                    rawconfig["path-assemblage"][key] = rawconfig["path-assemblage"][key].replace(
                        key_replace, rawconfig["path-assemblage"][key_from])
                    #print("xxx %s" % rawconfig["path-assemblage"][key])
                    break

    #replace var
    #from path var
    for (key, value) in rawconfig["variable-assemblage"].items():
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

            for (find_key, find_value) in rawconfig["path-assemblage"].items():
                if (find_key == key_from):
                    rawconfig["variable-assemblage"][key] = rawconfig["variable-assemblage"][key].replace(
                        key_replace, rawconfig["path-assemblage"][key_from])
                    break

            for (find_key, find_value) in rawconfig["variable-assemblage"].items():
                if (key == find_key):
                    break
                if (find_key == key_from):
                    rawconfig["variable-assemblage"][key] = rawconfig["variable-assemblage"][key].replace(
                        key_replace, rawconfig["variable-assemblage"][key_from])
                    break

    #replace env
    #from path var env
    current_var = rawconfig["environ"]["current"]
    #replace path+
    step = 0
    for value in rawconfig["environ"][current_var]['path+']:
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
            # print ( key0 ) #${...}
            key_from = key_replace.split('{')[1].split('}')[0].strip()
            # print ( key1 ) #...

            for (find_key, find_value) in rawconfig["path-assemblage"].items():
                if (find_key == key_from):
                    rawconfig["environ"][current_var]['path+'][step] = rawconfig["environ"][current_var]['path+'][step].replace(
                        key_replace, rawconfig["path-assemblage"][key_from])
                    break

            for (find_key, find_value) in rawconfig["variable-assemblage"].items():
                if (find_key == key_from):
                    rawconfig["environ"][current_var]['path+'][step] = rawconfig["environ"][current_var]['path+'][step].replace(
                        key_replace, rawconfig["variable-assemblage"][key_from])
                    break
        step += 1

    for (key, value) in rawconfig["environ"][current_var].items():
        #print (key) #...
        if(key == "path+"):
            continue

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

            for (find_key, find_value) in rawconfig["path-assemblage"].items():
                if (find_key == key_from):
                    rawconfig["environ"][current_var][key] = rawconfig["environ"][current_var][key].replace(
                        key_replace, rawconfig["path-assemblage"][key_from])
                    break

            for (find_key, find_value) in rawconfig["variable-assemblage"].items():
                if (find_key == key_from):
                    rawconfig["environ"][current_var][key] = rawconfig["environ"][current_var][key].replace(
                        key_replace, rawconfig["variable-assemblage"][key_from])
                    break

            for (find_key, find_value) in rawconfig["environ"][current_var].items():
                if (key == find_key):
                    break
                if (find_key == key_from):
                    rawconfig["environ"][current_var][key] = rawconfig["environ"][current_var][key].replace(
                        key_replace, rawconfig["environ"][current_var][key_from])
                    break



    #replace cmd
    #from path var env cmd
    for (cmd, stream) in rawconfig["command"].items():
        #print (key) #...

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

                for (find_key, find_value) in rawconfig["path-assemblage"].items():
                    if (find_key == key_from):
                        rawconfig['command'][cmd][step] = rawconfig['command'][cmd][step].replace(
                            key_replace, rawconfig["path-assemblage"][key_from])
                        break

                for (find_key, find_value) in rawconfig["variable-assemblage"].items():
                    if (find_key == key_from):
                        rawconfig['command'][cmd][step] = rawconfig['command'][cmd][step].replace(
                            key_replace, rawconfig["variable-assemblage"][key_from])
                        break

                current_env_var = rawconfig["environ"]["current"]
                for (find_key, find_value) in rawconfig["environ"][current_env_var].items():
                    if (find_key == key_from):
                        rawconfig['command'][cmd][step] = rawconfig['command'][cmd][step].replace(
                            key_replace, rawconfig["environ"][current_env_var][key_from])
                        break
            step += 1

    #list
    while (True):
        if (args['list'] == True):

            if ( args['--raw'] == True ):
                list_config = rawconfig
            else:
                list_config = config

            if( args['path'] == True):
                dict0 = copy.deepcopy(list_config['path-assemblage'])
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )

            elif( args['var'] == True):
                dict0 = copy.deepcopy(list_config['variable-assemblage'])
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )


            elif( args['env'] == True):
                current_var = list_config['environ']['current']
                print ("env %s" % current_var)
                dict0 = copy.deepcopy(list_config['environ'][current_var])

                print ("path+:")
                for (key) in dict0["path+"]:
                    print ("  %s" % key)

                print ("variable:")
                for (key, value) in dict0.items():
                    if ( key == 'path+' ):
                        continue
                    print("  %-24s %s" % (key, value) )

            elif( args['cmd'] == True):
                dict0 = copy.deepcopy(list_config['command'])
                for (key, value) in dict0.items():
                    print("group: %s" % key)
                    step = 1
                    for cmd in value:
                        print("%-3s %s" % (step, cmd))
                        step += 1

            else:
                ""
            return
        else:
            ''
        break

    # set into env
    env = os.environ
    current_var = rawconfig['environ']['current']
    dict0 = copy.deepcopy(rawconfig['environ'][current_var])
    for (key) in dict0["path+"]:
        env["PATH"] = key + os.path.pathsep + env["PATH"]
    for (key, value) in dict0.items():
        if (key == 'path+'):
            continue
        env[key] = value
    print("env %s" % current_var)
    print("path+:")
    for path in env["PATH"].split(os.path.pathsep):
        print("  %s" % path)
    print("variable:")
    for (key, value) in env.items():
        if(key == 'PATH'):
            continue
        print("  %-30s %s" % (key, value))

    while ( True ):
        if( args['j'] == True ):
            if(args['<name>'] is None):
                print("please appoint a command")
                return
            current_var = args['<name>']

            #print ("group %s" % current_vars)
            dict0 = copy.deepcopy(rawconfig['command'])
            list0 = []
            if( current_var in dict0 ):
                list0 = dict0[current_var]
            else:
                list0.append(current_var)
            #print (list0)
            communicateWithCommandLine(list0)
            os._exit(0)
            return
        else:
            ''
        break

    return

if __name__ == '__main__':

    main_function()
