#!/usr/bin/env bash

ename=qqtdebug0

build.qqt() {
    src_path=/home/abel/Develop/a0-develop/LibQt
    src=${src_path}/QQt.pro
    build=/home/abel/Develop/c0-buildstation/QQt/${QTVERSION}/${QSYS}/Debug
    mkdir -p $build
    cd $build
    echo build $(pwd)
    rm -rf src/bin examples/*/bin
    rm -rf ${src_path}/../QQt/${QTVERSION}/${QSYS}/Debug
    qmake $src ${QTSPEC} "CONFIG+=debug" "CONFIG+=qml_debug" ${QTCONFIG} && make qmake_all
    make -j4
}

#env effect
mm export 'qt5' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt
#env reset (need)
source $(mm source root)/${ename}_unset.sh


#env effect
mm export 'qt4' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt
#env reset (need)
source $(mm source root)/${ename}_unset.sh


#env effect
mm export 'mips32' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt
#env reset (need)
source $(mm source root)/${ename}_unset.sh

