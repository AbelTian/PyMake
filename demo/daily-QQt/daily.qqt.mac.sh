#!/usr/bin/env bash

daily.qqt (){
    src_path=/Users/abel/Develop/a0-develop/LibQQt
    src=${src_path}/QQt.pro
    build=/Users/abel/Develop/c0-buildstation/QQt/${QSYS}/${QTVERSION}/Debug
    mkdir -p $build
    cd $build
    #rm -rf src examples
    #rm -rf ${src_path}/sdk
    qmake $src ${QTSPEC} ${QTCONFIG} "CONFIG+=debug" "CONFIG+=qml_debug" && make qmake_all
    make -j4
}

daily.qqt.release(){
    src_path=/Users/abel/Develop/a0-develop/LibQQt
    src=${src_path}/QQt.pro
    build=/Users/abel/Develop/c0-buildstation/QQt/${QTVERSION}/${QSYS}/Release
    mkdir -p $build
    cd $build
    #rm -rf src examples
    #rm -rf ${src_path}/sdk
    qmake $src ${QTSPEC} ${QTCONFIG} "CONFIG+=release" && make qmake_all
    make -j4
}

#env effect
mm set cur env 'macOS'
#do command in this env
mm exec build.qqt
#env reset (no need)

#mm set cur env qt4
#mm exec daily.qqt
#mm exec daily.qqt.release

#env effect
#mm set cur env 'android.mobile'
#do command in this env
#mm exec daily.qqt
#mm exec daily.qqt.release
#env reset (no need)

#env effect
#mm set cur env 'android.x86'
#do command in this env
#mm exec daily.qqt
#mm exec daily.qqt.release
#env reset (no need)

#mm set cur env iOS
#mm exec daily.qqt
#mm exec daily.qqt.release

mm set cur env iOSSimulator
mm exec build.qqt

mm set cur env macOS
