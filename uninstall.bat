@echo off
::��ʹ�� uninstall.bat ����ж��

set mmpath=C:\Windows

set mmfile=%mmpath%\mm.bat
call :uninstall

set mmfile=%mmpath%\pymm.bat
call :uninstall

set mmfile=%mmpath%\pymake.bat
call :uninstall

set mmfile=%mmpath%\pyenv.bat
call :uninstall

set mmfile=%mmpath%\pyvc.bat
call :uninstall

set mmfile=%mmpath%\pycmd.bat
call :uninstall

set mmfile=%mmpath%\pyexecvp.bat
call :uninstall

set mmfile=%mmpath%\pyccvp.bat
call :uninstall

set mmfile=%mmpath%\pyinfo.bat
call :uninstall

set mmfile=%mmpath%\pypaths.bat
call :uninstall

exit /b 0

::================================================================
:uninstall
call del /q /f %mmfile%
goto :eof
