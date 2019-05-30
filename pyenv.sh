#!/usr/bin/env bash

while [ 1 ]
do


export PYENVFLAG=1
if [ "$1" = "" ]
then
    echo usage:
    echo "  pyenv <env-name>"
    echo "  pyenv open <env-name>"
    echo "  pyenv close <env-name>"
    echo "  <env name>: 'current' is suggested."
    echo ------
    echo please appoint a env name.
    break
elif [ "$1" = "open" ]
then
    if [ "$2" = "" ]
    then
        echo usage:
        echo "  pyenv <env-name>"
        echo "  pyenv open <env-name>"
        echo "  pyenv close <env-name>"
        echo "  <env name>: 'current' is suggested."
        echo ------
        echo please appoint a env name.
        break
    fi
    export PYENVNAME=$2
elif [ "$1" = "close" ]
then
    if [ "$2" = "" ]
    then
        echo usage:
        echo "  pyenv <env-name>"
        echo "  pyenv open <env-name>"
        echo "  pyenv close <env-name>"
        echo "  <env name>: 'current' is suggested."
        echo ------
        echo please appoint a env name.
        break
    fi
    export PYENVNAME=$2
    export PYENVFLAG=0
else
    export PYENVNAME=$1
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

echo preparing env ...
export PYENVINDEX=$(echo $RANDOM)
echo env index: \[$PYENVINDEX\]

export PYMMSOURCEROOT=$("${PYPROGRAMPATHNAME}" source root)
echo location : \[$PYMMSOURCEROOT\]

export PYMMSOURCECONFIG=$("$PYPROGRAMPATHNAME" source config)
echo configure: \[$PYMMSOURCECONFIG\] \[1\]

export PYMMDEFAULTENVNAME=$("$PYPROGRAMPATHNAME" get current env)
echo environme: \[$PYMMDEFAULTENVNAME\] \[default\]
export PYENVEXISTEDFLAG=$("$PYPROGRAMPATHNAME" have env $PYENVNAME)
if [ "$PYENVEXISTEDFLAG" = "False" ]; then
    echo environme: \[$PYENVNAME\] is not existed.
    break
fi
echo environme: \[$PYENVNAME\] \[$PYENVEXISTEDFLAG\] \[USED\]

export PYMMSHELLROOT=$("$PYPROGRAMPATHNAME" get default exec root)
echo exec root: \[$PYMMSHELLROOT\] \[default\]
echo exec root: \[$(pwd)\] \[here\]

"$PYPROGRAMPATHNAME" export2 $PYENVNAME to $PYENVINDEX --local --custom

if [ $PYENVFLAG -eq 0 ]; then
    if [ -f "${PYMMSHELLROOT}/${PYENVINDEX}_unset.sh" ]; then
        chmod +x "${PYMMSHELLROOT}/${PYENVINDEX}_unset.sh"
        source "${PYMMSHELLROOT}/${PYENVINDEX}_unset.sh"
        echo successed: \[$PYENVNAME\] closed
    else
        echo failed\ \ \ : \[$PYENVNAME\] close failed
    fi
else
    if [ -f "${PYMMSHELLROOT}/${PYENVINDEX}_effect.sh" ]; then
        chmod +x "${PYMMSHELLROOT}/${PYENVINDEX}_effect.sh"
        source "${PYMMSHELLROOT}/${PYENVINDEX}_effect.sh"
        echo successed: \[$PYENVNAME\] opened
    else
        echo failed\ \ \ : \[$PYENVNAME\] open failed
    fi
fi

#clean
rm -f "${PYMMSHELLROOT}/${PYENVINDEX}_effect.sh" "${PYMMSHELLROOT}/${PYENVINDEX}_unset.sh"

#unset filepath
#unset PYENVEXISTEDFLAG
#unset PYENVFLAG
#unset PYENVINDEX
#unset PYENVNAME
#unset PYMMDEFAULTENVNAME
#unset PYMMSOURCECONFIG
#unset PYMMSOURCEROOT
#unset PYPROGRAMNAME
#unset PYPROGRAMPATH
#unset PYPROGRAMPATHNAME
#unset PYMMSHELLROOT

break
done