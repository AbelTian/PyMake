@echo off

call pyenv.bat %*

if %PYENVFLAG% == 0 (
    echo pyvc env : CLS-VCVARSALL="%CLS-VCVARSALL:/=\%"
    call "%CLS-VCVARSALL%"
    echo pyvc env : [%PYENVNAME%] closed£¬but you should use new vcvarsall overlap it.
) else (
    echo pyvc env : RUN-VCVARSALL="%RUN-VCVARSALL:/=\%"
    call "%RUN-VCVARSALL%"
    echo pyvc env : [%PYENVNAME%] opened, sure.
)
