#!/usr/bin/env bash
file=$(readlink -n "$0")
filepath=${file%/*}
py=$(which python3)
${py} $filepath/pymake8.py "$@"
