#!/usr/bin/env bash
#get *.sh path
filepath=$(cd `dirname $0`; pwd)

#
chmod +x $filepath/*.sh
chmod +x $filepath/USERSUPPORT/*.sh
