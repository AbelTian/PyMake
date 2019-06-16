@echo off

:: pyvcexport.bat 在当前目录，导出某个环境。

if "%1" == "" (
    echo usage:
    echo "  pyvcexport <env-name> [ <script-name> ]"
    echo ------
    echo please appoint a env name. & exit /b 0
)

set PYENVNAME=%1
if ""%1"" == """" (
    set PYENVNAME=current
)
if /i "%1" == """" (
    set PYENVNAME=current
)

set PYSCRIPTNAME=%2
if ""%2"" == """" (
    set PYSCRIPTNAME=env
)
if /i "%2" == """" (
    set PYSCRIPTNAME=env
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

rem for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYMMDEFAULTENVNAME=%%i" )
rem echo environme: [%PYMMDEFAULTENVNAME%] [default]
rem if not "%2" == "" (
rem     set PYENVNAME=%2
rem ) else (
rem     set PYENVNAME=%PYMMDEFAULTENVNAME%
rem )

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

rem echo %PYENVNAME%
rem echo %PYSCRIPTNAME%
call "%PYPROGRAMPATHNAME%" vc export2 here %PYENVNAME% to %PYSCRIPTNAME% --local --custom
