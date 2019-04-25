#!/usr/bin/env bash


pymake source file "$(pwd)/../example/pymake6-mac.json"
pycmd test

echo "work path   : ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ is work path."
echo "current path: $(pwd)"

echo "two path equals, success."
