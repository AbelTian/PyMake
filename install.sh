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

sourcefile=pycmd.sh
mmfile=pycmd
install

sourcefile=pyexecvp.sh
mmfile=pyexecvp
install

sourcefile=pyccvp.sh
mmfile=pyccvp
install

sourcefile=pylanguage.sh
mmfile=pylanguage
install

sourcefile=pyinfo.sh
mmfile=pyinfo
install

sourcefile=pypaths.sh
mmfile=pypaths
install

echo installed.