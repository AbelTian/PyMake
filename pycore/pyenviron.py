from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import os
import sys
import ctypes
import inspect
import codecs
import locale
import copy

from .pybase import *

plat = getplatform()
if(plat == "Windows"):
    if sys.hexversion > 0x03000000:
        import winreg
    else:
        import _winreg as winreg

cmd_codec = "utf8"
cmd_return = "\n"
if(plat == "Windows"):
    cmd_codec = "ansi"
    # but windows, it is \r\n, python helpping me?
    cmd_return = "\n"

class MyWin32Environ(object):
    def __init__(self, scope = 'user'):
        # assert scope in ('user', 'system')
        self.scope = scope
        if(scope == 'user'):
            self.root = winreg.HKEY_CURRENT_USER
            self.subkey = 'Environment'
        else:
            self.root = winreg.HKEY_LOCAL_MACHINE
            self.subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

    def information(self):
        root0 = [
            "[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment]"
        ]
        root1 = [
            "[HKEY_CURRENT_USER\Environment]"
        ]
        return root0, root1

    def search_key(self, name):
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        key = ''
        value = ''
        try:
            i = 0
            while i >= 0:
                key, value, type = winreg.EnumValue(regkey, i)
                i += 1
                #print(i, key, value, type)
                if str(key).lower() == str(name).lower():
                    break
        except:
            key = ''
            value = ''
        winreg.CloseKey(regkey)
        #print(key)
        return value

    def get_key(self, name):
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        value = ''
        try:
            value, _ = winreg.QueryValueEx(regkey, name)
        except:
            value = ''
        winreg.CloseKey(regkey)
        #print(value)
        return value

    def del_key(self, name):
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        try:
            winreg.DeleteValue(regkey, name)
        except WindowsError:
            # Ignores if the key value doesn't exists
            pass
        winreg.CloseKey(regkey)

    def set_variable(self, name, value):
        # Note: for 'system' scope, you must run this as Administrator
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(regkey, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(regkey)

    def set_path(self, name, value):
        if(value is None):
            return ''
        if(value == ''):
            return ''
        #if(os.path.isabs(value) is False
        #   or os.path.isdir(value) is False):
        #    return ''

        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        key = ''
        reg_type = winreg.REG_EXPAND_SZ
        try:
            key, reg_type = winreg.QueryValueEx(regkey, name)
        except WindowsError:
            # If the value does not exists yet, we (guess) use a string list as the
            # reg_type
            key = ''
            reg_type = winreg.REG_EXPAND_SZ
            #print(key)
        value1 = value
        if(key != ''):
            value1 = value + os.path.pathsep + key
        #print(value1)
        winreg.SetValueEx(regkey, name, 0, reg_type, value1)
        winreg.CloseKey(regkey)
        return value1

    def del_path(self, name, value):
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)

        value1 = ''
        reg_type = winreg.REG_EXPAND_SZ
        try:
            value1, reg_type = winreg.QueryValueEx(regkey, name)
        except WindowsError:
            # If the value does not exists yet, we (guess) use a string list as the
            # reg_type
            return ''

        keyvaluelist = str(value1).split(';')

        clean_list = []
        for key1 in keyvaluelist:
            for key3 in str(value).split(';'):
                key3 = key3.replace('\\', '/')
                key0 = str(key1).replace('\\', '/')
                if(key0 == key3):
                    if(clean_list.__contains__(key1) is False):
                        clean_list.append(key1)

        for key4 in clean_list:
            while (keyvaluelist.__contains__(key4)):
                keyvaluelist.remove(key4)

        while(keyvaluelist.__contains__('')):
            keyvaluelist.remove('')

        value1 = ';'.join(keyvaluelist)

        #print(value1)
        winreg.SetValueEx(regkey, name, 0, reg_type, value1)
        winreg.CloseKey(regkey)
        return value1

    def refresh(self):
        return 0

        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x1A

        SMTO_NORMAL = 0x0000
        SMTO_ABORTIFHUNG = 0x0002

        result = ctypes.c_long()
        SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
        SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Environment', SMTO_ABORTIFHUNG, 5000, ctypes.byref(result))
        return result


class MyUnixEnviron(object):
    def __init__(self, scope = 'user'):
        # assert scope in ('user', 'system')
        self.scope = scope
        if(scope == 'user'):
            userhome = getuserroot()
            plat = getplatform()
            self.root = userhome + os.path.sep + '.bashrc'
            if(plat == "Darwin"):
                self.root = userhome + os.path.sep + '.bash_profile'
        else:
            self.root = '/etc/profile'

    def information(self):
        #unix
        root0 = [
            "/etc/profile",
            "/etc/paths",
            "/etc/paths.d/*"
        ]
        userhome = getuserroot()
        root1 = [
            userhome + os.path.sep + '.bash_profile',
            userhome + os.path.sep + '.inputrc'
        ]

        #linux
        root01 = [
            "/etc/profile",
            "/etc/profile.d/*.sh"
        ]
        root11 = [
            userhome + os.path.sep + '.profile',
            userhome + os.path.sep + '.bashrc',
            userhome + os.path.sep + '.inputrc'
        ]

        plat = getplatform()
        if(plat == "Darwin"):
            return root0, root1

        return root01, root11

    def search_key(self, name):
        value = ''

        #read all
        storelines = []
        with open(self.root, 'r', encoding=cmd_codec) as f:
            for l in f.readlines():
                while (l.endswith('\r') or l.endswith('\n') or l.endswith('\r\n')):
                    l = l.rstrip('\r\n')
                    l = l.rstrip('\n')
                    l = l.rstrip('\r')
                storelines.append(l)

        # filter #pymake end and #pymake start
        startindex = -1
        stopindex = -1
        for i in range(len(storelines) - 1, -1, -1):
            print(storelines[i])
            if(str(storelines[i]).__contains__('#pymake end')):
                stopindex = i
            if(str(storelines[i]).__contains__('#pymake start')):
                startindex = i

        #judgement
        if (startindex == -1 and stopindex == -1):
            #print('you have not used pymake to set any system environ.')
            env = os.environ
            if (env.__contains__(name)):
                print(env[name])
                value = env[name]
            return value

        if(startindex < 0 or stopindex < 0 or startindex > stopindex):
            #print('please dont manually modify pymake env section.')
            env = os.environ
            if (env.__contains__(name)):
                print(env[name])
                value = env[name]
            return value

        #format
        for i in range(startindex, stopindex):
            l = l.strip()
            storelines[i] = l

        # clean ''
        clean_list = []
        for l in storelines:
            if (l == ''):
                clean_list.append(l)
                continue
        # print(clean_list)

        for l in clean_list:
            if (storelines.__contains__(l) is True):
                storelines.remove(l)

        #parse path,variable
        for i in range(startindex, stopindex):
            l = storelines[i]
            key = str(l).split('=')[0].strip()
            key = key.replace('export ', '')
            key = key.strip()
            value0 = '='.join(str(l).split('=')[1:]).split()
            print(key, value)
            if(key == name):
                value = value0
                break

        return value

    def get_key(self, name):
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        value = ''
        try:
            value, _ = winreg.QueryValueEx(regkey, name)
        except:
            value = ''
        winreg.CloseKey(regkey)
        #print(value)
        return value

    def del_key(self, name):
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        try:
            winreg.DeleteValue(regkey, name)
        except WindowsError:
            # Ignores if the key value doesn't exists
            pass
        winreg.CloseKey(regkey)

    def set_variable(self, name, value):
        # Note: for 'system' scope, you must run this as Administrator
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(regkey, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(regkey)

    def set_path(self, name, value):
        if(value is None):
            return ''
        if(value == ''):
            return ''
        #if(os.path.isabs(value) is False
        #   or os.path.isdir(value) is False):
        #    return ''

        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        key = ''
        reg_type = winreg.REG_EXPAND_SZ
        try:
            key, reg_type = winreg.QueryValueEx(regkey, name)
        except WindowsError:
            # If the value does not exists yet, we (guess) use a string list as the
            # reg_type
            key = ''
            reg_type = winreg.REG_EXPAND_SZ
            #print(key)
        value1 = value
        if(key != ''):
            value1 = value + os.path.pathsep + key
        #print(value1)
        winreg.SetValueEx(regkey, name, 0, reg_type, value1)
        winreg.CloseKey(regkey)
        return value1

    def del_path(self, name, value):
        regkey = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)

        value1 = ''
        reg_type = winreg.REG_EXPAND_SZ
        try:
            value1, reg_type = winreg.QueryValueEx(regkey, name)
        except WindowsError:
            # If the value does not exists yet, we (guess) use a string list as the
            # reg_type
            return ''

        keyvaluelist = str(value1).split(';')

        clean_list = []
        for key1 in keyvaluelist:
            for key3 in str(value).split(';'):
                key3 = key3.replace('\\', '/')
                key0 = str(key1).replace('\\', '/')
                if(key0 == key3):
                    if(clean_list.__contains__(key1) is False):
                        clean_list.append(key1)

        for key4 in clean_list:
            while (keyvaluelist.__contains__(key4)):
                keyvaluelist.remove(key4)

        while(keyvaluelist.__contains__('')):
            keyvaluelist.remove('')

        value1 = ';'.join(keyvaluelist)

        #print(value1)
        winreg.SetValueEx(regkey, name, 0, reg_type, value1)
        winreg.CloseKey(regkey)
        return value1

    def refresh(self):
        return 0

        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x1A

        SMTO_NORMAL = 0x0000
        SMTO_ABORTIFHUNG = 0x0002

        result = ctypes.c_long()
        SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
        SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Environment', SMTO_ABORTIFHUNG, 5000, ctypes.byref(result))
        return result
