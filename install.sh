#!/usr/bin/env bash

#install path
mmpath=/usr/local/bin

#get pymake.sh path (current path)
filepath=$(cd `dirname $0`; pwd)
chmod +x ${filepath}/*.sh

#create pymake link
sudo ln -sf ${filepath}/pymake.sh ${mmpath}/mm
sudo ln -sf ${filepath}/pymake.sh ${mmpath}/pymm
sudo ln -sf ${filepath}/pymake.sh ${mmpath}/pymake

sudo ln -sf ${filepath}/pyenv.sh ${mmpath}/pyenv
sudo ln -sf ${filepath}/pycmd.sh ${mmpath}/pycmd
sudo ln -sf ${filepath}/pyexecvp.sh ${mmpath}/pyexecvp

sudo ln -sf ${filepath}/pyinfo.sh ${mmpath}/pyinfo
