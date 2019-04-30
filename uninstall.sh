#!/usr/bin/env bash

#install path
mmpath=/usr/local/bin

#delete pymake link
sudo rm -f ${mmpath}/mm
sudo rm -f ${mmpath}/pymm
sudo rm -f ${mmpath}/pymake

sudo rm -f ${mmpath}/pyenv
sudo rm -f ${mmpath}/pycmd
sudo rm -f ${mmpath}/pyexecvp
sudo rm -f ${mmpath}/pyccvp

sudo rm -f ${mmpath}/pyinfo
