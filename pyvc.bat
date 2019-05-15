@echo off

:: 在<source-root>/<source-file>.json，即$(mm source)文件里面添加，
:: 在每个使用MSVC的ENV配置里必须加入两个环境变量，
:: "VCVARSALL"="${vcvarsall-201x}"，${vcvarsall-201x} 路径集保存到 path-assemblage。  
:: "VCVARSALLPARAM"="amd64_x86"，这个环境变量根据ENV的目标决定。    
:: 只有这样，pyvc.bat 才能执行有效。  

:: bat环境变量不区分大小写。
:: 建议增加"RUN-VCVARSALL"="${VCVARSALL} ${VCVARSALLPARAM}"。
:: 用户自行决定配置"CLS-VCVARSALL"和"CLS-VCVARSALLPARAM"。

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
