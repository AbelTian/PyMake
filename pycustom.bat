@echo off

:: pycustom.bat 使用某个环境，在当前目录，执行用户输入的命令和参数。

if ""%1"" == """" (
    rem echo you can execute command with params in default env.
    echo usage:
    echo "  pycustom <cmd-name> [ <cmd-params>... ]"
    echo -----
    echo please appoint a cmd name. & exit /b 0
)
set PYEXECNAME=%1

set PYEXECPARAM[2]=%2
if ""%2"" == """" ( set PYEXECPARAM[2]="" )
set PYEXECPARAM[3]=%3
if ""%3"" == """" ( set PYEXECPARAM[3]="" )
set PYEXECPARAM[4]=%4
if ""%4"" == """" ( set PYEXECPARAM[4]="" )
set PYEXECPARAM[5]=%5
if ""%5"" == """" ( set PYEXECPARAM[5]="" )
set PYEXECPARAM[6]=%6
if ""%6"" == """" ( set PYEXECPARAM[6]="" )
set PYEXECPARAM[7]=%7
if ""%7"" == """" ( set PYEXECPARAM[7]="" )
set PYEXECPARAM[8]=%8
if ""%8"" == """" ( set PYEXECPARAM[8]="" )
set PYEXECPARAM[9]=%9
if ""%9"" == """" ( set PYEXECPARAM[9]="" )

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

rem for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYMMDEFAULTENVNAME=%%i" )
rem echo environme: [%PYMMDEFAULTENVNAME%] [default]
rem if not "%3" == "" (
rem     set PYENVNAME=%3
rem ) else (
rem     set PYENVNAME=%PYMMDEFAULTENVNAME%
rem )
set PYENVNAME=current

rem for /F %%i in ('"%PYPROGRAMPATHNAME%" have env %PYENVNAME%') do ( set "PYEXECFLAG=%%i" )
rem if "%PYEXECFLAG%" == "False" (
rem     echo environme: [%PYENVNAME%] is not existed.
rem     exit /b 0
rem )
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

rem echo %PYEXECNAME%
rem echo %PYEXECPARAM[2]%
rem echo %PYEXECPARAM[3]%
rem echo %PYEXECPARAM[4]%
rem echo %PYEXECPARAM[5]%
rem echo %PYEXECPARAM[6]%
rem echo %PYEXECPARAM[7]%
rem echo %PYEXECPARAM[8]%
rem echo %PYEXECPARAM[9]%

if not ""%9"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]% --params %PYEXECPARAM[3]% --params %PYEXECPARAM[4]% --params %PYEXECPARAM[5]% --params %PYEXECPARAM[6]% --params %PYEXECPARAM[7]% --params %PYEXECPARAM[8]% --params %PYEXECPARAM[9]%
) else if not ""%8"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]% --params %PYEXECPARAM[3]% --params %PYEXECPARAM[4]% --params %PYEXECPARAM[5]% --params %PYEXECPARAM[6]% --params %PYEXECPARAM[7]% --params %PYEXECPARAM[8]%
) else if not ""%7"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]% --params %PYEXECPARAM[3]% --params %PYEXECPARAM[4]% --params %PYEXECPARAM[5]% --params %PYEXECPARAM[6]% --params %PYEXECPARAM[7]%
) else if not ""%6"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]% --params %PYEXECPARAM[3]% --params %PYEXECPARAM[4]% --params %PYEXECPARAM[5]% --params %PYEXECPARAM[6]%
) else if not ""%5"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]% --params %PYEXECPARAM[3]% --params %PYEXECPARAM[4]% --params %PYEXECPARAM[5]%
) else if not ""%4"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]% --params %PYEXECPARAM[3]% --params %PYEXECPARAM[4]%
) else if not ""%3"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]% --params %PYEXECPARAM[3]%
) else if not ""%2"" == """" (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME% --params %PYEXECPARAM[2]%
) else (
    call "%PYPROGRAMPATHNAME%" custom exec-with-params here %PYEXECNAME%
)
