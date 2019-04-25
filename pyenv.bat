@echo off

::���ļ��������ֲ���Ч��������������á�
::setlocal enabledelayedexpansion

set PYENVFLAG=True
if "%1" == "" (
    echo "pyenv <env-name>"
    echo please appoint a env name. & exit /b 0
) else if "%1" == "open" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
    set PYENVNAME=%2
) else if "%1" == "close" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
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
echo env index: [%PYENVINDEX%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source root') do ( set "PYMMSOURCEROOT=%%i" )
echo location : [%PYMMSOURCEROOT%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source config') do ( set "PYMMSOURCECONFIG=%%i" )
echo configure: [%PYMMSOURCECONFIG%] [1]
for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYMMDEFAULTENVNAME=%%i" )
echo environme: [%PYMMDEFAULTENVNAME%] [default]
for /F %%i in ('"%PYPROGRAMPATHNAME%" have env %PYENVNAME%') do ( set "PYENVEXISTEDFLAG=%%i" )
if "%PYENVEXISTEDFLAG%" == "False" (
    echo environme: [%PYENVNAME%] is not existed.
    exit /b 0
)
echo environme: [%PYENVNAME%] [%PYENVEXISTEDFLAG%] [USED]
for /F %%i in ('"%PYPROGRAMPATHNAME%" get default exec root') do ( set "PYMMSHELLROOT=%%i" )
echo exec root: [%PYMMSHELLROOT%] [default]

call "%PYPROGRAMPATHNAME%" export %PYENVNAME% %PYENVINDEX%

if "%PYENVFLAG%" == "False" (
    call "%PYMMSHELLROOT%\%PYENVINDEX%_unset.bat"
    echo user env : [%PYENVNAME%] closed
) else (
    call "%PYMMSHELLROOT%\%PYENVINDEX%_effect.bat"
    echo user env : [%PYENVNAME%] opened
)

::clean
del /q /f "%PYMMSHELLROOT%\%PYENVINDEX%_effect.bat" "%PYMMSHELLROOT%\%PYENVINDEX%_unset.bat"

exit /b 0