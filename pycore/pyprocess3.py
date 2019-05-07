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

# windows *unix
def communicateWithCommandLine3(list0):
    shell = "powershell"

    plat = getplatform()
    #if(plat == "Windows"):
    #    shell = os.environ.get('COMSPEC') + ' ' + "/q /d /s /a /v:on /e:on /f:on"
    #else:
    #    shell = os.environ.get('SHELL')
    #print ( 'Running under', shell )

    global  cmd_event
    cmd_event = threading.Event()
    global cmd_exit_flag
    cmd_exit_flag = 0

    startupinfo = None
    createflags = 0
    if (plat == 'Windows' ):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.dwFlags |= subprocess.STARTF_USESTDHANDLES
        startupinfo.wShowWindow = subprocess.SW_HIDE
        #createflags = subprocess.CREATE_NEW_CONSOLE

    p = subprocess.Popen(shell, shell=False,
                         bufsize=-1,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         #if dont do this, windows stdout piory is high, stderr cant output full message
                         #when split stdout and stderr, lots of app wont manager the output order
                         stderr=subprocess.STDOUT,
                         startupinfo=startupinfo, creationflags=createflags)
    read_thread = threading.Thread(target=read_thread_function, args=(p,))
    read_thread.start()
    read_err_thread = threading.Thread(target=read_stderr_thread_function, args=(p,))
    #read_err_thread.start()
    write_command_thread = threading.Thread(target=write_command_thread_function, args=(p, list0))
    write_command_thread.start()
    write_thread = threading.Thread(target=write_thread_function, args=(p,))
    write_thread.start()
    # time.sleep(1)

    try:
        p.wait()
    except (KeyboardInterrupt):
        p.returncode = 1

    if (read_thread.isAlive()):
        stopThread(read_thread)
    if (read_err_thread.isAlive()):
        stopThread(read_err_thread)
    if (write_command_thread.isAlive()):
        stopThread(write_command_thread)
    if (write_thread.isAlive()):
        stopThread(write_thread)

    # time.sleep(1)
    return p.returncode
