#!/usr/bin/env bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
#echo .... $DIR

PYPROGRAMPATH=${DIR}
PYPROGRAMNAME=pymake.sh
PYPROGRAMPATHNAME=$PYPROGRAMPATH/$PYPROGRAMNAME

WORKROOT=$(pymake get default exec root)
WORKROOT=$WORKROOT/MyShell
mkdir -p $WORKROOT

command=pymake language exec-with-params here "sh -c env" --params "pytest.py"
echo $command
$command

command=pymake language exec-with-params here "env" --params "pytest.py"
echo $command
$command

command=pymake language exec-with-params here "sh file" --params "pytest.py"
echo $command
$command

command=pymake language exec-with-params here "sh -c file" --params "pytest.py"
echo $command
$command

command=pymake language exec-with-params here "file" --params "build.pro"  --suffix .sh
echo $command
$command

command=pymake language exec-with-params here "test_file.sh" --params "test.6"
echo $command
$command

command=pymake language exec-with-params here "file" --params "test.6"
echo $command
$command
