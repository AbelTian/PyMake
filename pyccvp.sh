#!/usr/bin/env bash
file=$(readlink -n "$0")
filepath=${file%/*}
if [ "${filepath}" = "" ]
then
    filepath=$(cd `dirname $0`; pwd)
fi

$filepath/pyexecvp.sh "$@"
