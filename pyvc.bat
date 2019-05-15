@echo off

:: ��<source-root>/<source-file>.json����$(mm source)�ļ�������ӣ�
:: ��ÿ��ʹ��MSVC��ENV��������������������������
:: "VCVARSALL"="${vcvarsall-201x}"��${vcvarsall-201x} ·�������浽 path-assemblage��  
:: "VCVARSALLPARAM"="amd64_x86"�����������������ENV��Ŀ�������    
:: ֻ��������pyvc.bat ����ִ����Ч��  

:: bat�������������ִ�Сд��
:: ��������"RUN-VCVARSALL"="${VCVARSALL} ${VCVARSALLPARAM}"��
:: �û����о�������"CLS-VCVARSALL"��"CLS-VCVARSALLPARAM"��

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
) else (
    set PYENVNAME=%1
)

set PYPROGRAMPATH=%~dp0
set PYPROGRAMNAME=pymake.bat
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%

for /F %%i in ('"%PYPROGRAMPATHNAME%" get current env') do ( set "PYMMDEFAULTENVNAME=%%i" )
rem echo environme: [%PYMMDEFAULTENVNAME%] [default]
for /F %%i in ('"%PYPROGRAMPATHNAME%" have env %PYENVNAME%') do ( set "PYENVEXISTEDFLAG=%%i" )
if "%PYENVEXISTEDFLAG%" == "False" (
    echo environme: [%PYENVNAME%] is not existed.
    exit /b 0
)
rem echo environme: [%PYENVNAME%] [%PYENVEXISTEDFLAG%] [USED]

call "%PYPROGRAMPATH%\pyenv.bat" %PYENVNAME%

if "%PYENVFLAG%" == "False" (
    echo pyvc env : CLS-VCVARSALL="%CLS-VCVARSALL:/=\%" %CLS-VCVARSALLPARAM%
    call "%CLS-VCVARSALL:/=\%" %CLS-VCVARSALLPARAM%
    echo pyvc env : [%PYENVNAME%] closed, but you should use new vcvarsall overlap it.
) else (
    echo pyvc env : RUN-VCVARSALL="%VCVARSALL:/=\%" %VCVARSALLPARAM%
    call "%VCVARSALL:/=\%" %VCVARSALLPARAM%
    echo pyvc env : [%PYENVNAME%] opened, sure.
)
