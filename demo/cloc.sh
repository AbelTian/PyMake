#!/usr/bin/env bash

#name
pwd

#cloc 所在路径
filepath=$(cd "$(dirname "$0")"; pwd)
perl $filepath/cloc-1.74.pl .

#date
date
