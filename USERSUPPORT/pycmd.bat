@echo off

:: pycmd.bat 会强制使用pymake.bat的默认环境配置。即自带一个默认环境。
:: pycmd.bat 会使用默认环境配置导出命令，
:: pycmd.bat 却没有导出默认环境使用。
:: pycmd.bat 所以用户必须谨慎使用，以防导出的不是自己想要的命令，或者命令无法执行。

if "%1" == "" (
    echo please appoint a cmd name. & exit /b 0
) else if "%1" == "exec" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
    set PYEXECNAME=%2
) else if "%1" == "cc" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
    set PYEXECNAME=%2
) else (
    set PYEXECNAME=%1
)

set PYPROGRAMPATH=%~dp0..
set PYPROGRAMNAME=pymake.bat
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%\%PYPROGRAMNAME%

echo starting cmd ...
for /F %%i in ('echo %random%') do ( set "PYEXECINDEX=%%i" )
echo cmd index: [%PYEXECINDEX%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source root') do ( set "PYMMSOURCEROOT=%%i" )
echo location : [%PYMMSOURCEROOT%]
for /F %%i in ('"%PYPROGRAMPATHNAME%" source config') do ( set "PYMMSOURCECONFIG=%%i" )
echo configure: [%PYMMSOURCECONFIG%] [1]
for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYENVNAME=%%i" )
echo environme: [%PYENVNAME%] [default]
for /F %%i in ('"%PYPROGRAMPATHNAME%" have cmd %PYEXECNAME%') do ( set "PYEXECFLAG=%%i" )
if "%PYEXECFLAG%" == 0 (
    echo pycmd env: [%PYEXECNAME%] is not existed. exit 1.
) else (
    call "%PYPROGRAMPATHNAME%" type here %PYEXECNAME% %PYEXECINDEX%
    call "%CD%\%PYEXECINDEX%_exec.bat"
    del /q /f "%CD%\%PYEXECINDEX%_exec.bat"
)
