#!/usr/bin/env bash
#get pymake.sh path
filepath=$(cd `dirname $0`; pwd)

#create mm link
sudo ln -sf $filepath/pymake.sh /usr/local/bin/mm
