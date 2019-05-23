@echo off

:: pyexecvp.bat 使用某个环境，在当前目录，执行用户输入的命令和参数。

if "%1" == "" (
    echo usage:
    echo "  pyexecvp <cmd-name> [ <cmd-params> ] [<env-name>]"
    echo "  <env name>: 'current' is suggested."
    echo -----
    echo please appoint a cmd name. & exit /b 0
)
set PYEXECNAME=%1

set PYEXECPARAM=%2
if ""%2"" == """" (
    set PYEXECPARAM=""
)

set PYENVNAME=%3
if "%3" == "" (
    set PYENVNAME=
)

set PYPROGRAMPATH=%~dp0
set PYPROGRAMNAME=pymake.bat
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%


rem echo starting cmd ...
rem for /F %%i in ('echo %random%') do ( set "PYEXECINDEX=%%i" )
rem echo cmd index: [%PYEXECINDEX%]
rem for /F %%i in ('"%PYPROGRAMPATHNAME%" source root') do ( set "PYMMSOURCEROOT=%%i" )
rem echo location : [%PYMMSOURCEROOT%]
rem for /F %%i in ('"%PYPROGRAMPATHNAME%" source config') do ( set "PYMMSOURCECONFIG=%%i" )
rem echo configure: [%PYMMSOURCECONFIG%] [1]


for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYMMDEFAULTENVNAME=%%i" )
rem echo environme: [%PYMMDEFAULTENVNAME%] [default]
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
rem echo environme: [%PYENVNAME%] [%PYEXECFLAG%] [USED]

rem for /F %%i in ('"%PYPROGRAMPATHNAME%" have cmd %PYEXECNAME%') do ( set "PYEXECFLAG=%%i" )
rem if "%PYEXECFLAG%" == "False" (
rem     echo command  : [%PYEXECNAME%] is system wild command.
rem ) else (
rem     echo command  : [%PYEXECNAME%] [%PYEXECFLAG%] [EXISTED]
rem )

rem for /F %%i in ('"%PYPROGRAMPATHNAME%" get default exec root') do ( set "PYMMSHELLROOT=%%i" )
rem echo exec root: [%PYMMSHELLROOT%] [default]
rem echo exec root: [%CD%] [here]

if not ""%PYEXECPARAM%"" == """" (
    call "%PYPROGRAMPATHNAME%" use %PYENVNAME% exec-with-params here %PYEXECNAME% --params %PYEXECPARAM%
) else (
    call "%PYPROGRAMPATHNAME%" use %PYENVNAME% exec-with-params here %PYEXECNAME%
)
