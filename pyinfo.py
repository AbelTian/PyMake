# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyInfo 1.0.

Usage:
  pyinfo.py get pc
  pyinfo.py get pc home
  pyinfo.py get pc [ setting ]
  pyinfo.py get pc [ desk ] [ doc ] [ download ] [ music ] [ picture ] [ movie ]
  pyinfo.py get pc [ favorite ] [ search ] [ contact ]
  pyinfo.py get pc [ develop ]
  pyinfo.py get date [ -y | -m | -d ] [ -f <sep-character> ]
  pyinfo.py get time [ -h | -m | -s ] [ -f <sep-character> ]
  pyinfo.py get datetime [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get platform
  pyinfo.py (-h | --help)
  pyinfo.py --version

Command:
  get              lots of important information.

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import os
import re
import sys
import uuid
import shutil
import time
import json
import copy
import types
from pycore.pycore import *

def main_function():

    # record current directory [pwd, execute path]
    pymakeworkpath = os.getcwd()
    #print( "pymake work path:", pymakeworkpath )

    # record pymake file directory [program file path]
    pymakefilepath = os.path.split(os.path.realpath(__file__))[0]
    #print( "pymake file path:", pymakefilepath )

    # record pymake user source root [env, *.json] [ + auto create ]
    pymakesourceroot = pymakefilepath + os.path.sep + 'USERSOURCE'
    if (not os.path.exists(pymakesourceroot)):
        os.makedirs(pymakesourceroot)
    #print( "pymake user source path:", pymakesourceroot )

    # record pymake user shell root [ dynamic work path ] [ ignored -> v7.2 ]
    pymakeshellroot = pymakefilepath + os.path.sep + 'USERSOURCE' + os.path.sep + 'USERSHELL'
    #if (not os.path.exists(pymakeshellroot)):
    #    os.makedirs(pymakeshellroot)
    #print( "pymake user shell path:", pymakeshellroot )

    """
    [pymake]
    [source]
    root = ~/.pymake
    config = pymake.json
    """
    userroot = getuserroot()
    configroot = getconfigroot()
    plat = getplatform()
    #record pymake configure directory. [ in user config path ]
    pymakeroot = userroot + os.path.sep + '.pymake'
    if (not os.path.exists(pymakeroot)):
        os.makedirs(pymakeroot)

    #initial pymake.ini
    pymakeini = pymakeroot + os.path.sep + 'pymake.ini'
    conf = MyConfigParser()
    conf.read(pymakeini)
    if( not conf.has_section('pymake') ):
        conf.add_section('pymake')
        conf.write(open(pymakeini, 'w'))
    if( not conf.has_section('source') ):
        conf.add_section('source')
        conf.write(open(pymakeini, 'w'))
    if( not conf.has_option('source', 'root') ):
        conf.set('source', 'root', pymakesourceroot)
        conf.write(open(pymakeini, 'w'))
    if(not conf.has_option('source', 'config')):
        conf.set('source', 'config', 'pymake.json')
        conf.write(open(pymakeini, 'w'))

    #record user source root directory
    sourceroot = conf.get('source', 'root')
    #record source config file name
    sourcefile = conf.get('source', 'config')
    #record source config file
    sourceconfigfile = sourceroot + os.path.sep + sourcefile
    #print ("root: %s config: %s" % (sourceroot, sourcefile))
    #print("use source config: %s" % (sourceconfigfile) )

    #record default source config file name
    defaultsourcefile = 'pymake.json'
    #record default source config file
    defaultsourceconfigfile = sourceroot + os.path.sep + defaultsourcefile
    #print ("root: %s default config: %s" % (sourceroot, defaultsourcefile))
    #print("default source config: %s" % (defaultsourceconfigfile) )

    # init pymake.json in sourceroot [ + program create ]
    if (not os.path.exists(sourceroot)):
        os.makedirs(sourceroot)
    os.chdir(sourceroot)

    args = docopt(__doc__, version='pyinfo.py v1.0')
    #print(args)


    # I set this,
    # pymake default execute user bat/sh in pymakeshellroot,
    # user can use here param to restrict exec action.
    # cd user shell root [ default shell execute path ]
    pymakeshellroot = sourceroot
    os.chdir(pymakeshellroot)

    # get
    while (True):
        if (args['get'] == True):
            if (args['pc'] is True):
                userroot = getuserroot()
                #linux path is chinese, why?
                #windows only
                userdoc = userroot + os.path.sep + "Documents"
                userdown = userroot + os.path.sep + "Downloads"
                userset = getconfigroot()
                userdesk = userroot + os.path.sep + "Desktop"
                usermusic = userroot + os.path.sep + "Music"
                usermovie = userroot + os.path.sep + "Videos" #Movies
                userfavo = userroot + os.path.sep + "Favorites"
                usersearch = userroot + os.path.sep + "Searches"
                usercontact = userroot + os.path.sep + "Contacts"
                userpictures = userroot + os.path.sep + "Pictures"
                userdev = userroot + os.path.sep + "Develop"
                if (args['home']):
                    print(userroot)
                elif (args['setting']):
                    print(userset)
                elif (args['doc']):
                    print(userdoc)
                elif (args['download']):
                    print(userdown)
                elif (args['desk']):
                    print(userdesk)
                elif (args['music']):
                    print(usermusic)
                elif (args['movie']):
                    print(usermovie)
                elif (args['favorite']):
                    print(userfavo)
                elif (args['search']):
                    print(usersearch)
                elif (args['contact']):
                    print(usercontact)
                elif (args['picture']):
                    print(userpictures)
                elif (args['develop']):
                    print(userdev)
                else:
                    print(userroot)
                    print(userset)
                    print(userdesk)
                    print(userdoc)
                    print(userdown)
                    print(usermusic)
                    print(userpictures)
                    print(usermovie)
                    print(usersearch)
                    print(usercontact)
                    print(userdev)
                return
            else:
                ''
            return
        else:
            ''
        break

    return

if __name__ == '__main__':
    main_function()
