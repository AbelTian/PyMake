#!/usr/bin/env bash

#main while
while [ 1 ]
do



if [ "$1" = "" ]; then
    echo "pylanguage <cmd-name> [ <cmd-params> ... ]"
    echo please appoint a cmd name.
    break
fi
export PYEXECNAME=$1

export PYEXECPARAM2=$2
export PYEXECPARAM3=$3
export PYEXECPARAM4=$4
export PYEXECPARAM5=$5
export PYEXECPARAM6=$6
export PYEXECPARAM7=$7
export PYEXECPARAM8=$8
export PYEXECPARAM9=$9


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
#echo $1 $2 $3
#if [ "$3" != "" ]; then
#    export PYENVNAME=$3
#else
#    export PYENVNAME=$PYMMDEFAULTENVNAME
#fi
export PYENVNAME=current
#echo $PYENVNAME
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

#echo $PYEXECPARAM
#echo $PYEXECPARAM2
#echo $PYEXECPARAM3
#echo $PYEXECPARAM4
#echo $PYEXECPARAM5
#echo $PYEXECPARAM6
#echo $PYEXECPARAM7
#echo $PYEXECPARAM8
#echo $PYEXECPARAM9
#echo "$PYPROGRAMPATHNAME" use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3" --params "$PYEXECPARAM4" --params "$PYEXECPARAM5" --params "$PYEXECPARAM6" --params "$PYEXECPARAM7" --params "$PYEXECPARAM8" --params "$PYEXECPARAM9"


if [ "$PYEXECPARAM9" != "" ]; then
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3" --params "$PYEXECPARAM4" --params "$PYEXECPARAM5" --params "$PYEXECPARAM6" --params "$PYEXECPARAM7" --params "$PYEXECPARAM8" --params "$PYEXECPARAM9"
elif [ "$PYEXECPARAM8" != "" ]; then
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3" --params "$PYEXECPARAM4" --params "$PYEXECPARAM5" --params "$PYEXECPARAM6" --params "$PYEXECPARAM7" --params "$PYEXECPARAM8"
elif [ "$PYEXECPARAM7" != "" ]; then
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3" --params "$PYEXECPARAM4" --params "$PYEXECPARAM5" --params "$PYEXECPARAM6" --params "$PYEXECPARAM7"
elif [ "$PYEXECPARAM6" != "" ]; then
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3" --params "$PYEXECPARAM4" --params "$PYEXECPARAM5" --params "$PYEXECPARAM6"
elif [ "$PYEXECPARAM5" != "" ]; then
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3" --params "$PYEXECPARAM4" --params "$PYEXECPARAM5"
elif [ "$PYEXECPARAM4" != "" ]; then
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3" --params "$PYEXECPARAM4"
elif [ "$PYEXECPARAM3" != "" ]; then
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2" --params "$PYEXECPARAM3"
elif [ "$PYEXECPARAM2" != "" ]; then
    #echo .....
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME" --params "$PYEXECPARAM2"
else
    "$PYPROGRAMPATHNAME" language use $PYENVNAME exec-with-params here "$PYEXECNAME"
fi

break
done