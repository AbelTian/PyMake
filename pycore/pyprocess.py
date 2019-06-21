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


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    #print ("xxdfdf %s" % res)
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
    return

def stopThread(thread):
    _async_raise(thread.ident, SystemExit)
    return

cmd_event = threading.Event()
cmd_exit_flag = 0

# read stdout pipe
def read_thread_function(p):
    ''
    plat = getplatform()
    if (plat == "Windows"):
        p.stdout.readline()
        p.stdout.readline()
        p.stdout.readline()

    cmd_codec = (codecs.lookup(locale.getpreferredencoding()).name)
    global cmd_event
    global cmd_exit_flag
    while (True):
        l = p.stdout.readline().rstrip()
        #print(l)
        try:
            l = l.decode(cmd_codec)
        except:
            l = str(l).encode('raw_unicode_escape')
            l = l.decode(cmd_codec)
        #print(l)

        if (l is None):
            #print ('cccc')
            break

        if (p.poll() is not None):
            #print("bbbb")
            break

        #windows when p is closing, pipe write some blank line to parent
        if (cmd_exit_flag == 1 and l is ''):
            #print ("read thread: l is empty")
            break

        if ("pymake-command-status:" in l):
            #you must input legal format params
            #print (l)
            ret = int(l.split(':')[-1].strip())
            # java windows return 0 or 1
            #print (l)
            #print("command status %d" % (ret))
            if( ret != 0 ):
                # cmd running fail, child process exit
                cmd_exit_flag = 1
                p.stdin.write(("exit %d\n".encode(cmd_codec) % (ret)))
                p.stdin.flush()
                #print ("exit %d" % (ret))
                #print ("read thread exit fail %d, i go" % (ret))
                break
            cmd_event.set()
            continue

        print (l)
        #print (cmd_exit_flag)
        #print ("ccccccccc")
        #p.stdout.flush()
    return


# read stderr pipe
def read_stderr_thread_function(p):
    ''
    cmd_codec = (codecs.lookup(locale.getpreferredencoding()).name)
    global cmd_event
    global cmd_exit_flag
    while (True):
        l = p.stderr.readline().rstrip().decode(cmd_codec)

        if (l is None):
            #print ('ddd')
            break

        #print("read err: %s" % p.poll())
        if (p.poll() is not None):
            #print("eee")
            break

        #windows when p is closing, pipe write some blank line to parent
        if (cmd_exit_flag == 1 and l is ''):
            #print ("read err: l is empty")
            break

        print (l)
        #print (cmd_exit_flag)
        #print ("dddddddddddddd")
        #stdout.flush()
    return

# auto command execute
def write_command_thread_function(p, cmd_list):
    ''
    cmd_codec = (codecs.lookup(locale.getpreferredencoding()).name)
    global cmd_event
    global cmd_exit_flag
    while (True):
        cmd_event.clear()
        cmd = cmd_list.pop(0) + '\n'
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

# user input
def write_thread_function(p):
    ''
    cmd_codec = (codecs.lookup(locale.getpreferredencoding()).name)
    while (True):
        line = sys.stdin.readline()
        if (line is None):
            #print ("write thread: i go, line is none")
            break

        if (p.poll() is not None):
            #print ("write thread: i go, p is done")
            break
        p.stdin.write(line.encode(cmd_codec))
        p.stdin.flush()
    return

# windows *unix
def communicateWithCommandLine(list0):

    #shell = pwd.getpwuid(os.getuid()).pw_shell
    #if shell is None: shell = os.environ.get('SHELL')
    #if shell is None: shell = os.environ.get('COMSPEC')
    shell = ""
    plat = getplatform()
    if(plat == "Windows"):
        shell = os.environ.get('COMSPEC') + ' ' + "/q /d /s /a /v:on /e:on /f:on"
    else:
        shell = os.environ.get('SHELL')
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
    #print(p.returncode)
    if(p.returncode > 2147483647):
        p.returncode = 2147483647
    elif (p.returncode < -2147483647 ):
        p.returncode = -2147483647

    return p.returncode
