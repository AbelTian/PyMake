#!/usr/bin/env bash

ename=qqtrelease0

build.qqt.release() {
    src_path=/Users/abel/Develop/a0-develop/LibQQt
    src=/Users/abel/Develop/a0-develop/LibQQt/QQt.pro
    build=/Users/abel/Develop/c0-buildstation/QQt/${QTVERSION}/${QSYS}/Release
    mkdir -p $build
    cd $build
    echo build $(pwd)
    rm -rf src/bin examples/*/bin
    rm -rf ${src_path}/../QQt/${QTVERSION}/${QSYS}/Release
    qmake $src ${QTSPEC} "CONFIG+=release" ${QTCONFIG} && make qmake_all
    make -j4
}

#env effect
mm export 'macOS' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt.release
#env reset (need)
source $(mm source root)/${ename}_unset.sh


#env effect
mm export 'qt4' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt.release
#env reset (need)
source $(mm source root)/${ename}_unset.sh


#env effect
mm export 'android.mobile' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt.release
#env reset (need)
source $(mm source root)/${ename}_unset.sh


#env effect
mm export 'android.x86' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt.release
#env reset (need)
source $(mm source root)/${ename}_unset.sh


#env effect
mm export iOS ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt.release
#env reset (need)
source $(mm source root)/${ename}_unset.sh


#env effect
mm export 'iOSSimulator' ${ename}
source $(mm source root)/${ename}_effect.sh
#do command in this env
build.qqt.release
#env reset (need)
source $(mm source root)/${ename}_unset.sh
