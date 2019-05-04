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

mmfile=pycmd
uninstall

mmfile=pyexecvp
uninstall

mmfile=pyccvp
uninstall

mmfile=pyinfo
uninstall

mmfile=pypaths
uninstall

echo uninstalled.