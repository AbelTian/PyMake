#!/usr/bin/env bash
# create mm link
# sudo ln -s xxx/pymake6.sh /usr/local/bin/mm

#env effect
mm set env cur 'qt.android'
mm export
source $(mm source root)/env_effect.sh
#do command in this env

#env reset (need)
source $(mm source root)/env_unset.sh

