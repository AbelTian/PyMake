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
  pyinfo.py get time [ -H | -M | -S ] [ -f <sep-character> ]
  pyinfo.py get date [ -t | -T ] [ -Y | -m | -d ] [ -f <sep-character> ]
  pyinfo.py get datetime [ -t | -T ] [ -Y | -m | -d | -H | -M | -S ] [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get datetime [ <timestamp> ] --timestamp [ -t | -T ] [ -Y | -m | -d | -H | -M | -S ] [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get datetime [ <std-datetime-string> ] --datetime [ -t | -T ] [ -Y | -m | -d | -H | -M | -S ] [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get datetime [ <std-datetime1-string> <std-datetime2-string> ] --datetime --diff [ -t | -T ] [ -Y | -m | -d | -H | -M | -S ] [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get datetime [ <timestamp1> <timestamp2> ] --timestamp --diff [ -t | -T ] [ -Y | -m | -d | -H | -M | -S ] [ -f <sep-character> <sep2-character> <sep3-character> ]
  pyinfo.py get timestamp [ <std-datetime-string> ] [ -t | -T ]
  pyinfo.py get platform
  pyinfo.py get command list [ --pymake ]
  pyinfo.py (-h | --help)
  pyinfo.py --version

Command:
  get              lots of important information.

Params:
  <std-datetime-string>         YYYY-mm-dd HH:MM:SS
  <timestamp>                   seconds to 1970-01-01 00:00:00, unique.
  -t | -T                       output timestamp, different precision.
  -Y | -m | -d | -H | -M | -S   outputting quantity.
  -f                            outputting style.

Options:
  -h --help     Show this screen.
  --version     Show version.
  --timestamp   restrict inputting timestamp.
  --datetime    restrict inputting std datetime string.
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
    #print(args)

    pyinfoworkpath = os.getcwd()
    pyinfoprogrampath = os.path.split(os.path.realpath(__file__))[0]

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
                tuple_time = datetime.datetime.now()
                if(args['-t'] is True):
                    #str0 = str("%d" % time.mktime(datetime.date.timetuple(datetime.date(2014, 5, 5))) )
                    str0 = str("%s" % tuple_time.date())
                    strp_tuple = tuple_time.strptime(str0, "%Y-%m-%d")
                    str0 = str("%d" % strp_tuple.timestamp())
                    print(str0)
                    return
                elif (args['-T'] is True):
                    str0 = str("%s" % tuple_time.date())
                    strp_tuple = tuple_time.strptime(str0, "%Y-%m-%d")
                    str0 = str("%s" % strp_tuple.timestamp())
                    print(str0)
                    return

                if (args['-Y'] is True):
                    print(datetime.datetime.now().strftime("%Y"))
                elif (args['-m'] is True):
                    print(datetime.datetime.now().strftime("%m"))
                elif (args['-d'] is True):
                    print(datetime.datetime.now().strftime("%d"))
                else:
                    sep = "%Y-%m-%d"
                    if (args['<sep-character>'] is not None):
                        sep = str("%%Y%s%%m%s%%d" % (args['<sep-character>'], args['<sep-character>']))
                    print(datetime.datetime.now().strftime(sep))
            elif (args['datetime'] is True):
                # print(datetime.datetime.today())
                # print(datetime.date.today())
                tuple_time = datetime.datetime.now()
                #print(tuple_time)

                if(args['--diff'] is True):
                    tuple_time1 = tuple_time
                    tuple_time2 = tuple_time

                    float_time1 = 0
                    float_time2 = 0
                    if(args['<std-datetime1-string>'] is not None):
                        tuple_time1 = datetime.datetime.strptime(args['<std-datetime1-string>'], '%Y-%m-%d %H:%M:%S')
                        float_time1 = tuple_time1.timestamp()
                    if(args['<std-datetime2-string>'] is not None):
                        float_time2 = tuple_time2.timestamp()
                        tuple_time2 = datetime.datetime.strptime(args['<std-datetime2-string>'], '%Y-%m-%d %H:%M:%S')

                    if (args['<timestamp1>'] is not None):
                        float_time1 = float(args['<timestamp1>'])
                        tuple_time1 = datetime.datetime.fromtimestamp(float(args['<timestamp1>']))
                    if (args['<timestamp2>'] is not None):
                        float_time2 = float(args['<timestamp2>'])
                        tuple_time2 = datetime.datetime.fromtimestamp(float(args['<timestamp2>']))

                    tuple_time = datetime.datetime.fromtimestamp(float_time1 - float_time2)

                    #detla_time = tuple_time1 - tuple_time2
                    #print(detla_time.total_seconds())
                    #struct_time = time.localtime(detla_time.total_seconds())
                    #print(time.ctime(detla_time.total_seconds()))
                    #print(time.time())
                    #print(struct_time)
                    #print(datetime.datetime(*struct_time[0:6]))
                    #print(datetime.datetime.replace(datetime.datetime.today(), *struct_time[0:6]))
                    #day0 = datetime.datetime.replace(datetime.datetime.today(), year=1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
                    #print(day0)
                    #print(datetime.datetime.fromtimestamp(detla_time.total_seconds()))
                    #struct_time = day0.timetuple()
                    #print(time.mktime(struct_time))
                    #time0 = time.strptime("0001-1-1 0:0:0","%Y-%m-%d %H:%M:%S")
                    #print(time0)

                    if (args['-t'] is True):
                        str0 = str("%d" % tuple_time.timestamp())
                        print(str0)
                        return
                    elif (args['-T'] is True):
                        str0 = str("%s" % tuple_time.timestamp())
                        print(str0)
                        return

                #--timestamp
                if (args['<timestamp>'] is not None):
                    # string_time = datetime.datetime.fromtimestamp(float(args['<timestamp>'])).strftime('%Y-%m-%d %H:%M:%S')
                    #tuple_time = time.localtime(float(args['<timestamp>']))
                    #print(tuple_time)
                    #tuple_time = time.strptime(datetime.datetime.fromtimestamp(float(args['<timestamp>'])).strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
                    #print(tuple_time)
                    tuple_time = datetime.datetime.fromtimestamp(float(args['<timestamp>']))
                    #print(tuple_time)
                    if (args['-t'] is True):
                        str0 = str("%d" % tuple_time.timestamp())
                        print(str0)
                        return
                    elif (args['-T'] is True):
                        str0 = str("%s" % tuple_time.timestamp())
                        print(str0)
                        return

                #--datetime
                if (args['<std-datetime-string>'] is not None):
                    #struct_time = time.strptime(args['<std-datetime-string>'], '%Y-%m-%d %H:%M:%S')
                    #print(struct_time)
                    #time struct time -> datetime tuple time
                    #tuple_time = datetime.datetime(*struct_time[0:6])
                    #print(tuple_time)
                    tuple_time = datetime.datetime.strptime(args['<std-datetime-string>'], '%Y-%m-%d %H:%M:%S')
                    #print(tuple_time)
                    #c_time = datetime.datetime.ctime(tuple_time)
                    if (args['-t'] is True):
                        str0 = str("%d" % tuple_time.timestamp())
                        print(str0)
                        return
                    elif (args['-T'] is True):
                        str0 = str("%s" % tuple_time.timestamp())
                        print(str0)
                        return

                if(args['-t'] is True):
                    #datetime tuple time -> time struct time
                    #str0 = str("%d" % time.mktime(datetime.datetime.timetuple(tuple_time)))
                    str0 = str("%d" % tuple_time.timestamp())
                    print(str0)
                    return
                elif (args['-T'] is True):
                    str0 = str("%s" % tuple_time.timestamp())
                    print(str0)
                    return

                if (args['-Y'] is True):
                    print(tuple_time.strftime("%Y"))
                elif (args['-m'] is True):
                    print(tuple_time.strftime("%m"))
                elif (args['-d'] is True):
                    print(tuple_time.strftime("%d"))
                elif (args['-H'] is True):
                    print(tuple_time.strftime("%H"))
                elif (args['-M'] is True):
                    print(tuple_time.strftime("%M"))
                elif (args['-S'] is True):
                    print(tuple_time.strftime("%S"))
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
                    print(tuple_time.strftime(sep))
            elif (args['timestamp'] is True):
                tuple_time = datetime.datetime.now()
                if (args['<std-datetime-string>'] is not None):
                    tuple_time = tuple_time.strptime(args['<std-datetime-string>'], '%Y-%m-%d %H:%M:%S')

                if (args['-t'] is True):
                    str0 = str("%d" % tuple_time.timestamp())
                    print(str0)
                    #print(str0.split('.')[0])
                elif (args['-T'] is True):
                    str0 = str("%s" % tuple_time.timestamp())
                    print(str0)
                else:
                    str0 = str("%s" % tuple_time.timestamp())
                    print(str0)
            elif (args['command'] is True):
                plat = getplatform()
                for fi in os.listdir(pyinfoprogrampath):
                    if(fi == "install.bat" or fi == "uninstall.bat"):
                        continue

                    postfix = ".sh"
                    if(plat == "Windows"):
                        postfix = '.bat'

                    if(fi.endswith(postfix) is True):
                        print(fi)

                print("pycodec.py")
            else:
                ''
            return
        else:
            ''
        break

    return

if __name__ == '__main__':
    main_function()
