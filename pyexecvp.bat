@echo off

:: pyexecvp.bat �ڵ�ǰ����ִ��pymake���������Դ�һ�����������Դ�������
:: pyexecvp.bat ʹ��pymake��Ĭ�ϻ��������������û����뻷������ôʹ���û�����Ļ�����
:: pyexecvp.bat �ᵼ����������ʹ�á�
:: pyexecvp.bat �û�Ӧ�����⣬�������Ƿ���Ŀ�껷�������

if "%1" == "" (
    echo "pyexecvp <cmd-name> [ <cmd-params> ] [<env-name>]"
    echo "<env name>: 'current' is suggested."
    echo please appoint a cmd name. & exit /b 0
)
set PYEXECNAME=%1

if not "%3" == "" (
    set PYENVNAME=%3
)

set PYEXECNAME=%1
set PYEXECPARAM=%2
set PYENVNAME=%3

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
if not "%3" == "" (
    set PYENVNAME=%3
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
call "%PYMMSHELLROOT%\%PYEXECINDEX%_exec.bat" %PYEXECPARAM%
del /q /f "%PYMMSHELLROOT%\%PYEXECINDEX%_exec.bat"
del /q /f "%PYMMSHELLROOT%\%PYEXECINDEX%_effect.bat" "%PYMMSHELLROOT%\%PYEXECINDEX%_unset.bat"
