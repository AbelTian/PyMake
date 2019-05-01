# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyMake 7.2.

Usage:
  pymake7.py source
  pymake7.py source file [ <source-path-file> ]
  pymake7.py source root [ <source-root-path> ]
  pymake7.py source config [ --add  ] [ <config-file-name> ]
  pymake7.py source config [ --del  ] [ <config-file-name> ]
  pymake7.py source config [ --mod  ] [ <config-file-name> ] [<new-config-file-name>]
  pymake7.py source config [ --switch  ] [ <config-file-name> ]
  pymake7.py source config [ --restore  ]
  pymake7.py source config [ --show ]
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
  pymake7.py program
  pymake7.py program root
  pymake7.py program file
  pymake7.py program configure
  pymake7.py program configure root
  pymake7.py program configure file
  pymake7.py get all
  pymake7.py get all ( info | information )
  pymake7.py get all ( stat | status )
  pymake7.py get all settings [ path | env | cmd ] [<name>] [-r | --raw] [-a | --all]
  pymake7.py get default exec root
  pymake7.py get exec root [ default | here ]
  pymake7.py initialize
  pymake7.py -------------------------------------------------------------
  pymake7.py port
  pymake7.py port root [ <source-config-root> ] [ to <target-config-root> ]
  pymake7.py port config [ <source-config-file> ] [ to <target-config-file> ]
  pymake7.py port file [ <source-path-file> ] [ to <target-path-file> ]
  pymake7.py port reset
  pymake7.py translate
  pymake7.py translate ( path | env | cmd )
  pymake7.py translate ( path | env | cmd ) <key-name> [ to <target-key-name> ] [ -f | --force ]
  pymake7.py translate ( path | env | cmd ) [ -a | --all ] [ -f | --force ]
  pymake7.py translate path-env-cmd [ -a | --all ] [ -f | --force ]
  pymake7.py translate all [ -a | --all ] [ -f | --force ]
  pymake7.py translate section
  pymake7.py translate section <section-name> [ to <target-section-name> ] [ -f | --force ]
  pymake7.py translate section [ -a | --all ] [ -f | --force ]
  pymake7.py -------------------------------------------------------------
  pymake7.py exec-with-params [ here | hh ] [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py execvp [ here | hh ] [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py ccvp [ here | hh ] [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py use <env-name> exec-with-params [ here | hh ] [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py use <env-name> execvp [ here | hh ] [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py use <env-name> ccvp [ here | hh ] [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py *************************************************************
  pymake7.py here exec-with-params [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py here execvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py here ccvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py here use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py here use <env-name> execvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py here use <env-name> ccvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py hh exec-with-params [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py hh execvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py hh ccvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py hh use <env-name> exec-with-params [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py hh use <env-name> execvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py hh use <env-name> ccvp [ <command-name> ] [ --params=<command-params> ... ]
  pymake7.py -------------------------------------------------------------
  pymake7.py backup [ here | hh ] [ <zip-file-name> ]
  pymake7.py here backup [ <zip-file-name> ]
  pymake7.py hh backup [ <zip-file-name> ]
  pymake7.py -------------------------------------------------------------
  pymake7.py import cmd [ hh | here ] [ <script-file> ] [ -f | --force ] [ --encoding=<encoding-name> ]
  pymake7.py import cmd [ hh | here ] [ -a | --all ] [ -f | --force ] [ --recursive ] [ --filter=<name-filter> ... ]
  pymake7.py *************************************************************
  pymake7.py here import cmd [ <script-file> ] [ -f | --force ] [ --encoding=<encoding-name> ]
  pymake7.py here import cmd [ -a | --all ] [ -f | --force ] [ --recursive ] [ --filter=<name-filter> ... ]
  pymake7.py hh import cmd [ <script-file> ] [ -f | --force ] [ --encoding=<encoding-name> ]
  pymake7.py hh import cmd [ -a | --all ] [ -f | --force ] [ --recursive ] [ --filter=<name-filter> ... ]
  pymake7.py -------------------------------------------------------------
  pymake7.py (-h | --help)
  pymake7.py --version

Command:
  source           switch to another source file
  source root      config root directory
  source config    config source conf file
  set path         path assemblage
  set env          set env variable
  set cmd          set cmd stream
  export           output private env variable to a bat file or sh file [default:current, env]
  type             output command to a bat file or sh file [default:cmd]
  see              check command stream
  ss               check command stream
  cmd              check command stream
  list             list config values, show command also too.
  set cur env      set default env, set current env.
  use              use selected env exec commands
  here             at here do exec commands e.g.
  hh               at here do exec commands e.g.
  exec             exec commands list.
  cc               exec commands list.
  have             check env or path or cmd item whether user has configured.
  has              check env or path or cmd item whether user has configured.
  clean            clean *_effect.sh *_unset.sh *_exec.sh, or .bat.
  program          pymake.py program information.
  get              lots of important information about pymake.py.
  initialize       if program crashed, user can use this command to reset.
  port             port from source to target .json file, configure source root and config file.
  translate        translate section from source to target, and other section.
  exec-with-params exec a command with params, it is also execvp and ccvp.
  backup           backup all env .json to a zip file.
  import           import user path or env or cmd to env .json file. example, import cmd [ <script-file>: x.bat x.cmd x.sh x.ps1 ... ]

Options:
  -h --help     Show this screen.
  --version     Show version.
  --add
  --del
  --mod         add or delete or modify a config or path
  --switch      switch to another source
  --show        display source config files
  --restore     reset to source config file pymake.json.
  -r, --raw     expand editing config values

  --encoding=<encoding-name>    script file encoding, support utf8, gbk, ... and so on. [default:utf8]
  --filter=<name-filter> ...    filter file name postfix, separated by |, example: .bat | .sh | .ps1.
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
            "root.prod": "${root}/d0-product",
            "root.sdk": "${root}/d1-sdks",
            "root.tool": "${root}/b0-toolskits",
            "root.build": "${root}/c0-buildstation",
            "root.test": "${root}/f0-test",
            "root.webrc": "${root}/e0-webrc",
            "cc": "${root.tool}/a0-compiler",
            "cmake.bin": "${cc}/CMake.app/Contents/bin",
            "pymake":"${cc}/PyMake",
            "qt": "${root.tool}/macLibraries/Qt",
            "qt5.9.version": "5.9.2",
            "qt5.9.ios": "${qt}/${qt5.9.version}/ios",
            "qt5.9.ios.bin": "${qt}/${qt5.9.version}/ios/bin",
            "qt5.9.clang": "${qt}/${qt5.9.version}/clang_64",
            "qt5.9.clang.bin": "${qt}/${qt5.9.version}/clang_64/bin",
            "qt5.9.android_arm": "${qt}/${qt5.9.version}/android_armv7",
            "qt5.9.android_arm.bin": "${qt}/${qt5.9.version}/android_armv7/bin",
            "qt5.9.android_x86": "${qt}/${qt5.9.version}/android_x86",
            "qt5.9.android_x86.bin": "${qt}/${qt5.9.version}/android_x86/bin",
            "qt5.8.android_x86": "${qt}/5.8/android_x86",
            "qt5.8.android_arm": "${qt}/5.8/android_armv7",
            "qt5.8.clang": "${qt}/5.8/clang_64",
            "qt5.8.ios": "${qt}/5.8/ios",
            "qt5.8.android_x86.bin": "${qt}/5.8/android_x86/bin",
            "qt5.8.android_arm.bin": "${qt}/5.8/android_armv7/bin",
            "qt5.8.clang.bin": "${qt}/5.8/clang_64/bin",
            "qt5.8.ios.bin": "${qt}/5.8/ios/bin",
            "qt4.version": "4.8.7",
            "qt4.8.clang": "${qt}/${qt4.version}/clang_64",
            "qt4.8.clang.bin": "${qt}/${qt4.version}/clang_64/bin",
            "qt4.8.clang.lib": "${qt}/${qt4.version}/clang_64/lib",
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
            "ios.simulator.sysroot": "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk",
            "xcode.bin": "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin",
            "mac.sysroot": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk"
        },
        "environ": {
            "android.mobile": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.9.android_arm.bin}",
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
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.android_arm}",
                "QTSPEC": "-spec android-g++",
                "QTCONFIG": "",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar",
                "PYMAKE_MYNAME": "T.D.R",
                "a_special_var_const": "hello world",
                "QKIT": "ANDROID",
                "QSYS": "Android"
            },
            "android.x86": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.9.android_x86.bin}",
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
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.android_x86}",
                "QTSPEC": "-spec android-g++",
                "QTCONFIG": "CONFIG+=x86",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar",
                "QKIT": "ANDROIDX86",
                "QSYS": "AndroidX86"
            },
            "ios": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.9.ios.bin}"
                ],
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.ios}",
                "QTSPEC": "-spec macx-ios-clang",
                "QTCONFIG": "CONFIG+=iphoneos CONFIG+=device -after QMAKE_MAC_XCODE_SETTINGS+=qteam qteam.name=DEVELOPMENT_TEAM qteam.value=4EGMLT3G6T",
                "QKIT": "iOS",
                "QSYS": "iOS"
            },
            "iossimulator": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.9.ios.bin}"
                ],
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.ios}",
                "QTSPEC": "-spec macx-ios-clang",
                "QTCONFIG": "CONFIG+=iphonesimulator CONFIG+=simulator",
                "QKIT": "iOSSimulator",
                "QSYS": "iOSSimulator"
            },
            "qt4": {
                "path+": [
                    "${cmake.bin}",
                    "${qt4.8.clang.bin}"
                ],
                "QTVERSION": "${qt4.version}",
                "QTDIR": "${qt4.8.clang}",
                "QTSPEC": "-spec macx-llvm",
                "QTCONFIG": "CONFIG+=x86_64",
                "QKIT": "macOS",
                "QSYS": "MacOS"
            },
            "macos": {
                "path+": [
                    "${cmake.bin}",
                    "${qt5.9.clang.bin}"
                ],
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.clang}",
                "QTSPEC": "-spec macx-clang",
                "QTCONFIG": "CONFIG+=x86_64",
                "QKIT": "macOS",
                "QSYS": "macOS"
            },
            "current": "macos"
        },
        "variable-assemblage": [
            "QQt",
            "LibQQt",
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
            "${source-path}/configure -prefix ${install-path} -hostprefix ${install-path} -xplatform android-g++ -release -nomake tests -nomake examples -android-ndk $ANDROID_NDK_ROOT -android-sdk $ANDROID_SDK_ROOT -android-ndk-host $ANDROID_NDK_HOST -android-toolchain-version $ANDROID_NDK_TOOLCHAIN_VERSION -skip qtwebkit-examples -no-warnings-are-errors",
            "${qt5.path.source}/configure -prefix ${qt5.path.install} -hostprefix ${qt5.path.install} -xplatform android-g++ -release -nomake tests -nomake examples -android-ndk $ANDROID_NDK_ROOT -android-sdk $ANDROID_SDK_ROOT -android-ndk-host $ANDROID_NDK_HOST -android-toolchain-version $ANDROID_NDK_TOOLCHAIN_VERSION -skip qtwebkit-examples -no-warnings-are-errors"
        ],
        "command": {
            "test":[
                "echo $(pwd)"
            ],
            "qqt.build": [
                "src_path=${root.src}/LibQQt",
                "src=${root.src}/LibQQt/QQt.pro",
                "build=${root.build}/QQt/${QSYS}/${QTVERSION}/Debug",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "qmake ${src} ${QTSPEC} CONFIG+=debug CONFIG+=qml_debug ${QTCONFIG} && make qmake_all",
                "make -j4"
            ],
            "qqt.clean": [
                "src=${root.src}/LibQQt/QQt.pro",
                "build=${root.build}/QQt/${QSYS}/${QTVERSION}/Debug",
                "cd $build",
                "make clean"
            ],
            "qt": [
                "open \"/Applications/Qt Creator.app\""
            ],
            "cmake": [
                "open ${root.tool}/macCompilers/CMake.app"
            ],
            "prod": [
                "open ${root.prod}/ProductExecTool/macOS/ProductExecTool_debug.app"
            ],
            "libtool": [
                "open ${root.prod}/AddLibraryTool/macOS/AddLibraryTool_debug.app"
            ],
            "qt.check": [
                "src=${root.tool}/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=${root.build}/qt4.8.7",
                "install=${root.tool}/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure --help"
            ],
            "qt4.build": [
                "src=${root.tool}/z0-Source/qt",
                "build=${root.build}/qt",
                "install=${root.tool}/macLibraries/Qt/4.8/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "CXXFLAGS=-stdlib=libc++",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "qt4.8.7.build": [
                "src=${root.tool}/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=${root.build}/qt4.8.7",
                "install=${root.tool}/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "qtsoap.build": [
                "src=/Users/abel/Develop/c1-webrc/qt-solutions/qtsoap",
                "build=${root.build}/qtsoap",
                "install=/Users/abel/Develop/d1-product/QtSoap",
                "cd $build",
                "${src}/configure -library"
            ],
            "qqt.push": [
                "src=${root.src}/LibQQt",
                "cd $src",
                "git push",
                "git push --tag"
            ],
            "qqt.pull": [
                "src=${root.src}/LibQQt",
                "cd $src",
                "git pull"
            ],
            "qqt.cloc": [
                "src=${root.src}/LibQQt",
                "cd $src",
                "perl ${pymake}/demo/cloc-1.74.pl  .",
                "date"
            ],
            "android.sdk": [
                "${root.tool}/macAndroidLibraries/android-sdk-macosx/tools/android"
            ]
        }
    }

    # record current directory [pwd, execute path]
    pymakeworkpath = os.getcwd()
    #print( "pymake work path:", pymakeworkpath )

    # record pymake file directory [program file path]
    pymakefilepath = os.path.split(os.path.realpath(__file__))[0]
    #print( "pymake file path:", pymakefilepath )

    # record pymake user source root [env, *.json] [ + auto create ]
    pymakesourceroot = pymakefilepath + os.path.sep + 'UserSource'
    if (not os.path.exists(pymakesourceroot)):
        os.makedirs(pymakesourceroot)
    #print( "pymake user source path:", pymakesourceroot )

    #record default user source config file name
    pymakedefaultsourcefile = 'pymake.json'
    #print( "pymake user default source file:", pymakedefaultsourcefile )

    # record pymake user shell root [ dynamic work path ] [ ignored -> v7.2 ]
    pymakeshellroot = pymakesourceroot + os.path.sep + 'UserShell'
    if (not os.path.exists(pymakeshellroot)):
        os.makedirs(pymakeshellroot)
    #print( "pymake user shell path:", pymakeshellroot )

    """
    [pymake]
    [source]
    root = ~/.pymake
    config = pymake.json
    """
    userroot = getuserroot()
    configroot = getconfigroot()
    plat = getplatform()
    #record pymake configure directory. [ in user config path ]
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
        conf.set('source', 'config', pymakedefaultsourcefile)
        conf.write(open(pymakeini, 'w'))

    args = docopt(__doc__, version='pymake7.py v7.2')
    #print(args)

    #initialize
    while (True):
        if(args['initialize'] is True):
            conf.set('source', 'root', pymakesourceroot)
            conf.set('source', 'config', pymakedefaultsourcefile)
            conf.write(open(pymakeini, 'w'))
            r = conf.get('source', 'root')
            f = conf.get('source', 'config')
            print("SOURCE        : %s%s%s" % (r, os.path.sep, f))
            print("SOURCE ROOT   : %s" % (r))
            print("SOURCE CONFIG : %s" % (f))
            print("successed")
            return
        else:
            ""
        break

    # init pymake.json in sourceroot [ + program create ]
    #record user source root directory
    sourceroot = conf.get('source', 'root')
    #record source config file name
    sourcefile = conf.get('source', 'config')
    #record source config file
    sourceconfigfile = sourceroot + os.path.sep + sourcefile
    #print("root: %s, config: %s" % (sourceroot, sourcefile))
    #print("use source config: %s" % (sourceconfigfile) )
    #record default source config file
    defaultsourceconfigfile = sourceroot + os.path.sep + pymakedefaultsourcefile
    #print ("root: %s, default config: %s" % (sourceroot, pymakedefaultsourcefile))
    #print("default source config: %s" % (defaultsourceconfigfile) )

    if (not os.path.exists(sourceroot)):
        os.makedirs(sourceroot)
    os.chdir(sourceroot)
    if (os.path.exists(sourceroot)):
        if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)
            and os.path.abspath(sourceroot) != os.path.abspath(pymakefilepath)):
            if (not os.path.exists(defaultsourceconfigfile)):
                writeJsonData(defaultsourceconfigfile, d)

    #record source config file postfix
    pymakesuffix = '.json'
    #source
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
                #path0 = args['<source-path-file>']
                #path1 = os.path.relpath(args['<source-path-file>'], pymakeworkpath)
                #path2 = os.path.relpath(args['<source-path-file>'], pymakesourceroot)
                #path3 = os.path.relpath(args['<source-path-file>'], pymakeshellroot)
                #print ("source config file: %s" % path0)
                #print ("rel path: pwd     : %s" % path1)
                #print ("rel path: src     : %s" % path2)
                #print ("rel path: exec    : %s" % path3)
                #print ("real path: %s" % os.path.realpath(path0))
                #print ("real path: %s" % os.path.realpath(path1))
                #print ("real path: %s" % os.path.realpath(path2))
                #print ("real path: %s" % os.path.realpath(path3))
                #print ("abspath: %s" % os.path.abspath(path0))
                #print ("abspath: %s" % os.path.abspath(path1))
                #print ("abspath: %s" % os.path.abspath(path2))
                #print ("abspath: %s" % os.path.abspath(path3))
                if(not args['<source-path-file>'].endswith(pymakesuffix)):
                    print("you can't set an un.json file.")
                    return
                if(os.path.isdir(args['<source-path-file>'])):
                    print("please input an abspath .json file.")
                    return
                if(os.path.islink(args['<source-path-file>'])):
                    print("your file path cant be a link.")
                    return
                if(not os.path.isabs(args['<source-path-file>'])):
                    print("your file path is not an abspath.")
                    return
                r = os.path.split(os.path.realpath(args['<source-path-file>']))[0]
                f = os.path.split(os.path.realpath(args['<source-path-file>']))[1]
                conf.set('source', 'root', r)
                conf.set('source', 'config', f)
                conf.write(open(pymakeini, 'w'))
                print ("change source to %s" % os.path.realpath(args['<source-path-file>']))
                print ("source root    : %s" % r)
                print ("source config  : %s" % f)
            else:
                r = conf.get('source', 'root')
                f = conf.get('source', 'config')
                print ("%s%s%s" % (r, os.path.sep, f))

            # check source status
            # record user source root directory
            sourceroot = conf.get('source', 'root')
            # record source config file name
            sourcefile = conf.get('source', 'config')
            # record source config file
            sourceconfigfile = sourceroot + os.path.sep + sourcefile
            # print ("root: %s config: %s" % (sourceroot, sourcefile))
            # print("use source config: %s" % (sourceconfigfile) )
            if (not os.path.exists(sourceroot)):
                os.makedirs(sourceroot)
            os.chdir(sourceroot)
            if (os.path.exists(sourceroot)):
                if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)
                    and os.path.abspath(sourceroot) != os.path.abspath(pymakefilepath)):
                    if (not os.path.exists(sourceconfigfile)):
                        writeJsonData(sourceconfigfile, d)
            return
        else:
            ''
        break

    # check source root directory
    if (os.path.exists(sourceroot) is False):
        print("You have changed sourceroot manually, please change it using source command")
        return

    # check source root .json file
    if (os.path.abspath(sourceroot) == os.path.abspath(pymakeroot) or
            os.path.abspath(sourceroot) == os.path.abspath(pymakefilepath)):
        print ("I checked you use pymakeroot or pymakefileroot to be sourceroot, suggestting you use source command changing one.")
        print ("this progrom can store building env and building command forever, please repleace source root then using me.")
        return
    elif (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)):
        if (not os.path.exists(defaultsourceconfigfile)):
            writeJsonData(defaultsourceconfigfile, d)
            print ("initialize pymake.json in source root %s." % sourceroot)
        if(not os.path.exists(sourceconfigfile)):
            print ("source config file %s is not existed." % sourceconfigfile)
            print ("You can use source command to fix it.")
            return

    # I set this,
    # pymake default execute user bat/sh in pymakeshellroot,
    # user can use here param to restrict exec action.
    # cd user shell root [ default shell execute path ]
    pymakeshellroot = sourceroot
    os.chdir(pymakeshellroot)

    #backup
    while (True):
        if ( args['backup'] is True ):
            import zipfile
            os.chdir(sourceroot)
            if(args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)

            if(args['<zip-file-name>'] is None):
                files = os.listdir(os.getcwd())
                for f in files:
                    if (f.endswith('.zip')):
                        print(f)
                return

            file = os.path.realpath(args['<zip-file-name>'])
            if (file.endswith('.zip') is False):
                print("please use a .zip file name.")
                return

            os.chdir(sourceroot)

            files = os.listdir(os.getcwd())
            if ( files.__len__() < 1 ):
                print("has no .json file in %s" % sourceroot)
                return

            ziphandle = zipfile.ZipFile(file, 'w')
            for f in files:
                if (f.endswith('.json')):
                    print(f)
                    ziphandle.write(f, compress_type=zipfile.ZIP_DEFLATED)
            ziphandle.close()
            return
        else:
            ''
        break

    #port translate function
    portdefaultsourceconfig = pymakedefaultsourcefile
    portdefaulttargetconfig = 'temporary-target.json'
    portiniconfig = 'port.ini'
    portinifile = os.path.join(pymakeshellroot, "port.ini")
    def init_portconf():
        portconf = MyConfigParser()
        portconf.read(portinifile)
        if (not portconf.has_section('port')):
            portconf.add_section('port')
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'sourceroot')):
            portconf.set('port', 'sourceroot', sourceroot)
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'sourceconfig')):
            portconf.set('port', 'sourceconfig', portdefaultsourceconfig)
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'targetroot')):
            portconf.set('port', 'targetroot', sourceroot)
            portconf.write(open(portinifile, 'w'))
        if (not portconf.has_option('port', 'targetconfig')):
            portconf.set('port', 'targetconfig', portdefaulttargetconfig)
            portconf.write(open(portinifile, 'w'))
        #print (portinifile)
        #print ("sourceroot  :", portconf['port']['sourceroot'])
        #print ("sourceconfig:", portconf['port']['sourceconfig'])
        #print ("targetroot  :", portconf['port']['targetroot'])
        #print ("targetconfig:", portconf['port']['targetconfig'])
        return portconf, portinifile

    def init_portconfig(portconf = MyConfigParser()):
        portsourceconfigfile=os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig'])
        porttargetconfigfile=os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig'])
        d_temp = {
            "path-assemblage": {
            },
            "environ":{
                "default":{
                    "path+": [
                    ]
                },
                "current": "default"
            },
            "command":{
            }
        }
        if(not os.path.exists(portsourceconfigfile)):
            writeJsonData(portsourceconfigfile, d_temp)
        if(not os.path.exists(porttargetconfigfile)):
            writeJsonData(porttargetconfigfile, d_temp)

        srcsize = os.path.getsize(portsourceconfigfile)
        tarsize = os.path.getsize(porttargetconfigfile)
        if(srcsize < 166):
            writeJsonData(portsourceconfigfile, d_temp)
        if(tarsize < 166):
            writeJsonData(porttargetconfigfile, d_temp)

        portconfig = readJsonData(portsourceconfigfile)
        porttargetconfig = readJsonData(porttargetconfigfile)

        #hard
        if(portconfig.__contains__("path-assemblage") is False):
            portconfig['path-assemblage']={}
            writeJsonData(portsourceconfigfile, portconfig)
        if(portconfig.__contains__("environ") is False):
            portconfig['environ']={}
            writeJsonData(portsourceconfigfile, portconfig)
        if (portconfig.__contains__("command") is False):
            portconfig['command'] = {}
            writeJsonData(portsourceconfigfile, portconfig)

        #soft
        #if(portconfig['environ'].__contains__("default") is False):
        #    portconfig['environ']['default']={"path+":[]}
        #    writeJsonData(portsourceconfigfile, portconfig)
        #if(portconfig['environ']['default'].__contains__("path+") is False):
        #    portconfig['environ']['default']['path+']=[]
        #    writeJsonData(portsourceconfigfile, portconfig)
        #if(portconfig['environ'].__contains__("current") is False):
        #    portconfig['environ']['current']='default'
        #    writeJsonData(portsourceconfigfile, portconfig)

        #hard
        if(porttargetconfig.__contains__("path-assemblage") is False):
            porttargetconfig['path-assemblage']={}
            writeJsonData(porttargetconfigfile, porttargetconfig)
        if(porttargetconfig.__contains__("environ") is False):
            porttargetconfig['environ']={}
            writeJsonData(porttargetconfigfile, porttargetconfig)
        if(porttargetconfig.__contains__("command") is False):
            porttargetconfig['command']={}
            writeJsonData(porttargetconfigfile, porttargetconfig)

        #soft
        order_of_keys = porttargetconfig['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        if (list_of_tuples.__len__() < 2):
            if(porttargetconfig['environ'].__contains__("default") is False):
                porttargetconfig['environ']['default']={"path+":[]}
                writeJsonData(porttargetconfigfile, porttargetconfig)
            if(porttargetconfig['environ']['default'].__contains__("path+") is False):
                porttargetconfig['environ']['default']['path+']=[]
                writeJsonData(porttargetconfigfile, porttargetconfig)
            if(porttargetconfig['environ'].__contains__("current") is False):
                porttargetconfig['environ']['current']='default'
                writeJsonData(porttargetconfigfile, porttargetconfig)

        #move 'current' to be last key
        order_of_keys = porttargetconfig['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        #print(order_of_keys)
        #print(list_of_tuples)
        #print(list_of_tuples[-1])
        if(list_of_tuples[-1] != 'current'):
            #print(".....")
            current_var = porttargetconfig['environ']['current']
            porttargetconfig['environ'].__delitem__('current')
            porttargetconfig['environ']['current']=current_var
            writeJsonData(porttargetconfigfile, porttargetconfig)
        return portconfig, porttargetconfig

    # port translate
    while (True):
        if (args['port'] is True):
            portconf, portinifile = init_portconf()
            if (args['root'] is True):
                if( args['<source-config-root>'] is not None ):
                    if (not os.path.isdir(args['<source-config-root>'])
                        or os.path.islink(args['<source-config-root>'])
                        or not os.path.isabs(args['<source-config-root>'])):
                        print("please input a legal source abspath.")
                        return
                    portconf.set('port', 'sourceroot', args['<source-config-root>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: source config root is %s." % portconf['port']['sourceroot'])

                if( args['<target-config-root>'] is not None ):
                    if (not os.path.isdir(args['<target-config-root>'])
                        or os.path.islink(args['<target-config-root>'])
                        or not os.path.isabs(args['<target-config-root>'])):
                        print("please input a legal target abspath.")
                        return
                    portconf.set('port', 'targetroot', args['<target-config-root>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: target config root is %s." % portconf['port']['targetroot'])

                print("port: source root is %s" % portconf['port']['sourceroot'])
                print("port: target root is %s" % portconf['port']['targetroot'])
            elif (args['config'] is True):
                if( args['<source-config-file>'] is not None ):
                    if (not args['<source-config-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<source-config-file>'])
                        or os.path.islink(args['<source-config-file>'])
                        or os.path.isabs(args['<source-config-file>'])):
                        print("please input a real source .json file.")
                        return
                    portconf.set('port', 'sourceconfig', args['<source-config-file>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: source config file is %s." % portconf['port']['sourceconfig'])

                if( args['<target-config-file>'] is not None ):
                    if (not args['<target-config-file>'].endswith(pymakesuffix)
                        or os.path.isdir(args['<target-config-file>'])
                        or os.path.islink(args['<target-config-file>'])
                        or os.path.isabs(args['<target-config-file>'])):
                        print("please input a real target .json file.")
                        return
                    portconf.set('port', 'targetconfig', args['<target-config-file>'])
                    portconf.write(open(portinifile, 'w'))
                    #print("port: target config file is %s." % portconf['port']['targetconfig'])

                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
            elif (args['file'] is True):
                if(args['<source-path-file>'] is not None):
                   if( not args['<source-path-file>'].endswith(pymakesuffix)
                       or os.path.isdir(args['<source-path-file>'])
                       or os.path.islink(args['<source-path-file>'])
                       or not os.path.isabs(args['<source-path-file>'])):
                        print("please input a legal source abspath .json file.")
                        return
                   r = os.path.split(os.path.realpath(args['<source-path-file>']))[0]
                   f = os.path.split(os.path.realpath(args['<source-path-file>']))[1]
                   portconf.set('port', 'sourceroot', r)
                   portconf.set('port', 'sourceconfig', f)
                   portconf.write(open(portinifile, 'w'))

                if(args['<target-path-file>'] is not None):
                   if(not args['<target-path-file>'].endswith(pymakesuffix)
                      or os.path.isdir(args['<target-path-file>'])
                      or os.path.islink(args['<target-path-file>'])
                      or not os.path.isabs(args['<target-path-file>'])):
                        print("please input a legal target abspath .json file.")
                        return
                   r = os.path.split(os.path.realpath(args['<target-path-file>']))[0]
                   f = os.path.split(os.path.realpath(args['<target-path-file>']))[1]
                   portconf.set('port', 'targetroot', r)
                   portconf.set('port', 'targetconfig', f)
                   portconf.write(open(portinifile, 'w'))

                print("port: source file   is %s" % os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig']))
                print("port: source root   is %s" % portconf['port']['sourceroot'])
                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target file   is %s" % os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig']))
                print("port: target root   is %s" % portconf['port']['targetroot'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
            elif (args['reset'] is True):
                portconf.set('port', 'sourceroot', sourceroot)
                portconf.set('port', 'sourceconfig', pymakedefaultsourcefile)
                portconf.set('port', 'targetroot', sourceroot)
                portconf.set('port', 'targetconfig', portdefaulttargetconfig)
                portconf.write(open(portinifile, 'w'))
                print("port: source file   is %s" % os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig']))
                print("port: source root   is %s" % portconf['port']['sourceroot'])
                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target file   is %s" % os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig']))
                print("port: target root   is %s" % portconf['port']['targetroot'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
                print("successed")
            else:
                print("port: source file   is %s" % os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig']))
                print("port: source root   is %s" % portconf['port']['sourceroot'])
                print("port: source config is %s" % portconf['port']['sourceconfig'])
                print("port: target file   is %s" % os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig']))
                print("port: target root   is %s" % portconf['port']['targetroot'])
                print("port: target config is %s" % portconf['port']['targetconfig'])
            return
        elif (args['translate'] is True):
            import itertools
            portconf, portinifile = init_portconf()
            portconfig, porttargetconfig = init_portconfig(portconf)
            portsourceconfigfile = os.path.join(portconf['port']['sourceroot'], portconf['port']['sourceconfig'])
            porttargetconfigfile = os.path.join(portconf['port']['targetroot'], portconf['port']['targetconfig'])
            print("translate: source file   is %s" % portsourceconfigfile)
            print("translate: source root   is %s" % portconf['port']['sourceroot'])
            print("translate: source config is %s" % portconf['port']['sourceconfig'])
            print("translate: target file   is %s" % porttargetconfigfile)
            print("translate: target root   is %s" % portconf['port']['targetroot'])
            print("translate: target config is %s" % portconf['port']['targetconfig'])
            print("---------------------------------------------------------------------")
            print(Fore.MAGENTA + "%-30s%-30s%s" % ( "[source] " + portconf['port']['sourceconfig'], "[target] " + portconf['port']['targetconfig'], "[status]"))

            def translate_section(section_name = None):
                if(section_name is None):
                    return

                masterkey = section_name

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if (args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                # print("src key:%s" % srckey)

                if (args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                # print("tar key:%s" % tarkey)

                if (args['<key-name>'] is not None
                    or args['<target-key-name>'] is not None):
                    # print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if (args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]" + existedflag + "[FORCE]"))
                        return

                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]" + existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]" + existedflag))
                    return

                if (args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if (args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag + "[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                # print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                # print(keylist1)
                # print(keylist2)
                count = 1
                for (key1, key2) in itertools.zip_longest(keylist1, keylist2):
                    if (key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if (key2 is None):
                        key2 = str("[EMPTY] %s" % count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return

            def translate_envsection(section_name = None):
                if(section_name is None):
                    return

                masterkey = section_name

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if(args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                #print("src key:%s" % srckey)

                if(args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                #print("tar key:%s" % tarkey)

                if(args['<key-name>'] is not None
                   or args['<target-key-name>'] is not None):
                    #print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if(args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]"+existedflag+"[FORCE]"))
                        return

                    if(porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]"+existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]"+existedflag))
                    return

                if(args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if(args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]"+existedflag+"[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    tarkey = ''
                    if (args['-f'] or args['--force'] is True):
                        tarkey = portconfig[masterkey]['current']
                    else:
                        tarkey = porttargetconfig[masterkey]['current']
                    porttargetconfig[masterkey].__delitem__('current')
                    porttargetconfig[masterkey]['current'] = tarkey
                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return

            if (args['path'] is True):
                print(Fore.CYAN + "path-assemblage:")

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if(args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                #print("src key:%s" % srckey)

                if(args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                #print("tar key:%s" % tarkey)

                if(args['<key-name>'] is not None
                   or args['<target-key-name>'] is not None):
                    #print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig['path-assemblage'].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if(args['-f'] or args['--force'] is True):
                        if (portconfig['path-assemblage'].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig['path-assemblage'][tarkey] = copy.deepcopy(portconfig['path-assemblage'][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]"+existedflag+"[FORCE]"))
                        return

                    if(porttargetconfig['path-assemblage'].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]"+existedflag))
                        return
                    else:
                        if (portconfig['path-assemblage'].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig['path-assemblage'][tarkey] = copy.deepcopy(portconfig['path-assemblage'][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]"+existedflag))
                    return

                if(args['-a'] or args['--all'] is True):
                    for key in portconfig['path-assemblage'].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig['path-assemblage'].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if(args['-f'] or args['--force'] is True):
                            porttargetconfig['path-assemblage'][key] = copy.deepcopy(portconfig['path-assemblage'][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]"+existedflag+"[FORCE]"))
                        else:
                            if (porttargetconfig['path-assemblage'].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig['path-assemblage'][key] = copy.deepcopy(portconfig['path-assemblage'][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig['path-assemblage'].keys():
                    keylist1.append(key)
                for key in porttargetconfig['path-assemblage'].keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            elif (args['env'] is True):
                print(Fore.CYAN + "environ:")
                masterkey = "environ"

                srckey = ''
                tarkey = ''
                #print(args['<key-name>'], args['<target-key-name>'])
                if(args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                #print("src key:%s" % srckey)

                if(args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                #print("tar key:%s" % tarkey)

                if(args['<key-name>'] is not None
                   or args['<target-key-name>'] is not None):
                    #print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if(args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]"+existedflag+"[FORCE]"))
                        return

                    if(porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]"+existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        porttargetconfig[masterkey].__delitem__('current')
                        porttargetconfig[masterkey]['current'] = tarkey
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]"+existedflag))
                    return

                if(args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if(args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]"+existedflag+"[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    tarkey = ''
                    if (args['-f'] or args['--force'] is True):
                        tarkey = portconfig[masterkey]['current']
                    else:
                        tarkey = porttargetconfig[masterkey]['current']
                    porttargetconfig[masterkey].__delitem__('current')
                    porttargetconfig[masterkey]['current'] = tarkey
                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            elif (args['cmd'] is True):
                print(Fore.CYAN + "command:")
                masterkey = "command"

                srckey = ''
                tarkey = ''
                # print(args['<key-name>'], args['<target-key-name>'])
                if (args['<key-name>'] is not None):
                    srckey = args['<key-name>']
                # print("src key:%s" % srckey)

                if (args['<target-key-name>'] is not None):
                    tarkey = args['<target-key-name>']
                else:
                    tarkey = srckey
                # print("tar key:%s" % tarkey)

                if (args['<key-name>'] is not None
                    or args['<target-key-name>'] is not None):
                    # print("src key:%s, tar key:%s" % (srckey, tarkey))

                    existedflag = '[       ]'
                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if (args['-f'] or args['--force'] is True):
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]" + existedflag + "[FORCE]"))
                        return

                    if (porttargetconfig[masterkey].__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]" + existedflag))
                        return
                    else:
                        if (portconfig[masterkey].__contains__(srckey) is False):
                            print("please ensure the source key %s is existed." % srckey)
                            return
                        porttargetconfig[masterkey][tarkey] = copy.deepcopy(portconfig[masterkey][srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]" + existedflag))
                    return

                if (args['-a'] or args['--all'] is True):
                    for key in portconfig[masterkey].keys():
                        existedflag = '[       ]'
                        if (porttargetconfig[masterkey].__contains__(key)):
                            existedflag = '[EXISTED]'

                        if (args['-f'] or args['--force'] is True):
                            porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag + "[FORCE]"))
                        else:
                            if (porttargetconfig[masterkey].__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[masterkey][key] = copy.deepcopy(portconfig[masterkey][key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                # print(portconfig.keys())
                for key in portconfig[masterkey].keys():
                    keylist1.append(key)
                for key in porttargetconfig[masterkey].keys():
                    keylist2.append(key)
                # print(keylist1)
                # print(keylist2)
                count = 1
                for (key1, key2) in itertools.zip_longest(keylist1, keylist2):
                    if (key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if (key2 is None):
                        key2 = str("[EMPTY] %s" % count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            elif (args['path-env-cmd'] or args['all'] is True):
                print(Fore.CYAN + "path-assemblage:")
                masterkey = "path-assemblage"
                translate_section(masterkey)

                print(Fore.CYAN + "environ:")
                masterkey = "environ"
                translate_envsection(masterkey)

                print(Fore.CYAN + "command:")
                masterkey = "command"
                translate_section(masterkey)
            elif (args['section'] is True):
                print(Fore.CYAN + "section:")
                srckey = ''
                tarkey = ''
                #print(args['<section-name>'], args['<target-section-name>'])
                if (args['<section-name>'] is not None):
                    srckey = args['<section-name>']
                #print("src section:%s" % srckey)

                if (args['<target-section-name>'] is not None):
                    tarkey = args['<target-section-name>']
                else:
                    tarkey = srckey
                #print("tar section:%s" % tarkey)

                if (args['<section-name>'] is not None
                    or args['<target-section-name>'] is not None):
                    #print("src section:%s, tar section:%s" % (srckey, tarkey))

                    if(tarkey == "path-assemblage"
                       or tarkey == "environ"
                       or tarkey == "command"):
                        print("please ensure your target section name, it cant be pymake's section.")
                        return

                    existedflag = '[       ]'
                    if (porttargetconfig.__contains__(tarkey)):
                        existedflag = '[EXISTED]'

                    if (args['-f'] or args['--force'] is True):
                        if (portconfig.__contains__(srckey) is False):
                            print("please ensure the source section %s is existed." % srckey)
                            return
                        porttargetconfig[tarkey] = copy.deepcopy(portconfig[srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS]" + existedflag + "[FORCE]"))
                        return

                    if (porttargetconfig.__contains__(tarkey)):
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[CANCEL ]" + existedflag))
                        return
                    else:
                        if (portconfig.__contains__(srckey) is False):
                            print("please ensure the source section %s is existed." % srckey)
                            return
                        porttargetconfig[tarkey] = copy.deepcopy(portconfig[srckey])
                        writeJsonData(porttargetconfigfile, porttargetconfig)
                        print(Fore.MAGENTA + "%-30s%-30s%s" % (srckey, tarkey, "[SUCCESS][     ]" + existedflag))
                    return

                if (args['-a'] or args['--all'] is True):
                    for key in portconfig.keys():
                        existedflag = '[       ]'
                        if (porttargetconfig.__contains__(key)):
                            existedflag = '[EXISTED]'

                        if (key == "path-assemblage"
                            or key == "environ"
                            or key == "command"):
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag + "[RESERVED]"))
                            continue

                        if (args['-f'] or args['--force'] is True):
                            porttargetconfig[key] = copy.deepcopy(portconfig[key])
                            print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag + "[FORCE]"))
                        else:
                            if (porttargetconfig.__contains__(key)):
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[CANCEL ]" + existedflag))
                            else:
                                porttargetconfig[key] = copy.deepcopy(portconfig[key])
                                print(Fore.MAGENTA + "%-30s%-30s%s" % (key, key, "[SUCCESS]" + existedflag))

                    writeJsonData(porttargetconfigfile, porttargetconfig)
                    return

                keylist1 = []
                keylist2 = []
                # print(portconfig.keys())
                for key in portconfig.keys():
                    keylist1.append(key)
                for key in porttargetconfig.keys():
                    keylist2.append(key)
                # print(keylist1)
                # print(keylist2)
                count = 1
                for (key1, key2) in itertools.zip_longest(keylist1, keylist2):
                    if (key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if (key2 is None):
                        key2 = str("[EMPTY] %s" % count)
                        count += 1
                    print("%-30s%-30s%s" % (key1, key2, '[NORMAL]'))
                return
            else:
                print(Fore.CYAN + "all sections:")
                keylist1 = []
                keylist2 = []
                #print(portconfig.keys())
                for key in portconfig.keys():
                    keylist1.append(key)
                for key in porttargetconfig.keys():
                    keylist2.append(key)
                #print(keylist1)
                #print(keylist2)
                count = 1
                for (key1,key2) in itertools.zip_longest(keylist1, keylist2):
                    if(key1 is None):
                        key1 = str("[EMPTY] %s" % count)
                        count += 1
                    if(key2 is None):
                        key2 = str("[EMPTY] %s" %count)
                        count += 1
                    print("%-30s%-30s%s" % (key1,key2,'[NORMAL]'))
            return
        else:
            ''
        break

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

    # clean *_effect *_unset *_exec .bat[.sh]
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

    config = readJsonData(sourceconfigfile)
    #print(config)

    # import command
    while (True):
        if (args['import'] is True):
            import itertools
            if(args['cmd'] is True):
                os.chdir(sourceroot)
                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)

                if (args['<script-file>'] is not None):
                    #print("%-30s %-5s %-5s" % (args['<script-file>'], os.path.isdir(args['<script-file>']), os.path.islink(args['<script-file>'])))
                    if (os.path.isdir(args['<script-file>'])):
                        print(Fore.CYAN + "%-30s%-30s" % ("[file] ", "[command] "))
                        keylist1 = []
                        keylist2 = []
                        for key in os.listdir(args['<script-file>']):
                            keylist1.append(key)
                        for key in config['command'].keys():
                            keylist2.append(key)

                        dirlist = []
                        for (key) in keylist1:
                            # print("%-30s %-5s %-5s" % (key, os.path.isdir(key), os.path.islink(key)))
                            if (os.path.isdir(args['<script-file>'] + os.path.sep + key)
                                or os.path.islink(args['<script-file>'] + os.path.sep + key)):
                                dirlist.append(key)
                        #print(dirlist)

                        for key in dirlist:
                            keylist1.remove(key)

                        # print(keylist1)
                        # print(keylist2)
                        count2 = 1
                        for (key1, key2) in itertools.zip_longest(keylist1, keylist2, fillvalue=""):
                            if (key1 is not ""):
                                key1 = str("%s" % (key1))
                            if (key2 is not ""):
                                key2 = str("%-4s%s" % (count2, key2))
                                count2 += 1
                            print("%-30s%-30s" % (key1, key2))
                        return

                    if (os.path.isdir(args['<script-file>'])
                        or os.path.islink(args['<script-file>'])):
                        print("please input a legal script file.")
                        return

                    useencoding = 'utf8'
                    if(args['--encoding'] is not None):
                        useencoding = args['--encoding']

                    local_path = os.path.realpath(args['<script-file>'])
                    #print(os.path.dirname(local_path))
                    #print(os.path.basename(local_path) )
                    #print(os.path.splitext(os.path.basename(local_path))[0])
                    #print(os.path.splitext(os.path.basename(local_path))[1])
                    if(os.path.exists(local_path) is False):
                        print('failed: %s is not existed.' % args['<script-file>'])
                        return

                    command_name = os.path.splitext(os.path.basename(local_path))[0]

                    #print(args)
                    if(config['command'].__contains__(command_name) is True):
                        if ( args['-f'] or args['--force'] is True):
                            #print('-f')
                            #set in force
                            command_content = []
                            with open(local_path, 'r', encoding=useencoding) as f:
                                for l in f.readlines():
                                    command_content.append(l.rstrip('\r').rstrip('\n'))
                            config['command'][command_name] = command_content
                            writeJsonData(sourceconfigfile, config)
                            print('successed')
                            return
                        print("failed: command %s is existed." % command_name)
                        return

                    # set in
                    command_content = []
                    with open(local_path, 'r', encoding=useencoding) as f:
                        for l in f.readlines():
                            command_content.append(l.rstrip('\r').rstrip('\n'))
                    config['command'][command_name] = command_content
                    writeJsonData(sourceconfigfile, config)
                    print('successed')
                    return

                if( args['-a'] or args['--all'] is True):
                    #print('-a')
                    #if(args[''])
                    if (args['-f'] or args['--force'] is True):
                        print('-f')
                    return

                print(Fore.CYAN + "%-30s%-30s" % ( "[file] ", "[command] " ))
                keylist1 = []
                keylist2 = []
                for key in os.listdir(os.getcwd()):
                    keylist1.append(key)
                for key in config['command'].keys():
                    keylist2.append(key)

                dirlist = []
                for (key) in keylist1:
                    #print("%-30s %-5s %-5s" % (key, os.path.isdir(key), os.path.islink(key)))
                    if (os.path.isdir(key)
                        or os.path.islink(key)):
                        dirlist.append(key)
                #print(dirlist)

                for key in dirlist:
                    keylist1.remove(key)

                #print(keylist1)
                #print(keylist2)
                count2 = 1
                for (key1, key2) in itertools.zip_longest(keylist1, keylist2, fillvalue=""):
                    if (key1 is not ""):
                        key1 = str("%s" % (key1))
                    if (key2 is not ""):
                        key2 = str("%-4s%s" % (count2, key2))
                        count2 += 1
                    print("%-30s%-30s" % (key1, key2))
                return
            else:
                ''
        else:
            ''
        break

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
            writeJsonData(sourceconfigfile, config)
            return
        else:
            ''
        break

    # need return, set return, default break.
    # get
    while (True):
        if (args['get'] == True):
            if (args['all'] is True):
                if (args['stat'] is True):
                    print("%s" % pymakeworkpath)
                    print("%s" % os.getcwd())
                    return
                elif (args['status'] is True):
                    print("EXECUTE ROOT [HERE   ]: %s" % pymakeworkpath)
                    print("EXECUTE ROOT [DEFAULT]: %s" % os.getcwd())
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
                elif (args['information'] is True):
                    if(config.__contains__("environ") is True):
                        if (config['environ'].__contains__("current") is True):
                            print("CURRENT ENVIRON %s" % (config["environ"]["current"]))
                        else:
                            print("CURRENT ENVIRON failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    else:
                        print("CURRENT ENVIRON failed: please check your .json file content, it is not compatible version .json.")

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
                elif (args['settings'] is True):
                    #print('break to display backward.')
                    break
                else:
                    if(config.__contains__("environ") is True):
                        if (config['environ'].__contains__("current") is True):
                            print("CURRENT ENVIRON %s" % (config["environ"]["current"]))
                        else:
                            print("CURRENT ENVIRON failed: .json file is broken, environ section lost current key, please use set command fix it.")
                    else:
                        print("CURRENT ENVIRON failed: please check your .json file content, it is not compatible version .json.")

                    r = conf.get('source', 'root')
                    f = conf.get('source', 'config')
                    print("SOURCE        : %s%s%s" % (r, os.path.sep, f))
                    print("SOURCE ROOT   : %s" % (r))
                    print("SOURCE CONFIG : %s" % (f))
                    print("-----------------------------------------")
                    print("PROGRAM       : %s" % os.path.realpath(__file__))
                    print("PROGRAM ROOT  : %s" % os.path.split(os.path.realpath(__file__))[0])
                    print("PROGRAM FILE  : %s" % os.path.split(os.path.realpath(__file__))[1])
                    print("-----------------------------------------")
                    print("CONFIGURE     : %s" % (pymakeini))
                    print("CONFIGURE ROOT: %s" % (pymakeroot))
                    print("CONFIGURE FILE: %s" % (os.path.split(os.path.realpath(pymakeini))[1]))
                    print("-----------------------------------------")
                    print("PORT INI      : %s" % portinifile)
                    print("PORT INI ROOT : %s" % os.path.split(os.path.realpath(portinifile))[0])
                    print("PORT INI CONF : %s" % os.path.split(os.path.realpath(portinifile))[1])
                    print("-----------------------------------------")
                    print("EXECUTE ROOT [HERE   ]: %s" % pymakeworkpath)
                    print("EXECUTE ROOT [DEFAULT]: %s" % os.getcwd())
                    print("-----------------------------------------")
                    plat = getplatform()
                    if (plat == "Windows"):
                        print("INSTALL ROOT  : %s" % "C:\Windows")
                    else:
                        print("INSTALL ROOT  : %s" % "/usr/local/bin")
                    return
            elif (args['env'] is True):
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
            elif (args['exec'] is True):
                if (args['here'] is True):
                    print("%s" % (pymakeworkpath))
                    return
                else:
                   ""
                print("%s" % (pymakeshellroot))
                return
            else:
                ''
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
                if (args['<name>'] is not None):
                    if(dict0.__contains__(args['<name>']) is False):
                        print("there is no this path item in path assemblage.")
                        return
                    value = dict0[args['<name>']]
                    print(Fore.GREEN + "%s" % (value))
                else:
                    for (k, v) in dict0.items():
                        print(Fore.BLUE+ "%-24s %s" % (k, v) )

            elif( args['env'] == True):
                env = os.environ

                current_var = args['<name>']
                if (args['<name>'] is None):
                    current_var = list_config['environ']['current']
                elif (args['<name>'] is not None):
                    current_var = args['<name>']
                    if (current_var == "current"):
                        current_var = list_config['environ']['current']
                    if (list_config['environ'].__contains__(current_var) is False):
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
                    if(dict0.__contains__(args['<name>']) is False):
                        print("there is no this cmd in command group.")
                        return
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

    # get
    while (True):
        if (args['get'] is True):
            if (args['all'] is True):
                if (args['settings'] is True):
                    list_config = config
                    if (args['--raw'] is True):
                        list_config = rawconfig

                    if (args['env'] == True):
                        env = os.environ
                        if (args['<name>'] is not None):
                            current_var = args['<name>']
                            if (current_var == "current"):
                                current_var = list_config['environ']['current']
                            if (list_config['environ'].__contains__(current_var) is False):
                                print("please ensure the environ is right")
                                return
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.CYAN + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.BLUE + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
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
                            return

                        for current_var in list_config['environ'].keys():
                            if (current_var == "current"):
                                continue
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.RESET + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.BLUE + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
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
                        return
                    else:
                        ''
                else:
                    ''
            else:
                ''
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

            current_var = args['<name>']
            if(args['<name>'] is None):
                current_var = list_config['environ']['current']
            elif (args['<name>'] is not None):
                current_var = args['<name>']
                if(current_var == "current"):
                    current_var = list_config['environ']['current']
                if (list_config['environ'].__contains__(current_var) is False):
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

    # set into env [False]
    while (False):
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

    # custom command function
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

    # cmd_type function
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

        else:
            ""
        break

    # export function
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

    # get
    while (True):
        if (args['get'] is True):
            if (args['all'] is True):
                if (args['settings'] is True):

                    list_config = config
                    if (args['--raw'] is True):
                        list_config = rawconfig

                    if (args['path'] == True):
                        dict0 = copy.deepcopy(list_config['path-assemblage'])
                        if (args['<name>'] is not None):
                            if (dict0.__contains__(args['<name>']) is False):
                                print("there is no this path item in path assemblage.")
                                return
                            value = dict0[args['<name>']]
                            print(Fore.GREEN + "%s" % (value))
                        else:
                            for (k, v) in dict0.items():
                                print(Fore.BLUE + "%-24s %s" % (k, v))

                    elif (args['env'] == True):
                        env = os.environ
                        if (args['<name>'] is not None):
                            current_var = args['<name>']
                            if (current_var == "current"):
                                current_var = list_config['environ']['current']
                            if (list_config['environ'].__contains__(current_var) is False):
                                print("please ensure the environ is right")
                                return
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.CYAN + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.BLUE + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
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
                            return

                        for current_var in list_config['environ'].keys():
                            if (current_var == "current"):
                                continue
                            dict0 = copy.deepcopy(list_config['environ'][current_var])
                            print(Fore.RESET + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.BLUE + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
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

                    elif (args['cmd'] == True):
                        dict0 = copy.deepcopy(list_config['command'])
                        if (args['<name>'] is not None):
                            # print(Fore.CYAN + "group: %s" % args['<name>'])
                            if (dict0.__contains__(args['<name>']) is False):
                                print("there is no this cmd in command group.")
                                return
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
                        print(Fore.BLACK + "path-assemblage:")
                        for (k, v) in list_config['path-assemblage'].items():
                            print(Fore.BLUE + "%-24s %s" % (k, v))

                        print(Fore.BLACK + "environ:")
                        env = os.environ
                        for current_var in list_config['environ'].keys():
                            if (current_var == "current"):
                                continue

                            dict0 = copy.deepcopy(list_config['environ'][current_var])

                            print(Fore.RESET + "env %s" % current_var)
                            print(Fore.MAGENTA + "path+:")
                            for (key) in dict0["path+"]:
                                print(Fore.BLUE + "  %s" % key)
                            if (args['-a'] or args['--all'] is True):
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

                        print(Fore.BLACK + "command:")
                        current_var = args['<name>']
                        if (args['<name>'] is not None):
                            if (args['<name>'] == "current"):
                                current_var = list_config['environ']['current']

                            if (list_config['environ'].__contains__(current_var) is False):
                                print('please ensure your env name is right.')
                                return

                            local_command = list_config['command']
                            if (args['--raw'] is True):
                                local_command = raw_command(current_var)

                            dict0 = copy.deepcopy(local_command)
                        else:
                            dict0 = copy.deepcopy(list_config['command'])

                        for (key, value) in dict0.items():
                            print(Fore.CYAN + "cmd %s" % key)
                            step = 1
                            for cmd in value:
                                print(Fore.RED + "%-3s %s" % (step, cmd))
                                step += 1

                    return
                else:
                    ''
            else:
                ''
        else:
            ''
        break

    # windows unix
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

    #windows not compatibility, unix only
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

    # use env exec command
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

            if (current_env == 'current'
                or rawconfig['environ'].__contains__(current_env) is False):
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
                #if(getplatform()=="Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                #else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList0(list0)

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
        else :
            ""
        break

    # cc exec
    while (True):
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
            #if(getplatform()=="Windows"):
            #    cmd_list, temp_file_name = createCmdList0(list0)
            #else:
            #    cmd_list, temp_file_name = createCmdList01(list0)
            # good compatibility
            cmd_list, temp_file_name = createCmdList0(list0)

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

    #windows, unix
    def createCmdList02(local = True, list0 = [], params0 = []):

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
            cmd_call = "call "
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
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        params_string = ""
        for param in params0:
            params_string += param + " "
        #print(params_string)

        if ( local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            for cmd in list0:
                cmd_list.append(cmd + ' ' + params_string)

        # append exit 0
        cmd_list.append(cmd_exit)
        #print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w") as f:
            for line in cmd_list:
                f.write(line + "\n")
        #print(cmd_execute)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        # print (cmd_list)
        return cmd_list, name

    # use env exec-with-params/execvp/ccvp command
    while (True):
        if (args['use'] is True):
            if (args['<env-name>'] is None):
                print("please appoint a environ")
                return

            if (rawconfig['environ'].__contains__(args['<env-name>']) is False):
                print("please ensure the environ is right")
                return

            current_env = args['<env-name>']
            if (args['<env-name>'] == "current"):
                current_env = rawconfig['environ']['current']

            if (current_env == 'current'
                or rawconfig['environ'].__contains__(current_env) is False):
                print(
                    ".json file is broken, environ section current env config is lost, please use set command fix it.")
                return

            if (args['execvp'] or args['ccvp'] is True):

                if (args['<command-name>'] is None):
                    print("please appoint your command")
                    return

                if (args['here'] or args['hh'] is True):
                    os.chdir(pymakeworkpath)

                # create cmd_list
                current_var = current_env
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                list0 = []
                local = True
                current_var = args['<command-name>']
                if (current_var in dict0):
                    list0.extend(dict0[current_var])
                    local = True
                else:
                    list0.append(current_var)
                    local = False

                params0 = []
                for current_var in args['--params']:
                    params0.append(current_var)

                cmd_list = []
                temp_file_name = ""
                # if (getplatform() == "Windows"):
                #    cmd_list, temp_file_name = createCmdList0(list0)
                # else:
                #    cmd_list, temp_file_name = createCmdList01(list0)
                # good compatibility
                cmd_list, temp_file_name = createCmdList02(local, list0, params0)

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
        else:
            ''
        break

    # exec-with-params ccvp execvp
    while (True):
        if (args['exec-with-params'] or args['execvp'] or args['ccvp'] is True):
            #print(args)
            if (args['<command-name>'] is None):
                print("please appoint your command")
                return

            if (args['here'] or args['hh'] is True):
                os.chdir(pymakeworkpath)

            #print ("group %s" % current_vars)
            dict0 = copy.deepcopy(rawconfig['command'])

            list0 = []
            local = True
            current_var = args['<command-name>']
            if (current_var in dict0):
                list0.extend(dict0[current_var])
                local = True
            else:
                list0.append(current_var)
                local = False

            params0 = []
            #print(args['<command-name>'])
            #print(args['--params'])
            #print(args['<command-params>'])
            for current_var in args['--params']:
                params0.append(current_var)

            cmd_list = []
            temp_file_name = ""
            # if (getplatform() == "Windows"):
            #    cmd_list, temp_file_name = createCmdList0(list0)
            # else:
            #    cmd_list, temp_file_name = createCmdList01(list0)
            # good compatibility
            cmd_list, temp_file_name = createCmdList02(local, list0, params0)

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

    # here [False]
    while (False):
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
