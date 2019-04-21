#!/usr/bin/env bash
#get pymake.sh path
filepath=$(cd `dirname $0`; pwd)/..

#create pymake link
sudo ln -sf $filepath/pymake.sh /usr/local/bin/pymake
