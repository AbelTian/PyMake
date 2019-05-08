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

#no necessary
cmd_echo_line = 1

# read stdout pipe
def powershell_read_thread_function(p):
    ''
    plat = getplatform()
    if (plat == "Windows"):
        p.stdout.readline()
        p.stdout.readline()
        p.stdout.readline()

    cmd_codec = (codecs.lookup(locale.getpreferredencoding()).name)
    cmd_codec = "ansi"
    global cmd_event
    global cmd_exit_flag
    global cmd_echo_line
    while (True):
        l = p.stdout.readline().rstrip().decode(cmd_codec)
        #print(l)

        if(cmd_echo_line == 1):
            cmd_echo_line = 0
            #print(cmd_echo_line)
            #print(cmd_exit_flag)
            #print(l)
            #print("BBBBBBBBBBBBBBBBBBBBBBBB")
            #some case, it is a empty line, I think it should be a "PS xxx>exit 0" string. continue.
            if(str(l).__contains__('exit')):
                break
            continue

        if (l is None):
            #print ('cccc')
            break

        if (p.poll() is not None):
            #print("bbbb")
            break

        #windows powershell, echo line maybe echoed as a normal output line. [not]
        #windows powershell, a command finished, maybe write one blank line to parent, forward catched, continuted to here.
        if(cmd_exit_flag == 1):
            if(str(l).startswith("PS")):
                if(str(l).split(">")[1].lstrip().startswith("exit")):
                    #print(cmd_echo_line)
                    #print(cmd_exit_flag)
                    #print(l)
                    #print("PPPPPPPPPPPPPPPPPPPPP")
                    break
            else:
                print(l)
                print("if you catched, please push a issue.")
                break

        #windows cmd, when p is closing, pipe write some blank line to parent
        if (cmd_exit_flag == 1 and l is ''):
            #print ("read thread: l is empty")
            break

        if ("pymake-command-status:" in l):
            cmd_echo_line = 1
            #print(cmd_echo_line)
            #print(cmd_exit_flag)
            #print(l)
            #print("EEEEEEEEEEEEEEEEEEEEEEEE")
            ret = int(l.split(':')[-1].strip())
            # java windows return 0 or 1
            #print (l)
            #print("command status %d" % (ret))
            if( ret != 0 ):
                # cmd running fail, child process exit
                cmd_exit_flag = 1
                p.stdin.write(("exit %d\n".encode(cmd_codec) % (ret)))
                p.stdin.flush()
                print ("exit %d" % (ret))
                #print ("read thread exit fail %d, i go" % (ret))
                break
            cmd_event.set()
            continue

        print (l)
        #print (cmd_exit_flag)
        #print ("ccccccccc")
        #p.stdout.flush()
    return


# auto command execute
def powershell_write_command_thread_function(p, cmd_list):
    ''
    cmd_codec = (codecs.lookup(locale.getpreferredencoding()).name)
    cmd_codec = "ansi"
    cmd_return = "\n"
    global cmd_event
    global cmd_exit_flag
    while (True):
        cmd_event.clear()
        cmd = cmd_list.pop(0) + cmd_return
        #print  ("command:%s" % cmd)

        # the last or the mid exit exit flag = 1
        if ("exit" in cmd):
        #if(cmd.lstrip().startswith("exit")):
            cmd_exit_flag = 1

        p.stdin.write(cmd.encode(cmd_codec))
        p.stdin.flush()

        if ( cmd_exit_flag == 1 ):
            #print ("write: i go")
            ""
            break

        # p.stdin.write("ping 127.0.0.1 -c 2 \n")
        # p.stdin.flush()
        cmd_event.wait()
    return

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
    read_thread = threading.Thread(target=powershell_read_thread_function, args=(p,))
    read_thread.start()
    read_err_thread = threading.Thread(target=read_stderr_thread_function, args=(p,))
    #read_err_thread.start()
    write_command_thread = threading.Thread(target=powershell_write_command_thread_function, args=(p, list0))
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
