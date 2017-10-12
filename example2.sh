#!/usr/bin/env bash

mm set env cur 'qt'
#do command in this env
mm k build
mm k 'ls -l'
mm k 'java -version'

#no need to reset
