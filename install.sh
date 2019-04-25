#!/usr/bin/env bash
#get pymake.sh path (current path)
filepath=$(cd `dirname $0`; pwd)

chmod +x $filepath/*.sh

#create pymake link
sudo ln -sf $filepath/pymake.sh /usr/local/bin/mm
sudo ln -sf $filepath/pymake.sh /usr/local/bin/pymm
sudo ln -sf $filepath/pymake.sh /usr/local/bin/pymake
sudo ln -sf $filepath/pyenv.sh /usr/local/bin/pyenv
sudo ln -sf $filepath/pycmd.sh /usr/local/bin/pycmd
sudo ln -sf $filepath/pyinfo.sh /usr/local/bin/pyinfo
