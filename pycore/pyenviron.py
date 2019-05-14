from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import os
import sys
import ctypes
import inspect
import codecs
import locale

from .pybase import *

class MyWin32Environ():
    plat = getplatform()
    if(plat == "Windows"):
        if sys.hexversion > 0x03000000:
            import winreg
        else:
            import _winreg as winreg

    def __init__(self, scope):
        # assert scope in ('user', 'system')
        self.scope = scope
        if scope == 'user':
            self.root = winreg.HKEY_CURRENT_USER
            self.subkey = 'Environment'
        else:
            self.root = winreg.HKEY_LOCAL_MACHINE
            self.subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

    def search_key(self, name):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        key_value = ''
        try:
            i = 0
            while i >= 0:
                key_value, path, value = winreg.EnumValue(key, i)
                i += 1
                print(key_value, path, value)
                if key_value == name:
                    break
        except:
            key_value = ''
        winreg.CloseKey(key)
        print(key_value)
        return key_value

    def get_key(self, name):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        try:
            value, _ = winreg.QueryValueEx(key, name)
        except:
            value = ''
        winreg.CloseKey(key)
        print(value)
        return value

    def del_key(self, name):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        try:
            winreg.DeleteValue(key, name)
        except WindowsError:
            # Ignores if the key value doesn't exists
            pass
        winreg.CloseKey(key)

    def set_variable(self, name, value):
        # Note: for 'system' scope, you must run this as Administrator
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)

    def set_path(self, name, value):
        if(value is None):
            return ''
        if(value == ''):
            return ''
        if(os.path.isabs(value) is False
           or os.path.isdir(value) is False):
            return ''

        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        key_value = ''
        try:
            key_value, reg_type = winreg.QueryValueEx(key, name)
        except WindowsError:
            # If the value does not exists yet, we (guess) use a string list as the
            # reg_type
            reg_type = winreg.REG_EXPAND_SZ
        key_value = value + os.path.pathsep + key_value
        print(key_value)
        winreg.SetValueEx(key, name, 0, reg_type, key_value)
        winreg.CloseKey(key)
        return key_value

    def del_path(self, name, value):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)

        key_value = ''
        try:
            key_value, reg_type = winreg.QueryValueEx(key, name)
        except WindowsError:
            # If the value does not exists yet, we (guess) use a string list as the
            # reg_type
            return ''

        keyvaluelist = str(key_value).split(';')
        if(keyvaluelist.__contains__('')):
            keyvaluelist.remove('')
        if(keyvaluelist.__contains__(value)):
            keyvaluelist.remove(value)
        key_value = ';'.join(keyvaluelist)

        print(key_value)
        winreg.SetValueEx(key, name, 0, reg_type, key_value)
        winreg.CloseKey(key)
        return key_value

    def refresh(self):
        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x1A

        SMTO_ABORTIFHUNG = 0x0002

        result = ctypes.c_long()
        SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
        SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Environment', SMTO_ABORTIFHUNG, 5000, ctypes.byref(result))
        return result




SET_ENV = r'''
@echo
set %{key}%={value}
echo %{key}%

if {user}==sys (
    setx /M｛key｝ "%{key}%"
) else (
    setx {key} "%{key}%"
)
'''

ADD_ENV = r'''
@echo off

if {user}==sys (
    set regPath= HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session" "Manager\Environment
) else (
    set regPath= HKEY_CURRENT_USER\Environment
)

set key={key}
set value={value}
:: 判断是否存在该路径
reg query %regPath% /v %key% 1>nul 2>nul
if %ERRORLEVEL%==0 (
    :: 取值
    For /f "tokens=3* delims= " %%i in ('Reg Query %regPath% /v %key% ') do (
        if "%%j"=="" (Set oldValue=%%i) else (Set oldValue=%%i %%j)
    )
) else Set oldValue="."

:: 备份注册表
reg export %regPath% %~dp0%~n0.reg
:: 写入环境变量
if "%oldValue%"=="." (
    reg add %regPath% /v %key% /t REG_EXPAND_SZ /d "%value%" /f
) else (
    reg add %regPath% /v %key% /t REG_EXPAND_SZ /d "%oldValue%;%value%" /f
)
'''


# 连续运行 bat 命令
def runbat(self, bat):
    tmp_bat_file = 'tmp.bat'
    with open(tmp_bat_file, 'w') as f:
        f.writelines(bat)
    self.runcmd(tmp_bat_file)


# 添加环境变量
def _append_env(self, is_sys, key, value):
    # 运行设置环境变量命令
    user = 'sys' if is_sys else 'me'
    cmds = ADD_ENV.format(user=user, key=key, value=value)
    self.runbat(cmds)


# 设置环境变量
def _set_env(self, is_sys, key, value):
    user = 'sys' if is_sys else 'me'
    cmds = SET_ENV.format(user=user, key=key, value=value)
    self.runbat(cmds)


import ctypes

if sys.hexversion > 0x03000000:
    import winreg
else:
    import _winreg as winreg
import subprocess
from subprocess import check_call


class Registry(object):
    def __init__(self, key_location, key_path):
        self.reg_key = winreg.OpenKey(key_location, key_path, 0, winreg.KEY_ALL_ACCESS)

    def set_key(self, name, value):
        try:
            _, reg_type = winreg.QueryValueEx(self.reg_key, name)
        except WindowsError:
            # If the value does not exists yet, we (guess) use a string as the
            # reg_type
            reg_type = winreg.REG_SZ
        winreg.SetValueEx(self.reg_key, name, 0, reg_type, value)

    def delete_key(self, name):
        try:
            winreg.DeleteValue(self.reg_key, name)
        except WindowsError:
            # Ignores if the key value doesn't exists
            pass


ENV_HTTP_PROXY = u'http://87.254.212.121:8080'

class EnvironmentVariables(Registry):
    """
    Configures the HTTP_PROXY environment variable, it's used by the PIP proxy
    """

    def __init__(self):
        super(EnvironmentVariables, self).__init__(winreg.HKEY_LOCAL_MACHINE,
                                                   r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment')

    def on(self):
        self.set_key('HTTP_PROXY', ENV_HTTP_PROXY)
        self.refresh()

    def off(self):
        self.delete_key('HTTP_PROXY')
        self.refresh()

    def refresh(self):
        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x1A

        SMTO_ABORTIFHUNG = 0x0002

        result = ctypes.c_long()
        SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
        SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'Environment', SMTO_ABORTIFHUNG, 5000, ctypes.byref(result));


def run_cmd(cmd, cwd=None, runas=None):
    u"""
    运行cmd命令。
    """
    if not sys.platform.startswith('win') and runas and runas != 'root':
        cmd = 'su - {} -c "{}"'.format(runas, cmd)
    # logger.info(cmd)
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            shell=True,
                            cwd=cwd)
    return proc


def get_output(cmd, cwd=None, wait=True, runas=None):
    u"""
    获得命令执行后的标准输出或错误输出。
    """
    proc = run_cmd(cmd, cwd=cwd, runas=runas)
    lines = []
    if wait:
        while proc.poll() is None:
            if proc.stdout:
                lines.extend(proc.stdout.readlines())
    lines.extend(proc.stdout.readlines())
    return lines


class Win32Environment:
    """Utility class to get/set windows environment variable"""

    def __init__(self, scope):
        # assert scope in ('user', 'system')
        self.scope = scope
        if scope == 'user':
            self.root = winreg.HKEY_CURRENT_USER
            self.subkey = 'Environment'
        else:
            self.root = winreg.HKEY_LOCAL_MACHINE
            self.subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

    def search(self, name):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        key_value = ''
        try:
            i = 0
            while i >= 0:
                key_value, path, value = winreg.EnumValue(key, i)
                i += 1
                if key_value == name:
                    break
        except:
            key_value = ''
        return key_value

    def getenv(self, name):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        try:
            value, _ = winreg.QueryValueEx(key, name)
        except:
            value = ''
        return value

    def setenv(self, name, value):
        # Note: for 'system' scope, you must run this as Administrator
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)
        winreg.CloseKey(key)
        # For some strange reason, calling SendMessage from the current process
        # doesn't propagate environment changes at all.
        # TODO: handle CalledProcessError (for assert)
        check_call(
            '''\"%s" -c "import win32api, win32con;assert win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE,0, 'Environment')"''' % sys.executable)

    def get_userenv(self, name):
        # Note: for 'system' scope, you must run this as Administrator
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        value, _ = winreg.QueryValueEx(key, name)
        return value


def set_env_path(env_obj, env_name, env_path, refresh=False):
    need_add = False
    path_values = None
    exist_path = None
    if env_obj.search(env_name):
        exist_path = env_obj.get_userenv(env_name)
    if not exist_path and env_obj.search(env_name.upper()):
        exist_path = env_obj.get_userenv(env_name.upper())

    if refresh:
        exist_path = None
    if exist_path:
        path_values = [i for i in exist_path.split(';')]
        for i in env_path.split(';'):
            if i not in path_values:
                path_values.append(i)
                need_add = True
    if not need_add and path_values:
        return '已添加环境变量{}:{}'.format(env_name, exist_path)

    if path_values:
        env_path = ';'.join(path_values)

    env_obj.setenv(env_name, os.path.expanduser(env_path))
    path_value = env_obj.get_userenv(env_name)
    return '已添加环境变量{}:{}'.format(env_name, path_value)


def local_test_environ_function():
    env_obj = Win32Environment(scope="SYSTEM")
    print
    set_env_path(env_obj, 'JAVA_HOME', '', refresh=True)

    print
    set_env_path(env_obj, 'Path', '%JAVA_HOME%\\bin;%JAVA_HOME%\\jre\\bin')

    print
    set_env_path(env_obj, 'CLASSPATH',
                 '.;%JAVA_HOME%\\lib\\dt.jar;%JAVA_HOME%\\lib\\tools.jar')