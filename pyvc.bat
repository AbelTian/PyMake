@echo off

:: ��<source-root>/<source-file>.json����$(mm source)�ļ�������ӣ�
:: ��ÿ��ʹ��MSVC��ENV��������������������������
:: "VCVARSALL"="${vcvarsall-201x}"��${vcvarsall-201x} ·�������浽 path-assemblage��  
:: "VCVARSALLPARAM"="amd64_x86"�����������������ENV��Ŀ�������    
:: ֻ��������pyvc.bat ����ִ����Ч��  

:: bat�������������ִ�Сд��
:: ��������"RUN-VCVARSALL"="${VCVARSALL} ${VCVARSALLPARAM}"��
:: �û����о�������"CLS-VCVARSALL"��"CLS-VCVARSALLPARAM"��

set PYENVFLAG=True
if "%1" == "" (
    echo usage:
    echo "  pyvc <env-name>"
    echo "  pyvc open <env-name>"
    echo "  pyvc close <env-name>"
    echo "  <env name>: 'current' is suggested."
    echo ------
    echo please appoint a env name. & exit /b 0
) else if "%1" == "open" (
    if "%2" == "" (
        echo usage:
        echo "  pyvc <env-name>"
        echo "  pyvc open <env-name>"
        echo "  pyvc close <env-name>"
        echo "  <env name>: 'current' is suggested."
        echo ------
        echo please appoint a env name. & exit /b 0
    )
    set PYENVNAME=%2
) else if "%1" == "close" (
    if "%2" == "" (
        echo usage:
        echo "  pyvc <env-name>"
        echo "  pyvc open <env-name>"
        echo "  pyvc close <env-name>"
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

echo preparing vc env ...
for /F %%i in ('echo %random%') do ( set "PYENVINDEX=%%i" )
rem echo env index: [%PYENVINDEX%]
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

call "%PYPROGRAMPATHNAME%" vc export2 here %PYENVNAME% to %PYENVINDEX% --local --custom
if not "%ERRORLEVEL%" == "0" (
    exit /b %ERRORLEVEL%
)

rem echo %ERRORLEVEL%
if "%PYENVFLAG%" == "False" (
    call "%PYMMSHELLROOT%\%PYENVINDEX%_unset.bat"
    echo vc env   : [%PYENVNAME%] closed
) else (
    call "%PYMMSHELLROOT%\%PYENVINDEX%_effect.bat"
    echo vc env   : [%PYENVNAME%] opened
)

::clean
del /q /f "%PYMMSHELLROOT%\%PYENVINDEX%_effect.bat" "%PYMMSHELLROOT%\%PYENVINDEX%_unset.bat"
