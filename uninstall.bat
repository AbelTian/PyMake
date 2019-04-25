@echo off
::请使用 uninstall.bat 进行卸载

set mmfile=C:\Windows\mm.bat
call :uninstall

set mmfile=C:\Windows\pymm.bat
call :uninstall

set mmfile=C:\Windows\pymake.bat
call :uninstall

set mmfile=C:\Windows\pyenv.bat
call :uninstall

set mmfile=C:\Windows\pyvc.bat
call :uninstall

set mmfile=C:\Windows\pycmd.bat
call :uninstall

set mmfile=C:\Windows\pyinfo.bat
call :uninstall

::================================================================
:uninstall
call del /q /f %mmfile%
goto :eof
