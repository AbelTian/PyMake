@echo off

:: pypowershell.bat 在当前环境执行pymake保存的命令，自带一个环境，可以带参数。
:: pypowershell.bat 使用pymake的默认环境导出命令，如果用户输入环境，那么使用用户输入的环境。
:: pypowershell.bat 会导出环境进行使用。
:: pypowershell.bat 用户应当留意，导出的是否是目标环境的命令。

if "%1" == "" (
    echo usage:
    echo "  pypowershell <cmd-name> [ <cmd-params> ] [<env-name>]"
    echo "  <env name>: 'current' is suggested."
    echo "  please appoint a cmd name."
    echo usage 2:
    echo "  pypowershell open <env-name>"
    echo "  pypowershell close <env-name>"
    echo "  please appoint a env name." & exit /b 0
)

set PYEXECNAME=%1
set PYEXECPARAM=%2
set PYENVNAME=%3
if "%1" == "" (
    set PYEXECNAME=
)
if ""%2"" == """" (
    set PYEXECPARAM=
)
if "%3" == "" (
    set PYENVNAME=
)

set PYENVFLAG=None
if "%1" == "open" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
    set PYENVNAME=%2
    set PYENVFLAG=True
) else if "%1" == "close" (
    if "%2" == "" ( echo please appoint a env name. & exit /b 0 )
    set PYENVNAME=%2
    set PYENVFLAG=False
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

for /F %%i in ('"%PYPROGRAMPATHNAME%" get default exec root') do ( set "PYMMSHELLROOT=%%i" )
echo exec root: [%PYMMSHELLROOT%] [default]
echo exec root: [%CD%] [here]

if not "%PYENVFLAG%" == "None" (
    call "%PYPROGRAMPATHNAME%" powershell export %PYENVNAME% to %PYEXECINDEX%
    if "%PYENVFLAG%" == "False" (
        "%PYMMSHELLROOT%\powershell.%PYEXECINDEX%_unset.ps1"
        echo user env : [%PYENVNAME%] closed. [powershell]
        exit /b 0
    ) else (
        "%PYMMSHELLROOT%\powershell.%PYEXECINDEX%_effect.ps1"
        echo user env : [%PYENVNAME%] opened. [powershell]
        exit /b 0
    )
)

for /F %%i in ('"%PYPROGRAMPATHNAME%" have cmd %PYEXECNAME%') do ( set "PYEXECFLAG=%%i" )
if "%PYEXECFLAG%" == "False" (
    echo command  : [%PYEXECNAME%] is system wild command.
) else (
    echo command  : [%PYEXECNAME%] [%PYEXECFLAG%] [EXISTED]
)

if not ""%PYEXECPARAM%"" == """" (
    call "%PYPROGRAMPATHNAME%" powershell use %PYENVNAME% exec-with-params here %PYEXECNAME% --params %PYEXECPARAM%
) else (
    call "%PYPROGRAMPATHNAME%" powershell use %PYENVNAME% exec-with-params here %PYEXECNAME%
)