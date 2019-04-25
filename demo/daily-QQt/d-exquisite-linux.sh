#!/usr/bin/env bash

build.module (){
    src_path=/home/tdr/Develop/a0-develop
    build_path=/home/tdr/Develop/c0-buildstation
    src=${src_path}/${module_name}/${module_name}.pro
    build=${build_path}/${module_name}/${QSYS}/${QTVERSION}/Debug
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
    source $(mm source root)/$2_effect.sh
}

env.close () {
    source $(mm source root)/$1_unset.sh
}

#####################################################
module_name=QQtExquisite

#env effect
env.open 'qt5' $module_name
#do command in this env
build.module
#env reset
env.close $module_name


#env effect
env.open 'qt5.armhf32' $module_name
#do command in this env
build.module
#env reset
env.close $module_name
