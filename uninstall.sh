#!/usr/bin/env bash

#install path
mmpath=/usr/local/bin

uninstall () {
    sudo rm -f ${mmpath}/${mmfile}
    echo uninstall ${mmfile}
}

#delete pymake link
mmfile=mm
uninstall

mmfile=pymm
uninstall

mmfile=pymake
uninstall

mmfile=pyenv
uninstall

mmfile=pytype
uninstall

mmfile=pyexport
uninstall

mmfile=pycmd
uninstall

mmfile=pyexecvp
uninstall

mmfile=pyccvp
uninstall

mmfile=pypython
uninstall

mmfile=pylanguage
uninstall

mmfile=pyclean
uninstall

mmfile=pyinfo
uninstall

mmfile=pypaths
uninstall

mmfile=pyedit
uninstall

mmfile=pysys
uninstall

mmfile=pysystem
uninstall

mmfile=pylocal
uninstall

mmfile=pycustom
uninstall

echo uninstalled.