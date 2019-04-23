#!/usr/bin/env bash
#get pycmd.sh path
filepath=$(cd `dirname $0`; pwd)

#create pycmd link
sudo ln -sf $filepath/pycmd.sh /usr/local/bin/pycmd
