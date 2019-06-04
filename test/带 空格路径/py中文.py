# -*- coding: utf-8 -*-
#!/usr/bin/env python
BBB="""PyInfo 1.0.

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


#try:
#    import chardet
#except ModuleNotFoundError as e:
#    print("要先安装包!!! 请进入python安装目录，执行一下代码。")
#    print("pip install chardet")
#    os._exit(1)
#finally:
#    ''
    
def main_function():
    print("BBB")
    print(__file__)
    print(os.getcwd())
    print(len(sys.argv))
    print(sys.argv)
    for path0 in sys.argv:
        print ("PARAMS:", path0)
    return

if __name__ == '__main__':
    main_function()
