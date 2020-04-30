@echo off
rem cd /d ${root.src}

setlocal enabledelayedexpansion
set MODULEARRAY=QQt QQtTool QQtExquisite QQtHighGrade QQtInput QQtInstallFramework QQtMediaExtention QQtRuntimeExtention QQtStyle QQtSupport
set ENVARRAY=mingw32 mingw64 android.mobile android.x86
for %%i in  (%MODULEARRAY%) do ( 
    rem echo %%i 
    for %%j in (%ENVARRAY%) do (
        set MODULENAME=%%i
        set ENVNAME=%%j
        set WORKROOT=
        rem echo !MODULENAME! !ENVNAME!
        call :build !ENVNAME! !MODULENAME! !WORKROOT!
        call ping 127.0.0.1 -n 2 1>nul
    )
)
exit /b 0

:build 
if "%ENVNAME%" == "" ( SET ENVNAME=current )
if "%MODULENAME%" == "" ( SET MODULENAME=QQt )
if "%MODULENAME%" == "QQt" ( SET WORKROOT=LibQQt )
if "%WORKROOT%" == "" ( SET WORKROOT=%MODULENAME% )
if not "%1" == "" ( SET ENVNAME=%1 )
if not ""%2"" == """" ( SET MODULENAME=%2 )
if not "%3" == "" ( SET WORKROOT=%3 )
rem echo %ENVNAME% %MODULENAME% %WORKROOT%
echo start cmd /k "pyenv %ENVNAME% && cd /d %CD%\%WORKROOT% && build.qmake %MODULENAME%"
start cmd /k "pyenv %ENVNAME% && cd /d %CD%\%WORKROOT% && build.qmake %MODULENAME%"
goto :eof
