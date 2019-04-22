from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import os
import sys
import ctypes
import inspect
import codecs
import locale
import threading
import subprocess

from .pybase import *
from .pyprocess import *

def communicateWithCommandLine2(list0):
    shell = ""
    plat = getplatform()
    if(plat == "Windows"):
        shell = os.environ.get('COMSPEC') + ' ' + "/k"
    else:
        return communicateWithCommandLine(list0)
    #print ( 'Running under', shell )

    shell += ' ' + list0[0]
    #print(shell)

    startupinfo = None
    createflags = 0
    if (plat == 'Windows' ):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.dwFlags |= subprocess.STARTF_USESTDHANDLES
        startupinfo.wShowWindow = not subprocess.SW_HIDE
        createflags = subprocess.CREATE_NEW_CONSOLE

    p = subprocess.Popen(shell, shell=False,
                         bufsize=-1,
                         stdin=None, stdout=None,
                         #if dont do this, windows stdout piory is high, stderr cant output full message
                         #when split stdout and stderr, lots of app wont manager the output order
                         stderr=None,
                         startupinfo=startupinfo, creationflags=createflags)

    return 0
