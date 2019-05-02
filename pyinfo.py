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
  pyinfo.py get date [ -Y | -m | -d ] [ -f <sep-character> ]
  pyinfo.py get time [ -H | -M | -S ] [ -f <sep-character> ]
  pyinfo.py get datetime [ -Y | -m | -d | -H | -M | -S ] [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get datetime [ <std-datetime-string> ] [ -t | -T ]
  pyinfo.py get datetime [ <timestamp> ] [ --string ] [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get datetime timedelta <time1> [ <time2> ] [ --struct | --number ] [ --format=<format-string> ]
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
import datetime
import json
import copy
import types
from pycore.pycore import *

def main_function():

    args = docopt(__doc__, version='pyinfo.py v1.0')
    print(args)

    # get
    while (True):
        if (args['get'] == True):
            if (args['pc'] is True):
                userroot = getuserroot()
                plat = getplatform()
                #linux path is chinese, why?
                #windows darwin
                userdoc = userroot + os.path.sep + "Documents"
                userdown = userroot + os.path.sep + "Downloads"
                userset = getconfigroot()
                userdesk = userroot + os.path.sep + "Desktop"
                usermusic = userroot + os.path.sep + "Music"
                usermovie = userroot + os.path.sep + "Videos"
                if(plat == "Darwin"):
                    usermovie = userroot + os.path.sep + "Movies"
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
            elif (args['platform'] is True):
                plat = getplatform()
                print(plat)
            elif (args['time'] is True):
                #print(datetime.datetime.today())
                #print(datetime.date.today())
                if(args['-H'] is True):
                    print(datetime.datetime.now().strftime("%H"))
                elif (args['-M'] is True):
                    print(datetime.datetime.now().strftime("%M"))
                elif (args['-S'] is True):
                    print(datetime.datetime.now().strftime("%S"))
                else:
                    sep = "%H:%M:%S"
                    if(args['<sep-character>'] is not None):
                        sep = str("%%H%s%%M%s%%S" % ( args['<sep-character>'], args['<sep-character>']))
                    print(datetime.datetime.now().strftime(sep))
            elif (args['date'] is True):
                # print(datetime.datetime.today())
                # print(datetime.date.today())
                if (args['-Y'] is True):
                    print(datetime.datetime.now().strftime("%Y"))
                elif (args['-m'] is True):
                    print(datetime.datetime.now().strftime("%m"))
                elif (args['-d'] is True):
                    print(datetime.datetime.now().strftime("%d"))
                else:
                    sep = "%Y:%m:%d"
                    if (args['<sep-character>'] is not None):
                        sep = str("%%Y%s%%m%s%%d" % (args['<sep-character>'], args['<sep-character>']))
                    print(datetime.datetime.now().strftime(sep))
            elif (args['datetime'] is True):
                # print(datetime.datetime.today())
                # print(datetime.date.today())
                if (args['-Y'] is True):
                    print(datetime.datetime.now().strftime("%Y"))
                elif (args['-m'] is True):
                    print(datetime.datetime.now().strftime("%m"))
                elif (args['-d'] is True):
                    print(datetime.datetime.now().strftime("%d"))
                elif (args['-t'] is True):
                    str0 = str("%d" % time.mktime(datetime.datetime.today().timetuple()))
                    if(args['<std-datetime-string>'] is not None):
                        struct_time = time.localtime(float(args['<std-datetime-string>']))
                        str0 = str("%d" % time.mktime(struct_time))
                        print(str0)
                    print(str0.split('.')[0])
                elif (args['-T'] is True):
                    print(datetime.datetime.today().timestamp())
                else:
                    sep = "%Y-%m-%d %H:%M:%S"
                    sep1 = '-'
                    sep2 = ' '
                    sep3 = ':'
                    if (args['<sep-character>'] is not None):
                        sep1 = args['<sep-character>']
                    if (args['<sep2-character>'] is not None):
                        sep2 = args['<sep2-character>']
                    if (args['<sep3-character>'] is not None):
                        sep3 = args['<sep3-character>']
                    sep = str("%%Y%s%%m%s%%d%s%%H%s%%M%s%%S" % ( sep1, sep1, sep2, sep3, sep3))
                    print(datetime.datetime.now().strftime(sep))
            else:
                ''
            return
        else:
            ''
        break

    return

if __name__ == '__main__':
    main_function()
