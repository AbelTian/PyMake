#!/usr/bin/env bash

build.module (){
    src_path=/Users/abel/Develop/a0-develop
    build_path=/Users/abel/Develop/c0-buildstation
    src=/Users/abel/Develop/a0-develop/${module_name}/${module_name}.pro
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

env.open () {
    mm export $1 $2
    source $(mm get default exec root)/$2_effect.sh
}

env.close () {
    source $(mm get default exec root)/$1_unset.sh
}

#####################################################
module_name=QQtExquisite

#env effect
env.open 'macOS' $module_name
#do command in this env
build.module
#env reset
env.close $module_name


#env effect
env.open 'iOSSimulator' $module_name
#do command in this env
#build.module
#env reset
env.close $module_name
