# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import re
import sys
import uuid
import shutil
import time
import json
import copy
import types
import platform
from collections import OrderedDict

if ( sys.version_info[0] == 2 ):
    import ConfigParser as PyConfigParser
else:
    import configparser as PyConfigParser

class MyConfigParser(PyConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        PyConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr


class MyOrderedDict(OrderedDict):
    def prepend(self, key, value, dict_setitem=dict.__setitem__):
        root = self[0]
        first = root[1]
        if key in self:
            link = self[key]
            link_prev, link_next, _ = link
            link_prev[1] = link_next
            link_next[0] = link_prev
            link[0] = root
            link[1] = first
            root[1] = first[0] = link
        else:
            root[1] = first[0] = self[key] = [root, first, key]
            dict_setitem(self, key, value)

    def insert(self, index, key, value):
        self[key] = value
        for ii, k in enumerate(list(self.keys())):
            if ii >= index and k != key:
                self.move_to_end(k)

#include inherret
def instanceof(variate):
    type1=""
    if (isinstance(variate,int)):
        type1 = "int"
    elif (isinstance(variate,str)):
        type1 = "str"
    elif (isinstance(variate,float)):
        type1 = "float"
    elif (isinstance(variate,list)):
        type1 = "list"
    elif (isinstance(variate,tuple)):
        type1 = "tuple"
    elif (isinstance(variate,dict)):
        type1 = "dict"
    elif (isinstance(variate,set)):
        type1 = "set"
    else:
        type1 = "valid"
    return type1

def typeof(variate):
    type1 = ""
    if (type(variate) == type(1)):
        type1 = "int"
    elif (type(variate) == type("str")):
        type1 = "str"
    elif (type(variate) == type(12.3)):
        type1 = "float"
    elif (type(variate) == type([1])):
        type1 = "list"
    elif (type(variate) == type(())):
        type1 = "tuple"
    elif (type(variate) == type({"key1":"123"})):
        type1 = "dict"
    elif (type(variate) == type({"key1"})):
        type1 = "set"
    else:
        type1 = "valid"
    return type1

def getplatform( ):
    sysstr = platform.system()
    #print ( sysstr )
    #if(sysstr =="Windows"):
    #    print ("Call Windows tasks")
    #if(sysstr =="Darwin"):
    #    print ("Call Darwin tasks")
    #elif(sysstr == "Linux"):
    #    print ("Call Linux tasks")
    #else:
    #    print ("Other System tasks")
    return sysstr

def getplatform_release():
    sysstr = platform.release()
    #7
    #XP
    #17.4.0
    #3.10.84-14528008
    return sysstr

def getcmd_codec():
    if (sys.version_info[0] == 2):
        return None
    else:
        if(getplatform() == "Windows"):
            if(getplatform_release() == "XP"):
                return None
            else:
                return "ansi"
        else:
            return 'utf8'
    return 'utf8'

def myopen(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True): # known special case of open
    if (sys.version_info[0] == 2):
        return open(name=file, mode=mode)
    else:
        if(getplatform() == "Windows"):
            if(getplatform_release() == "XP"):
                encoding = None
        return open(file=file, mode=mode, encoding=encoding)
    return open(file=file, mode=mode, encoding=encoding)

def getuserroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        #root = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"]
        root = os.environ["USERPROFILE"]
    else:
        root = os.environ["HOME"]
    return root

def getconfigroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        root = os.environ["APPDATA"]
    else:
        root = os.environ["HOME"]
    return root

def readJsonData(file):

    datas = ""
    with open(file, 'r', encoding='utf8') as json_file:
        for line in json_file.readlines():
            datas += line
    data = json.loads(datas, encoding='utf-8', object_pairs_hook=OrderedDict);


    #with open(file, 'r') as json_file:
    #    data = json.load(json_file)

    return data

def writeJsonData(file, data):

    with open(file, 'w', encoding='utf8') as json_file:
        json_file.write(json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False))


    #with open(file, 'w') as json_file:
    #    json.dump(data, json_file, indent=4)


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
            "wincc": "${root.tool}/macCompilers",
			"cmake.bin": "${wincc}/CMake.app/Contents/bin",
            "pymake": "${cc}/PyMake",
            "qt": "${root.tool}/macLibraries/Qt",
            "qt4.8.version": "4.8.6",
            "qt4.8.clang": "${qt}/${qt4.8.version}/clang_64",
            "qt4.8.clang.bin": "${qt4.8.clang}/bin",
            "qt5.8.version": "5.8",
            "qt5.8.android_x86": "${qt}/${qt5.8.version}/android_x86",
            "qt5.8.android_x86.bin": "${qt5.8.android_x86}/bin",
            "qt5.8.android_arm": "${qt}/${qt5.8.version}/android_armv7",
            "qt5.8.android_arm.bin": "${qt5.8.android_arm}/bin",
            "qt5.8.clang": "${qt}/${qt5.8.version}/clang_64",
            "qt5.8.clang.bin": "${qt5.8.clang}/bin",
            "qt5.8.ios": "${qt}/${qt5.8.version}/ios",
            "qt5.8.ios.bin": "${qt5.8.ios}/bin",
            "qt5.9.version": "5.9.2",
            "qt5.9.ios": "${qt}/${qt5.9.version}/ios",
            "qt5.9.ios.bin": "${qt}/${qt5.9.version}/ios/bin",
            "qt5.9.clang": "${qt}/${qt5.9.version}/clang_64",
            "qt5.9.clang.bin": "${qt}/${qt5.9.version}/clang_64/bin",
            "qt5.9.android_arm": "${qt}/${qt5.9.version}/android_armv7",
            "qt5.9.android_arm.bin": "${qt}/${qt5.9.version}/android_armv7/bin",
            "qt5.9.android_x86": "${qt}/${qt5.9.version}/android_x86",
            "qt5.9.android_x86.bin": "${qt}/${qt5.9.version}/android_x86/bin",
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
                    "${qt5.9.android_arm.bin}",
                    "${java1.8.bin}",
                    "${android.sdk}",
                    "${sdk.plat.tool}",
                    "${sdk.build.tool}",
                    "${sdk.tool}",
                    "${ant.bin}",
                    "${ndk.arm.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
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
                    "${qt5.9.android_x86.bin}",
                    "${java1.8.bin}",
                    "${android.sdk}",
                    "${sdk.plat.tool}",
                    "${sdk.build.tool}",
                    "${sdk.tool}",
                    "${ant.bin}",
                    "${ndk.x86.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "CLICOLOR": "1",
                "ANDROID_API_VERSION": "android-23",
                "ANDROID_HOME": "${android.sdk}",
                "ANDROID_SDK_ROOT": "${android.sdk}",
                "ANDROID_NDK_PLATFORM": "android-23",
                "ANDROID_NDK_ROOT": "${android.ndk}",
                "ANDROID_NDK_HOST": "darwin-x86_64",
                "ANDROID_NDK_TOOLCHAIN_PREFIX": "x86_64",
                "ANDROID_NDK_TOOLCHAIN_VERSION": "4.9",
                "ANDROID_NDK_TOOLS_PREFIX": "x86_64-linux-android",
                "NDK_TOOLCHAIN_PATH": "${ndk.x86.bin}",
                "NDK_TOOLS_PREFIX": "x86_64-linux-android",
                "PYMAKE_MYNAME": "T.D.R",
                "a_special_var_const": "hello world",
                "QTDIR": "${qt5.android_x86}",
                "QTSPEC": "-spec android-g++",
                "QTCONFIG": "",
                "JAVA_HOME": "${java1.8.home}",
                "CLASSPATH": ".:${JAVA_HOME}/lib/dt/jar:${JAVA_HOME}/lib/tools.jar",
                "QTVERSION": "${qt5.android_x86.version}",
                "QKIT": "ANDROIDX86",
                "QSYS": "AndroidX86"
            },
            "qt4": {
                "path+": [
                    "${qt4.8.clang.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt4.version}",
                "QTDIR": "${qt4.8.clang}",
                "QTSPEC": "-spec macx-llvm",
                "QTCONFIG": "CONFIG+=x86_64",
                "QKIT": "macOS",
                "QSYS": "macOS"
            },
            "ios": {
                "path+": [
                    "${qt5.9.ios.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.ios}",
                "QTSPEC": "-spec macx-ios-clang",
                "QTCONFIG": "CONFIG+=iphoneos CONFIG+=device -after QMAKE_MAC_XCODE_SETTINGS+=qteam qteam.name=DEVELOPMENT_TEAM qteam.value=4EGMLT3G6T",
                "QKIT": "iOS",
                "QSYS": "iOS"
            },
            "iossimulator": {
                "path+": [
                    "${qt5.9.ios.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.ios}",
                "QTSPEC": "-spec macx-ios-clang",
                "QTCONFIG": "CONFIG+=iphonesimulator CONFIG+=simulator",
                "QKIT": "iOSSimulator",
                "QSYS": "iOSSimulator"
            },
            "macos": {
                "path+": [
                    "${qt5.9.clang.bin}"
                ],
                "make0": "make",
                "CMAKEGENERATOR": "Unix Makefiles",
                "QTVERSION": "${qt5.9.version}",
                "QTDIR": "${qt5.9.clang}",
                "QTSPEC": "-spec macx-clang",
                "QTCONFIG": "CONFIG+=x86_64",
                "QKIT": "macOS",
                "QSYS": "macOS"
            },
            "current": "macos"
        },
        "command": {
            "test": [
                "echo $(pwd)"
            ],
            "test.6": [
                "echo 中文"
            ],
            "test.7": [
                "echo $PATH"
            ],
            "qqt.build": [
                "src_path=${root.src}/LibQQt",
                "src=${root.src}/LibQQt/QQt.pro",
                "build=${root.build}/QQt/$QSYS/$QTVERSION/Debug",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "qmake ${src} $QTSPEC CONFIG+=debug CONFIG+=qml_debug $QTCONFIG && make qmake_all",
                "make -j4"
            ],
            "qqt.clean": [
                "src=${root.src}/LibQQt/QQt.pro",
                "build=${root.build}/QQt/$QSYS/$QTVERSION/Debug",
                "cd $build",
                "make clean"
            ],
            "qt": [
                "open \"/Applications/Qt Creator.app\""
            ],
            "cmake0": [
                "open ${wincc}/CMake.app"
            ],
            "prod": [
                "open /Users/abel/Develop/d0-product/ProductExecTool/macOS/ProductExecTool_debug.app"
            ],
            "libtool": [
                "open /Users/abel/Develop/d0-product/AddLibraryTool/macOS/AddLibraryTool_debug.app"
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
                "/Users/abel/Develop/b0-toolskits/macAndroidLibraries/android-sdk-macosx/tools/android"
            ],
            "test.2": [
                "#echo $*",
                "param=$*",
                "ping 127.0.0.1 $param"
            ],
            "open-dir": [
                "open $1"
            ],
            "daily.qqt": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=$src_path/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Debug",
                "mkdir -p $build",
                "cd $build",
                "rm -rf src examples",
                "qmake $src $QTSPEC $QTCONFIG CONFIG+=debug CONFIG+=qml_debug && make qmake_all",
                "make -j4"
            ],
            "daily.qqt.release": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=$src_path/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Release",
                "mkdir -p $build",
                "cd $build",
                "rm -rf src examples",
                "qmake $src $QTSPEC $QTCONFIG CONFIG+=release && make qmake_all",
                "make -j4"
            ],
            "build.qqt": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=/Users/abel/Develop/a0-develop/LibQQt/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Debug",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "qmake ${src} $QTSPEC CONFIG+=debug CONFIG+=qml_debug $QTCONFIG && make qmake_all",
                "make -j4"
            ],
            "build.qqt.release": [
                "src_path=/Users/abel/Develop/a0-develop/LibQQt",
                "src=$src_path/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Release",
                "mkdir -p $build",
                "cd $build",
                "qmake $src $QTSPEC $QTCONFIG CONFIG+=release && make qmake_all",
                "make -j4"
            ],
            "clean.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Debug",
                "cd $build",
                "make clean"
            ],
            "clean.qqt.release": [
                "src=/Users/abel/Develop/a0-develop/LibQQt/QQt.pro",
                "build=/Users/abel/Develop/c0-buildstation/QQt/$QSYS/$QTVERSION/Release",
                "cd $build",
                "make clean"
            ],
            "check.qt": [
                "src=/Users/abel/Develop/b0-toolskits/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=/Users/abel/Develop/c0-buildstation/qt4.8.7",
                "install=/Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure --help"
            ],
            "build.qt": [
                "src=/Users/abel/Develop/b0-toolskits/z0-Source/qt",
                "build=/Users/abel/Develop/c0-buildstation/qt",
                "install=/Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "CXXFLAGS=-stdlib=libc++",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "build.qt4.8.7": [
                "src=/Users/abel/Develop/b0-toolskits/z0-Source/qt-everywhere-opensource-src-4.8.7",
                "build=/Users/abel/Develop/c0-buildstation/qt4.8.7",
                "install=/Users/abel/Develop/b0-toolskits/macLibraries/Qt/4.8.7/gcc_64",
                "mkdir -p $build",
                "cd $build",
                "echo build $(pwd)",
                "${src}/configure -prefix ${install}",
                "make -j4",
                "make install"
            ],
            "build.soap": [
                "src=/Users/abel/Develop/c1-webrc/qt-solutions/qtsoap",
                "build=/Users/abel/Develop/c0-buildstation/qtsoap",
                "install=/Users/abel/Develop/d1-product/QtSoap",
                "cd $build",
                "${src}/configure -library"
            ],
            "push.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt",
                "cd $src",
                "git push",
                "git push --tag"
            ],
            "pull.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt",
                "cd $src",
                "git pull"
            ],
            "cloc.qqt": [
                "src=/Users/abel/Develop/a0-develop/LibQQt",
                "cd $src",
                "perl ${pymake}/demo/cloc-1.74.pl  .",
                "date"
            ],
            "cloc.light": [
                "src=/Users/abel/Develop/a0-develop/LightUnderWater/App",
                "cd $src",
                "perl /Users/abel/Develop/b1-buildshell/cloc-1.74.pl  .",
                "date"
            ],
            "qtdir": [
                "echo $QTDIR"
            ],
            "test.3": [
                "#echo $*",
                "ping $*"
            ],
            "test.4": [
                "echo param1: $1",
                "echo param2: $2",
                "echo param3: $3",
                "echo param4: $4"
            ],
            "build.qmake": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"$1.pro\" ]; then",
                "   echo $1.pro existed.",
                "else",
                "   echo has $1.pro? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/$profilename.pro",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "qmake $src $QTSPEC CONFIG+=debug CONFIG+=qml_debug $QTCONFIG && make qmake_all",
                "make -j4",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "cmake": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"CMakeLists.txt\" ]; then",
                "   echo CMakeLists.txt existed.",
                "else",
                "   echo has CMakeLists.txt? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/CMakeLists.txt",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "open ${wincc}/CMake.app",
                "errorlevel=$?",
                "if [ $errorlevel -ne 0 ]; then",
                "   echo cmake exit code: $errorlevel",
                "   break",
                "fi",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "build.cmake.sdk": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"CMakeLists.txt\" ]; then",
                "   echo CMakeLists.txt existed.",
                "else",
                "   echo has CMakeLists.txt? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/CMakeLists.txt",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "cmake $src_path -G\"$CMAKEGENERATOR\" -DCMAKE_INSTALL_PREFIX=${root.sdk}/$profilename/$QSYS -DCMAKE_BUILD_TYPE=Debug",
                "errorlevel=$?",
                "if [ $errorlevel -ne 0 ]; then",
                "   echo cmake exit code: $errorlevel",
                "   break",
                "fi",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "build.cmake.app": [
                "while [ 1 ]",
                "do",
                "src_path=$(pwd)",
                "profilename=$1",
                "if [ \"$profilename\" == \"\" ]; then",
                "   echo please input a project name",
                "   break",
                "fi",
                "if [ -f \"CMakeLists.txt\" ]; then",
                "   echo CMakeLists.txt existed.",
                "else",
                "   echo has CMakeLists.txt? please add here command to restrict.",
                "   break",
                "fi",
                "src=$src_path/CMakeLists.txt",
                "build=${root.build}/$profilename/$QSYS/$QTVERSION/Debug",
                "prod=${root.prod}/$profilename/$QSYS",
                "sdk=${root.sdk}/$profilename/$QSYS",
                "mkdir -p $build",
                "cd $build",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "echo build at: $build",
                "echo $QTSPEC $QTCONFIG",
                "cmake $src_path -G\"$CMAKEGENERATOR\" -DCMAKE_INSTALL_PREFIX=${root.prod}/$profilename/$QSYS -DCMAKE_BUILD_TYPE=Debug",
                "errorlevel=$?",
                "if [ $errorlevel -ne 0 ]; then",
                "   echo cmake exit code: $errorlevel",
                "   break",
                "fi",
                "echo build inf $QTSPEC $QTCONFIG",
                "echo src file: $src",
                "echo src path: $src_path",
                "echo build at: $build",
                "echo sdk   at: $sdk",
                "echo prod  at: $prod",
                "break",
                "done"
            ],
            "test.5": [
                "exit 0"
            ]
        }
    }

    # record current directory [pwd, execute path]
    pymakeworkpath = os.getcwd()
    #print( "pymake work path:", pymakeworkpath )
    #here work root

    # record pymake file directory [program file path]
    pymakefilepath = os.path.split(os.path.realpath(__file__))[0]
    #print( "pymake file path:", pymakefilepath )
    pymakefilepath = os.path.realpath(pymakefilepath + os.path.sep + '..' + os.path.sep + '..')

    # record pymake user source root [env, *.json] [ + auto create ]
    pymakesourceroot = pymakefilepath + os.path.sep + 'UserSource'
    if (not os.path.exists(pymakesourceroot)):
        os.makedirs(pymakesourceroot)
    #print( "pymake user source path:", pymakesourceroot )

    #record default user source config file name
    pymakedefaultsourcefile = 'pymake.json'
    #print( "pymake user default source file:", pymakedefaultsourcefile )

    # record pymake user shell root [ dynamic work path ]
    pymakeshellroot = pymakesourceroot + os.path.sep + 'UserShell'
    if (not os.path.exists(pymakeshellroot)):
        os.makedirs(pymakeshellroot)
    #print( "pymake user shell path:", pymakeshellroot )
    #default work root

    """
    [pymake]
    [work]
    root = default
    there = $pymakeshellroot
    [source]
    root = $pymakesourceroot
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
    if( not conf.has_section('work') ):
        conf.add_section('work')
        conf.write(open(pymakeini, 'w'))
    if( not conf.has_option('work', 'root') ):
        conf.set('work', 'root', 'default')
        conf.write(open(pymakeini, 'w'))
    if(not conf.has_option('work', 'there')):
        conf.set('work', 'there', pymakeshellroot)
        conf.write(open(pymakeini, 'w'))

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

    #prepare to user source root
    if (not os.path.exists(sourceroot)):
        os.makedirs(sourceroot)
    os.chdir(sourceroot)

    if (os.path.exists(sourceroot)):
        if (os.path.abspath(sourceroot) != os.path.abspath(pymakeroot)
            and os.path.abspath(sourceroot) != os.path.abspath(pymakefilepath)):
            if (not os.path.exists(defaultsourceconfigfile)):
                writeJsonData(defaultsourceconfigfile, d)

    def open_file(file0):
        plat = getplatform()
        cmd0 = ''
        if (plat == "Windows"):
            if (file0.__contains__(' ')):
                cmd0 = 'start "" ' + '"%s"' % file0
            else:
                cmd0 = "start " + file0
        elif (plat == "Darwin"):
            if (file0.__contains__(' ')):
                cmd0 = 'open ' + '"%s"' % file0
            else:
                cmd0 = "open " + file0
        else:
            if (file0.__contains__(' ')):
                cmd0 = 'xdg-open ' + '"%s" ' % file0 + ">/dev/null 2>&1"
            else:
                cmd0 = "xdg-open " + '%s ' % file0 + ">/dev/null 2>&1"
        return cmd0

    #record source config file postfix
    pymakesuffix = '.json'

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

    # record user shell root directory [default]
    shellroot = sourceroot + os.path.sep + "UserShell"
    # print("execute directory: %s" % (shellroot) )
    
    # support pymake default shell root, pymake custom shell root, pymake current shell root.
    # record pymake custom shell root [ user custom work path ]
    workroottype = conf.get('work', 'root')
    customshellroot = conf.get('work', 'there')
    if (not os.path.exists(customshellroot)):
        os.makedirs(customshellroot)
    #custom work root

    if(workroottype == 'default'):
       shellroot = pymakeshellroot
    elif (workroottype == 'here'):
       shellroot = pymakeworkpath
    elif (workroottype == 'there'):
       shellroot = customshellroot

    # shellroot = pymakefilepath
    # if(workroottype == 'default'):
    #    print("WORK STARTING : %s" % (pymakeshellroot))
    # elif (workroottype == 'here'):
    #    print("WORK STARTING : %s" % (pymakeworkpath))
    # elif (workroottype == 'there'):
    #    print("WORK STARTING : %s" % (c))
    # print("execute directory: %s" % (shellroot) )

    # I set this,
    # pymake execute user bat/sh in shellroot,
    # user can use here param to restrict exec action.
    # cd user shell root [ default shell execute path ]
    #prepare to user shell root
    if (not os.path.exists(shellroot)):
        os.makedirs(shellroot)
    os.chdir(shellroot)


    #port translate function
    portdefaultsourceconfig = pymakedefaultsourcefile
    portdefaulttargetconfig = 'temporary-target.json'
    portiniconfig = 'port.ini'
    portinifile = os.path.join(sourceroot, "port.ini")
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



    # debug.
    debugini = sourceroot + os.path.sep + "debug.ini"
    debugconf = MyConfigParser()
    debugconf.read(debugini)
    if (not debugconf.has_section('debug')):
        debugconf.add_section('debug')
        debugconf.write(open(debugini, 'w'))

    if( not debugconf.has_option('debug', 'switch') ):
        debugconf.set('debug', 'switch', '0')
        debugconf.write(open(debugini, 'w'))

    debugswitch = debugconf['debug']['switch']
    if(debugswitch != '0' and debugswitch != '1'):
        debugswitch = '0'
        debugconf.set('debug', 'switch', debugswitch)
        debugconf.write(open(debugini, 'w'))


    config = readJsonData(sourceconfigfile)
    #print(config)

    def check_config():
        #hard
        if(config.__contains__("path-assemblage") is False):
            config['path-assemblage']={}
            writeJsonData(sourceconfigfile, config)
        if(config.__contains__("environ") is False):
            config['environ']={}
            writeJsonData(sourceconfigfile, config)
        if (config.__contains__("command") is False):
            config['command'] = {}
            writeJsonData(sourceconfigfile, config)

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

        #soft
        order_of_keys = config['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        if (list_of_tuples.__len__() < 2):
            if(config['environ'].__contains__("default") is False):
                config['environ']['default']={"path+":[]}
                writeJsonData(sourceconfigfile, config)
            if(config['environ']['default'].__contains__("path+") is False):
                config['environ']['default']['path+']=[]
                writeJsonData(sourceconfigfile, config)
            if(config['environ'].__contains__("current") is False):
                config['environ']['current']='default'
                writeJsonData(sourceconfigfile, config)

        #move 'current' to be last key
        order_of_keys = config['environ'].keys()
        list_of_tuples = [key for key in order_of_keys]
        #print(order_of_keys)
        #print(list_of_tuples)
        #print(list_of_tuples[-1])
        if(list_of_tuples[-1] != 'current'):
            #print(".....")
            current_var = config['environ']['current']
            config['environ'].__delitem__('current')
            config['environ']['current']=current_var
            writeJsonData(sourceconfigfile, config)
        return

    check_config()

    # record system environ
    pymakesystemenviron = copy.deepcopy(os.environ)

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

            #NO! ignore [in command, has various interpretations]
            #for (find_key, find_value) in pymakesystemenviron.items():
            #    if (key == find_key):
            #        break
            #    if (str(find_key).lower() == 'path'):
            #        continue
            #    if (find_key == key_from):
            #        rawconfig["path-assemblage"][key] = rawconfig["path-assemblage"][key].replace(
            #            key_replace, pymakesystemenviron[key_from])
            #        # print("xxx %s" % rawconfig["path-assemblage"][key])
            #        break

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

    # raw path function, parse custom path tuple
    def raw_path(pathgroup0):
        pathgroup = copy.deepcopy(pathgroup0)

        # replace path
        for (key, value) in enumerate(pathgroup):
            # print (key) #...

            startpos = 0
            while (True):
                # print (startpos)

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
                    if (key == find_key):
                        break
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, rawconfig["path-assemblage"][key_from])
                        # print("xxx %s" % pathgroup[key])
                        break
        return pathgroup

    # custom command function
    # custom command stream from rawconfig
    def raw_command(env_name=None):
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

    # custom string dict -> raw dict
    def raw_string(pathgroup0, env_name=None):
        pathgroup = {k: v for k, v in pathgroup0.items()}
        #print(pathgroup)

        dict0 = {k: v for k, v in rawconfig['path-assemblage'].items()}
        dict1 = {}
        current_env = env_name
        if(current_env == "current"):
            current_env = rawconfig['environ']['current']
        if(env_name is not None):
            dict1 = {k: v for k, v in rawconfig['environ'][current_env].items()}
        dict2 = {k: v for k, v in os.environ.items()}

        # replace path
        for (key, value) in pathgroup.items():
            #print (key, value) #...

            if(instanceof(value) != 'str'):
                continue

            if (dict0.__contains__(value) is True):
                pathgroup[key] = dict0[value]
                #print(pathgroup[key])
                continue

            if (dict2.__contains__(value) is True):
                pathgroup[key] = dict2[value]
                continue

            if (dict1.__contains__(value) is True):
                pathgroup[key] = dict1[value]
                continue

            startpos = 0
            while (True):
                # print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                # print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                # print ( key1 ) #...

                for (find_key, find_value) in dict0.items():
                    #print("%-30s, %-30s, %-30s, path-assemblage" % (key, key_from, find_key))
                    if (key == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    #if (find_key == "path"):
                    #    continue
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, dict0[key_from])
                        #print("path-assemblage %s" % pathgroup[key])
                        break

                for (find_key, find_value) in dict2.items():
                    #print("%-30s, %-30s, %-30s, system env" % (key, key_from, find_key))
                    if (key == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    if (find_key == "path"):
                        continue
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, dict2[key_from])
                        # print("system env %s" % pathgroup[key])
                        break

                for (find_key, find_value) in dict1.items():
                    #print("%-30s, %-30s, %-30s, separate env" % (key, key_from, find_key))
                    if (key == find_key):
                        break
                    if (find_key == 'path+'):
                        continue
                    # if (find_key == "path"):
                    #    continue
                    if (find_key == key_from):
                        pathgroup[key] = pathgroup[key].replace(key_replace, dict1[key_from])
                        # print("separate env %s" % pathgroup[key])
                        break

        return pathgroup

    # custom string dict -> raw dict [ignore case]
    def raw_string1(pathgroup0, env_name=None):
        #pathgroup = {k: v.lower() for k, v in pathgroup0.items()}
        pathgroup1 = {k: v for k, v in pathgroup0.items()}
        #print(pathgroup)

        dict0 = {k.lower(): v for k, v in rawconfig['path-assemblage'].items()}
        dict1 = {}
        current_env = env_name
        if(current_env == "current"):
            current_env = rawconfig['environ']['current']
        if(env_name is not None):
            dict1 = {k.lower(): v for k, v in rawconfig['environ'][current_env].items()}
        dict2 = {k.lower(): v for k, v in os.environ.items()}

        # replace path
        for (key, value) in pathgroup0.items():
            #print (key, value) #...

            if(instanceof(value) != 'str'):
                continue

            if (dict0.__contains__(value.lower()) is True):
                pathgroup1[key] = dict0[value.lower()]
                #print(pathgroup1[key])
                continue

            if (dict2.__contains__(value.lower()) is True):
                pathgroup1[key] = dict2[value.lower()]
                continue

            if (dict1.__contains__(value.lower()) is True):
                pathgroup1[key] = dict1[value.lower()]
                continue

            startpos = 0
            while (True):
                # print (startpos)

                index = value.find('${', startpos)
                if (index == -1):
                    break

                index2 = value.find('}', index)
                startpos = index2

                key_replace = value[index:index2 + 1]
                # print ( key0 ) #${...}
                key_from = key_replace.split('{')[1].split('}')[0].strip()
                # print ( key1 ) #...

                for (find_key, find_value) in dict0.items():
                    #print("%-30s, %-30s, %-30s, path-assemblage" % (key, key_from, find_key))
                    if (key.lower() == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    #if (find_key == "path"):
                    #    continue
                    if (find_key == key_from.lower()):
                        pathgroup1[key] = pathgroup1[key].replace(key_replace, key_replace.lower())
                        pathgroup1[key] = pathgroup1[key].replace(key_replace.lower(), dict0[key_from.lower()])
                        #print("path-assemblage %s" % pathgroup1[key])
                        break

                for (find_key, find_value) in dict2.items():
                    #print("%-30s, %-30s, %-30s, system env" % (key, key_from, find_key))
                    if (key.lower() == find_key):
                        break
                    #if (find_key == 'path+'):
                    #    continue
                    if (find_key == "path"):
                        continue
                    if (find_key == key_from.lower()):
                        pathgroup1[key] = pathgroup1[key].replace(key_replace, key_replace.lower())
                        pathgroup1[key] = pathgroup1[key].replace(key_replace.lower(), dict2[key_from.lower()])
                        # print("system env %s" % pathgroup1[key])
                        break

                for (find_key, find_value) in dict1.items():
                    #print("%-30s, %-30s, %-30s, separate env" % (key, key_from, find_key))
                    if (key.lower() == find_key):
                        break
                    if (find_key == 'path+'):
                        continue
                    # if (find_key == "path"):
                    #    continue
                    if (find_key == key_from.lower()):
                        pathgroup1[key] = pathgroup1[key].replace(key_replace, key_replace.lower())
                        pathgroup1[key] = pathgroup1[key].replace(key_replace.lower(), dict1[key_from.lower()])
                        #print("separate env %s" % pathgroup1[key])
                        break

        return pathgroup1

    # which command [internal]
    def which_command(env_name = None, name = '', postfix = []):
        if(name is None or name == ''):
            return None

        #get python command.
        pycmd = name

        #get path ext
        pathext = []
        pathext.append('')
        pathext.extend(postfix)
        plat = getplatform()
        if(plat == "Windows"):
            pathext.extend(os.environ['PATHEXT'].split(os.path.pathsep))
        else:
            pathext.extend(['.sh','.out','.cmd'])

        #find in current path
        specialpath = [
            pymakeworkpath,
            os.getcwd()
        ]
        list0 = copy.deepcopy(specialpath)
        list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                # print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        if(env_name is not None):
            if(rawconfig['environ'].__contains__(env_name) is False):
                print("Fault Error! .json file is broken, env %s is losing!" % env_name)
                return None

            #find in separate env
            list0 = copy.deepcopy(rawconfig['environ'][env_name]['path+'])
            list0.reverse()
            for path0a in list0:
                for path0 in path0a.split(os.path.pathsep):
                    path0 = path0.strip()
                    # print(path0)
                    path1 = ''
                    for pext0 in pathext:
                        path1 = path0 + os.path.sep + pycmd + pext0
                        if(os.path.isfile(path1)):
                            if (plat == "Windows"):
                                return path1.replace('/', '\\')
                            else:
                                return path1.replace('\\', '/')

        # find in env. [custom+, local+, system]
        env = os.environ
        #for pathA in env['PATH'].split(os.path.pathsep):
        #    print(pathA)
        list0 = copy.deepcopy(env['PATH'].split(os.path.pathsep))
        #list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                #print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    #print("[%s]" % path1)
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        return None

    # which file [internal]
    def which_file(env_name = None, name = '', postfix = []):
        if(name is None or name == ''):
            return None

        #get python command.
        pycmd = name

        #get path ext
        pathext = []
        pathext.append('')
        pathext.extend(postfix)
        plat = getplatform()
        if(plat == "Windows"):
            pathext.extend([])
        else:
            pathext.extend([])

        #find in current path
        specialpath = [
            pymakeworkpath,
            os.getcwd()
        ]
        list0 = copy.deepcopy(specialpath)
        list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                # print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        if(env_name is not None):
            if(rawconfig['environ'].__contains__(env_name) is False):
                print("Fault Error! .json file is broken, env %s is losing!" % env_name)
                return None

            #find in separate env
            list0 = copy.deepcopy(rawconfig['environ'][env_name]['path+'])
            list0.reverse()
            for path0a in list0:
                for path0 in path0a.split(os.path.pathsep):
                    path0 = path0.strip()
                    # print(path0)
                    path1 = ''
                    for pext0 in pathext:
                        path1 = path0 + os.path.sep + pycmd + pext0
                        if(os.path.isfile(path1)):
                            if (plat == "Windows"):
                                return path1.replace('/', '\\')
                            else:
                                return path1.replace('\\', '/')

        # find in env. [custom+, local+, system]
        env = os.environ
        #for pathA in env['PATH'].split(os.path.pathsep):
        #    print(pathA)
        list0 = copy.deepcopy(env['PATH'].split(os.path.pathsep))
        #list0.reverse()
        for path0a in list0:
            for path0 in path0a.split(os.path.pathsep):
                path0 = path0.strip()
                #print(path0)
                path1 = ''
                for pext0 in pathext:
                    path1 = path0 + os.path.sep + pycmd + pext0
                    #print("[%s]" % path1)
                    if(os.path.isfile(path1)):
                        if (plat == "Windows"):
                            return path1.replace('/', '\\')
                        else:
                            return path1.replace('\\', '/')

        return None

    # pymake expand command-line.
    #current_var = args['<env-name>']
    #args = raw_string(args, current_var)
    #print(args)
    #for (k, v) in args.items():
    #    if(isinstance(v, str)):
    #        print(k, v)
    #return

    # system command function
    # system command stream from rawconfig path-assemblage
    def raw_command_system():
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

                step += 1
        return command_dict

    #.bat .sh, windows, unix, system
    def createCmdList06(env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            if(env_name != None):
                cmd_list.append("call %s_effect.bat" % name)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            if(env_name != None):
                cmd_list.append("source %s_effect.sh" % name)

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        if ( local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            for cmd in list0:
                if (str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        cmd_list.append('"' + cmd + '"' + ' ' + params_string)
                    else:
                        cmd_list.append(cmd + ' ' + params_string)
                else:
                    cmd_list.append(cmd + ' ' + params_string)

        # append exit 0
        cmd_list.append(cmd_exit)
        #print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

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
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        return cmd_list, name

    # system export function
    def system_env_export (env_name = None, file_name = None):
        if(env_name == None):
            return env_name, '', ''

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
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
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
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
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset



    # get open path's cmd list
    def open_command (pathlist0, env_name = None):
        pathgroup0 = {}
        for (k,v) in enumerate(pathlist0):
            pathgroup0[str('-pymake-open-p%d'%k)] = str(v)

        cmd_list = []
        pathgroup1 = {}
        #if(args['-i'] or args['--ignorecase'] is True):
        #    pathgroup1 = raw_string1(pathgroup0, env_name)
        #else:
        #    pathgroup1 = raw_string(pathgroup0, env_name)
        pathgroup1 = raw_string1(pathgroup0, env_name)

        plat = getplatform()
        for (k, v) in pathgroup1.items():
            path0 = str(v)
            pathslist = path0.split(os.path.pathsep)
            while (pathslist.__contains__('')):
                pathslist.remove('')
            #print(pathslist)
            for path0 in pathslist:
                cmd0 = ''
                if (plat == "Windows"):
                    if(path0.__contains__(' ')):
                        cmd0 = 'start "" ' + '"%s"' % path0
                    else:
                        cmd0 = "start " + path0
                elif (plat == "Darwin"):
                    if(path0.__contains__(' ')):
                        cmd0 = 'open ' + '"%s"' % path0
                    else:
                        cmd0 = "open " + path0
                else:
                    if(path0.__contains__(' ')):
                        cmd0 = 'xdg-open ' + '"%s" ' % path0 + ">/dev/null 2>&1"
                    else:
                        cmd0 = "xdg-open " + '%s ' % path0 + ">/dev/null 2>&1"
                cmd_list.append(cmd0)

        return cmd_list


    # pymake local const variable.
    localini = sourceroot + os.path.sep + "local.ini"
    localconf = MyConfigParser()
    localconf.read(localini)
    if (not localconf.has_section('local')):
        localconf.add_section('local')
        localconf.write(open(localini, 'w'))
    if (not localconf.has_section('path+')):
        localconf.add_section('path+')
        localconf.write(open(localini, 'w'))
    if (not localconf.has_section('variable')):
        localconf.add_section('variable')
        localconf.write(open(localini, 'w'))

    #status readonly
    #if( not localconf.has_option('local', 'status') ):
    #    localconf.set('local', 'status', 'readonly')
    #    localconf.write(open(localini, 'w'))

    #localswitch = localconf['local']['status']
    #if(localswitch != 'readonly'):
    #    localswitch = 'readonly'
    #    localconf.set('local', 'status', localswitch)
    #    localconf.write(open(localini, 'w'))

    #switch [1, default]
    if( not localconf.has_option('local', 'switch') ):
        localconf.set('local', 'switch', '1')
        localconf.write(open(localini, 'w'))

    localswitch = localconf['local']['switch']
    if(localswitch != '0' and localswitch != '1'):
        localswitch = '1'
        localconf.set('local', 'switch', localswitch)
        localconf.write(open(localini, 'w'))

    localenv = {}
    localenv['path+'] = []

    # set into env [no effect to system environ]
    while (True):
        #if(int(localswitch) == 0):
        #    break

        env = os.environ

        localenv['PYMAKEDEFAULTSOURCEROOT'] = pymakesourceroot
        localenv['PYMAKEDEFAULTSOURCECONFIG'] = pymakedefaultsourcefile

        localenv['PYMAKESOURCEFILE'] = sourceconfigfile
        localenv['PYMAKESOURCEROOT'] = sourceroot
        localenv['PYMAKESOURCECONFIG'] = sourcefile

        localenv['PYMAKEDEFAULTWORKROOT'] = pymakeshellroot
        localenv['PYMAKETHEREROOT'] = customshellroot
        localenv['PYMAKEHEREROOT'] = pymakeworkpath
        localenv['PYMAKEWORKROOT'] = shellroot

        localenv['PYMAKEPROGRAM'] = os.path.realpath(__file__)
        localenv['PYMAKEPROGRAMROOT'] = os.path.split(os.path.realpath(__file__))[0]
        localenv['PYMAKEPROGRAMFILE'] = os.path.split(os.path.realpath(__file__))[1]

        localenv['PYMAKEPROGRAMCONFIGURE'] = os.path.realpath(pymakeini)
        localenv['PYMAKEPROGRAMCONFIGUREROOT'] = os.path.split(os.path.realpath(pymakeini))[0]
        localenv['PYMAKEPROGRAMCONFIGUREFILE'] = os.path.split(os.path.realpath(pymakeini))[1]

        if(getplatform() == 'Windows'):
            localenv['PYMAKEINSTALLROOT'] = env['windir']
        else:
            localenv['PYMAKEINSTALLROOT'] = '/usr/local/bin'

        localenv['path+'].append(localenv['PYMAKEPROGRAMROOT'])
        localenv['path+'].append(localenv['PYMAKESOURCEROOT'])
        localenv['path+'].append(localenv['PYMAKEDEFAULTWORKROOT'])
        #if(localenv['path+'].__contains__(localenv['PYMAKETHEREROOT']) is False):
        localenv['path+'].append(localenv['PYMAKETHEREROOT'])
        #if(localenv['path+'].__contains__(localenv['PYMAKEHEREROOT']) is False):
        localenv['path+'].append(localenv['PYMAKEHEREROOT'])
        #if(localenv['path+'].__contains__(localenv['PYMAKEWORKROOT']) is False):
        localenv['path+'].append(localenv['PYMAKEWORKROOT'])

        #store to file
        for (key, value) in enumerate(localenv["path+"]):
            localconf.set('path+', str("%d" % key), value)

        for (key, value) in localenv.items():
            if (key == 'path+'):
                continue
            localconf.set('variable', key, value)

        localconf.write(open(localini, 'w'))

        #set into env
        for (key) in localenv["path+"]:
            env["PATH"] = key + os.path.pathsep + env["PATH"]

        for (key, value) in localenv.items():
            if (key == 'path+'):
                continue
            env[key] = value
        break


    #initial custom environ module
    pymakecustomini = sourceroot + os.path.sep + "custom.ini"
    conf2 = MyConfigParser()
    conf2.read(pymakecustomini)
    if( not conf2.has_section('custom') ):
        conf2.add_section('custom')
        conf2.write(open(pymakecustomini, 'w'))
    if( not conf2.has_option('custom', 'switch') ):
        conf2.set('custom', 'switch', '1')
        conf2.write(open(pymakecustomini, 'w'))

    switch0 = conf2['custom']['switch']
    if(switch0 != '0' and switch0 != '1'):
        switch0 = '1'
        conf2.set('custom', 'switch', switch0)
        conf2.write(open(pymakecustomini, 'w'))

    custompathfile = sourceroot + os.path.sep + "custom.path+.ini"
    customenvfile = sourceroot + os.path.sep + "custom.var+.ini"

    storecustompaths = []
    storecustomvars = []

    envcustomlistpaths = []
    envcustomlistvars = {}

    envcustomlistrawpaths = []
    envcustomlistrawvars = {}

    plat = getplatform()
    cmd_codec = "utf8"
    cmd_return = "\n"
    if (plat == "Windows"):
        cmd_codec = "ansi"
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
    else:
        cmd_codec = "utf8"
        cmd_return = "\n"

    #custom environ
    #user can use custom environ to effect pymake basic environment.
    #it will effect every executing environment.
    while (True):

        if(int(switch0) == 0):
            break

        #print("open custom environ.")

        # set custom path+ to env.
        # print(sourceroot)
        # print(shellroot)
        # init file
        #custompathfile = sourceroot + os.path.sep + "custom.path+.ini"
        if (os.path.exists(custompathfile) is False):
            with open(custompathfile, 'w', encoding=cmd_codec) as f:
                ''

        # read all
        custompaths = []
        with open(custompathfile, 'r', encoding=cmd_codec) as f:
            for l in f.readlines():
                # important format
                # l = l.strip()
                while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                    l = l.rstrip('\r\n')
                    l = l.rstrip('\n')
                    l = l.rstrip('\r')
                # if(l == ''):
                #    continue
                custompaths.append(l)
        # while(custompaths.__contains__('') is True):
        # custompaths.remove('')
        # print(custompaths)
        # print(os.linesep)
        # for l in custompaths:
        #    print("AAAA:" + l)

        # write back

        #strip
        storecustompaths = copy.deepcopy(custompaths)
        for (i, l) in enumerate(storecustompaths):
            # import format
            l = l.strip()
            storecustompaths[i] = l

        # added by local, ignore
        '''
        # default [ fixed ]
        # add pymake default source root to environ.
        if (storecustompaths.__contains__(pymakesourceroot) is False):
            storecustompaths.append(pymakesourceroot)
        # add pymake default shell root to environ.
        if (storecustompaths.__contains__(pymakeshellroot) is False):
            storecustompaths.append(pymakeshellroot)
        # default [ movable, follow user source root ]
        # add user source root to environ.
        if (sourceroot != pymakesourceroot and storecustompaths.__contains__(sourceroot) is False):
            storecustompaths.append(sourceroot)
        # add user shell root to environ.
        if (customshellroot != pymakeshellroot and storecustompaths.__contains__(customshellroot) is False):
            storecustompaths.append(customshellroot)
        if (pymakeworkpath != pymakeshellroot and storecustompaths.__contains__(pymakeworkpath) is False):
            storecustompaths.append(pymakeworkpath)
        if (shellroot != pymakeshellroot and storecustompaths.__contains__(shellroot) is False):
            storecustompaths.append(shellroot)
        '''
        
        #clean repeat path [for store]
        clean_list = []
        temp_list = []
        for l in storecustompaths:
            if (l == ''):
                continue
            if (os.path.isabs(l) is False):
                continue
            if (temp_list.__contains__(str(l).replace('\\', '/').lower())):
                clean_list.append(l)
                continue
            else:
                temp_list.append(str(l).replace('\\', '/').lower())
        #print(clean_list)
        storecustompaths.reverse()
        for l in clean_list:
            if (storecustompaths.__contains__(l) is True):
                storecustompaths.remove(l)
        storecustompaths.reverse()

        if (custompaths != storecustompaths):
            with open(custompathfile, 'w', encoding=cmd_codec) as f:
                for l in storecustompaths:
                    f.write(l + cmd_return)

        # set into env

        #raw
        envcustompaths = copy.deepcopy(storecustompaths)
        envcustomrawpaths = raw_path(envcustompaths)
        #print(envcustompaths)
        #print(envcustomrawpaths)

        #envcustomlistpaths
        for (key,l) in zip(envcustompaths, envcustomrawpaths):
            if (l == ''):
                continue
            #print(os.path.isabs(l), l)
            if (os.path.isabs(l) is False):
                continue
            envcustomlistpaths.append(key)

        # clean illgal path
        clean_list = []
        for l in envcustomrawpaths:
            if (l == ''):
                clean_list.append(l)
                continue
            if (os.path.isabs(l) is False):
                clean_list.append(l)
                continue
        #print(clean_list)

        for l in clean_list:
            if (envcustomrawpaths.__contains__(l) is True):
                envcustomrawpaths.remove(l)

        env = os.environ
        for l in envcustomrawpaths:
            env["PATH"] = l + os.path.pathsep + env["PATH"]

        for l in envcustomrawpaths:
            envcustomlistrawpaths.append(l)

        # set custom env+ to env.
        #customenvfile = sourceroot + os.path.sep + "custom.var+.ini"
        # print(customenvfile)
        # init
        if (os.path.exists(customenvfile) is False):
            with open(customenvfile, 'w', encoding=cmd_codec) as f:
                ''

        # read all
        customenvs = []
        with open(customenvfile, 'r', encoding=cmd_codec) as f:
            for l in f.readlines():
                # important format
                # l = l.strip()
                while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                    l = l.rstrip('\r\n')
                    l = l.rstrip('\n')
                    l = l.rstrip('\r')
                # if(l == ''):
                #    continue
                customenvs.append(l)

        # write back

        #strip
        storecustomvars = copy.deepcopy(customenvs)
        for (i, l) in enumerate(storecustomvars):
            # important format
            l = l.strip()
            storecustomvars[i] = l

        avarkeyvalue = "PYMAKEAUTHOR=T.D.R."
        if (storecustomvars.__contains__(avarkeyvalue) is False):
            storecustomvars.append(avarkeyvalue)

        #clean repeat var [for store]
        clean_list = []
        temp_list = []
        for l in storecustomvars:
            if (l == ''):
                continue
            if (str(l).__contains__('=') is False):
                continue
            if (temp_list.__contains__(str(l).split('=')[0].strip().lower())):
                clean_list.append(l)
                continue
            else:
                temp_list.append(str(l).split('=')[0].strip().lower())
        #print(clean_list)
        storecustomvars.reverse()
        for l in clean_list:
            if (storecustomvars.__contains__(l) is True):
                storecustomvars.remove(l)
        storecustomvars.reverse()

        if (storecustomvars != customenvs):
            with open(customenvfile, 'w', encoding=cmd_codec) as f:
                for l in storecustomvars:
                    f.write(l + cmd_return)

        # set into env

        #raw
        envcustomvars = copy.deepcopy(storecustomvars)
        envcustomrawvars = raw_path(envcustomvars)
        #print(envcustomvars)
        #print(envcustomrawvars)
        for (key0,l) in zip(envcustomvars, envcustomrawvars):
            if (l == ''):
                continue
            if (str(l).__contains__('=') is False):
                continue
            key = str(key0).split('=')[0].strip()
            value = '='.join(str(key0).split('=')[1:]).strip()
            envcustomlistvars[key] = value

        # clean illgal var
        clean_list = []
        for l in envcustomrawvars:
            if (l == ''):
                clean_list.append(l)
                continue
            if (str(l).__contains__('=') is False):
                clean_list.append(l)
                continue
        # print(clean_list)

        for l in clean_list:
            if (envcustomrawvars.__contains__(l) is True):
                envcustomrawvars.remove(l)

        env = os.environ
        for l in envcustomrawvars:
            key = str(l).split('=')[0].strip()
            value = '='.join(str(l).split('=')[1:]).strip()
            env[key] = value

        for l in envcustomrawvars:
            key = str(l).split('=')[0].strip()
            value = '='.join(str(l).split('=')[1:]).strip()
            envcustomlistrawvars[key] = value

        break

    # initial vc module
    #record vc shell root.
    vcroot = sourceroot + os.path.sep + "VCShell"
    if(not os.path.exists(vcroot)):
        os.mkdir(vcroot)


    def vc_createCmdList08(shellenvname = None, env_name = None, local = True, list0 = [], params0 = []):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        #print(env_name)

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
            if (shellenvname is not None):
                cmd_list.append('call \"%s_effect%s\"' % (shellenvname, cmd_suffix))
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)
            if (shellenvname is not None):
                cmd_list.append('source \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        #print(params0)
        params_string = ""
        for param in params0:
            #print(param)
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        if ( local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            for cmd in list0:
                if(str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(str(cmd))
                    #print(Fore.RED + "which command:", pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        cmd_list.append('"' + cmd + '"' + ' ' + params_string)
                    else:
                        cmd_list.append(cmd + ' ' + params_string)
                else:
                    cmd_list.append(cmd + ' ' + params_string)

        # append exit 0
        cmd_list.append(cmd_exit)
        #print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

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
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        return cmd_list, name

    def vc_powershell_createCmdList08(shellenvname = None, env_name = None, local=True, list0=[], params0=[]):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        # print (name)

        #plat = getplatform()

        cmd_status = "echo pymake-command-status:$LASTEXITCODE"
        cmd_sep = ';'
        cmd_suffix = ".ps1"
        cmd_suffix_powershell = cmd_suffix
        cmd_exit = 'exit $LASTEXITCODE'
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash"
        cmd_call = "./"
        # cmd_list.append(cmd_header)
        cmd_list.append("./%s_effect%s" % (name, cmd_suffix))

        if(shellenvname is not None):
            cmd_list.append('. \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        # print(params_string)

        if (local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_powershell)):
                    cmd_suffix_powershell = ''

                powershellexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    powershellexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break
                    powershellexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [+custom]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a powershell command, or powershell command-line.
                    powershellexecfile = cmd
                    break

                #print(powershellexecfile)
                #wow
                #cmd_list.append(powershellexecfile + ' ' + params_string)
                if (str(powershellexecfile).__contains__(' ')):
                    if(os.path.isfile(powershellexecfile)):
                        cmd_list.append(". \"%s\" @args" % powershellexecfile)
                    else:
                        cmd_list.append(". %s @args" % powershellexecfile)
                else:
                    cmd_list.append(". %s @args" % powershellexecfile)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )

        cmd_execute = "" + name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        # print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        # if (plat == "Windows"):
        #    ""
        # else:
        #    os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        cmd_list.append(cmd_call + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        cmd_list.append(cmd_exit)

        # print (cmd_list)
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name

    def vc_python_createCmdList08(shellenvname = None, env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
            if (shellenvname is not None):
                cmd_list.append('call \"%s_effect%s\"' % (shellenvname, cmd_suffix))
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)
            if (shellenvname is not None):
                cmd_list.append('source \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        cmd_suffix_python = '.py'
        cmd_codec_python = "utf8"
        cmd_return_python = "\n"

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        pythonexecfile = ''
        if ( local is True):
            #fixed
            pythonexecfile = name + '_exec' + cmd_suffix_python
            with open(pythonexecfile, 'w', encoding=cmd_codec_python) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return_python)
            #print(1, pythonexecfile)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_python)):
                    cmd_suffix_python = ''

                pythonexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    pythonexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break
                    pythonexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a python command, or python command-line.
                    pythonexecfile = cmd
                    break

                #print(2, pythonexecfile)
                #cmd_list.append(pythonexecfile + ' ' + params_string)

        #print params.
        #print(3, pythonexecfile)

        #get python command.
        pycmd = ''
        if(plat == "Windows"):
            pycmd = 'python.exe'
        else:
            pycmd = 'python3'

        pycmd = which_command(env_name, pycmd)

        #print(pycmd)
        if(plat == "Windows"):
            if(pycmd is None):
                pycmd = 'py'
            elif(pycmd != 'py'):
                pycmd = 'python'
        else:
            pycmd = 'python3'

        if(os.path.isfile(pythonexecfile)):
            if(plat == "Windows"):
                cmd_list.append("call %s \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))
        else:
            if(plat == "Windows"):
                cmd_list.append("call %s -c \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s -c \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

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

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name

    def vc_language_createCmdList08(shellenvname = None, suffix = None, encoding = None, env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            cmd_suffix = ".bat"
            cmd_header = "@echo off"
            cmd_call = "call "
            # window close echo, close promot
            cmd_list.append(cmd_header)
            # os.system("type env_effect.bat > cmd_exec.bat")
            cmd_list.append("call %s_effect.bat" % name)
            if (shellenvname is not None):
                cmd_list.append('call \"%s_effect%s\"' % (shellenvname, cmd_suffix))
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_suffix = ".sh"
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)
            if (shellenvname is not None):
                cmd_list.append('source \"%s_effect%s\"' % (shellenvname, cmd_suffix))

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        if(env_name == "current"):
            env_name = rawconfig['environ']['current']

        cmd_suffix_language = cmd_suffix
        cmd_codec_language = cmd_codec
        cmd_return_language = cmd_return

        if(suffix is not None):
            cmd_suffix_language = suffix
        if(encoding is not None):
            cmd_codec_language = encoding

        list1 = []
        # for current_var in str(args['<command-param>']).split():
        #    list1.append(current_var)
        if (params0.__len__() > 0):
            current_var = params0[0]
            list1.append(current_var)
            params0.pop(0)
        #print(list1)

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        local2 = True
        if (list1.__len__() > 0):
            current_var = list1[0]
            if (current_var in rawconfig['command']):
                local2 = True
            else:
                local2 = False

        languageparams = ''
        #actually only one param.
        if (local2 is True):
            for param1 in list1:
                languageparams += param1
        else:
            for param1 in list1:
                # warning: now pymake is in user setted workroot.

                languageparams = ""
                while (True):
                    # find in current path [+--workroot]
                    languageparams = os.getcwd() + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break
                    languageparams = pymakeworkpath + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        languageparams = path0 + os.path.sep + param1
                        #print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        languageparams = path0 + os.path.sep + param1
                        # print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a language command, or language command-line.
                    languageparams = param1
                    break

                    # print(2, languageparams)
                    # cmd_list.append(languageparams + ' ' + params_string)

        if(list1.__len__() >0):
            ''
            if(local2 is True):
                ''
                current_var = env_name
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                inside_name = name + '_2'
                languageparams = inside_name + '_exec' + cmd_suffix_language

                with open(languageparams, 'w', encoding=cmd_codec_language) as f:
                    for cmd1 in list1:
                        for cmd in dict0[cmd1]:
                            f.write(cmd + cmd_return_language)

                #print(1, cmd_suffix_language)
                #print(1, cmd_return_language)
                #print(1, cmd_codec_language)
                #print(1, languageparams)
            else:
                ''

        #print(3, languageparams)
        if(list1.__len__() >0 ):
            if(local2 is True):
                params_string = languageparams + ' ' + params_string
            else:
                if(str(languageparams).__contains__(' ')):
                    params_string = '"' + languageparams + '"' + ' ' + params_string
                else:
                    params_string = languageparams + ' ' + params_string
        #print(params_string)

        languageexecfile = ''
        if ( local is True):
            #fixed
            #inside_name = name
            #inside_name = hex( int( inside_name, 16 ) + 1).split('x')[1]
            inside_name = name + '_1'
            #print(inside_name)
            languageexecfile = inside_name + '_exec' + cmd_suffix
            with open(languageexecfile, 'w', encoding=cmd_codec) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return)
            #print(1, languageexecfile)
        else:
            languageexecfile = ''
            #actually now has only one command.
            for cmd in list0:
                #actually this is a command.
                if (str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(cmd)
                    #print(pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        languageexecfile = '"' + cmd + '"'
                    else:
                        languageexecfile = cmd
                else:
                    languageexecfile = cmd

        #print(3, languageexecfile)
        if(plat == "Windows"):
            cmd_list.append("call %s %s" % (languageexecfile, '%*'))
        else:
            if(languageexecfile.endswith('.sh')):
                cmd_list.append("sh %s %s" % (languageexecfile, '"$@"'))
            else:
                cmd_list.append("%s %s" % (languageexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' '+ params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name, cmd_suffix, cmd_suffix_language

    #vc json export function
    def vc_json_export(dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        cmd_suffix = ".json"
        cmd_codec = 'utf8'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'vcenv'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += cmd_suffix

        if(os.path.exists(cmd_effect) is False):
            tempdict = {
                'environ': {

                }
            }
            writeJsonData(cmd_effect, tempdict)

        vcdict = readJsonData(cmd_effect)
        if(vcdict.__contains__('environ') is False):
            vcdict['environ'] = {}
        vcdict['environ'][current_var] = dict0
        writeJsonData(cmd_effect, vcdict)

        return cmd_effect

    #vc powershell export function
    def vc_powershell_export(dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        cmd_suffix = ".ps1"
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = "" + file_name
        cmd_effect += '_effect' + cmd_suffix

        # export path
        lines = ""
        for (key) in dict0["path+"]:
            lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

        # export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)

        # print(lines.split('\n'))
        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        # export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = "" + file_name
        cmd_unset += '_unset' + cmd_suffix

        # export unset path
        lines = ""
        for (key) in dict0["path+"]:
            # lines += ("$env:Path = $env:Path.Replace(\"%s;\", \"\")" % key) + cmd_return
            lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return
        # export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:%s} = \"\"" % key) + cmd_return

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        return cmd_effect, cmd_unset

    def vc_powershell_export2(dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        cmd_suffix = ".ps1"
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = "" + file_name
        cmd_effect += '_effect' + cmd_suffix

        lines = ""
        # +system
        if (args['-s'] or args['--system'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

            # export var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export path
            for (key) in localenv['path+']:
                lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

            # export var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in envcustomlistrawpaths:
                lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

            # export var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)
        else:
            ''

        # export path
        for (key) in dict0["path+"]:
            lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

        # export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)

        # print(lines.split('\n'))
        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        # export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = "" + file_name
        cmd_unset += '_unset' + cmd_suffix

        lines = ""
        # +system
        if (args['-s'] or args['--system'] is True):
            # export unset path
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

            # export unset var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                lines += ("${env:%s} = \"\"" % key) + cmd_return
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export unset path
            for (key) in localenv['path+']:
                lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

            # export unset var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:%s} = \"\"" % key) + cmd_return
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export unset path
            for (key) in envcustomlistrawpaths:
                lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

            # export unset var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                lines += ("${env:%s} = \"\"" % key) + cmd_return
        else:
            ''

        # export unset path
        for (key) in dict0["path+"]:
            # lines += ("$env:Path = $env:Path.Replace(\"%s;\", \"\")" % key) + cmd_return
            lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return

        # export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:%s} = \"\"" % key) + cmd_return

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        return cmd_effect, cmd_unset

    # vc export function
    # dict0: VC effect env
    # env_name: separate env
    # file_name: script name
    def vc_export (dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
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
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
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
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return cmd_effect, cmd_unset

    def vc_export2 (dict0 = None, env_name = None, file_name = None):
        if(dict0 is None):
            return "", "", ""

        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
            env_set = 'export '

        #export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = file_name
        cmd_effect += '_effect' + cmd_suffix

        lines = ""

        # +system
        if (args['-s'] or args['--system'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                else:
                    lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

            # export var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                if (plat == "Windows"):
                    lines += (env_set + key + '=' + value + cmd_return)
                else:
                    lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export path
            for (key) in localenv['path+']:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                else:
                    lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

            # export var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += (env_set + key + '=' + value + cmd_return)
                else:
                    lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export path
            # print(envcustomlistrawpaths)
            for (key) in envcustomlistrawpaths:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
                else:
                    lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

            # export var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += (env_set + key + '=' + value + cmd_return)
                else:
                    lines += (env_set + key + '=\"' + value + '\"' + cmd_return)
        else:
            ''

        #export path
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        #export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = file_name
        cmd_unset += '_unset' + cmd_suffix

        lines = ""

        # +system
        if (args['-s'] or args['--system'] is True):
            # export unset path
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                else:
                    lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

            # export unset var
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                if (plat == "Windows"):
                    lines += ('set ' + key + '=' + cmd_return)
                else:
                    lines += ('unset ' + key + cmd_return)
        else:
            ''

        # +local
        if (args['-l'] or args['--local'] is True):
            # export unset path
            for (key) in localenv['path+']:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                else:
                    lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

            # export unset var
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += ('set ' + key + '=' + cmd_return)
                else:
                    lines += ('unset ' + key + cmd_return)
        else:
            ''

        # +custom
        if (args['-c'] or args['--custom'] is True):
            # export unset path
            for (key) in envcustomlistrawpaths:
                if (plat == "Windows"):
                    lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
                else:
                    lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

            # export unset var
            for (key, value) in envcustomlistrawvars.items():
                if (key == 'path+'):
                    continue
                if (plat == "Windows"):
                    lines += ('set ' + key + '=' + cmd_return)
                else:
                    lines += ('unset ' + key + cmd_return)
        else:
            ''

        #export unset path
        for (key) in dict0["path+"]:
            if (plat == "Windows"):
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return cmd_effect, cmd_unset

    # vc settings function
    def vc_settings(env_name = None):
        current_env = env_name
        if(env_name is None):
            current_env = rawconfig['environ']['current']

        print("source file: %s" % sourceconfigfile)
        vcvarslist = [
            'vcvarsall-1998',
            'vcvarsall-2003',
            'vcvarsall-2005',
            'vcvarsall-2008',
            'vcvarsall-2010',
            'vcvarsall-2012',
            'vcvarsall-2013',
            'vcvarsall-2015',
            'vcvarsall-2017',
            'vcvarsall-2019',
            'vcvarsall-20XX'
        ]
        print('path-assemblage:')
        for key in vcvarslist:
            if (rawconfig['path-assemblage'].__contains__(key) is False):
                rawconfig['path-assemblage'][key] = "<CAN SET>"
            print('  "%s": "%s"' % (key, rawconfig['path-assemblage'][key]))

        current_vcvarsall = 'vcvarsall'
        current_vcvarsallparam = 'vcvarsallparam'
        print('system env:')
        if (pymakesystemenviron.__contains__(current_vcvarsall) is False):
            pymakesystemenviron[current_vcvarsall] = "<CAN SET>"
        print('  "%s"     : "%s"' % (current_vcvarsall, pymakesystemenviron[current_vcvarsall]))
        if (pymakesystemenviron.__contains__(current_vcvarsallparam) is False):
            pymakesystemenviron[current_vcvarsallparam] = "<CAN SET>"
        print('  "%s": "%s"' % (current_vcvarsallparam, pymakesystemenviron[current_vcvarsallparam]))

        print('custom env:')
        if (envcustomlistrawvars.__contains__(current_vcvarsall) is False):
            envcustomlistrawvars[current_vcvarsall] = "<CAN SET>"
        print('  "%s"     : "%s"' % (current_vcvarsall, envcustomlistrawvars[current_vcvarsall]))
        if (envcustomlistrawvars.__contains__(current_vcvarsallparam) is False):
            envcustomlistrawvars[current_vcvarsallparam] = "<CAN SET>"
        print('  "%s": "%s"' % (current_vcvarsallparam, envcustomlistrawvars[current_vcvarsallparam]))

        print('env %s:' % current_env)
        if (rawconfig['environ'][current_env].__contains__(current_vcvarsall) is False):
            rawconfig['environ'][current_env][current_vcvarsall] = "<CAN SET>"
        print('  "%s"     : "%s"' % (current_vcvarsall, rawconfig['environ'][current_env][current_vcvarsall]))
        if (rawconfig['environ'][current_env].__contains__(current_vcvarsallparam) is False):
            rawconfig['environ'][current_env][current_vcvarsallparam] = "<CAN SET>"
        print('  "%s": "%s"' % (current_vcvarsallparam, rawconfig['environ'][current_env][current_vcvarsallparam]))
        return




    #powershell export env function
    def powershell_environ_export(env_name = None, file_name = None):
        # select env
        current_var = rawconfig['environ']['current']
        if (env_name is not None):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        cmd_suffix = ".ps1"
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash" + cmd_return
        env_set = ''

        # export effect env
        cmd_effect = 'env'
        if (file_name is not None):
            cmd_effect = "" + file_name
        cmd_effect += '_effect' + cmd_suffix

        # export path
        lines = ""
        for (key) in dict0["path+"]:
            lines += ("if ( !$env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Insert(0, \"%s;\") }" % (key, key)) + cmd_return

        # export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:" + key + '} = \'' + value + '\'' + cmd_return)

        # print(lines.split('\n'))
        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        # export unset env
        cmd_unset = 'env'
        if (file_name is not None):
            cmd_unset = "" + file_name
        cmd_unset += '_unset' + cmd_suffix

        # export unset path
        lines = ""
        for (key) in dict0["path+"]:
            # lines += ("$env:Path = $env:Path.Replace(\"%s;\", \"\")" % key) + cmd_return
            lines += ("if ( $env:Path.Contains(\"%s;\" ) ) { $env:Path = $env:Path.Replace(\"%s;\", \"\") }" % (key, key)) + cmd_return
        # export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            lines += ("${env:%s} = \"\"" % key) + cmd_return

        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header)
            f.write(lines)

        return current_var, cmd_effect, cmd_unset

    # powershell [windows, unix]
    def createCmdList03(env_name = None, local=True, list0=[], params0=[]):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        # print (name)

        #plat = getplatform()

        cmd_status = "echo pymake-command-status:$LASTEXITCODE"
        cmd_sep = ';'
        cmd_suffix = ".ps1"
        cmd_suffix_powershell = cmd_suffix
        cmd_exit = 'exit $LASTEXITCODE'
        cmd_codec = 'ansi'
        if (getplatform_release() == "XP"):
            cmd_codec = None
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_header = "#!/usr/bin/env bash"
        cmd_call = "./"
        # cmd_list.append(cmd_header)
        cmd_list.append("./%s_effect%s" % (name, cmd_suffix))

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        # print(params_string)

        if (local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_powershell)):
                    cmd_suffix_powershell = ''

                powershellexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    powershellexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break
                    powershellexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_powershell
                    if(os.path.exists(powershellexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [+custom]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        powershellexecfile = path0 + os.path.sep + cmd + cmd_suffix_powershell
                        if (os.path.exists(powershellexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a powershell command, or powershell command-line.
                    powershellexecfile = cmd
                    break

                #print(powershellexecfile)
                #wow
                #cmd_list.append(powershellexecfile + ' ' + params_string)
                if (str(powershellexecfile).__contains__(' ')):
                    if(os.path.isfile(powershellexecfile)):
                        cmd_list.append(". \"%s\" @args" % powershellexecfile)
                    else:
                        cmd_list.append(". %s @args" % powershellexecfile)
                else:
                    cmd_list.append(". %s @args" % powershellexecfile)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )

        cmd_execute = "" + name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        # print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        # if (plat == "Windows"):
        #    ""
        # else:
        #    os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        cmd_list.append(cmd_call + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)
        cmd_list.append(cmd_exit)

        # print (cmd_list)
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name


    # python export function
    def python_env_export (env_name = None, file_name = None):
        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
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
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
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
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset

    # python [windows unix]
    def createCmdList05(env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
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
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        cmd_suffix_python = '.py'
        cmd_codec_python = "utf8"
        cmd_return_python = "\n"

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        pythonexecfile = ''
        if ( local is True):
            #fixed
            pythonexecfile = name + '_exec' + cmd_suffix_python
            with open(pythonexecfile, 'w', encoding=cmd_codec_python) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return_python)
            #print(1, pythonexecfile)
        else:
            #actually now has only one command.
            for cmd in list0:
                # warning: now pymake is in user setted workroot.
                if(str(cmd).endswith(cmd_suffix_python)):
                    cmd_suffix_python = ''

                pythonexecfile = ""
                while(True):
                    # find in current path [+workroot]
                    pythonexecfile = os.getcwd() + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break
                    pythonexecfile = pymakeworkpath + os.path.sep + cmd + cmd_suffix_python
                    #print(2, pythonexecfile)
                    if(os.path.exists(pythonexecfile)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if(find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        pythonexecfile = path0 + os.path.sep + cmd + cmd_suffix_python
                        #print(2, pythonexecfile)
                        if (os.path.exists(pythonexecfile)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a python command, or python command-line.
                    pythonexecfile = cmd
                    break

                #print(2, pythonexecfile)
                #cmd_list.append(pythonexecfile + ' ' + params_string)

        #print params.
        #print(3, pythonexecfile)

        #get python command.
        pycmd = ''
        if(plat == "Windows"):
            pycmd = 'python.exe'
        else:
            pycmd = 'python3'

        pycmd = which_command(env_name, pycmd)

        #print(pycmd)
        if(plat == "Windows"):
            if(pycmd is None):
                pycmd = 'py'
            elif(pycmd != 'py'):
                pycmd = 'python'
        else:
            pycmd = 'python3'

        if(os.path.isfile(pythonexecfile)):
            if(plat == "Windows"):
                cmd_list.append("call %s \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))
        else:
            if(plat == "Windows"):
                cmd_list.append("call %s -c \"%s\" %s" % (pycmd, pythonexecfile, '%*'))
            else:
                cmd_list.append("%s -c \"%s\" %s" % (pycmd, pythonexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

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

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name





    # language export function
    def language_env_export (env_name = None, file_name = None):
        #select env
        current_var = rawconfig['environ']['current']
        if( env_name is not None ):
            current_var = env_name
        dict0 = copy.deepcopy(rawconfig['environ'][current_var])

        plat = getplatform()
        if (plat == "Windows"):
            cmd_suffix = ".bat"
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
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
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
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
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset

    # language [ .bat .sh .ps1 .py ...] [windows unix] --suffix --encoding
    def createCmdList07(suffix = None, encoding = None, env_name = None, local = True, list0 = [], params0 = []):
        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
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
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        if(env_name == "current"):
            env_name = rawconfig['environ']['current']

        cmd_suffix_language = cmd_suffix
        cmd_codec_language = cmd_codec
        cmd_return_language = cmd_return

        if(suffix is not None):
            cmd_suffix_language = suffix
        if(encoding is not None):
            cmd_codec_language = encoding

        list1 = []
        # for current_var in str(args['<command-param>']).split():
        #    list1.append(current_var)
        if (params0.__len__() > 0):
            current_var = params0[0]
            list1.append(current_var)
            params0.pop(0)
        #print(list1)

        params_string = ""
        for param in params0:
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        local2 = True
        if (list1.__len__() > 0):
            current_var = list1[0]
            if (current_var in rawconfig['command']):
                local2 = True
            else:
                local2 = False

        languageparams = ''
        #actually only one param.
        if (local2 is True):
            for param1 in list1:
                languageparams += param1
        else:
            for param1 in list1:
                # warning: now pymake is in user setted workroot.

                languageparams = ""
                while (True):
                    # find in current path [+--workroot]
                    languageparams = os.getcwd() + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break
                    languageparams = pymakeworkpath + os.path.sep + param1
                    # print(2, languageparams)
                    if (os.path.exists(languageparams)):
                        break

                    # find in .json environ
                    separateenvlistpath = os.path.pathsep.join(rawconfig['environ'][env_name]['path+'])
                    separateenvlistpath = separateenvlistpath.split(os.path.pathsep)
                    separateenvlistpath.reverse()
                    #for path0 in separateenvlistpath:
                    #    print(path0)
                    find_flag = 0
                    for path0 in separateenvlistpath:
                        languageparams = path0 + os.path.sep + param1
                        #print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # find in basic environ [custom+]
                    env = os.environ
                    find_flag = 0
                    for path0 in env["PATH"].split(os.path.pathsep):
                        languageparams = path0 + os.path.sep + param1
                        # print(2, languageparams)
                        if (os.path.exists(languageparams)):
                            find_flag = 1
                            break
                    if (find_flag == 1):
                        break

                    # none? a language command, or language command-line.
                    languageparams = param1
                    break

                    # print(2, languageparams)
                    # cmd_list.append(languageparams + ' ' + params_string)

        if(list1.__len__() >0):
            ''
            if(local2 is True):
                ''
                current_var = env_name
                local_command = raw_command(current_var)
                dict0 = copy.deepcopy(local_command)

                inside_name = name + '_2'
                languageparams = inside_name + '_exec' + cmd_suffix_language

                with open(languageparams, 'w', encoding=cmd_codec_language) as f:
                    for cmd1 in list1:
                        for cmd in dict0[cmd1]:
                            f.write(cmd + cmd_return_language)

                #print(1, cmd_suffix_language)
                #print(1, cmd_return_language)
                #print(1, cmd_codec_language)
                #print(1, languageparams)
            else:
                ''

        #print(3, languageparams)
        if(list1.__len__() >0 ):
            if(local2 is True):
                params_string = languageparams + ' ' + params_string
            else:
                if(str(languageparams).__contains__(' ')):
                    params_string = '"' + languageparams + '"' + ' ' + params_string
                else:
                    params_string = languageparams + ' ' + params_string
        #print(params_string)

        languageexecfile = ''
        if ( local is True):
            #fixed
            #inside_name = name
            #inside_name = hex( int( inside_name, 16 ) + 1).split('x')[1]
            inside_name = name + '_1'
            #print(inside_name)
            languageexecfile = inside_name + '_exec' + cmd_suffix
            with open(languageexecfile, 'w', encoding=cmd_codec) as f:
                for cmd in list0:
                    f.write(cmd + cmd_return)
            #print(1, languageexecfile)
        else:
            languageexecfile = ''
            #actually now has only one command.
            for cmd in list0:
                #actually this is a command.
                if (str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(cmd)
                    #print(pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        languageexecfile = '"' + cmd + '"'
                    else:
                        languageexecfile = cmd
                else:
                    languageexecfile = cmd

        #print(3, languageexecfile)
        if(plat == "Windows"):
            cmd_list.append("call %s %s" % (languageexecfile, '%*'))
        else:
            if(languageexecfile.endswith('.sh')):
                cmd_list.append("sh %s %s" % (languageexecfile, '"$@"'))
            else:
                cmd_list.append("%s %s" % (languageexecfile, '"$@"'))

        # append exit 0
        cmd_list.append(cmd_exit)

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("call " + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' '+ params_string + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            #cmd_list.append("./" + cmd_execute + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + params_string + cmd_sep + ' ' + cmd_status)

        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print( cmd )
            print("---------------------------")

        return cmd_list, name, cmd_suffix, cmd_suffix_language


    # cmd type2 function
    def cmd_type2 (cmd_name = None, file_name = None, env_name = None):

        if (cmd_name is None):
            for (key, value) in rawconfig['command'].items():
                print(Fore.CYAN + "%s" % key)
            return

        if (rawconfig['command'].__contains__(cmd_name) is False):
            print("please check your command name")
            return

        if (env_name is None or env_name == rawconfig['environ']['current']):
            list0 = copy.deepcopy(rawconfig['command'][cmd_name])
        else:
            list0 = copy.deepcopy(raw_command(env_name)[cmd_name])

        # for cmd in list0:
        #    print(Fore.RED + "%s" % (cmd))

        temp_file_name = ""
        if (file_name is None):
            temp_file_name = "cmd"
        else:
            temp_file_name = "" + file_name

        cmd_header = ""
        cmd_codec = "utf8"
        # but windows, it is \r\n, python helpping me?
        cmd_return = "\n"
        cmd_suffix = ""
        if (getplatform() == "Windows"):
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_header = "@echo off"
            cmd_suffix = ".bat"
        else:
            cmd_codec = 'utf8'
            cmd_header = "#!/usr/bin/env bash"
            cmd_suffix = ".sh"

        suffix = args['--suffix']
        if (suffix is not None):
            cmd_suffix = str("%s" % suffix)

        encoding = args['--encoding']
        if (encoding is not None):
            cmd_codec = encoding

        cmd_exec = temp_file_name + cmd_suffix
        with open(cmd_exec, 'w', encoding=cmd_codec) as f:
            # f.write(cmd_header + cmd_return)
            cmd = ''
            #add shebang line
            if(list(list0).__len__()>0):
                cmd = list0[0]
            #print(".....")
            if(getplatform() == "Windows"):
                if (cmd_suffix == '.bat'):
                    if (cmd.startswith('@echo') is False):
                        f.write(cmd_header + cmd_return)
            else:
                if (cmd_suffix == '.sh'):
                    if (cmd.startswith('#!') is False):
                        f.write(cmd_header + cmd_return)

            for cmd in list0:
                f.write(cmd + cmd_return)

        if (plat == "Windows"):
            ""
        else:
            if(cmd_suffix == '.sh'):
                os.system("chmod +x " + cmd_exec)

        # print(cmd_codec)
        # print(cmd_suffix)
        # print(cmd_exec)

        return cmd_exec









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
        with open(cmd_exec, 'w', encoding=cmd_codec) as f:
            cmd = ''
            #add shebang line
            if(list(list0).__len__()>0):
                cmd = list0[0]
            #print(".....")
            if(getplatform() == "Windows"):
                if (cmd.startswith('@echo') is False):
                    f.write(cmd_header + cmd_return)
            else:
                if (cmd.startswith('#!') is False):
                    f.write(cmd_header + cmd_return)
            for cmd in list0:
                f.write(cmd + cmd_return)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_exec)

        return cmd_exec





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
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            cmd_return = "\n"
            cmd_header = "@echo off" + cmd_return
            env_set = 'set '
        else:
            cmd_suffix = ".sh"
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash" + cmd_return
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
                lines += (env_set + 'PATH=' + key + os.path.pathsep + '%PATH%' + cmd_return)
            else:
                lines += (env_set + 'PATH="' + key + '"' + os.path.pathsep + '$PATH' + cmd_return)

        #export var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += (env_set + key + '=' + value + cmd_return)
            else:
                lines += (env_set + key + '=\"' + value + '\"' + cmd_return)

        with open(cmd_effect, 'w', encoding=cmd_codec) as f:
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
                lines += (env_set + 'PATH=%PATH:' + key + ';=%' + cmd_return)
            else:
                lines += (env_set + 'PATH=$(' + 'echo ${PATH//' + key.replace('/', '\/') + ':/})' + cmd_return)

        #export unset var
        for (key, value) in dict0.items():
            if (key == 'path+'):
                continue
            if (plat == "Windows"):
                lines += ('set ' + key + '=' + cmd_return)
            else:
                lines += ('unset ' + key + cmd_return)
        with open(cmd_unset, 'w', encoding=cmd_codec) as f:
            f.write(cmd_header)
            f.write(lines)

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_effect)
            os.system("chmod +x " + cmd_unset)

        #return file name
        return current_var, cmd_effect, cmd_unset



    # .bat .sh, windows unix
    def createCmdList0(list0):

        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
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
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        for cmd in list0:
            cmd_list.append(cmd)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        if (plat == "Windows"):
            ""
        else:
            os.system("chmod +x " + cmd_execute)

        cmd_list.clear()
        if (plat == "Windows"):
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call " + cmd_execute + ' ' + cmd_sep + ' ' + cmd_status)
        else:
            # cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("./" + cmd_execute + ' ' + cmd_sep + ' ' + cmd_status)
        cmd_list.append(cmd_exit)

        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        # print (cmd_list)
        return cmd_list, name

    #.bat .sh, windows not compatibility, unix only [ignore]
    def createCmdList01(list0):

        cmd_list = []

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%errorlevel%"
            cmd_sep = '&'
            cmd_header = "@echo off"
            cmd_exit = 'exit /b %ERRORLEVEL%'
            # window close echo, close promot
            cmd_list.append(cmd_header + ' ' + cmd_sep + ' ' + cmd_status)
            cmd_list.append("call %s_effect.bat" % name + ' ' + cmd_sep + ' ' + cmd_status)
        else:
            cmd_status = "echo pymake-command-status:$?"
            cmd_sep = ';'
            cmd_exit = 'exit $?'
            cmd_header = "#!/usr/bin/env bash"
            cmd_list.append("source %s_effect.sh" % name + ' ' + cmd_sep + ' ' + cmd_status)

        for cmd in list0:
            cmd_list.append(cmd + ' ' + cmd_sep + ' ' + cmd_status)

        # append exit 0
        cmd_list.append(cmd_exit)
        # print( cmd_list )
        return cmd_list, name



    #.bat .sh, windows, unix
    def createCmdList02(env_name = None, local = True, list0 = [], params0 = []):

        cmd_list = []

        if(env_name is None):
            env_name = rawconfig['environ']['current']
        #print(env_name)

        name = uuid.uuid4().__str__()
        name = name.split('-')[0]
        #print (name)

        plat = getplatform()
        if (plat == "Windows"):
            cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
            cmd_sep = '&'
            cmd_codec = "ansi"
            if (getplatform_release() == "XP"):
                cmd_codec = None
            # but windows, it is \r\n, python helpping me?
            cmd_return = "\n"
            cmd_exit = 'exit /b %ERRORLEVEL%'
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
            cmd_exit = 'exit $?'
            cmd_codec = "utf8"
            cmd_return = "\n"
            cmd_header = "#!/usr/bin/env bash"
            cmd_call = "./"
            cmd_list.append(cmd_header)
            cmd_list.append("source %s_effect.sh" % name)

        #print(params0)
        params_string = ""
        for param in params0:
            #print(param)
            if(str(param).__contains__(' ')):
                params_string += '"' + param + '"' + ' '
            else:
                params_string += param + ' '
        #print(params_string)

        if ( local is True):
            for cmd in list0:
                cmd_list.append(cmd)
        else:
            for cmd in list0:
                if(str(cmd).__contains__(' ')):
                    pycmd = which_command(env_name, str(cmd))
                    #print(str(cmd))
                    #print(Fore.RED + "which command:", pycmd)
                    if(pycmd is not None and os.path.isfile(pycmd)):
                        cmd_list.append('"' + cmd + '"' + ' ' + params_string)
                    else:
                        cmd_list.append(cmd + ' ' + params_string)
                else:
                    cmd_list.append(cmd + ' ' + params_string)

        # append exit 0
        cmd_list.append(cmd_exit)
        #print( cmd_list )

        cmd_execute = name + "_exec" + cmd_suffix
        with open(cmd_execute, "w", encoding=cmd_codec) as f:
            for line in cmd_list:
                f.write(line + cmd_return)
        #print(cmd_execute)

        if(debugswitch == '1'):
            print("IN: execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

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
        if(debugswitch == '1'):
            print("CMD: call execute file: %s" % cmd_execute)
            for cmd in cmd_list:
                print(cmd)
            print("---------------------------")

        return cmd_list, name

    '''
    #edit.ini
    [page]
    number = 0
    '''
    pymakeeditini = os.path.join(sourceroot, 'edit.ini')
    conf3 = MyConfigParser()
    conf3.read(pymakeeditini)
    if( not conf3.has_section('edit') ):
        conf3.add_section('edit')
        conf3.write(open(pymakeeditini, 'w'))
    if( not conf3.has_option('edit', 'page') ):
        conf3.set('edit', 'page', '0')
        conf3.write(open(pymakeeditini, 'w'))

    page1 = conf3['edit']['page']
    #0->
    if(page1 < '0' or page1 > '9'):
        page1 = '0'
        conf3.set('edit', 'page', page1)
        conf3.write(open(pymakeeditini, 'w'))


    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QListView, QTextEdit
    from PyQt5 import uic
    from PyQt5.QtCore import Qt
    from PyQt5.QtCore import QStringListModel, QModelIndex, QItemSelectionModel
    from PyQt5.QtCore import QEvent
    from PyQt5.QtGui import QKeyEvent, QTextCursor, QTextDocument, QFontMetrics
    #from PyQt5.Qsci import QsciScintilla

    class Application(QApplication):
        def __init__(self, argv=[]):
            QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
            QApplication.__init__(self, argv)

    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            QMainWindow.__init__(self, parent)

            self.setupUi()
            self.setupData()
            self.statusBar.showMessage("Ready!GO!")

        def eventFilter(self, watched, event):
            ''
            if(event.type() == QEvent.Paint):
                return QMainWindow.eventFilter(self, watched, event)

            #print(event, watched)
            if(watched == self.textEditCommands):
                if(event.type() == QEvent.KeyPress):
                    if(event.key() == Qt.Key_S):
                        if(event.modifiers() & Qt.ControlModifier == Qt.ControlModifier):
                            #CTRL+S
                            #print(watched, event)
                            self.onBtnSaveCommandsClicked()
                            return False
                    #elif(event.key() == Qt.Key_Tab):
                    #    ''
                    #    self.textEditCommands.insertPlainText('    ')
                    #    return False

            elif(watched == self.textEditSeparatePath or watched == self.textEditSeparateEnv):
                if(event.type() == QEvent.KeyPress):
                    if(event.key() == Qt.Key_S):
                        if(event.modifiers() & Qt.ControlModifier == Qt.ControlModifier):
                            #CTRL+S
                            #print(watched, event)
                            self.onBtnSaveSeparateClicked()
                            return False


            elif(watched == self.textEditPaths):
                if(event.type() == QEvent.KeyPress):
                    if(event.key() == Qt.Key_S):
                        if(event.modifiers() & Qt.ControlModifier == Qt.ControlModifier):
                            #CTRL+S
                            #print(watched, event)
                            self.onBtnSavePathsClicked()
                            return False

            elif (watched == self.textEditCustomPath or watched == self.textEditCustomEnv):
                if(event.type() == QEvent.KeyPress):
                    if(event.key() == Qt.Key_S):
                        if(event.modifiers() & Qt.ControlModifier == Qt.ControlModifier):
                            #CTRL+S
                            #print(watched, event)
                            self.onBtnSaveCustomClicked()
                            return False

            elif(watched == self.textEditProgram):
                if(event.type() == QEvent.KeyPress):
                    if(event.key() == Qt.Key_S):
                        if(event.modifiers() & Qt.ControlModifier == Qt.ControlModifier):
                            #CTRL+S
                            #print(watched, event)
                            self.onBtnSaveProgramClicked()
                            return False

            return QMainWindow.eventFilter(self, watched, event)

        def setupUi(self):
            pyedituipath = pymakefilepath + os.path.sep + "tools/pyedit/mainwindow.ui"
            pyedituipath = os.path.join(pymakefilepath, 'tools', 'pyedit', 'mainwindow.ui')
            uic.loadUi(pyedituipath, self)

            self.indexPageProgram = 0
            self.indexPageSystem = 1
            self.indexPageLocal = 2
            self.indexPageCustom = 3
            self.indexPageSeparate = 4
            self.indexPageExecute = 5
            self.indexPageSource = 6
            self.indexPagePaths = 7
            self.indexPageCommands = 8
            self.indexPageReadMe = 9
            self.btnProgram.clicked.connect(self.onBtnProgramClicked)
            self.btnSystem.clicked.connect(self.onBtnSystemClicked)
            self.btnLocal.clicked.connect(self.onBtnLocalClicked)
            self.btnCustom.clicked.connect(self.onBtnCustomClicked)
            self.btnSeparate.clicked.connect(self.onBtnSeparateClicked)
            self.btnExecute.clicked.connect(self.onBtnExecuteClicked)
            self.btnSource.clicked.connect(self.onBtnSourceClicked)
            self.btnPaths.clicked.connect(self.onBtnPathsClicked)
            self.btnCommands.clicked.connect(self.onBtnCommandsClicked)
            self.btnReadMe.clicked.connect(self.onBtnReadMeClicked)

            self.btnSaveProgram.clicked.connect(self.onBtnSaveProgramClicked)
            self.btnSaveCustom.clicked.connect(self.onBtnSaveCustomClicked)
            self.btnSaveSeparate.clicked.connect(self.onBtnSaveSeparateClicked)
            self.btnSavePaths.clicked.connect(self.onBtnSavePathsClicked)
            self.btnSaveCommands.clicked.connect(self.onBtnSaveCommandsClicked)
            self.btnSaveExecute.clicked.connect(self.onBtnSaveExecuteClicked)
            self.btnSaveSource.clicked.connect(self.onBtnSaveSourceClicked)

            self.toolBtnCmdNew.clicked.connect(self.onToolBtnCmdNewClicked)
            self.toolBtnCmdDel.clicked.connect(self.onToolBtnCmdDelClicked)
            self.toolBtnCmdRename.clicked.connect(self.onToolBtnCmdRenameClicked)
            self.toolBtnCmdClone.clicked.connect(self.onToolBtnCmdCloneClicked)

            self.toolBtnEnvNew.clicked.connect(self.onToolBtnEnvNewClicked)
            self.toolBtnEnvDel.clicked.connect(self.onToolBtnEnvDelClicked)
            self.toolBtnEnvRename.clicked.connect(self.onToolBtnEnvRenameClicked)
            self.toolBtnEnvClone.clicked.connect(self.onToolBtnEnvCloneClicked)

            self.textEditProgram.installEventFilter(self)
            self.textEditCustomPath.installEventFilter(self)
            self.textEditCustomEnv.installEventFilter(self)
            self.textEditSeparatePath.installEventFilter(self)
            self.textEditSeparateEnv.installEventFilter(self)
            self.textEditPaths.installEventFilter(self)
            self.textEditCommands.installEventFilter(self)

            self.lineEditSearchPaths.textChanged.connect(self.onLineEditSearchPathsTextChanged)

            #self.onBtnProgramClicked()
            self.stackedWidget.setCurrentIndex(int(page1))


        def setPage(self, index):
            ''
            page1 = str(index)
            conf3.set('edit', 'page', page1)
            conf3.write(open(pymakeeditini, 'w'))

        def onBtnProgramClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageProgram)
            self.setPage(self.indexPageProgram)

        def onBtnSystemClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageSystem)
            self.setPage(self.indexPageSystem)

        def onBtnLocalClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageLocal)
            self.setPage(self.indexPageLocal)

        def onBtnCustomClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageCustom)
            self.setPage(self.indexPageCustom)

        def onBtnSeparateClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageSeparate)
            self.setPage(self.indexPageSeparate)

        def onBtnExecuteClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageExecute)
            self.setPage(self.indexPageExecute)

        def onBtnSourceClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageSource)
            self.setPage(self.indexPageSource)

        def onBtnPathsClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPagePaths)
            self.setPage(self.indexPagePaths)

        def onBtnCommandsClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageCommands)
            self.setPage(self.indexPageCommands)

        def onBtnReadMeClicked(self):
            self.stackedWidget.setCurrentIndex(self.indexPageReadMe)
            self.setPage(self.indexPageReadMe)

        def setupData(self):
            #program
            self.labelProgramIni.setText(pymakeini)
            with open(pymakeini, 'r', encoding=cmd_codec) as f:
                '''
                for l in f.readlines():
                    while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                        l = l.rstrip('\r\n')
                        l = l.rstrip('\n')
                        l = l.rstrip('\r')
                    self.textEditProgram.append(l)
                '''
                self.textEditProgram.append(''.join(f.readlines()))

            #custom
            self.labelCustom.setText(custompathfile + '\n' + customenvfile)
            with open(custompathfile, 'r', encoding=cmd_codec) as f:
                '''
                for l in f.readlines():
                    while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                        l = l.rstrip('\r\n')
                        l = l.rstrip('\n')
                        l = l.rstrip('\r')
                    self.textEditCustomPath.append(l)
                '''
                self.textEditCustomPath.append(''.join(f.readlines()))
            with open(customenvfile, 'r', encoding=cmd_codec) as f:
                '''
                for l in f.readlines():
                    while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                        l = l.rstrip('\r\n')
                        l = l.rstrip('\n')
                        l = l.rstrip('\r')
                    self.textEditCustomEnv.append(l)
                '''
                self.textEditCustomEnv.append(''.join(f.readlines()))


            '''
            for (key) in envcustomlistpaths:
                self.textEditCustomPath.append(key)
            for (key, value) in envcustomlistvars.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                self.textEditCustomEnv.append(key + '=' + value)
            '''

            #system
            for (key) in pymakesystemenviron['PATH'].split(os.path.pathsep):
                self.textEditSystemPath.append(key)
            for (key, value) in pymakesystemenviron.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                self.textEditSystemEnv.append(str("{0[0]}={0[1]}").format((key,value)))

            #execute
            if (workroottype == 'default'):
                self.radioBtnDefault.setChecked(True)
            elif (workroottype == 'here'):
                self.radioBtnHere.setChecked(True)
            elif (workroottype == 'there'):
                self.radioBtnThere.setChecked(True)
            self.lineEditThere.setText(customshellroot)

            #source
            self.labelSource.setText(sourceconfigfile)
            self.lineEditSourceRoot.setText(sourceroot)
            self.lineEditSourceConfig.setText(sourcefile)

            #local
            for (key) in localenv['path+']:
                self.textEditLocalPath.append(key)
            for (key, value) in localenv.items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                self.textEditLocalEnv.append(key + '=' + value)

            self.labelLocal.setText(localini)

            #separete
            self.labelSeparate.setText(sourceconfigfile)

            self.envmodel = QStringListModel(self.listViewSeparateEnvList)
            self.listViewSeparateEnvList.setModel(self.envmodel)
            self.envlist = list(config['environ'].keys())
            self.envlist.remove('current')
            #print(config['environ'].keys())
            if (self.envlist.__len__() <= 0):
                config['environ']['default']={}
                config['environ']['default']['path+']=[]
                config['environ']['current']='default'
                self.envlist.append("default")
            self.envmodel.setStringList(self.envlist)

            self.listViewSeparateEnvList.clicked.connect(self.onListViewSeparateEnvListClicked)
            self.listViewSeparateEnvList.selectionModel().currentRowChanged.connect(self.onListViewSeparateEnvListClicked)

            current_env = config['environ']['current']
            self.envIndex = QModelIndex()
            self.envIndex = self.listViewSeparateEnvList.model().index( self.envlist.index(current_env) )
            self.listViewSeparateEnvList.setCurrentIndex(self.envIndex)
            self.listViewSeparateEnvList.setEditTriggers(QListView.NoEditTriggers)


            #path assemblage
            self.labelPaths.setText(sourceconfigfile)
            paths = ''
            for k, v in config['path-assemblage'].items():
                paths += k + '=' + v + cmd_return
            self.textEditPaths.clear()
            self.textEditPaths.insertPlainText(paths)

            #command
            self.labelCommands.setText(sourceconfigfile)
            self.cmdmodel = QStringListModel(self.listViewCommands)
            self.listViewCommands.setModel(self.cmdmodel)
            self.cmdlist = list(config['command'].keys())
            #print(config['command'].keys())
            if (self.cmdlist.__len__() <= 0):
                config['command']['cmd.new1']=[]
                self.cmdlist.append("cmd.new1")
            self.cmdmodel.setStringList(self.cmdlist)

            current_cmd = self.cmdlist[0]
            self.labelCommand.setText(current_cmd)
            for (key) in config['command'][current_cmd]:
                #'' loading make 4 blank?
                self.textEditCommands.append(key)

            self.listViewCommands.clicked.connect(self.onListViewCommandsClicked)
            self.listViewCommands.selectionModel().currentRowChanged.connect(self.onListViewCommandsClicked)

            self.cmdIndex = QModelIndex()
            self.cmdIndex = self.listViewCommands.model().index( self.cmdlist.index(current_cmd) )
            self.listViewCommands.setCurrentIndex(self.cmdIndex)
            self.listViewCommands.setEditTriggers(QListView.NoEditTriggers)

            self.btnSource.setHidden(True)
            self.btnExecute.setHidden(True)

            #command edit, use QTextEdit? use QsciScililla?
            mertics = QFontMetrics(self.textEditCommands.font())
            self.textEditCommands.setTabStopWidth(4* mertics.width(' '))
            self.textEditCommands.setAcceptRichText(False)
            #self.textEditCommands.setLineWrapMode(QTextEdit.NoWrap)

            mertics = QFontMetrics(self.textEditProgram.font())
            self.textEditProgram.setTabStopWidth(4* mertics.width(' '))
            self.textEditProgram.setAcceptRichText(False)
            #self.textEditProgram.setLineWrapMode(QTextEdit.NoWrap)

            mertics = QFontMetrics(self.textEditCustomPath.font())
            self.textEditCustomPath.setTabStopWidth(4* mertics.width(' '))
            self.textEditCustomPath.setAcceptRichText(False)
            #self.textEditCustomPath.setLineWrapMode(QTextEdit.NoWrap)

            mertics = QFontMetrics(self.textEditCustomEnv.font())
            self.textEditCustomEnv.setTabStopWidth(4* mertics.width(' '))
            self.textEditCustomEnv.setAcceptRichText(False)
            #self.textEditCustomEnv.setLineWrapMode(QTextEdit.NoWrap)

            mertics = QFontMetrics(self.textEditSeparatePath.font())
            self.textEditSeparatePath.setTabStopWidth(4* mertics.width(' '))
            self.textEditSeparatePath.setAcceptRichText(False)
            #self.textEditSeparatePath.setLineWrapMode(QTextEdit.NoWrap)

            mertics = QFontMetrics(self.textEditSeparateEnv.font())
            self.textEditSeparateEnv.setTabStopWidth(4* mertics.width(' '))
            self.textEditSeparateEnv.setAcceptRichText(False)
            #self.textEditSeparateEnv.setLineWrapMode(QTextEdit.NoWrap)

            mertics = QFontMetrics(self.textEditPaths.font())
            self.textEditPaths.setTabStopWidth(4* mertics.width(' '))
            self.textEditPaths.setAcceptRichText(False)
            #self.textEditPaths.setLineWrapMode(QTextEdit.NoWrap)

        def onListViewSeparateEnvListClicked(self, index):
            if(not index.isValid()):
                self.statusBar.showMessage("Environ: invalid index!")
                return

            current_env = index.data()
            self.labelCurrentEnv.setText(current_env)

            paths = ''
            for (key) in config['environ'][current_env]['path+']:
                paths += key + cmd_return
            self.textEditSeparatePath.clear()
            self.textEditSeparatePath.insertPlainText(paths)

            envs = ''
            for (key, value) in config['environ'][current_env].items():
                if (key == 'path+'):
                    continue
                if (str(key).lower() == "path"):
                    continue
                envs += key + '=' + value + cmd_return
            self.textEditSeparateEnv.clear()
            self.textEditSeparateEnv.insertPlainText(envs)

            self.statusBar.showMessage("Show environ %s success!" % (current_env) )

        def onListViewCommandsClicked(self, index):
            if(not index.isValid()):
                self.statusBar.showMessage("Command: invalid index!")
                return

            current_cmd = index.data()
            self.labelCommand.setText(current_cmd)

            steps = ''
            for (key) in config['command'][current_cmd]:
                steps += key + cmd_return
            self.textEditCommands.clear()
            self.textEditCommands.insertPlainText(steps)

            self.statusBar.showMessage("Show command %s success!" % (current_cmd) )

        def onBtnSaveProgramClicked(self):
            programText = self.textEditProgram.toPlainText()
            with open(pymakeini, 'w', encoding=cmd_codec) as f:
                f.write(programText)
            self.statusBar.showMessage("Save program configure to file success!")
            self.setWindowTitle('Multi-environ Editor [WANTED: Software Reboot!]')

        def onBtnSaveCustomClicked(self):
            customPathText = self.textEditCustomPath.toPlainText()
            with open(custompathfile, 'w', encoding=cmd_codec) as f:
                f.write(customPathText)
            customEnvText = self.textEditCustomEnv.toPlainText()
            with open(customenvfile, 'w', encoding=cmd_codec) as f:
                f.write(customEnvText)
            self.statusBar.showMessage("Save custom environ success!")

        def onBtnSavePathsClicked(self):
            ''
            pathText = self.textEditPaths.toPlainText()
            config['path-assemblage'].clear()
            for l in pathText.split('\n'):
                key = str(l).split('=')[0].strip()
                value = '='.join(str(l).split('=')[1:]).strip()
                if(key == ''):
                    continue
                config['path-assemblage'][key] = value
            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Save path-assamblage section success!")

        def onBtnSaveSeparateClicked(self):
            ''
            index = self.listViewSeparateEnvList.currentIndex()
            if(not index.isValid()):
                self.statusBar.showMessage("Separate environ: has no selected env item!")
                return

            current_env = index.data()

            config['environ'][current_env].clear()
            config['environ'][current_env]['path+'] = []

            envVarText = self.textEditSeparateEnv.toPlainText()
            for l in envVarText.split('\n'):
                key = str(l).split('=')[0].strip()
                value = '='.join(str(l).split('=')[1:]).strip()
                if(key == ''):
                    continue
                if(key.lower() == 'path+'):
                    continue
                if(key.lower() == 'path'):
                    continue
                config['environ'][current_env][key] = value

            envPathText = self.textEditSeparatePath.toPlainText()
            for l in envPathText.split('\n'):
                key = str(l).strip()
                if(key == ''):
                    continue
                config['environ'][current_env]['path+'].append(key)

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Separate environ: save env item %s successed!" % (current_env))

        def onBtnSaveCommandsClicked(self):
            customCommandText = self.textEditCommands.toPlainText()
            current_cmd = self.listViewCommands.currentIndex().data()
            config['command'][current_cmd].clear()
            for l in customCommandText.split('\n'):
                l = str(l).replace('\t', '    ')
                config['command'][current_cmd].append(l)
            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Save command %s success!" % (current_cmd))

        def onToolBtnCmdNewClicked(self):
            ''
            cmdname = self.lineEditCmdName.text().strip()
            if(cmdname == ''):
                self.statusBar.showMessage("Command: cmd name is empty!")
                return

            #count <= 0
            if(self.cmdlist.__len__() <= 0):
                ''
                current_row = 0
                self.cmdlist.insert(current_row, cmdname)
                self.cmdmodel.insertRow(current_row)
                self.cmdmodel.setData(self.cmdmodel.index(current_row), cmdname)

                config['command'][cmdname] = []
                self.listViewCommands.setCurrentIndex(self.cmdmodel.index(current_row))

                writeJsonData(sourceconfigfile, config)
                self.statusBar.showMessage("Add command %s success!" % (cmdname))
                return

            index = self.listViewCommands.currentIndex()
            if(not index.isValid()):
                self.statusBar.showMessage("Command: has no command item selected!")
                return

            current_row = index.row()+1
            #current_cmd = index.data()

            if(self.cmdlist.__contains__(cmdname)):
                self.statusBar.showMessage("Command: %s is existed! index %s." % (cmdname,self.cmdlist.index(cmdname)))
                return

            self.cmdlist.insert(current_row, cmdname)
            self.cmdmodel.insertRow(current_row)
            self.cmdmodel.setData(self.cmdmodel.index(current_row), cmdname)

            config['command'][cmdname]=[]
            list_config = OrderedDict()
            for key in self.cmdlist:
                list_config[key] = copy.deepcopy(config['command'][key])
            config['command'] = {}
            for key in self.cmdlist:
                config['command'][key] = copy.deepcopy(list_config[key])

            self.listViewCommands.setCurrentIndex(self.cmdmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Add command %s success!" % (cmdname))

        def onToolBtnCmdDelClicked(self):
            ''
            cmdname = self.lineEditCmdName.text().strip()
            if(cmdname == ''):
                self.statusBar.showMessage("Command: cmd name is empty!")
                return

            if(not self.cmdlist.__contains__(cmdname)):
                self.statusBar.showMessage("Command: %s is not existed! no index." % (cmdname))
                return

            current_row = self.cmdlist.index(cmdname)
            #index = self.cmdmodel.index(current_row)
            #if(not index.isValid()):
            #    self.statusBar.showMessage("Command: command item is invalid, illegal index!")
            #    return

            config['command'].__delitem__(cmdname)
            self.cmdlist.remove(cmdname)
            self.cmdmodel.removeRow(current_row)
            # index = self.cmdmodel.index(current_row)
            if(current_row == self.cmdlist.__len__()):
                current_row = current_row - 1
            self.listViewCommands.setCurrentIndex(self.cmdmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Delete command %s success!" % (cmdname))

        def onToolBtnCmdRenameClicked(self):
            ''
            cmdname = self.lineEditCmdName.text().strip()
            if(cmdname == ''):
                self.statusBar.showMessage("Command: cmd name is empty!")
                return

            index = self.listViewCommands.currentIndex()
            if(not index.isValid()):
                self.statusBar.showMessage("Command: has no command item selected!")
                return

            if(self.cmdlist.__contains__(cmdname)):
                self.statusBar.showMessage("Command: %s is existed! index %s." % (cmdname,self.cmdlist.index(cmdname)))
                return

            current_row = index.row()
            current_cmd = index.data()

            #save list
            cmddata = copy.deepcopy(config['command'][current_cmd])

            #del
            config['command'].__delitem__(current_cmd)
            self.cmdlist.remove(current_cmd)
            self.cmdmodel.removeRow(current_row)

            #add
            self.cmdlist.insert(current_row, cmdname)
            self.cmdmodel.insertRow(current_row)
            self.cmdmodel.setData(self.cmdmodel.index(current_row), cmdname)

            config['command'][cmdname]=[]
            list_config = OrderedDict()
            for key in self.cmdlist:
                list_config[key] = copy.deepcopy(config['command'][key])
            config['command'] = {}
            for key in self.cmdlist:
                config['command'][key] = copy.deepcopy(list_config[key])
            config['command'][cmdname]=copy.deepcopy(cmddata)

            self.listViewCommands.setCurrentIndex(self.cmdmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Rename command %s to %s success!" % (current_cmd, cmdname))

        def onToolBtnCmdCloneClicked(self):
            ''
            cmdname = self.lineEditCmdName.text().strip()
            if(cmdname == ''):
                self.statusBar.showMessage("Command: cmd name is empty!")
                return

            index = self.listViewCommands.currentIndex()
            if(not index.isValid()):
                self.statusBar.showMessage("Command: has no command item selected!")
                return

            if(self.cmdlist.__contains__(cmdname)):
                self.statusBar.showMessage("Command: %s is existed! index %s." % (cmdname,self.cmdlist.index(cmdname)))
                return

            current_row = index.row()+1
            current_cmd = index.data()

            #save list
            cmddata = copy.deepcopy(config['command'][current_cmd])

            #no del
            #config['command'].__delitem__(current_cmd)
            #self.cmdlist.remove(current_cmd)
            #self.cmdmodel.removeRow(current_row)

            #add
            self.cmdlist.insert(current_row, cmdname)
            self.cmdmodel.insertRow(current_row)
            self.cmdmodel.setData(self.cmdmodel.index(current_row), cmdname)

            config['command'][cmdname]=[]
            list_config = OrderedDict()
            for key in self.cmdlist:
                list_config[key] = copy.deepcopy(config['command'][key])
            config['command'] = {}
            for key in self.cmdlist:
                config['command'][key] = copy.deepcopy(list_config[key])
            config['command'][cmdname]=copy.deepcopy(cmddata)

            self.listViewCommands.setCurrentIndex(self.cmdmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Clone command %s to %s success!" % (current_cmd, cmdname))

        def onToolBtnEnvNewClicked(self):
            ''
            envname = self.lineEditEnvName.text().strip()
            if(envname == ''):
                self.statusBar.showMessage("Environ: env name is empty!")
                return

            #count <= 0
            if(self.envlist.__len__() <= 0):
                ''
                current_row = 0
                self.envlist.insert(current_row, envname)
                self.envmodel.insertRow(current_row)
                self.envmodel.setData(self.envmodel.index(current_row), envname)

                if(config['environ'].__contains__('current')):
                    config['environ'].__delitem__('current')
                config['environ'][envname] = {}
                config['environ'][envname]['path+'] = []
                config['environ']['current'] = envname
                self.listViewCommands.setCurrentIndex(self.envmodel.index(current_row))

                writeJsonData(sourceconfigfile, config)
                self.statusBar.showMessage("Add env %s success!" % (envname))
                return

            index = self.listViewSeparateEnvList.currentIndex()
            if(not index.isValid()):
                self.statusBar.showMessage("Environ: has no env item selected!")
                return

            current_row = index.row()+1
            #current_env = index.data()

            if(self.envlist.__contains__(envname)):
                self.statusBar.showMessage("Environ: %s is existed! index %s." % (envname,self.envlist.index(envname)))
                return

            self.envlist.insert(current_row, envname)
            self.envmodel.insertRow(current_row)
            self.envmodel.setData(self.envmodel.index(current_row), envname)

            current_env_var = config['environ']['current']
            config['environ'][envname]={}
            config['environ'][envname]['path+']=[]
            list_config = OrderedDict()
            for key in self.envlist:
                list_config[key] = copy.deepcopy(config['environ'][key])
            config['environ'] = {}
            for key in self.envlist:
                config['environ'][key] = copy.deepcopy(list_config[key])
            config['environ']['current'] = current_env_var

            self.listViewSeparateEnvList.setCurrentIndex(self.envmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Add env %s success!" % (envname))

        def onToolBtnEnvDelClicked(self):
            ''
            envname = self.lineEditEnvName.text().strip()
            if(envname == ''):
                self.statusBar.showMessage("Environ: env name is empty!")
                return

            if(not self.envlist.__contains__(envname)):
                self.statusBar.showMessage("Environ: %s is not existed! no index." % (envname))
                return

            if(config['environ']['current'] == envname):
                self.statusBar.showMessage("Environ: %s is current env, cant be deleted!" % (envname))
                return

            current_row = self.envlist.index(envname)
            #index = self.envmodel.index(current_row)
            #if(not index.isValid()):
            #    self.statusBar.showMessage("Environ: env item is invalid, illegal index!")
            #    return

            config['environ'].__delitem__(envname)
            self.envlist.remove(envname)
            self.envmodel.removeRow(current_row)
            #index = self.envmodel.index(current_row)
            if(current_row == self.cmdlist.__len__()):
                current_row = current_row - 1
            self.listViewSeparateEnvList.setCurrentIndex(self.envmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Delete env %s success!" % (envname))

        def onToolBtnEnvRenameClicked(self):
            ''
            envname = self.lineEditEnvName.text().strip()
            if(envname == ''):
                self.statusBar.showMessage("Environ: env name is empty!")
                return

            index = self.listViewSeparateEnvList.currentIndex()
            if(not index.isValid()):
                self.statusBar.showMessage("Environ: has no env item selected!")
                return

            if(self.envlist.__contains__(envname)):
                self.statusBar.showMessage("Environ: %s is existed! index %s." % (envname, self.envlist.index(envname)))
                return

            current_row = index.row()
            current_env = index.data()

            #save list
            envdata = copy.deepcopy(config['environ'][current_env])

            #del
            config['environ'].__delitem__(current_env)
            self.envlist.remove(current_env)
            self.envmodel.removeRow(current_row)

            #add
            self.envlist.insert(current_row, envname)
            self.envmodel.insertRow(current_row)
            self.envmodel.setData(self.envmodel.index(current_row), envname)

            current_env_var = config['environ']['current']
            config['environ'][envname]={}
            config['environ'][envname]['path+']=[]
            list_config = OrderedDict()
            for key in self.envlist:
                list_config[key] = copy.deepcopy(config['environ'][key])
            config['environ'] = {}
            for key in self.envlist:
                config['environ'][key] = copy.deepcopy(list_config[key])
            config['environ'][envname]=copy.deepcopy(envdata)
            config['environ']['current'] = current_env_var

            self.listViewSeparateEnvList.setCurrentIndex(self.envmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Rename env %s to %s success!" % (current_env, envname))

        def onToolBtnEnvCloneClicked(self):
            ''
            envname = self.lineEditEnvName.text().strip()
            if(envname == ''):
                self.statusBar.showMessage("Environ: env name is empty!")
                return

            index = self.listViewSeparateEnvList.currentIndex()
            if(not index.isValid()):
                self.statusBar.showMessage("Environ: has no env item selected!")
                return

            if(self.envlist.__contains__(envname)):
                self.statusBar.showMessage("Environ: %s is existed! index %s." % (envname, self.envlist.index(envname)))
                return

            current_row = index.row()+1
            current_env = index.data()

            #save list
            envdata = copy.deepcopy(config['environ'][current_env])

            #no del
            #config['environ'].__delitem__(current_env)
            #self.envlist.remove(current_env)
            #self.envmodel.removeRow(current_row)

            #add
            self.envlist.insert(current_row, envname)
            self.envmodel.insertRow(current_row)
            self.envmodel.setData(self.envmodel.index(current_row), envname)

            current_env_var = config['environ']['current']
            config['environ'][envname]={}
            config['environ'][envname]['path+']=[]
            list_config = OrderedDict()
            for key in self.envlist:
                list_config[key] = copy.deepcopy(config['environ'][key])
            config['environ'] = {}
            for key in self.envlist:
                config['environ'][key] = copy.deepcopy(list_config[key])
            config['environ'][envname]=copy.deepcopy(envdata)
            config['environ']['current'] = current_env_var

            self.listViewSeparateEnvList.setCurrentIndex(self.envmodel.index(current_row))

            writeJsonData(sourceconfigfile, config)
            self.statusBar.showMessage("Clone env %s to %s success!" % (current_env, envname))

        def onLineEditSearchPathsTextChanged(self, text):
            ''
            doc = self.textEditPaths.document()
            textCursor = QTextCursor(doc)
            textCursor = doc.find(text, textCursor)

            if(textCursor.isNull()):
                #textCursor.movePosition(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                textCursor = QTextCursor(doc)
            self.textEditPaths.setTextCursor(textCursor)


            '''
                layout = textCursor.block().layout()
                cursorPos = textCursor.position() - textCursor.block().position()
                cursorLineNumber = layout.lineForTextPosition(cursorPos).lineNumber() + textCursor.block().firstLineNumber()
                cursorPos = self.textEditPaths.cursorRect(textCursor).topLeft()
                self.textEditPaths.verticalScrollBar().setValue(cursorPos.y())
            '''

            '''
            doc = self.textEditPaths.document()
            textCursor = QTextCursor(doc)
            textCursor = doc.find(text, textCursor)
            print(textCursor.isNull())
            if(not textCursor.isNull()):
                textCursor.movePosition(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                print(self.textEditPaths.cursorRect(textCursor))
                cursorPos = self.textEditPaths.cursorRect(textCursor).topLeft()
                if(cursorPos.x() >= 0 and cursorPos.y() >= 0):
                    self.textEditPaths.scrollContentsBy(0, cursorPos.y())
            '''

        def onBtnSaveSourceClicked(self):
            roottext = self.lineEditSourceRoot.text()
            configtext = self.lineEditSourceConfig.text()
            #roottext = roottext.strip()
            #configtext = configtext.strip()
            allpath = os.path.join(roottext, configtext)
            self.labelSource.setText(allpath)
            conf['source']['root'] = roottext
            conf['source']['config'] = configtext
            conf.write(open(pymakeini, 'w'))

            self.statusBar.showMessage("Save program configure, source config success!")
            self.setWindowTitle('Multi-environ Editor [WANTED: Software Reboot!]')

        def onBtnSaveExecuteClicked(self):
            roottext = 'default'
            if (self.radioBtnDefault.isChecked()):
                roottext = 'default'
            elif (self.radioBtnHere.isChecked()):
                roottext = 'here'
            elif (self.radioBtnThere.isChecked()):
                roottext = 'there'

            theretext = self.lineEditThere.text()
            conf['work']['root'] = roottext
            conf['work']['there'] = theretext
            conf.write(open(pymakeini, 'w'))

            self.statusBar.showMessage("Save program configure, work root config success!")
            self.setWindowTitle('Multi-environ Editor [WANTED: Software Reboot!]')


    app = Application(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


    return

if __name__ == '__main__':
    ret = main_function()
    if(ret == None):
        ret = 0
    os._exit(ret)
