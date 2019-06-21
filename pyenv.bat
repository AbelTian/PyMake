@echo off

::本文件变量，局部有效，不开启这个设置。
::setlocal enabledelayedexpansion

set PYENVFLAG=True
if "%1" == "" (
    echo usage:
    echo "  pyenv <env-name>"
    echo "  pyenv open <env-name>"
    echo "  pyenv close <env-name>"
    echo "  <env name>: 'current' is suggested."
    echo ------
    echo please appoint a env name. & exit /b 0
) else if "%1" == "open" (
    if "%2" == "" (
        echo usage:
        echo "  pyenv <env-name>"
        echo "  pyenv open <env-name>"
        echo "  pyenv close <env-name>"
        echo "  <env name>: 'current' is suggested."
        echo ------
        echo please appoint a env name. & exit /b 0
    )
    set PYENVNAME=%2
) else if "%1" == "close" (
    if "%2" == "" (
        echo usage:
        echo "  pyenv <env-name>"
        echo "  pyenv open <env-name>"
        echo "  pyenv close <env-name>"
        echo "  <env name>: 'current' is suggested."
        echo ------
        echo please appoint a env name. & exit /b 0
    )
    set PYENVNAME=%2
    set PYENVFLAG=False
) else (
    set PYENVNAME=%1
)

set PYPROGRAMPATH=%~dp0
set PYPROGRAMNAME=pymake.bat
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%

echo preparing env ...
for /F %%i in ('echo %random%') do ( set "PYENVINDEX=%%i" )
rem echo env index: [%PYENVINDEX%]
rem for /F %%i in ('"%PYPROGRAMPATHNAME%" source root') do ( set "PYMMSOURCEROOT=%%i" )
rem echo location : [%PYMMSOURCEROOT%]
rem for /F %%i in ('"%PYPROGRAMPATHNAME%" source config') do ( set "PYMMSOURCECONFIG=%%i" )
rem echo configure: [%PYMMSOURCECONFIG%] [1]
rem for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYMMDEFAULTENVNAME=%%i" )
rem echo environme: [%PYMMDEFAULTENVNAME%] [default]
rem for /F %%i in ('"%PYPROGRAMPATHNAME%" have env %PYENVNAME%') do ( set "PYENVEXISTEDFLAG=%%i" )
rem if "%PYENVEXISTEDFLAG%" == "False" (
rem     echo environme: [%PYENVNAME%] is not existed.
rem     exit /b 0
rem )
rem echo environme: [%PYENVNAME%] [%PYENVEXISTEDFLAG%] [USED]
rem for /F %%i in ('"%PYPROGRAMPATHNAME%" get default exec root') do ( set "PYMMSHELLROOT=%%i" )
rem echo exec root: [%PYMMSHELLROOT%] [default]
rem echo exec root: [%CD%] [here]
set PYMMSHELLROOT=%CD%

call "%PYPROGRAMPATHNAME%" export2 here %PYENVNAME% to %PYENVINDEX% --local --custom
if not "%ERRORLEVEL%" == "0" (
    exit /b %ERRORLEVEL%
)

if "%PYENVFLAG%" == "False" (
    call "%PYMMSHELLROOT%\%PYENVINDEX%_unset.bat"
    echo user env : [%PYENVNAME%] closed
) else (
    call "%PYMMSHELLROOT%\%PYENVINDEX%_effect.bat"
    echo user env : [%PYENVNAME%] opened
)

::clean
del /q /f "%PYMMSHELLROOT%\%PYENVINDEX%_effect.bat" "%PYMMSHELLROOT%\%PYENVINDEX%_unset.bat"

rem set filepath=
rem set PYENVEXISTEDFLAG=
rem set PYENVFLAG=
rem set PYENVINDEX=
rem set PYENVNAME=
rem set PYMMDEFAULTENVNAME=
rem set PYMMSOURCECONFIG=
rem set PYMMSOURCEROOT=
rem set PYMMSHELLROOT=
rem set PYPROGRAMPATH=
rem set PYPROGRAMNAME=
rem set PYPROGRAMPATHNAME=

exit /b 0
