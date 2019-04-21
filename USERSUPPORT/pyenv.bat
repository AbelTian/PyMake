@echo off

::本文件变量，局部有效，不开启这个设置。
::setlocal enabledelayedexpansion

set PYENVFLAG=1
if "%1" == "" (
    echo please appoint a env name. & exit /b 0
) else if "%1" == "open" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
    set PYENVNAME=%2
) else if "%1" == "close" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
    set PYENVNAME=%2
    set PYENVFLAG=0
) else (
    set PYENVNAME=%1
)

set PYPROGRAMPATH=%~dp0..
set PYPROGRAMNAME=pymake.bat
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%\%PYPROGRAMNAME%

echo preparing env ...
for /F %%i in ('echo %random%') do ( set "PYENVINDEX=%%i" )
echo env index: [%PYENVINDEX%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source root') do ( set "PYMMSOURCEROOT=%%i" )
echo location : [%PYMMSOURCEROOT%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source config') do ( set "PYMMSOURCECONFIG=%%i" )
echo configure: [%PYMMSOURCECONFIG%] [1]

call "%PYPROGRAMPATHNAME%" export %PYENVNAME% %PYENVINDEX%

if %PYENVFLAG% == 0 (
    call "%PYMMSOURCEROOT%\%PYENVINDEX%_unset.bat"
    echo user env : [%PYENVNAME%] closed
) else (
    call "%PYMMSOURCEROOT%\%PYENVINDEX%_effect.bat"
    echo user env : [%PYENVNAME%] opened
)

::clean
del /q /f "%PYMMSOURCEROOT%\%PYENVINDEX%_effect.bat" "%PYMMSOURCEROOT%\%PYENVINDEX%_unset.bat"

exit /b 0