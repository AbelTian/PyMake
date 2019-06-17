@echo off
::请使用 install.bat %* 进行安装

set mmpath=C:\Windows

set mmfile=mm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=pymm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=pymake.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=pyenv.bat
set filepath=%~dp0
set sourcefile=pyenv.bat
call :install %*

set mmfile=pyvc.bat
set filepath=%~dp0
set sourcefile=pyvc.bat
call :install %*

set mmfile=pyvcccvp.bat
set filepath=%~dp0
set sourcefile=pyvcccvp.bat
call :install %*

set mmfile=pyvcexport.bat
set filepath=%~dp0
set sourcefile=pyvcexport.bat
call :install %*

set mmfile=pyvcpython.bat
set filepath=%~dp0
set sourcefile=pyvcpython.bat
call :install %*

set mmfile=pyvcpowershell.bat
set filepath=%~dp0
set sourcefile=pyvcpowershell.bat
call :install %*

set mmfile=pytype.bat
set filepath=%~dp0
set sourcefile=pytype.bat
call :install %*

set mmfile=pyexport.bat
set filepath=%~dp0
set sourcefile=pyexport.bat
call :install %*

set mmfile=pycmd.bat
set filepath=%~dp0
set sourcefile=pycmd.bat
call :install %*

set mmfile=pyexecvp.bat
set filepath=%~dp0
set sourcefile=pyexecvp.bat
call :install %*

set mmfile=pyccvp.bat
set filepath=%~dp0
set sourcefile=pyccvp.bat
call :install %*

set mmfile=pypython.bat
set filepath=%~dp0
set sourcefile=pypython.bat
call :install %*

set mmfile=pypowershell.bat
set filepath=%~dp0
set sourcefile=pypowershell.bat
call :install %*

set mmfile=pylanguage.bat
set filepath=%~dp0
set sourcefile=pylanguage.bat
call :install %*

set mmfile=pyclean.bat
set filepath=%~dp0
set sourcefile=pyclean.bat
call :install %*

set mmfile=pyinfo.bat
set filepath=%~dp0
set sourcefile=pyinfo.bat
call :install %*

set mmfile=pypaths.bat
set filepath=%~dp0
set sourcefile=pypaths.bat
call :install %*

set mmfile=pyenv.ps1
set filepath=%~dp0
set sourcefile=pyenv.ps1
call :install_powershell %*

set mmfile=pyvc.ps1
set filepath=%~dp0
set sourcefile=pyvc.ps1
call :install_powershell %*

echo 安装成功。
exit /b 0

::================================================================
:install
echo @echo off > "%mmpath%\%mmfile%"
echo call "%filepath%\%sourcefile%" %* >> "%mmpath%\%mmfile%"
echo 安装 %mmfile%
goto :eof

:install_powershell
echo . "%filepath%\%sourcefile%" @args > "%mmpath%\%mmfile%"
echo 安装 %mmfile%
goto :eof
