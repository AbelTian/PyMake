#!/usr/bin/env bash

while [ 1 ]
do

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
#echo .... $DIR

export PYPROGRAMPATH=${DIR}
export PYPROGRAMNAME=tools/pyedit/pyedit.py
export PYPROGRAMPATHNAME=$PYPROGRAMPATH/$PYPROGRAMNAME

py=$(which python3)
${py} "$PYPROGRAMPATHNAME" "$@" &
exit $?

break
done