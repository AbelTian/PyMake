@echo off
::请使用 uninstall.bat 进行卸载

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

set mmfile=%mmpath%\pyinfo.bat
call :uninstall

::================================================================
:uninstall
call del /q /f %mmfile%
goto :eof
