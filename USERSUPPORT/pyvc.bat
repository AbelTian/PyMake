@echo off

set PYFILEPATH=%~dp0
call %PYFILEPATH%\pyenv.bat %*

if %PYENVFLAG% == 0 (
    echo pyvc env : CLS-VCVARSALL="%CLS-VCVARSALL:/=\%"
    call "%CLS-VCVARSALL:/=\%" "%CLS-VCVARSALLPARAM%"
    echo pyvc env : [%PYENVNAME%] closed, but you should use new vcvarsall overlap it.
) else (
    echo pyvc env : VCVARSALL="%VCVARSALL:/=\%" "%VCVARSALLPARAM%"
    call "%VCVARSALL:/=\%" "%VCVARSALLPARAM%"
    echo pyvc env : [%PYENVNAME%] opened, sure.
)
