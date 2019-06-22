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

set sourcefile=pyvcccvp.bat
set mmfile=pyvcccvp.bat
call :uninstall

set sourcefile=pyvcexport.bat
set mmfile=pyvcexport.bat
call :uninstall

set sourcefile=pyvcpython.bat
set mmfile=pyvcpython.bat
call :uninstall

set sourcefile=pyvcpowershell.bat
set mmfile=pyvcpowershell.bat
call :uninstall

set sourcefile=pyvclanguage.bat
set mmfile=pyvclanguage.bat
call :uninstall

set sourcefile=pytype.bat
set mmfile=pytype.bat
call :uninstall

set sourcefile=pyexport.bat
set mmfile=pyexport.bat
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

set sourcefile=pypython.bat
set mmfile=pypython.bat
call :uninstall

set sourcefile=pypowershell.bat
set mmfile=pypowershell.bat
call :uninstall

set sourcefile=pylanguage.bat
set mmfile=pylanguage.bat
call :uninstall

set sourcefile=pyclean.bat
set mmfile=pyclean.bat
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

set sourcefile=pyvc.ps1
set mmfile=pyvc.ps1
call :uninstall

echo 卸载成功。
exit /b 0

::================================================================
:uninstall
if exist "%mmpath%\%mmfile%" call del /q /f "%mmpath%\%mmfile%"
echo 卸载 %mmfile%
goto :eof
