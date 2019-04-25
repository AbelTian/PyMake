@echo off
::请使用 install.bat %* 进行安装

set mmfile=C:\Windows\mm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=C:\Windows\pymm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=C:\Windows\pymake.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=C:\Windows\pyenv.bat
set filepath=%~dp0
set sourcefile=pyenv.bat
call :install %*

set mmfile=C:\Windows\pyvc.bat
set filepath=%~dp0
set sourcefile=pyvc.bat
call :install %*

set mmfile=C:\Windows\pycmd.bat
set filepath=%~dp0
set sourcefile=pycmd.bat
call :install %*

set mmfile=C:\Windows\pyinfo.bat
set filepath=%~dp0
set sourcefile=pyinfo.bat
call :install %*

exit /b 0

::================================================================
:install
echo @echo off > %mmfile%
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
goto :eof
