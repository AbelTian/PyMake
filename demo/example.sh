#!/usr/bin/env bash

function env_effect(){
    mm export $1 $2
    source $(mm source root)/$2_effect.sh
}

function env_unset(){
    source $(mm source root)/$1_unset.sh
}

#env effect (shared environment)
mm set cur env 'qt.android'
#do command in this env
mm exec qqt.build
#env reset (no need)



#env effect (shared environment)
mm set cur env 'android.x86'
#do configed command in this env
mm exec qqt.build
#env reset (no need)


#env effect (private environment)
env_effect 'android.x86' x86
#do custom command in this env
java -version
#env reset (need)
env_unset x86

#env effect (shared environment)
mm set cur env 'android.x86'


#env effect (private environment)
env_effect 'android.mobile' mobile
#do custom command in this env
env_unset mobile





#env effect (shared environment)
mm export
source $(mm source root)/env_effect.sh
#do command in this env
java -version
#env reset (need)
source $(mm source root)/env_unset.sh



#env effect (shared environment)
mm set cur env 'qt.android'
#do command in this env
mm exec 'java -version'
#env reset (no need)
