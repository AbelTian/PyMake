@echo off
::��ʹ�� uninstall.bat ����ж��

set mmpath=C:\Windows

set sourcefile=mm.bat
set mmfile=%mmpath%\mm.bat
call :uninstall

set sourcefile=pymm.bat
set mmfile=%mmpath%\pymm.bat
call :uninstall

set sourcefile=pymake.bat
set mmfile=%mmpath%\pymake.bat
call :uninstall

set sourcefile=pyenv.bat
set mmfile=%mmpath%\pyenv.bat
call :uninstall

set sourcefile=pyvc.bat
set mmfile=%mmpath%\pyvc.bat
call :uninstall

set sourcefile=pycmd.bat
set mmfile=%mmpath%\pycmd.bat
call :uninstall

set sourcefile=pyexecvp.bat
set mmfile=%mmpath%\pyexecvp.bat
call :uninstall

set sourcefile=pyccvp.bat
set mmfile=%mmpath%\pyccvp.bat
call :uninstall

set sourcefile=pyinfo.bat
set mmfile=%mmpath%\pyinfo.bat
call :uninstall

set sourcefile=pypaths.bat
set mmfile=%mmpath%\pypaths.bat
call :uninstall

echo ж�سɹ���
exit /b 0

::================================================================
:uninstall
if exist "%mmfile%" call del /q /f %mmfile%
echo ж�� %sourcefile%
goto :eof
