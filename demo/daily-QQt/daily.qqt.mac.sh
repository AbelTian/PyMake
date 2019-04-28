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

build.module (){
    src_path=/Users/abel/Develop/a0-develop
    build_path=/Users/abel/Develop/c0-buildstation
    src=/Users/abel/Develop/a0-develop/LibQQt/${module_name}.pro
    build=/Users/abel/Develop/c0-buildstation/${module_name}/${QSYS}/${QTVERSION}/Debug
    echo build $src
    echo in $build
    mkdir -p $build
    cd $build
    #rm -rf src examples
    #rm -rf ${src_path}/sdk
    qmake $src ${QTSPEC} ${QTCONFIG} "CONFIG+=debug" "CONFIG+=qml_debug" && make qmake_all
    make -j4
}

module_name=QQt
. pyenv macos
build.module
. pyenv close macos

. pyenv iossimulator
build.module
. pyenv close iossimulator


#success
#env effect
#mm set cur env 'macos'
#do command in this env
#mm exec build.qqt
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

#success
#mm set cur env iossimulator
#mm exec build.qqt
#mm set cur env macos
