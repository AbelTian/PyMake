#!/usr/bin/env bash

#main while
while [ 1 ]
do


if [ "$1" = "" ]; then
    echo usage:
    echo "  pytype <cmd-name> [ <script-name> ] [ <env-name> ]"
    echo ------
    echo please appoint a cmd name.
    break
fi
export PYEXECNAME=$1

export PYSCRIPTNAME=$2
if [ "$2" = "" ]; then
    export PYSCRIPTNAME=
fi

export PYENVNAME=$3
if [ "$3" = "" ]; then
    export PYENVNAME=current
fi

#if has source[.] call , failed. source default work path is user home.
#这些都只是获取到了工作路径
#used for a link to sh
#file=$(readlink -n "$0")
#export PYPROGRAMPATH=${file%/*}
#if [ "${PYPROGRAMPATH}" != "" ]; then
#    PYPROGRAMPATH=$PYPROGRAMPATH/..
#else
#    #used for a real call to sh
#    PYPROGRAMPATH=$(cd `dirname $0`; pwd)/..
#fi

#used for call directory to this sh, include source[.] call.
#export PYPROGRAMPATH=$(cd ..; pwd)

#这个有价值，这个可以获得 source 直接调用的文件名。但是还没有达到目的。source调用的必须找到真的文件。
#DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
#echo "dir_path is $DIR_PATH"

#这段代码彻底解决了问题，怎么调用都是对的。= __file__
#在任意目录，
#直接调用 sh 文件
#调用 link
#source 调用 sh 文件
#source 调用 link 文件
#结果都是准确的。
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
#echo .... $DIR

export PYPROGRAMPATH=${DIR}
export PYPROGRAMNAME=pymake.sh
export PYPROGRAMPATHNAME=$PYPROGRAMPATH/$PYPROGRAMNAME

#echo $file
#echo $PYPROGRAMPATH
#echo $(pwd)
##. 获取到的是 -bash
#echo "$0" "$1"
#echo $(filename "$0")
#echo $0 | awk -F'\' '{print $NF}'

#echo starting cmd ...
#export PYEXECINDEX=$(echo $RANDOM)
#echo env index: \[$PYEXECINDEX\]

#export PYMMSOURCEROOT=$("${PYPROGRAMPATHNAME}" source root)
#echo location : \[$PYMMSOURCEROOT\]

#export PYMMSOURCECONFIG=$("$PYPROGRAMPATHNAME" source config)
#echo configure: \[$PYMMSOURCECONFIG\] \[1\]

#export PYMMDEFAULTENVNAME=$("$PYPROGRAMPATHNAME" get current env)
#echo environme: \[$PYMMDEFAULTENVNAME\] \[default\]
#if [ "$2" != "" ]; then
#    export PYENVNAME=$2
#else
#    export PYENVNAME=$PYMMDEFAULTENVNAME
#fi

#export PYEXECFLAG=$("$PYPROGRAMPATHNAME" have env $PYENVNAME)
#if [ "$PYEXECFLAG" = "False" ]; then
#    echo environme: \[$PYENVNAME\] is not existed.
#    break
#fi
#echo environme: \[$PYENVNAME\] \[$PYEXECFLAG\] \[USED\]

#export PYEXECFLAG=$("$PYPROGRAMPATHNAME" have cmd $PYEXECNAME)
#if [ "$PYEXECFLAG" = "False" ]; then
#    echo command\ \ : \[$PYEXECNAME\] is system wild command.
#else
#    echo command\ \ : \[$PYEXECNAME\] \[$PYEXECFLAG\] \[EXISTED\]
#fi

#export PYMMSHELLROOT=$("$PYPROGRAMPATHNAME" get default exec root)
#echo exec root: \[$PYMMSHELLROOT\] \[default\]
#echo exec root: \[$(pwd)\] \[here\]

"$PYPROGRAMPATHNAME" use $PYENVNAME type here $PYEXECNAME $PYSCRIPTNAME


break
done