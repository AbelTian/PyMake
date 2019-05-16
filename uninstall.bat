@echo off
::请使用 uninstall.bat 进行卸载

set mmpath=C:\Windows

set sourcefile=mm.bat
set mmfile=mm.bat
call :uninstall

set sourcefile=pymm.bat
set mmfile=pymm.bat
call :uninstall

set sourcefile=pymake.bat
set mmfile=pymake.bat
call :uninstall

set sourcefile=pyenv.bat
set mmfile=pyenv.bat
call :uninstall

set sourcefile=pyvc.bat
set mmfile=pyvc.bat
call :uninstall

set sourcefile=pycmd.bat
set mmfile=pycmd.bat
call :uninstall

set sourcefile=pyexecvp.bat
set mmfile=pyexecvp.bat
call :uninstall

set sourcefile=pyccvp.bat
set mmfile=pyccvp.bat
call :uninstall

set sourcefile=pypowershell.bat
set mmfile=pypowershell.bat
call :uninstall

set sourcefile=pyinfo.bat
set mmfile=pyinfo.bat
call :uninstall

set sourcefile=pypaths.bat
set mmfile=pypaths.bat
call :uninstall

set sourcefile=pyenv.ps1
set mmfile=pyenv.ps1
call :uninstall

echo 卸载成功。
exit /b 0

::================================================================
:uninstall
if exist "%mmpath%\%mmfile%" call del /q /f "%mmpath%\%mmfile%"
echo 卸载 %mmfile%
goto :eof
