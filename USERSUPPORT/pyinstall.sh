#!/usr/bin/env bash
#get pyenv.sh path
filepath=$(cd `dirname $0`; pwd)

#create pyenv link
sudo ln -sf $filepath/pyenv.sh /usr/local/bin/pyenv
