#!/usr/bin/env bash

mm set env cur 'qt'
#do command in this env
mm k build
mm k 'ls -l'

#no need to reset
