#!/usr/bin/env bash

filepath=$(cd `dirname $0`; pwd)

cd $filepath/..

sudo ./uninstall.sh

mm --version
pymm --version
pymake --version
pyenv current
pycmd test
pyinfo --version

sudo ./install.sh

mm --version
pymm --version
pymake --version
pyenv current
pycmd test
pyinfo --version
