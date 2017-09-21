"""PyCmd 1.0.

Usage:
  pycmd.py group [ --add | --del | --switch ] [ <config-file-name> ]
  pycmd.py group --mod <config-file-name> <new-config-file-name>
  pycmd.py group [ --show | --restore ]
  pycmd.py list [ --vars | --pathes | --commands | --task ]
  pycmd.py set ( env-var | env-path | cmd ) ( --add | --del | --mod ) <name> [ <value> ]
  pycmd.py stream (--add | --del | --mod ) <name> [ <values> ... ]
  pycmd.py exec <stream-names> ...
  pycmd.py (-h | --help)
  pycmd.py --version

Command:
  group            switch to another group file
  set env-path     config work directory
  set env-var
  set exec-dir     config execute directory
  list             list configed values

Options:
  -h --help     Show this screen.
  --version     Show version.
  --add
  --del
  --mod         add or delete or modify a config or path
  --switch      switch to another group
  --vars
  --pathes
  --commands
  --task        list info params
  --show        display haved task config files
  --restore     reset to pycmd.json task config file
"""

# -*- coding: utf-8 -*-

import os
import re
import sys
import pwd
import shutil
import time
import json
import locale
import codecs
import threading
import subprocess
from pycore.pycore import *
from pycore.docopt import docopt

def main_function():

    d = {
        "add-path-to-env": {
            "cmake-bin-path": "/Users/abel/Develop/b0-toolskits/compliers/CMake.app/Contents/bin",
            "macosx-sdk-xcode": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/System/Library/Frameworks",
            "make-and-toolchain-path": "/usr/bin",
            "qt5.9-clang64": "/Users/abel/Develop/b0-toolskits/Libraries/QtLibraries/5.9.1/clang_64/bin"
        },
        "env-variables": {
            "PYCMD_MYNAME": "T.D.R"
        },
        "store-named-command": {
            "mk-buildpath": "mkdir -p /Users/abel/Develop/c0-buildstation/mac-qqt",
            "cd-buildpath": "cd /Users/abel/Develop/c0-buildstation/mac-qqt",
            "cd-productpath": "cd /Users/abel/Develop/b1-Product/a0-qqtbased/Application",
            "gen": "cmake -G\"Unix Makefiles\" -DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR}../../b1-Product/a0-qqtbased/Application ../../a0-Developworkspace/a0-qqtpruduct-qqtfoundation/",
            "gen-xcode": "cmake -GXCode -DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR}../../b1-Product/a0-qqtbased/Application ../../a0-Developworkspace/a0-qqtpruduct-qqtfoundation/",
            "install": "make install",
            "make": "make -j4",
            "msg": "echo 'work completed!'",
            "pwd": "pwd",
            "rmcache": "rm -f CMakeCache.txt"
        },
        "execute-stream": {
            "buildqqt": [
                "mk-buildpath",
                "cd-buildpath",
                "rmcache",
                "gen",
                "make",
                "install",
                "msg"
            ],
            "genqqt": [
                "mk-buildpath",
                "cd-buildpath",
                "gen",
                "msg"
            ],
            "packageqqt": [
                "cd-productpath",
                "pwd"
            ]
        }
    }
    if (not os.path.exists('pycmd.json')):
        writeJsonData('pycmd.json', d)

    """
    [pycmd]
    config = pycmd.json
    """
    file = 'pycmd.json'
    conf = MyConfigParser()
    conf.read('pycmd.ini')
    if(conf.has_section('pycmd') ):
        if(conf.has_option('pycmd', 'config')):
            if(conf.get('pycmd', 'config')):
                file = conf.get('pycmd', 'config')
                print("use source config: %s" % file)
            else:
                conf.set('pycmd', 'config', 'pycmd.json')
                conf.write(open('pycmd.ini', 'w'))
                print('initial pycmd.ini')
        else:
            conf.set('pycmd', 'config', 'pycmd.json')
            conf.write(open('pycmd.ini', 'w'))
            print('initial pycmd.ini')
    else:
        conf.add_section('pycmd')
        conf.set('pycmd', 'config', 'pycmd.json')
        conf.write(open('pycmd.ini', 'w'))
        print ( 'initial pycmd.ini')

    args = docopt(__doc__, version='pycmd.py 1.0')
    #print(args)

    exceptFile = ( 'pycmd.ini', 'pycmd.py', '.gitignore', '.git', 'pycore', 'README.md', '.idea')
    while (True):
        if(args['group'] is True):
            if(args['--del'] is True):
                if (args['<config-file-name>'] is not None and args['<config-file-name>'] == 'pycmd.json'):
                    print('You can\'t remove pycmd\'s file...')
                elif (args['<config-file-name>'] is not None and not exceptFile.__contains__(args['<config-file-name>']) ):
                    os.remove(args['<config-file-name>'])
                    conf.set('pycmd', 'config', 'pycmd.json')
                    conf.write(open('pycmd.ini', 'w'))
                else:
                    print ( 'You can\'t remove pycmd\'s file...')
            elif(args['--add'] is True):
                if (args['<config-file-name>'] is not None and not exceptFile.__contains__(args['<config-file-name>']) ):
                    if(file != args['<config-file-name>']):
                        shutil.copyfile(file, args['<config-file-name>'])
                        conf.set('pycmd', 'config', args['<config-file-name>'])
                        conf.write(open('pycmd.ini', 'w'))
                    else:
                        print('You can\'t add same named file...')
                else:
                    print ( 'You can\'t add pycmd\'s file...')
            elif (args['--mod'] is True):
                if ( ( args['<config-file-name>'] and args[
                    '<new-config-file-name>']) is not None and not \
                        exceptFile.__contains__(
                        args['<config-file-name>'])):

                    os.rename(args['<config-file-name>'],
                              args['<new-config-file-name>'])

                    if (file == args['<config-file-name>']):
                        conf.set('pycmd', 'config',
                                 args['<new-config-file-name>'])
                        conf.write(open('pycmd.ini', 'w'))

                else:
                    print ('You can\'t mod pycmd\'s file...')
            elif(args['--show'] is True):
                files = os.listdir(os.getcwd())
                for f in files:
                    if (not exceptFile.__contains__(f)):
                        print(f)
            elif(args['--restore'] is True):
                conf.set('pycmd', 'config', 'pycmd.json')
                conf.write(open('pycmd.ini', 'w'))
            elif (args['--switch'] is True
                  or ( args['<config-file-name>'] is not None and args[\
                          '<config-file-name>'] != '' )):
                if (args['<config-file-name>'] is not None and not exceptFile.__contains__(args['<config-file-name>']) ):
                    if (os.path.exists(args['<config-file-name>'])):
                        conf.set('pycmd', 'config', args['<config-file-name>'])
                        conf.write(open('pycmd.ini', 'w'))
                        print("switch to group config: %s" % args[
                            '<config-file-name>'])
                    else:
                        print("group file %s isn't exists" % args[
                            '<config-file-name>'])
                else:
                    print('You can\'t switch pycmd\'s file...')
            else:
                print(file)
        else:
            ''
        return

    config = readJsonData(file)
    #print(config)


    while (True):
        if (args['list'] == True):
            if( args['--vars'] == True):
                dict0 = config['env-variables'].copy()
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )
            elif( args['--pathes'] == True):
                dict0 = config['add-path-to-env'].copy()
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )
            elif( args['--commands'] == True):
                dict0 = config['store-named-command'].copy()
                for (k, v) in dict0.items():
                    print("%-24s %s" % (k, v) )
            elif( args['--task'] == True):
                dict0 = config['execute-stream'].copy()
                for (k,v) in dict0.items():
                    print("%-24s %s" % (k,v) )
        else:
            ''
        break

    while (True):
        if (args['set'] == True):
            if (args['env-var'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config["env-variables"][args['<name>']] = args[
                            "<value>"]
                        print ( "successed %s:%s" % (args['<name>'],
                                                    args[ "<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['env-variables'].__contains__(
                                args['<name>'])):
                            config["env-variables"].__delitem__(
                                args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['env-variables'].__contains__(
                                args['<name>'])):
                            config["env-variables"][args['<name>']] = \
                            args["<value>"]
                            print ("successed %s:%s" % (args['<name>'],
                                                        args["<value>"]))
                        else:
                            ''
                    else:
                        ''
                else:
                    ''
            elif (args['env-path'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config["add-path-to-env"][args['<name>']] = args[
                            "<value>"]
                        print ( "successed %s:%s" % (args['<name>'],
                                                    args[ "<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['add-path-to-env'].__contains__(
                                args['<name>'])):
                            config["add-path-to-env"].__delitem__(
                                args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['add-path-to-env'].__contains__(
                                args['<name>'])):
                            config["add-path-to-env"][args['<name>']] = \
                            args["<value>"]
                            print ("successed %s:%s" % (args['<name>'],
                                                        args["<value>"]))
                        else:
                            ''
                    else:
                        ''
                else:
                    ''
            elif (args['cmd'] is True):
                if (args['--add'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        config["store-named-command"][args['<name>']] = args[
                            "<value>"]
                        print ( "successed %s:%s" % (args['<name>'],
                                                    args[ "<value>"]))
                    else:
                        ''
                elif (args['--del'] == True):
                    if (args["<name>"] is not None):
                        if (config['store-named-command'].__contains__(
                                args['<name>'])):
                            config["store-named-command"].__delitem__(
                                args['<name>'])
                            print ("successed %s" % (args['<name>']))
                        else:
                            ''
                    else:
                        ''
                elif (args['--mod'] == True):
                    if (args['<name>'] and args["<value>"] is not None):
                        if (config['store-named-command'].__contains__(
                                args['<name>'])):
                            config["store-named-command"][args['<name>']] = \
                            args["<value>"]
                            print ("successed %s:%s" % (args['<name>'],
                                                        args["<value>"]))
                        else:
                            ''
                    else:
                        ''
                else:
                    ''
            else:
                ''
        elif (args['stream'] is True):
            if (args['--add'] == True):
                if (args['<name>'] and args["<values>"] is not None):
                    config["execute-stream"][args['<name>']] = args[
                        "<values>"]
                    print ("successed %s:%s" % (args['<name>'],
                                                args["<values>"]))
                else:
                    ''
            elif (args['--del'] == True):
                if (args["<name>"] is not None):
                    if (config['execute-stream'].__contains__(
                            args['<name>'])):
                        config["execute-stream"].__delitem__(
                            args['<name>'])
                        print ("successed %s" % (args['<name>']))
                    else:
                        ''
                else:
                    ''
            elif (args['--mod'] == True):
                if (args['<name>'] and args["<values>"] is not None):
                    config["execute-stream"][args['<name>']] = args[
                        "<values>"]
                    print ("successed %s:%s" % (args['<name>'],
                                                args["<values>"]))
                else:
                    ''
            else:
                ''
        else:
            ''

        #print(config)
        writeJsonData(file, config)
        break

    def read_thread_function(p):
        ''
        code = (codecs.lookup(locale.getpreferredencoding()).name)
        while(True):
            l = p.stdout.readline().rstrip().decode(code)

            if (l is None):
                #print ('ddd')
                break

            if(p.poll() is not None):
                #print("eee")
                break

            print (l)
            #print (l)
            #stdout.flush()

    def write_thread_function(list0):
        ''


    ### config -> raw config
    rawconfig = config.copy()
    #print ( rawconfig )
    env = os.environ

    for (key, value) in rawconfig["env-variables"].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...
            if (env.has_key(key1)):
                rawconfig["env-variables"][key] = rawconfig["env-variables"][key].replace(key0, env[key1])
            else:
                for (key2, value2) in config["env-variables"].items():
                    if (key2 == key1):
                        rawconfig["env-variables"][key] = rawconfig["env-variables"][key].replace(key0, rawconfig["env-variables"][key1])
                        #print ("%s:%s" % (key, rawconfig["env-variables"][key]))
                    else:
                        ''

    for (key, value) in rawconfig["store-named-command"].items():
        #print (key) #...

        startpos = 0
        while (True):
            #print (startpos)

            index = value.find('${', startpos)
            if (index == -1):
                break

            index2 = value.find('}', index)
            startpos = index2

            key0 = value[index:index2 + 1]
            #print ( key0 ) #${...}
            key1 = key0.split('{')[1].split('}')[0].strip()
            #print ( key1 ) #...
            if (env.has_key(key1)):
                rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, env[key1])
            else:
                for (key2, value2) in rawconfig["env-variables"].items():
                    if (key2 == key1):
                        rawconfig["store-named-command"][key] = rawconfig["store-named-command"][key].replace(key0, rawconfig["env-variables"][key1])
                        #print ("%s:%s" % (key, rawconfig["store-named-command"][key]))
                    else:
                        ''

    while ( True ):

        if( args['exec'] == True):
            if(args['<stream-names>'] is not None):

                env = os.environ

                for (key, value) in rawconfig["env-variables"].items():
                    env[key] = value

                for (key, value) in env.items():
                    #print ("%-24s %s" % (key, value) )
                    ''

                for (name, path) in rawconfig["add-path-to-env"].items():
                    env["PATH"] = path + os.path.pathsep + env["PATH"]
                #print(env["PATH"].replace(os.path.pathsep, '\n'))


                list0 = []
                for stream in args['<stream-names>']:
                    if (rawconfig["execute-stream"].__contains__(stream)):
                        for cmd in rawconfig["execute-stream"][stream]:
                            if (rawconfig['store-named-command'].__contains__(cmd)):
                                # print("execute %s %s %s" % (stream, cmd, rawconfig['store-named-command'][cmd]))
                                list0.append( rawconfig['store-named-command'][cmd] )
                            else:
                                print ("can't find command %s" % cmd)
                    else:
                        print ("can't find stream %s" % stream)
                list0.append("exit 0")
                #print (list0)

                shell = pwd.getpwuid(os.getuid()).pw_shell
                if shell is None: shell = os.environ.get( 'SHELL'   )
                if shell is None: shell = os.environ.get( 'COMSPEC' )
                #print ( 'Running under', shell )

                p = subprocess.Popen(shell, shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                read_thread = threading.Thread(target=read_thread_function, args=(p,))
                read_thread.start()
                write_thread = threading.Thread(target=write_thread_function, args=(list0,))
                #write_thread.start()
                time.sleep(1)

                for cmd in list0:
                    #print  ("command:%s" % cmd)
                    p.stdin.write(cmd + '\n')
                    p.stdin.flush()
                    #p.stdin.write("ping 127.0.0.1 -c 2 \n")
                    #p.stdin.flush()

                p.wait()
                #read_thread.close()
                time.sleep(1)

                #return


            else:
                print ("stream-names is none")
        else:
            ''

        break

    return

if __name__ == '__main__':

    main_function()
