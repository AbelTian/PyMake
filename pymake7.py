# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyMake 7.1.

Usage:
  pymake7.py source
  pymake7.py source file [ <source-path-file> ]
  pymake7.py source root [ <source-root-path> ]
  pymake7.py source config [ --add | --del | --mod | --switch | --restore | --show ] [ <config-file-name> ] [<new-config-file-name>]
  pymake7.py -------------------------------------------------------------
  pymake7.py set path ( --add | --del | --mod ) <name> [ <value> ]
  pymake7.py set env [ path ] ( --add | --del | --mod ) <group> <name> [ <value> ]
  pymake7.py set cmd (--add | --del | --mod ) <name> [ <values> ... ]
  pymake7.py set cur env <name>
  pymake7.py list [ path | env | cmd ] [<name>] [-r | --raw] [-a | --all]
  pymake7.py env [<name>] [-p | --path] [-v | --var] [-r | --raw] [-a | --all]
  pymake7.py -------------------------------------------------------------
  pymake7.py here clean
  pymake7.py here export [ <env-name> ] [ to <file-name> ]
  pymake7.py here type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py here use <env-name> exec [ <command-names> ... ]
  pymake7.py here exec [ <command-names> ... ]
  pymake7.py here use <env-name> cc [ <command-names> ... ]
  pymake7.py here cc [ <command-names> ... ]
  pymake7.py -------------------------------------------------------------
  pymake7.py clean [ here | hh ]
  pymake7.py export [ here | hh ] [ <env-name> ] [ to <file-name> ]
  pymake7.py type [ here | hh ] [ <cmd-name> ] [ to <file-name> ]
  pymake7.py exec [ here | hh ] [ <command-names> ... ]
  pymake7.py cc [ here | hh ] [ <command-names> ... ]
  pymake7.py use <env-name> type [ here | hh ] [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py use <env-name> exec [ here | hh ] [ <command-names> ... ]
  pymake7.py use <env-name> cc [ here | hh ] [ <command-names> ... ]
  pymake7.py -------------------------------------------------------------
  pymake7.py set current env <name>
  pymake7.py set default env <name>
  pymake7.py show [ path | env | cmd ] [<name>] [-r | --raw] [-a | --all]
  pymake7.py environ [<name>] [-p | --path] [-v | --var] [-r | --raw] [-a | --all]
  pymake7.py see [ <cmd-name> ] [ use <env-name> ] [-r | --raw] [-a | --all]
  pymake7.py ss [ <cmd-name> ] [ use <env-name> ] [-r | --raw] [-a | --all]
  pymake7.py cmd [ <cmd-name> ] [ use <env-name> ] [-r | --raw] [-a | --all]
  pymake7.py use <env-name> see [ <cmd-name> ] [-r | --raw] [-a | --all]
  pymake7.py use <env-name> ss [ <cmd-name> ] [-r | --raw] [-a | --all]
  pymake7.py use <env-name> cmd [ <cmd-name> ] [-r | --raw] [-a | --all]
  pymake7.py -------------------------------------------------------------
  pymake7.py hh clean
  pymake7.py hh export [ <env-name> ] [ to <file-name> ]
  pymake7.py hh type [ <cmd-name> ]  [ to <file-name> ]
  pymake7.py hh use <env-name> exec [ <command-names> ... ]
  pymake7.py hh exec [ <command-names> ... ]
  pymake7.py hh use <env-name> cc [ <command-names> ... ]
  pymake7.py hh cc [ <command-names> ... ]
  pymake7.py -------------------------------------------------------------
  pymake7.py have path <name> [-r | --raw]
  pymake7.py have env [ path ] [ <group> ] [ <name> ] [-r | --raw]
  pymake7.py have cmd <name> [-r | --raw]
  pymake7.py has path <name> [-r | --raw]
  pymake7.py has env [ path ] [ <group> ] [ <name> ] [-r | --raw]
  pymake7.py has cmd <name> [-r | --raw]
  pymake7.py -------------------------------------------------------------
  pymake7.py get cur env
  pymake7.py get current env
  pymake7.py get default env
  pymake7.py get env
  pymake7.py get env ( cur | current | default )
  pymake7.py -------------------------------------------------------------
  pymake7.py get pc
  pymake7.py get pc home
  pymake7.py get pc [ setting ]
  pymake7.py get pc [ desk ] [ doc ] [ download ] [ music ] [ picture ] [ movie ]
  pymake7.py get pc [ favorite ] [ search ] [ contact ]
  pymake7.py get pc [ develop ]
  pymake7.py -------------------------------------------------------------
  pymake7.py program
  pymake7.py program root
  pymake7.py program file
  pymake7.py program configure
  pymake7.py program configure root
  pymake7.py program configure file
  pymake7.py get all
  pymake7.py get all ( info | information )
  pymake7.py get all ( stat | status )
  pymake7.py -------------------------------------------------------------
  pymake7.py inport
  pymake7.py outport
  pymake7.py -------------------------------------------------------------
  pymake7.py (-h | --help)
  pymake7.py --version

Command:
  source           switch to another source file
  source root      config root directory
  source config    config source conf file
  set path         path assessblage
  set env          set env variable
  set cmd          set cmd stream
  export           output private env variable to a bat file or sh file [default:current, env]
  type             output command to a bat file or sh file [default:cmd]
  see              check command stream
  ss               check command stream
  cmd              check command stream
  list             list configed values, show command also too.
  set cur env      set default env
  use              use selected env exec commands
  here             at here do exec commands e.g.
  hh               at here do exec commands e.g.
  exec             exec commands list.
  cc               exec commands list.
  have             check env or path or cmd item whether user has configured.
  has              check env or path or cmd item whether user has configured.
  clean            clean *_effect.sh *_unset.sh
  program          pymake.py program status.
  get              get lots of important information.

Options:
  -h --help     Show this screen.
  --version     Show version.
  --add
  --del
  --mod         add or delete or modify a config or path
  --switch      switch to another source
  --show        display haved stream config files
  --restore     reset to pymake.json stream config file
  -r, --raw     expand editing config values
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
from pycore.docopt import docopt


def main_function():

    d = {
        "path-assemblage": {
            "root": "/Users/abel/Develop",
            "root.src": "${root}/a0-develop",
            "root.prod": "${root}/b1-product",
            "root.tool": "${root}/b0-toolskits",
            "root.build": "${root}/c0-buildstation",
            "root.test": "${root}/c2-test",
            "root.webrc": "${root}/c1-webrc",
            "cc": "${root.tool}/compiler",
            "cmake.bin": "${cc}/CMake.app/Contents/bin",
            "qt": "${root.tool}/macLibraries/Qt",
            "qt5.9.clang": "${qt}/5.9.1/clang_64",
            "qt5.8.android_x86": "${qt}/5.8/android_x86",
            "qt5.8.android_arm": "${qt}/5.8/android_armv7",
            "qt5.8.clang": "${qt}/5.8/clang_64",
            "qt5.8.ios": "${qt}/5.8/ios",
            "qt4.8.clang": "${qt}/4.8.7/clang_64",
            "qt5.9.clang.bin": "${qt}/5.9.1/clang_64/bin",
            "qt5.8.android_x86.bin": "${qt}/5.8/android_x86/bin",
            "qt5.8.android_arm.bin": "${qt}/5.8/android_armv7/bin",
            "qt5.8.clang.bin": "${qt}/5.8/clang_64/bin",
            "qt5.8.ios.bin": "${qt}/5.8/ios/bin",
            "qt4.8.clang.bin": "${qt}/4.8.7/clang_64/bin",
            "android": "${root.tool}/macAndroidLibraries",
            "android.sdk": "${android}/android-sdk-macosx",
            "android.ndk": "${android}/android-ndk-r13b",
            "android.ant": "${android}/apache-ant-1.10.1",
            "android.java": "${android}/java-macosx/Java/JavaVirtualMachines",
            "sdk.plat.tool": "${android.sdk}/platform-tools",
            "sdk.build.tool": "${android.sdk}/build-tools",
            "sdk.tool": "${android.sdk}/tools",
            "java1.7.home": "${android.java}/jdk1.7.0_79.jdk/Contents/Home",
            "java1.8.home": "${android.java}/jdk1.8.0_111.jdk/Contents/Home",
            "java1.9.home": "${android.java}/jdk9.jdk/Contents/Home",
            "java1.7.bin": "${java1.7.home}/bin",
            "java1.8.bin": "${java1.8.home}/bin",
            "java1.9.bin": "${java1.9.home}/bin",
            "ant.bin": "${android.ant}/bin",
            "ndk.arm": "${android.ndk}/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64",
            "ndk.x86": "${android.ndk}/toolchains/x86-4.9/prebuilt/darwin-x86_64",
            "ndk.x86_64": "${android.ndk}/toolchains/x86_64-4.9/prebuilt/darwin-x86_64",
            "ndk.arm.bin": "${ndk.arm}/bin",
            "ndk.x86.bin": "${ndk.x86}/bin",
            "ndk.x86_64.bin": "${ndk.x86_64}/bin",
            "mac.sdk": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks"
        },
        "environ": {
            "android.mobile": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.8.android_arm.bin}",
                    "${java1.8.bin}",
                    "${android.sdk}",
                    "${sdk.plat.tool}",
                    "${sdk.build.tool}",
                    "${sdk.tool}",
                    "${ant.bin}",
                    "${ndk.arm.bin}"
                ],
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_SDK_ROOT": "${android.sdk}",
                "ANDROID_NDK_ROOT": "${android.ndk}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "arm-linux-androideabi",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_PLATFORM": "android-23",
                "NDK_TOOLCHAIN_PATH": "${ndk.arm.bin}",
                "NDK_TOOLS_PREFIX": "arm-linux-androideabi",
                "PYMAKE_MYNAME": "T.D.R",
                "a_special_var_const": "hello world",
                "QKIT": "Android",
                "QTDIR": "${qt5.8.android_arm}",
                "QTSPEC": "android-g++",
                "QTCONFIG": "arm",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar"
            },
            "android.x86": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.8.android_x86.bin}",
                    "${java1.8.bin}",
                    "${android.sdk}",
                    "${sdk.plat.tool}",
                    "${sdk.build.tool}",
                    "${sdk.tool}",
                    "${ant.bin}",
                    "${ndk.x86.bin}"
                ],
                "CLICOLOR": "1",
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_SDK_ROOT": "${android.sdk}",
                "ANDROID_NDK_ROOT": "${android.ndk}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "x86",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_PLATFORM": "android-23",
                "NDK_TOOLCHAIN_PATH": "${ndk.x86.bin}",
                "NDK_TOOLS_PREFIX": "i686-linux-android",
                "QKIT": "Android",
                "QTDIR": "${qt5.8.android_x86}",
                "QTSPEC": "android-g++",
                "QTCONFIG": "arm",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar"
            },
            "qt.mac": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.9.clang.bin}",
                    "${java1.8.bin}",
                    "${android.sdk}",
                    "${sdk.plat.tool}",
                    "${sdk.build.tool}",
                    "${sdk.tool}",
                    "${ant.bin}",
                    "${ndk.arm.bin}"
                ],
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_SDK_ROOT": "${android.sdk}",
                "ANDROID_NDK_ROOT": "${android.ndk}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "i686-linux-android",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_PLATFORM": "android-23",
                "NDK_TOOLCHAIN_PATH": "${ndk.arm.bin}",
                "NDK_TOOLS_PREFIX": "i686-linux-android",
                "QKIT": "macOS",
                "QTDIR": "${qt5.9.clang}",
                "QTSPEC": "macx-clang",
                "QTCONFIG": "x86_64",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar"
            },
            "current": "qt.mac"
        },
        "variable-assemblage": [
            "QQt",
            "a0-qqtfoundation",
            "${root.build}/${qqt.proj.name}/${qt.sys.mac}/${build.release}",
            "${root.src}/${qqt.proj.name}",
            "${qqt.proj.name}.pro",
            "${qqt.build.path}/src/bin",
            "${root.prod}/QQt",
            "qqtframe",
            "${qqt.build.path}/examples/${qqtframe.prod.name}/bin",
            "${qqt.build.path}/src/bin/QQt.framework",
            "QQt.framework/Versions/1/QQt",
            "${root.tool}/Source/qt5",
            "${root.build}/qt5",
            "androiddeployqt",
            "macdeployqt",
            "DownloadQueue",
            "/Users/abel/Develop/c1-webrc/DownloadQueue/DownloadQueue.pro",
            "${root.build}/${app.name}",
            "macdeployqt ${app.path.build}/${app.name}.app",
            "${prod.name}.app",
            "${mac.app}/Contents",
            "${mac.app.content}/MacOS",
            "${mac.app.content}/Frameworks",
            "${mac.app.content}/Resources",
            "${mac.app.content}/PlugIns",
            "${prod.name}.framework",
            "${prod.name}.framework/Versions",
            "${prod.name}.framework/Resources",
            "macdeployqt ${}"
        ],
        "command-assemblage": [
            "I'm not similar to these command, so list them here, rather than forgotten them",
            "cl-command, sys-command",
            "replace? no, append? easy!",
            "help you to remeber these command.",
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
        "command": {
            "qqt.build": [
                "mkdir -p ${app.path.build}",
                "cd ${app.path.build}",
                "qmake ${app.path.qmake} -spec ${QTSPEC} CONFIG+=${QTCONFIG} && make qmake_all",
                "make -j4"
            ],
            "qqt.rebuild": [
                "cd ${app.path.build}",
                "make clean",
                "qmake ${app.path.qmake} -spec ${QTSPEC} CONFIG+=${QTCONFIG} && make qmake_all",
                "make -j4"
            ],
            "qqt.clean": [
                "cd ${app.path.build}",
                "make clean"
            ],
            "qqt.install": [
                "cd ${app.path.build}",
                "make install"
            ],
            "qqt.deploy": [
                "cd ${app.path.build}",
                "${app.deploy}"
            ],
            "buildqt5android": [
                "mkdir -p ${qt5.path.build}",
                "cd ${qt5.path.build}",
                "${qt5.path.source}/configure -prefix ${qt5.path.install} -hostprefix ${qt5.path.install} -xplatform android-g++ -release -nomake tests -nomake examples -android-ndk $ANDROID_NDK_ROOT -android-sdk $ANDROID_SDK_ROOT -android-ndk-host $ANDROID_NDK_HOST -android-toolchain-version $ANDROID_NDK_TOOLCHAIN_VERSION -skip qtwebkit-examples -no-warnings-are-errors"
            ],
            "qt": [
                "cd ${root.build}",
                "open \"/Applications/Qt Creator.app\""
            ],
            "adb": [
                "adb devices"
            ],
            "android": [
                "/Users/abel/Develop/b0-toolskits/macAndroidLibraries/android-sdk-macosx/tools/android"
            ]
        }
    }

    # record initial current directory
    pymakeinitialpath = os.getcwd()
    # record current directory
    pymakeworkpath = os.getcwd()
    # record pymake file directory
    pymakefilepath = os.path.split(os.path.realpath(__file__))[0]
    #print( "pymake file path" + pymakefilepath )

    # pymake source root [default]
    pymakesourceroot = pymakefilepath + os.path.sep + 'USERSOURCE'
    if (not os.path.exists(pymakesourceroot)):
        os.makedirs(pymakesourceroot)

    """
    [pymake]
    [source]
    root = ~/.pymake
    config = pymake.json
    """
    userroot = getuserroot()
    configroot = getconfigroot()
    plat = getplatform()
    #record pymake configure directory. in user config path
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
        conf.set('source', 'root', pymakesourceroot)
        conf.write(open(pymakeini, 'w'))
    if(not conf.has_option('source', 'config')):
        conf.set('source', 'config', 'pymake.json')
        conf.write(open(pymakeini, 'w'))


    #record source root directory
    sourceroot = conf.get('source', 'root')
    #record source config file name
    file = conf.get('source', 'config')
    #print ("root: %s config: %s" % (sourceroot, file))
    #print(Fore.LIGHTBLACK_EX + "use source config: %s/%s" % (sourceroot, file) )
    # cd source root directory
    if (os.path.exists(sourceroot)):
        # chdir to source root
        os.chdir(sourceroot)
        if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)
                and os.path.abspath(sourceroot) != os.path.abspath(pymakefilepath)):
            if (not os.path.exists('pymake.json')):
                writeJsonData('pymake.json', d)

    args = docopt(__doc__, version='pymake7.py v7.1')
    #print(args)

    pymakesuffix = '.json'
    while (True):
        if(args['source'] is True):
            if(args['root'] is True):
                if ( args['<source-root-path>'] is not None):
                    conf.set('source', 'root', args['<source-root-path>'])
                    conf.write(open(pymakeini, 'w'))
                    print ("successed: change source root to %s" % args['<source-root-path>'])
                else:
                    print ("%s" % conf.get('source', 'root'))
            elif(args['config'] is True):
                sourceroot = conf.get('source', 'root')
                os.chdir(sourceroot)
                if(args['--del'] is True):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'] == 'pymake.json'):
                        print('You can\'t remove pymake\'s file...')
                    elif (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix)):
                        os.remove(args['<config-file-name>'])
                        conf.set('source', 'config', 'pymake.json')
                        conf.write(open(pymakeini, 'w'))
                        print ("successed: %s" % args['<config-file-name>'])
                    else:
                        print ('You can\'t remove pymake.json and un.json\'s file...')
                elif(args['--add'] is True):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix) and args['<config-file-name>'] != 'pymake.json'):
                        f = conf.get('source', 'config')
                        if( f != args['<config-file-name>']):
                            shutil.copyfile(f, args['<config-file-name>'])
                            conf.set('source', 'config', args['<config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                            print ("successed: %s" % args['<config-file-name>'])
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
                        print ("successed: %s" % args['<new-config-file-name>'])
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
                    print ("successed: %s" % 'pymake.json')
                elif (args['--switch'] is True or ( args['<config-file-name>'] is not None )):
                    if (args['<config-file-name>'] is not None and args['<config-file-name>'].endswith(pymakesuffix) ):
                        if (os.path.exists(args['<config-file-name>'])):
                            conf.set('source', 'config', args['<config-file-name>'])
                            conf.write(open(pymakeini, 'w'))
                            print("successed: switch to source config %s" % args['<config-file-name>'])
                        else:
                            print("failed: source file %s isn't exists, please --add it" % args['<config-file-name>'])
                    else:
                        print ('You can\'t switch pymake.json and un.json\'s file...')
                else:
                    print ("%s" % conf.get("source", "config"))
            elif (args['file'] is True):
                if(args['<source-path-file>'] is None):
                    print("please input an abspath .json file.")
                    return
                if(not args['<source-path-file>'].endswith(pymakesuffix)):
                    print("you can't set un.json file.")
                    return
                r = os.path.split(os.path.realpath(args['<source-path-file>']))[0]
                f = os.path.split(os.path.realpath(args['<source-path-file>']))[1]
                conf.set('source', 'root', r)
                conf.set('source', 'config', f)
                conf.write(open(pymakeini, 'w'))
                print ("change source to %s" % os.path.realpath(args['<source-path-file>']))
                print ("source root    : %s" % r)
                print ("source config  : %s" % f)
                return
            else:
                r = conf.get('source', 'root')
                f = conf.get('source', 'config')
                print ("%s%s%s" % (r, os.path.sep, f))
            return
        else:
            ''
        break

    #record source root directory
    sourceroot = conf.get('source', 'root')
    #record source config file name
    file = conf.get('source', 'config')
    #print ("root: %s config: %s" % (sourceroot, file))
    #print(Fore.LIGHTBLACK_EX + "use source config: %s/%s" % (sourceroot, file) )

    # record current directory
    #pymakeworkpath = os.getcwd() #have cd to sourceroot, cant initial here secondly.
    #print( "pymake work path:", pymakeworkpath )
    # record pymake file directory
    #pymakefilepath = os.path.split(os.path.realpath(__file__))[0] #have recorded
    #print( "pymake file path" + pymakefilepath )

    # cd source root directory
    if (os.path.exists(sourceroot)):
        # chdir to source root
        os.chdir(sourceroot)
    else:
        print("You have changed sourceroot manually, please change it using source command")
        return

    if (os.path.abspath(sourceroot) == os.path.abspath(pymakeroot) or
            os.path.abspath(sourceroot) == os.path.abspath(pymakefilepath)):
        print ("I checked you use pymakeroot or pymakefileroot to be sourceroot, suggestting you use source command changing one.")
        print ("this progrom can store building env and building command forever, please repleace source root then using me.")
        return
    elif (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)):
        if (not os.path.exists('pymake.json')):
            writeJsonData('pymake.json', d)
            print ("initial pymake.json in source root.")
        if(not os.path.exists(file)):
            print ("source config file is not existed.")
            return

    # set this command here .
    # program
    while (True):
        if(args['program'] is True):
            if(args['configure'] is True):
                if(args['root'] is True):
                    print("%s" % os.path.split(os.path.realpath(pymakeini))[0])
                    return
                elif (args['file'] is True):
                    print("%s" % os.path.split(os.path.realpath(pymakeini))[1])
                    return
                else:
                    print("%s" % os.path.realpath(pymakeini))
                    return
            else:
                if(args['root'] is True):
                    print("%s" % os.path.split(os.path.realpath(__file__))[0])
                    return
                elif (args['file'] is True):
                    print("%s" % os.path.split(os.path.realpath(__file__))[1])
                    return
                else:
                    print("%s" % os.path.realpath(__file__))
                    return
            return
        else:
            ''
        break

    config = readJsonData(file)
    #print(config)

    # set
    while (True):
        if (args['set'] == True):
            if (args['env'] is True):
                if (args['default'] or args['current'] or args['cur'] is True):
                    if (args["<name>"] is not None):
                        if (config['environ'].__contains__(args['<name>']) is False
                            or args['<name>'] == "current"):
                            print("please ensure the environ is right")
                            return
                        config["environ"]["current"] = args["<name>"]
                        print("successed: %s" % (args['<name>']))
                    else:
                        ""
                elif (args["path"] is True):
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] is not None):
                            config['environ'][args['<group>']]["path+"].append(args["<name>"])
                            print ("successed: %s:%s" % (args['<group>'], args['<name>']))
                        else:""
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['environ'][args['<group>']]["path+"].__contains__(args['<name>'])):
                                config['environ'][args['<group>']]["path+"].__delitem__(args['<name>'])
                                print("successed: %s:%s" % (args['<group>'], args['<name>']))
                            else:
                                print("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['variable'][args['<group>']]["path+"].__contains__(args['<name>'])):
                                index = config['variable'][args['<group>']]["path+"].index(args['<name>'])
                                config['variable'][args['<group>']]["path+"][index] = [args['<value>']]
                                print ("successed: %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                            else:
                                print("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                else:
                    if (args['--add'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            config['environ'][args['<group>']][args['<name>']] = args["<value>"]
                            print ("successed: %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                        else:
                            print ("failed %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
                    elif (args['--del'] == True):
                        if (args['<group>'] and args["<name>"] is not None):
                            if (config['variable'][args['<group>']].__contains__(args['<name>'])):
                                config['variable'][args['<group>']].__delitem__(args['<name>'])
                                print ("successed: %s:%s" % (args['<group>'], args['<name>']))
                            else:
                                print ("failed %s:%s" % (args['<group>'], args['<name>']))
                        else:
                            ''
                    elif (args['--mod'] == True):
                        if (args['<group>'] and args['<name>'] and args["<value>"] is not None):
                            if (config['variable'][args['<group>']].__contains__(args['<name>'])):
                                config['variable'][args['<group>']][args['<name>']] = args["<value>"]
                                print ("successed: %s:%s:%s" % (args['<group>'], args['<name>'], args["<value>"]))
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
                        print("successed: %s:%s" % (args['<name>'], args["<values>"]))
                    else:
                        print("failed %s:%s" % (args['<name>'], args["<values>"]))
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['command'].__contains__(args['<name>'])):
                            config["command"].__delitem__(args['<name>'])
                            print("successed: %s" % (args['<name>']))
                        else:
                            print("failed %s" % (args['<name>']))
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<values>"] is not None):
                        config["command"][args['<name>']] = args["<values>"]
                        print("successed: %s:%s" % (args['<name>'], args["<values>"]))
                    else:
                        print("failed %s:%s" % (args['<name>'], args["<values>"]))
                else:
                    ''
            elif (args['path'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config['path-assemblage'][args['<name>']] = args["<value>"]
                        print ("successed: %s:%s" % (args['<name>'], args["<value>"]))
                    else:
                        print ("failed %s:%s" % (args['<name>'], args["<value>"]))
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['path-assemblage'].__contains__(args['<name>'])):
                            config['path-assemblage'].__delitem__(args['<name>'])
                            print ("successed: %s" % (args['<name>']))
                        else:
                            print ("failed %s" % (args['<name>']))
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['path-assemblage'].__contains__(args['<name>'])):
                            config['path-assemblage'][args['<name>']] = args["<value>"]
                            print ("successed: %s:%s" % (args['<name>'], args["<value>"]))
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

    # get
    while (True):
        if (args['get'] == True):
            if (args['env'] is True):
                #if (args['default'] or args['current'] or args['cur'] is True):
                #else:
                #    ""
                if (config['environ'].__contains__("current") is True):
                    print("%s" % (config["environ"]["current"]))
                    return
                else:
                    print("failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    return
                return
            elif (args['all'] is True):
                if (args['stat'] is True):
                    print("%s" % pymakeinitialpath)
                    print("%s" % os.getcwd())
                    return
                elif (args['status'] is True):
                    print("EXECUTE ROOT [PWD]: %s" % pymakeinitialpath)
                    print("WORKING ROOT [VAR]: %s" % os.getcwd())
                    return
                elif (args['info'] is True):
                    if(config.__contains__("environ") is True):
                        if (config['environ'].__contains__("current") is True):
                            print("%s" % (config["environ"]["current"]))
                        else:
                            print("failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    else:
                        print("failed: please check your .json file content, it is not now version .json.")

                    r = conf.get('source', 'root')
                    f = conf.get('source', 'config')
                    print ("%s%s%s" % (r, os.path.sep, f))
                    print ("%s" % (r))
                    print ("%s" % (f))
                    print("-----------------------------------------")
                    print("%s" % os.path.realpath(__file__))
                    print("%s" % os.path.split(os.path.realpath(__file__))[0])
                    print("%s" % os.path.split(os.path.realpath(__file__))[1])
                    print("-----------------------------------------")
                    print("%s" % (pymakeini))
                    print("%s" % (pymakeroot))
                    print("%s" % (os.path.split(os.path.realpath(pymakeini))[1]))
                    return
                else:
                    if(config.__contains__("environ") is True):
                        if (config['environ'].__contains__("current") is True):
                            print("CUR ENVIRON   : %s" % (config["environ"]["current"]))
                        else:
                            print("CUR ENVIRON   : failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    else:
                        print("CUR ENVIRON   : failed: please check your .json file content, it is not now version .json.")

                    r = conf.get('source', 'root')
                    f = conf.get('source', 'config')
                    print ("SOURCE        : %s%s%s" % (r, os.path.sep, f))
                    print ("SOURCE ROOT   : %s" % (r))
                    print ("SOURCE CONFIG : %s" % (f))
                    print("-----------------------------------------")
                    print("PROGRAM       : %s" % os.path.realpath(__file__))
                    print("PROGRAM ROOT  : %s" % os.path.split(os.path.realpath(__file__))[0])
                    print("PROGRAM FILE  : %s" % os.path.split(os.path.realpath(__file__))[1])
                    print("-----------------------------------------")
                    print("CONFIGURE     : %s" % (pymakeini))
                    print("CONFIGURE ROOT: %s" % (pymakeroot))
                    print("CONFIGURE FILE: %s" % (os.path.split(os.path.realpath(pymakeini))[1]))
                    return
                return
            elif (args['pc'] is True):
                userroot = getuserroot()
                #linux path is chinese, why?
                #windows only
                userdoc = userroot + os.path.sep + "Documents"
                userdown = userroot + os.path.sep + "Downloads"
                userset = getconfigroot()
                userdesk = userroot + os.path.sep + "Desktop"
                usermusic = userroot + os.path.sep + "Music"
                usermovie = userroot + os.path.sep + "Videos" #Movies
                userfavo = userroot + os.path.sep + "Favorites"
                usersearch = userroot + os.path.sep + "Searches"
                usercontact = userroot + os.path.sep + "Contacts"
                userpictures = userroot + os.path.sep + "Pictures"
                userdev = userroot + os.path.sep + "Develop"
                if (args['home']):
                    print(userroot)
                elif (args['setting']):
                    print(userset)
                elif (args['doc']):
                    print(userdoc)
                elif (args['download']):
                    print(userdown)
                elif (args['desk']):
                    print(userdesk)
                elif (args['music']):
                    print(usermusic)
                elif (args['movie']):
                    print(usermovie)
                elif (args['favorite']):
                    print(userfavo)
                elif (args['search']):
                    print(usersearch)
                elif (args['contact']):
                    print(usercontact)
                elif (args['picture']):
                    print(userpictures)
                elif (args['develop']):
                    print(userdev)
                else:
                    print(userroot)
                    print(userset)
                    print(userdesk)
                    print(userdoc)
                    print(userdown)
                    print(usermusic)
                    print(userpictures)
                    print(usermovie)
                    print(usersearch)
                    print(usercontact)
                    print(userdev)
                return
            else:
                ''
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

        #fix windows platform path sep
        #but no nessesary
        plat = getplatform()
        if (plat == "Windows"):
            ""
            #rawconfig["path-assemblage"][key] = rawconfig["path-assemblage"][key].replace('/', os.path.sep)

    #replace env
    #from path var env
    for current_var in rawconfig["environ"].keys():
        if( current_var == "current"):
            continue
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

                for (find_key, find_value) in rawconfig["environ"][current_var].items():
                    if (key == find_key):
                        break
                    if (find_key == key_from):
                        rawconfig["environ"][current_var][key] = rawconfig["environ"][current_var][key].replace(
                            key_replace, rawconfig["environ"][current_var][key_from])
                        break

    # replace cmd
    # from path env
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

                current_env_var = rawconfig["environ"]["current"]
                for (find_key, find_value) in rawconfig["environ"][current_env_var].items():
                    if (find_key == key_from):
                        rawconfig['command'][cmd][step] = rawconfig['command'][cmd][step].replace(
                            key_replace, rawconfig["environ"][current_env_var][key_from])
                        break
            step += 1

    # list show
    while (True):
        if (args['show'] or args['list'] is True):

            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            if( args['path'] == True):
                dict0 = copy.deepcopy(list_config['path-assemblage'])
                for (k, v) in dict0.items():
                    print(Fore.BLUE+ "%-24s %s" % (k, v) )

            elif( args['env'] == True):
                env = os.environ
                current_var = list_config['environ']['current']
                if(args['<name>'] is not None):
                    current_var = args['<name>']

                if (list_config['environ'].__contains__(current_var) is False
                    or current_var == "current"):
                    print("please ensure the environ is right")
                    return

                dict0 = copy.deepcopy(list_config['environ'][current_var])

                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.MAGENTA + "path+:")
                for (key) in dict0["path+"]:
                    print(Fore.BLUE + "  %s" % key)
                if(args['-a'] or args['--all'] is True):
                    for path in env["PATH"].split(os.path.pathsep):
                        print(Fore.BLUE + "  %s" % path)
                print(Fore.MAGENTA + "variable:")
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                if (args['-a'] or args['--all'] is True):
                    for (key, value) in env.items():
                        if (key == 'PATH'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))

            elif( args['cmd'] == True):
                dict0 = copy.deepcopy(list_config['command'])
                if (args['<name>'] is not None):
                    #print(Fore.CYAN + "group: %s" % args['<name>'])
                    value = dict0[args['<name>']]
                    step = 1
                    for cmd in value:
                        print(Fore.RED + "%-3s %s" % (step, cmd))
                        step += 1
                else:
                    for (key, value) in dict0.items():
                        if (args['-a'] is not True and args['--all'] is not True):
                            print(Fore.CYAN + "%s" % key)
                            continue
                        print(Fore.CYAN + "group: %s" % key)
                        step = 1
                        for cmd in value:
                            print(Fore.RED + "%-3s %s" % (step, cmd))
                            step += 1
            else:
                current_var = rawconfig['environ']['current']
                print(Fore.CYAN + "%s" % current_var)
                for key in rawconfig['environ'].keys() :
                    if(key == 'current'):
                        continue
                    if(key == current_var):
                        continue
                    print("%s" % key)
            return
        else:
            ''
        break

    # have has
    while (True):
        if (args['have'] or args['has'] is True):

            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            if( args['env'] == True):
                if ( args['path'] == True):
                    #print(args['<group>'], args['<name>'])
                    if (args['<group>'] is None):
                        print ("please input your env name.")
                        return

                    current_env = args['<group>']
                    if (current_env == "current"):
                        current_env = list_config['environ']['current']

                    if (args['<name>'] is None):
                        print ("please input your path value.")
                        return
                    current_name = args['<name>']

                    if (list_config['environ'][current_env]['path+'].__contains__(current_name) is True):
                        print("True")
                    else:
                        print("False")
                    return

                #env name is empty
                if ( args['<group>'] is None ):
                    current_env = list_config['environ']['current']
                    if (list_config['environ'].__contains__(current_env) is True):
                        print("True")
                    else:
                        print("False")
                    return

                current_env = args['<group>']
                if (current_env == "current"):
                    current_env = list_config['environ']['current']

                # item var name is empty
                if ( args['<name>'] is None ):
                    if(list_config['environ'].__contains__(current_env) is True):
                        print("True")
                    else:
                        print("False")
                    return

                current_name = args['<name>']
                if( current_name == "path+" ):
                    print("please ensure your var name is legal.")
                    return

                #env name is ok
                #env-var name is ok
                if (list_config['environ'].__contains__(current_env) is True):
                    if (list_config['environ'][current_env].__contains__(current_name) is True):
                        print("True")
                    else:
                        print("False")
                    return
                else:
                    print("False")
                return

            elif( args['path'] == True):
                dict0 = copy.deepcopy(list_config['path-assemblage'])
                for (k, v) in dict0.items():
                    if( k == args['<name>']):
                        print ("True")
                        return
                print ("False")
                return

            elif( args['cmd'] == True):
                dict0 = copy.deepcopy(list_config['command'])
                for (k, v) in dict0.items():
                    if( k == args['<name>']):
                        print ("True")
                        return
                print ("False")
                return

            else:
                print("please ensure your assemblage name.")
                return
        else:
            ''
        break

    # env environ
    while (True):
        if (args['environ'] or args['env'] is True):

            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            env = os.environ
            current_var = list_config['environ']['current']
            if (args['<name>'] is not None):
                current_var = args['<name>']

            if (list_config['environ'].__contains__(current_var) is False
                or current_var == "current"):
                print("please ensure the environ is right")
                return

            dict0 = copy.deepcopy(list_config['environ'][current_var])

            if( args['-p'] or args['--path'] is True):
                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.MAGENTA + "path+:")
                for (key) in dict0["path+"]:
                    print(Fore.BLUE + "  %s" % key)
                if(args['-a'] or args['--all'] is True):
                    for path in env["PATH"].split(os.path.pathsep):
                        print(Fore.BLUE + "  %s" % path)

            elif (args['-v'] or args['--var'] is True):
                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.MAGENTA + "variable:")
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                if (args['-a'] or args['--all'] is True):
                    for (key, value) in env.items():
                        if (key == 'PATH'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))

            elif (args['<name>'] is not None):
                print (Fore.CYAN+ "env %s" % current_var)
                print(Fore.MAGENTA + "path+:")
                for (key) in dict0["path+"]:
                    print(Fore.BLUE + "  %s" % key)
                if(args['-a'] or args['--all'] is True):
                    for path in env["PATH"].split(os.path.pathsep):
                        print(Fore.BLUE + "  %s" % path)
                print(Fore.MAGENTA + "variable:")
                for (key, value) in dict0.items():
                    if (key == 'path+'):
                        continue
                    print(Fore.GREEN + "  %-30s %s" % (key, value))
                if (args['-a'] or args['--all'] is True):
                    for (key, value) in env.items():
                        if (key == 'PATH'):
                            continue
                        print(Fore.GREEN + "  %-30s %s" % (key, value))

            else:
                current_var = rawconfig['environ']['current']
                print(Fore.CYAN + "%s" % current_var)
                for key in rawconfig['environ'].keys() :
                    if(key == 'current'):
                        continue
                    if(key == current_var):
                        continue
                    print("%s" % key)
            return
        else:
            ''
        break

    # set into env
    while(False):
        env = os.environ
        current_var = rawconfig['environ']['current']
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])
        for (key) in dict0["path+"]:
            env["PATH"] = key + os.path.pathsep + env["PATH"]
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            env[key] = value
        break

    # custom command stream from rawconfig and custom environ
    def raw_command( env_name = None ):
        command_dict = copy.deepcopy(config['command'])

        # replace cmd
        # from path env
        for (cmd, stream) in command_dict.items():
            # print (key) #...

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
                    # print ( key0 ) #${...}
                    key_from = key_replace.split('{')[1].split('}')[0].strip()
                    # print ( key1 ) #...

                    for (find_key, find_value) in rawconfig["path-assemblage"].items():
                        if (find_key == key_from):
                            command_dict[cmd][step] = command_dict[cmd][step].replace(
                                key_replace, rawconfig["path-assemblage"][key_from])
                            break

                    current_env_var = env_name
                    if (env_name is None):
                        current_env_var = config["environ"]["current"]
                    for (find_key, find_value) in rawconfig["environ"][current_env_var].items():
                        if (find_key == key_from):
                            command_dict[cmd][step] = command_dict[cmd][step].replace(
                                key_replace, rawconfig["environ"][current_env_var][key_from])
                            break
                step += 1
        return command_dict

    # export
    def env_export (env_name = None, file_name = None):
        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_header = "@echo off\n"
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_header = "#!/usr/bin/env bash\n"
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        #export path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + '\n')
            else:
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '$PATH' + '\n')

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + '\n')
            else:
                lines += (env_set + key + '=\"' + value + '\"\n')

        with open(cmd_effect, 'w') as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        #export unset path
        lines = ""
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + '\n')
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + '\n')

        #export unset env
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + '\n')
            else:
                lines += ('unset ' + key + '\n')
        with open(cmd_unset, 'w') as f:
            f.write(cmd_header)
            f.write(lines)

        #return file name
        return current_var, cmd_effect, cmd_unset

    def cmd_type (cmd_name = None, file_name = None, env_name = None):
        if (cmd_name is None):
            for (key, value) in rawconfig['command'].items():
                print(Fore.CYAN + "%s" % key)
            return ""

        if (rawconfig['command'].__contains__(cmd_name) is False):
            print("please check your command name")
            return ""

        if(env_name is None or env_name == rawconfig['environ']['current']):
            list0 = copy.deepcopy(rawconfig['command'][cmd_name])
        else:
            list0 = copy.deepcopy(raw_command(env_name)[cmd_name])

        #for cmd in list0:
        #    print(Fore.RED + "%s" % (cmd))

        temp_file_name = ""
        if (file_name is None):
            temp_file_name = "cmd"
        else:
            temp_file_name = file_name

        if (getplatform() == "Windows"):
            cmd_header = "@echo off"
            cmd_suffix = "_exec.bat"
        else:
            cmd_header = "#!/usr/bin/env bash"
            cmd_suffix = "_exec.sh"

        cmd_exec = temp_file_name + cmd_suffix
        with open(cmd_exec, 'w') as f:
            f.write(cmd_header + '\n')
            for cmd in list0:
                f.write(cmd + '\n')

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_exec)

        return cmd_exec

    def createCmdList0(list0):

        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_return = "\r\n"
            cmd_exit = 'exit /b 0'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit 0'
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        for cmd in list0:
            if (plat == "Windows"):
                ""  # cmd = cmd.replace('/', '\\')
            cmd_list.append(cmd)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w") as f:
            for line in cmd_list:
                f.write(line + "\n")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
        cmd_list.append(cmd_exit)

        # print (cmd_list)
        return cmd_list, name

    def createCmdList01(list0):

        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%errorlevel%"
            cmd_sep = '&'
            cmd_header = "@echo off"
            cmd_exit = 'exit /b 0'
            # window close echo, close promot
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call %s_effect.bat" % name + ' ' + cmd_sep + ' ' + cmd_status)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_exit = 'exit 0'
            cmd_header = "#!/usr/bin/env bash"
            cmd_list.append("source %s_effect.sh" % name + ' ' + cmd_sep + ' ' + cmd_status)

        for cmd in list0:
            cmd_list.append(cmd + ' ' + cmd_sep + ' ' + cmd_status)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )
        return cmd_list, name

    # use - see/ss/cmd
    while (True):
        if (args['use'] is True):
            if(args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if(rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['ss'] or args['see'] or args['cmd'] is True):
                local_command = config['command']
                if ( args['--raw'] is True ):
                    local_command = raw_command(current_env)

                if (args['<cmd-name>'] is None):
                    for (key, value) in local_command.items():
                        if (args['-a'] is not True and args['--all'] is not True):
                            print(Fore.CYAN + "%s" % key)
                            continue
                        print(Fore.CYAN + "group: %s" % key)
                        step = 1
                        for cmd in value:
                            print(Fore.RED + "%-3s %s" % (step, cmd))
                            step += 1
                    return

                if (args['<cmd-name>'] is not None):
                    if (local_command.__contains__(args['<cmd-name>']) is False):
                        print("please check your command name")
                        return
                    value = local_command[args['<cmd-name>']]
                    step = 1
                    for cmd in value:
                        print(Fore.RED + "%-3s %s" % (step, cmd))
                        step += 1
                    return
        else:
            ""
        break

    # see ss cmd
    while (True):
        if (args['ss'] or args['see'] or args['cmd'] is True):
            list_config = config
            if ( args['--raw'] is True ):
                list_config = rawconfig

            if (args['<cmd-name>'] is None):
                for (key, value) in list_config['command'].items():
                    if (args['-a'] is not True and args['--all'] is not True):
                        print(Fore.CYAN + "%s" % key)
                        continue
                    print(Fore.CYAN + "group: %s" % key)
                    step = 1
                    for cmd in value:
                        print(Fore.RED + "%-3s %s" % (step, cmd))
                        step += 1
                return

            if (args['<cmd-name>'] is not None):
                if (list_config['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return
                value = list_config['command'][args['<cmd-name>']]
                step = 1
                for cmd in value:
                    print(Fore.RED + "%-3s %s" % (step, cmd))
                    step += 1
                return
        else:
            ""
        break

    # use env type command
    while(True):
        if (args['use'] is True):
            if(args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if(rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['type'] == True):
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)

                if(args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                if (args['<file-name>'] is None):
                    if (current_env == rawconfig['environ']['current']):
                        list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                    else:
                        list0 = copy.deepcopy(raw_command(current_env)[args['<cmd-name>']])

                    for cmd in list0:
                       print(Fore.RED + "%s" % (cmd))
                    return

                cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'], current_env )

                print("successed: use %s type %s to %s" % (current_env, args['<cmd-name>'], cmd_exec))
                return
            else:
                ""
        else:
            ""
        break

    # export
    while (True):
        if (args['export'] == True):
            current_env = args['<env-name>']
            if(args['<env-name>'] is None):
                current_env = rawconfig['environ']['current']
                print(Fore.CYAN + "%s" % current_env)
                for key in rawconfig['environ'].keys() :
                    if(key == 'current'):
                        continue
                    if(key == current_env):
                        continue
                    print("%s" % key)
                return

            if(rawconfig['environ'].__contains__(current_env) is False):
                print("please ensure the environ is right")
                return

            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)

            current_var, cmd_effect, cmd_unset = env_export(current_env, args['<file-name>'])

            print("successed: export %s to %s %s" % (current_var, cmd_effect, cmd_unset))
            return
        else:
            ""
        break

    # type
    while (True):
        if (args['type'] == True):
            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)

            if (args['<cmd-name>'] is None):
                for (key, value) in rawconfig['command'].items():
                    print(Fore.CYAN + "%s" % key)
                return

            if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                print("please check your command name")
                return

            if (args['<file-name>'] is None):
                list0 = copy.deepcopy(rawconfig['command'][args['<cmd-name>']])
                for cmd in list0:
                    print(Fore.RED + "%s" % (cmd))
                return

            cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'] )

            print("successed: type %s to %s" % (args['<cmd-name>'], cmd_exec))
            return

        else:""
        break

    # clean
    while (True):
        if (args['clean'] == True):
            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)

            plat = getplatform()
            if(plat == "Windows"):
                os.system("@del /f /q *_effect.bat *_unset.bat *_exec.bat")
            else:
                os.system("rm -f *_effect.sh *_unset.sh *_exec.sh")

            return
        else:
            ""
        break

    def exec_command(env_name = None, cmd_list0 = []):
        if (env_name is None):
            print("please appoint a environ")
            return

        if (rawconfig['environ'].__contains__(env_name) is False):
            print("please ensure the environ is right")
            return

        current_env = env_name
        if (env_name == "current"):
            current_env = rawconfig['environ']['current']

        if (rawconfig['environ'].__contains__(current_env) is False):
            print(".json file is broken, environ section current env config is lost, please use set command fix it.")
            return

        if (args['<command-names>'] == []):
            print("please appoint your commands")
            return

        if (args['here'] or args['hh'] is True):
            os.chdir(pymakeworkpath)

        # create cmd_list
        dict0 = copy.deepcopy(rawconfig['command'])
        list0 = []
        for current_var in args['<command-names>']:
            if (current_var in dict0):
                list0.extend(dict0[current_var])
            else:
                list0.append(current_var)
        cmd_list = []
        temp_file_name = ""
        if (getplatform() == "Windows"):
            cmd_list, temp_file_name = createCmdList0(list0)
        else:
            cmd_list, temp_file_name = createCmdList01(list0)
        # good compatibility
        # cmd_list = createCmdList0(list0)

        # export env
        current_var = current_env
        # print (current_var, temp_file_name)
        env_export(current_var, temp_file_name)

        ret = communicateWithCommandLine(cmd_list)

        # delete env file and cmd file
        if (getplatform() == "Windows"):
            temp_file = temp_file_name + "_exec.bat"
            if (os.path.exists(temp_file)):
                os.remove(temp_file)
            temp_file = temp_file_name + "_effect.bat"
            if (os.path.exists(temp_file)):
                os.remove(temp_file)
            temp_file = temp_file_name + "_unset.bat"
            if (os.path.exists(temp_file)):
                os.remove(temp_file)
        else:
            temp_file = temp_file_name + "_exec.sh"
            if (os.path.exists(temp_file)):
                os.remove(temp_file)
            temp_file = temp_file_name + "_effect.sh"
            if (os.path.exists(temp_file)):
                os.remove(temp_file)
            temp_file = temp_file_name + "_unset.sh"
            if (os.path.exists(temp_file)):
                os.remove(temp_file)

        os._exit(ret)
        return

    # use env exec command
    while(True):
        if (args['use'] is True):
            if(args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if(rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if(args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (rawconfig['environ'].__contains__(current_env) is False):
                print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['cc'] or args['exec'] is True):
                if(args['<command-names>'] == []):
                    print("please appoint your commands")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)

                dict0 = copy.deepcopy(local_command)
                list0 = []
                for current_var in args['<command-names>']:
                    if (current_var in dict0):
                        list0.extend(dict0[current_var])
                    else:
                        list0.append(current_var)

                cmd_list = []
                temp_file_name = ""
                if(getplatform()=="Windows"):
                    cmd_list, temp_file_name = createCmdList0(list0)
                else:
                    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                #cmd_list = createCmdList0(list0)

                # export env
                current_var = current_env
                #print (current_var, temp_file_name)
                env_export(current_var, temp_file_name)

                ret = communicateWithCommandLine(cmd_list)

                # delete env file and cmd file
                if(getplatform()=="Windows"):
                    temp_file = temp_file_name + "_exec.bat"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.bat"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.bat"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                else :
                    temp_file = temp_file_name + "_exec.sh"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_effect.sh"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)
                    temp_file = temp_file_name + "_unset.sh"
                    if(os.path.exists(temp_file)):
                        os.remove(temp_file)

                os._exit(ret)
                return

        else :""
        break

    # cc exec
    while ( True ):
        if (args['cc'] or args['exec'] is True):
            if (args['<command-names>'] == []):
                print("please appoint your commands")
                return

            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)

            #print ("group %s" % current_vars)
            dict0 = copy.deepcopy(rawconfig['command'])

            list0 = []
            for current_var in args['<command-names>']:
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                else:
                    list0.append(current_var)

            cmd_list = []
            temp_file_name = ""
            if(getplatform()=="Windows"):
                cmd_list, temp_file_name = createCmdList0(list0)
            else:
                cmd_list, temp_file_name = createCmdList01(list0)
            #good compatibility
            #cmd_list = createCmdList0(list0)

            current_var = rawconfig['environ']['current']
            env_export(current_var, temp_file_name)

            ret = communicateWithCommandLine(cmd_list)

            # delete env file and cmd file
            if(getplatform()=="Windows"):
                temp_file = temp_file_name + "_exec.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_effect.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_unset.bat"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
            else :
                temp_file = temp_file_name + "_exec.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_effect.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)
                temp_file = temp_file_name + "_unset.sh"
                if(os.path.exists(temp_file)):
                    os.remove(temp_file)

            os._exit(ret)
            return
        else:
            ""
        break

    # here
    while ( False ):
        if (args['here'] or args['hh'] is True):
            os.chdir(pymakeworkpath)

            if (args['clean'] == True):
                plat = getplatform()
                if (plat == "Windows"):
                    os.system("@del /f /q *_effect.bat *_unset.bat *_exec.bat")
                else:
                    os.system("rm -f *_effect.sh *_unset.sh *_exec.sh")
                return

            if (args['export'] == True):
                current_env = args['<env-name>']
                if (args['<env-name>'] is None):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print("please ensure the environ is right")
                    return

                if (args['<env-name>'] == "current"):
                    current_env = rawconfig['environ']['current']

                if (rawconfig['environ'].__contains__(current_env) is False):
                    print(".json file is broken, environ section current env config is lost, please use set command fix it.")
                    return

                current_var, cmd_effect, cmd_unset = env_export(current_env, args['<file-name>'])
                print("successed: export %s to %s %s" % (current_var, cmd_effect, cmd_unset))
                return

            if (args['type'] == True):
                if (args['<cmd-name>'] is None):
                    for (key, value) in rawconfig['command'].items():
                        print(Fore.CYAN + "%s" % key)
                    return

                if (rawconfig['command'].__contains__(args['<cmd-name>']) is False):
                    print("please check your command name")
                    return

                cmd_exec = cmd_type(args['<cmd-name>'], args['<file-name>'])

                print("successed: type %s to %s" % (args['<cmd-name>'], cmd_exec))
                return

        else:
            ""
        break

    return

if __name__ == '__main__':
    main_function()
