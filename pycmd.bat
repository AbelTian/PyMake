@echo off

:: pycmd.bat �ڵ�ǰ����ִ��pymake���������Դ�һ��������
:: pycmd.bat ʹ��pymake��Ĭ�ϻ��������������û����뻷������ôʹ���û�����Ļ�����
:: pycmd.bat �ᵼ����������ʹ�á�
:: pycmd.bat �û�Ӧ�����⣬�������Ƿ���Ŀ�껷�������

if "%1" == "" (
    echo "pycmd <cmd-name> [ <env-name> ]"
    echo please appoint a cmd name. & exit /b 0
)
set PYEXECNAME=%1

if not "%2" == "" (
    set PYENVNAME=%2
)

set PYPROGRAMPATH=%~dp0
set PYPROGRAMNAME=pymake.bat
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%


echo starting cmd ...
for /F %%i in ('echo %random%') do ( set "PYEXECINDEX=%%i" )
echo cmd index: [%PYEXECINDEX%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source root') do ( set "PYMMSOURCEROOT=%%i" )
echo location : [%PYMMSOURCEROOT%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source config') do ( set "PYMMSOURCECONFIG=%%i" )
echo configure: [%PYMMSOURCECONFIG%] [1]


for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYMMDEFAULTENVNAME=%%i" )
echo environme: [%PYMMDEFAULTENVNAME%] [default]
if not "%2" == "" (
    set PYENVNAME=%2
) else (
    set PYENVNAME=%PYMMDEFAULTENVNAME%
)
for /F %%i in ('"%PYPROGRAMPATHNAME%" have env %PYENVNAME%') do ( set "PYEXECFLAG=%%i" )
if "%PYEXECFLAG%" == "False" (
    echo environme: [%PYENVNAME%] is not existed.
    exit /b 0
)
echo environme: [%PYENVNAME%] [%PYEXECFLAG%] [USED]

for /F %%i in ('"%PYPROGRAMPATHNAME%" have cmd %PYEXECNAME%') do ( set "PYEXECFLAG=%%i" )
if "%PYEXECFLAG%" == "False" (
    echo command  : [%PYEXECNAME%] is not existed.
    exit /b 0
)
echo command  : [%PYEXECNAME%] [%PYEXECFLAG%] [EXISTED]

for /F %%i in ('"%PYPROGRAMPATHNAME%" get default exec root') do ( set "PYMMSHELLROOT=%%i" )
echo exec root: [%PYMMSHELLROOT%] [default]

call "%PYPROGRAMPATHNAME%" export %PYENVNAME% to %PYEXECINDEX%
call "%PYPROGRAMPATHNAME%" use %PYENVNAME% type %PYEXECNAME% to %PYEXECINDEX%
call "%PYMMSHELLROOT%\%PYEXECINDEX%_effect.bat"
call "%PYMMSHELLROOT%\%PYEXECINDEX%_exec.bat"
del /q /f "%PYMMSHELLROOT%\%PYEXECINDEX%_exec.bat"
del /q /f "%PYMMSHELLROOT%\%PYEXECINDEX%_effect.bat" "%PYMMSHELLROOT%\%PYEXECINDEX%_unset.bat"
