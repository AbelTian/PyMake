#!/usr/bin/env bash

#install path
mmpath=/usr/local/bin

#get pymake.sh path (current path)
filepath=$(cd `dirname $0`; pwd)
chmod +x ${filepath}/*.sh

install () {
    sudo ln -sf ${filepath}/${sourcefile} ${mmpath}/${mmfile}
    echo install ${mmfile}
}

#create pymake link
sourcefile=pymake.sh
mmfile=mm
install

sourcefile=pymake.sh
mmfile=pymm
install

sourcefile=pymake.sh
mmfile=pymake
install

sourcefile=pyenv.sh
mmfile=pyenv
install

sourcefile=pytype.sh
mmfile=pytype
install

sourcefile=pyexport.sh
mmfile=pyexport
install

sourcefile=pycmd.sh
mmfile=pycmd
install

sourcefile=pyexecvp.sh
mmfile=pyexecvp
install

sourcefile=pyccvp.sh
mmfile=pyccvp
install

sourcefile=pypython.sh
mmfile=pypython
install

sourcefile=pylanguage.sh
mmfile=pylanguage
install

sourcefile=pyclean.sh
mmfile=pyclean
install

sourcefile=pyinfo.sh
mmfile=pyinfo
install

sourcefile=pypaths.sh
mmfile=pypaths
install

sourcefile=pyedit.sh
mmfile=pyedit
install

sourcefile=pysys.sh
mmfile=pysys
install

sourcefile=pysystem.sh
mmfile=pysystem
install

sourcefile=pylocal.sh
mmfile=pylocal
install

sourcefile=pycustom.sh
mmfile=pycustom
install

echo installed.