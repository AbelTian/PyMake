from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import os
import sys
#import pwd
import json
import ctypes
import inspect
import codecs
import locale
import time
import threading
import subprocess
import platform
from collections import OrderedDict
from .colorama import init, Fore, Back, Style


init(autoreset=True)

if ( sys.version_info[0] == 2 ):
    import ConfigParser as PyConfigParser
else:
    import configparser as PyConfigParser

class MyConfigParser(PyConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        PyConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

def TestPlatform( ):
    print ("----------Operation System--------------------------")
    #  Python Version
    print (platform.python_version())

    #   exe pe type (32bit, WindowsPE)
    print (platform.architecture())

    #   computer network name, acer-PC
    print (platform.node())

    # os name and version, Windows-7-6.1.7601-SP1
    print (platform.platform())

    # cpu info 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel'
    print (platform.processor())

    # Python build time
    print (platform.python_build())

    #  python compiler info
    print (platform.python_compiler())

    if platform.python_branch()=="":
        print (platform.python_implementation())
        print (platform.python_revision())
    print (platform.release())
    print (platform.system())

    #print platform.system_alias()
    #  os version
    print (platform.version())

    #  all of up
    print (platform.uname())

def getplatform( ):
    sysstr = platform.system()
    #print ( sysstr )
    #if(sysstr =="Windows"):
    #    print ("Call Windows tasks")
    #elif(sysstr == "Linux"):
    #    print ("Call Linux tasks")
    #else:
    #    print ("Other System tasks")
    return sysstr

def getuserroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        root = os.environ["HOMEPATH"]
    else:
        root = os.environ["HOME"]
    return root

def getconfigroot():
    root = ""
    sysstr = platform.system()
    if(sysstr =="Windows"):
        root = os.environ["APPDATA"]
    else:
        root = os.environ["HOME"]
    return root

def readJsonData(file):

    datas = ""
    with open(file, 'r') as json_file:
        for line in json_file.readlines():
            datas += line
    data = json.loads(datas, encoding='utf-8', object_pairs_hook=OrderedDict);


    #with open(file, 'r') as json_file:
    #    data = json.load(json_file)

    return data

def writeJsonData(file, data):

    with open(file, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4, sort_keys=False))


    #with open(file, 'w') as json_file:
    #    json.dump(data, json_file, indent=4)



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

def stopThread(thread):
    _async_raise(thread.ident, SystemExit)

# read stdout pipe
def read_thread_function(p):
    ''
    plat = getplatform()
    if (plat == "Windows"):
        p.stdout.readline()
        p.stdout.readline()
        p.stdout.readline()

    code = (codecs.lookup(locale.getpreferredencoding()).name)
    global cmd_exit_flag
    while (True):
        l = p.stdout.readline().rstrip().decode(code)

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
            ret = int(l.split(':')[-1].strip())
            # java windows return 0 or 1
            #print (l)
            #print("command status %d" % (ret))
            if( ret != 0 ):
                # cmd running fail, child process exit
                cmd_exit_flag = 1
                p.stdin.write(("exit %d \n".encode(code) % (ret)))
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


# read stderr pipe
def read_stderr_thread_function(p):
    ''
    code = (codecs.lookup(locale.getpreferredencoding()).name)
    while (True):
        l = p.stderr.readline().rstrip().decode(code)

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

# auto command execute
def write_command_thread_function(p):
    ''
    code = (codecs.lookup(locale.getpreferredencoding()).name)
    global cmd_exit_flag
    while (True):
        cmd_event.clear()
        cmd = cmd_list.pop(0) + '\n'
        #print  ("command:%s" % cmd)

        # the last or the mid exit exit flag = 1
        if ("exit" in cmd):
        #if(cmd.lstrip().startswith("exit")):
            cmd_exit_flag = 1

        p.stdin.write(cmd.encode(code))
        p.stdin.flush()

        if ( cmd_exit_flag == 1 ):
            #print ("write: i go")
            ""
            break

        # p.stdin.write("ping 127.0.0.1 -c 2 \n")
        # p.stdin.flush()
        cmd_event.wait()

# user input
def write_thread_function(p):
    ''
    code = (codecs.lookup(locale.getpreferredencoding()).name)
    while (True):
        line = sys.stdin.readline()
        if (line is None):
            #print ("write thread: i go, line is none")
            break

        if (p.poll() is not None):
            #print ("write thread: i go, p is done")
            break
        p.stdin.write(line.encode(code))
        p.stdin.flush()

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
    global cmd_list
    cmd_list = []

    if( plat == "Windows"):
        cmd_status = "echo pymake-command-status:%ERRORLEVEL%"
        cmd_sep = '&'
        cmd_exit = 'exit /b 0'
        # window close echo, close promot
        cmd_list.append("echo off" + ' ' + cmd_sep + ' ' + cmd_status )
    else:
        cmd_status = "echo pymake-command-status:$?"
        cmd_sep = ';'
        cmd_exit = 'exit 0'

    for cmd in list0:
        cmd_list.append(cmd + ' ' + cmd_sep + ' ' + cmd_status )

    # append exit 0
    cmd_list.append (cmd_exit)
    #print( cmd_list )


    startupinfo = None
    createflags = 0
    if (plat == 'Windows' ):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.dwFlags |= subprocess.STARTF_USESTDHANDLES
        startupinfo.wShowWindow = subprocess.SW_HIDE
        #createflags = subprocess.CREATE_NEW_CONSOLE

    p = subprocess.Popen(shell, shell=True,
                         bufsize=-1,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         #if dont do this, windows stdout piory is high, stderr cant output full message
                         #when split stdout and stderr, lots of app wont manager the output order
                         stderr=subprocess.STDOUT,
                         startupinfo=startupinfo, creationflags=createflags)
    read_thread = threading.Thread(target=read_thread_function, args=(p, ))
    read_thread.start()
    read_err_thread = threading.Thread(target=read_stderr_thread_function, args=(p,))
    #read_err_thread.start()
    write_command_thread = threading.Thread(target=write_command_thread_function, args=(p,))
    write_command_thread.start()
    write_thread = threading.Thread(target=write_thread_function, args=(p,))
    write_thread.start()
    # time.sleep(1)

    p.wait()

    if (read_thread.isAlive()):
        stopThread(read_thread)
    if (read_err_thread.isAlive()):
        stopThread(read_err_thread)
    if (write_command_thread.isAlive()):
        stopThread(write_command_thread)
    if (write_thread.isAlive()):
        stopThread(write_thread)

    # time.sleep(1)
