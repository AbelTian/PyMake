@echo off

:: pypowershell.bat �ڵ�ǰ����ִ��pymake���������Դ�һ�����������Դ�������
:: pypowershell.bat ʹ��pymake��Ĭ�ϻ��������������û����뻷������ôʹ���û�����Ļ�����
:: pypowershell.bat �ᵼ����������ʹ�á�
:: pypowershell.bat �û�Ӧ�����⣬�������Ƿ���Ŀ�껷�������

if "%1" == "" (
    echo usage:
    echo "  pypowershell <cmd-name> [ <cmd-params> ] [<env-name>]"
    echo "  <env name>: 'current' is suggested."
    echo -----
    echo please appoint a cmd name. & exit /b 0
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

rem for /F %%i in ('"%PYPROGRAMPATHNAME%" get default exec root') do ( set "PYMMSHELLROOT=%%i" )
rem echo exec root: [%PYMMSHELLROOT%] [default]
rem echo exec root: [%CD%] [here]

rem for /F %%i in ('"%PYPROGRAMPATHNAME%" have cmd %PYEXECNAME%') do ( set "PYEXECFLAG=%%i" )
rem if "%PYEXECFLAG%" == "False" (
rem     echo command  : [%PYEXECNAME%] is system wild command.
rem ) else (
rem     echo command  : [%PYEXECNAME%] [%PYEXECFLAG%] [EXISTED]
rem )

if not ""%PYEXECPARAM%"" == """" (
    call "%PYPROGRAMPATHNAME%" powershell use %PYENVNAME% exec-with-params here %PYEXECNAME% --params %PYEXECPARAM%
) else (
    call "%PYPROGRAMPATHNAME%" powershell use %PYENVNAME% exec-with-params here %PYEXECNAME%
)