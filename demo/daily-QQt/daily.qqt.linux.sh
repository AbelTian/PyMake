#!/usr/bin/env bash

daily.qqt (){
    src_path=/home/tdr/Develop/a0-develop/LibQQt
    src=${src_path}/QQt.pro
    build=/home/tdr/Develop/c0-buildstation/QQt/${QSYS}/${QTVERSION}/Debug
    mkdir -p $build
    cd $build
    echo build $(pwd)
    #rm -rf ./*
    #rm -rf ${src_path}/../QQt/${QSYS}/${QTVERSION}/Debug
    qmake $src ${QTSPEC} "CONFIG+=debug" "CONFIG+=qml_debug" ${QTCONFIG} && make qmake_all
    make -j4
}

daily.qqt.release(){
    src_path=/home/abel/Develop/a0-develop/LibQQt
    src=${src_path}/QQt.pro
    build=/home/abel/Develop/c0-buildstation/QQt/${QSYS}/${QTVERSION}/Release
    mkdir -p $build
    cd $build
    echo build $(pwd)
    rm -rf ./*
    rm -rf ${src_path}/../QQt/${QSYS}/${QTVERSION}/Release
    qmake $src ${QTSPEC} ${QTCONFIG} "CONFIG+=release" && make qmake_all
    make -j4
}

ename=qqtdebug0

#env effect
mm export 'qt5' ${ename}
source $(mm get default exec root)/${ename}_effect.sh
#do command in this env
daily.qqt
#daily.qqt.release
#env reset (need)
source $(mm get default exec root)/${ename}_unset.sh


#env effect
mm export 'qt5.armhf32' ${ename}
source $(mm get default exec root)/${ename}_effect.sh
#do command in this env
daily.qqt
#daily.qqt.release
#env reset (need)
source $(mm get default exec root)/${ename}_unset.sh
