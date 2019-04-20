#!/usr/bin/env bash
#get pymake.sh path
filepath=$(cd `dirname $0`; pwd)

#create pymm link
sudo ln -sf $filepath/pymake8.sh /usr/local/bin/pymm
