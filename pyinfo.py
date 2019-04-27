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

    args = docopt(__doc__, version='pyinfo.py v1.0')
    #print(args)

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
