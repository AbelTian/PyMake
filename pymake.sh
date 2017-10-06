#!/usr/bin/env bash
file=$(readlink -n "$0")
filepath=${file%/*}
py=$(which python)
py=python3
${py} $filepath/pymake6.py "$@"
