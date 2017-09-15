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
import sys
import shutil
import time
import json
from pycore.pycore import *
from pycore.docopt import docopt

def main_function():

    d = {
        "env-variables": {
            "PYCMD_MYNAME": "T.D.R"
        },
        "add-path-to-env": {
            "gen-path": "/Users/abel/Develop/b0-toolskits/compliers/CMake.app/Contents/bin",
            "macos10.12-xcode": "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/System/Library/Frameworks",
            "make-and-toolchain-path": "/usr/bin",
            "qt5.9-clang64": "/Users/abel/Develop/b0-toolskits/Libraries/QtLibraries/5.9.1/clang_64/bin"
        },
        "store-named-command": {
            "cd-buildpath": "/Users/abel/Develop/c0-buildstation/mac-qqt",
            "cd-productpath": "/Users/abel/Develop/b1-Product/a0-qqtbased/Application",
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
                "cd-buildpath",
                "rmcache",
                "gen",
                "make",
                "install",
                "msg"
            ],
            "genqqt": [
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
    config = readJsonData(file)
    #print(config)

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
        break


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


    while ( True ):

        if( args['exec'] == True):
            if(args['<stream-names>'] is not None):

                env = os.environ
                
                for (key, value) in config["env-variables"].items():
                    env[key] = value

                for (key, value) in env.items():
                    #print ("%-24s %s" % (key, value) )
                    ''


                for (name, path) in config["add-path-to-env"].items():
                    env["PATH"] = path + os.path.pathsep + env["PATH"]
                #print(env["PATH"].replace(os.path.pathsep, '\n'))

                for stream in args['<stream-names>']:
                    if( config["execute-stream"].__contains__(stream) ):
                        for cmd in config["execute-stream"][stream]:
                            if( config['store-named-command'].__contains__(cmd) ):
                                #print("execute %s %s %s" % (stream, cmd, config['store-named-command'][cmd]))
                                if(cmd.strip().startswith('cd', 0, 2)):
                                    if (not os.path.exists(config['store-named-command'][cmd])):
                                        #os.makedirs(path)
                                        print ("path unexist %s create it" % config['store-named-command'][cmd])
                                    os.chdir(config['store-named-command'][cmd])
                                    #print ("chdir %s" % config['store-named-command'][cmd])
                                else:
                                    os.system(config['store-named-command'][cmd])
                                    #print ("now execute %s" % config['store-named-command'][cmd])
                                    ''
                            else:
                                print ("can't find command %s" % cmd)
                    else:
                        print ("can't find stream %s" % stream)
            else:
                print ("stream-names is none")
        else:
            ''

        break

    return

if __name__ == '__main__':

    main_function()
