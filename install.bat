@echo off
::请使用 install.bat %* 进行安装

set mmpath=C:\Windows

set mmfile=%mmpath%\mm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=%mmpath%\pymm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=%mmpath%\pymake.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=%mmpath%\pyenv.bat
set filepath=%~dp0
set sourcefile=pyenv.bat
call :install %*

set mmfile=%mmpath%\pyvc.bat
set filepath=%~dp0
set sourcefile=pyvc.bat
call :install %*

set mmfile=%mmpath%\pycmd.bat
set filepath=%~dp0
set sourcefile=pycmd.bat
call :install %*

set mmfile=%mmpath%\pyexecvp.bat
set filepath=%~dp0
set sourcefile=pyexecvp.bat
call :install %*

set mmfile=%mmpath%\pyccvp.bat
set filepath=%~dp0
set sourcefile=pyccvp.bat
call :install %*

set mmfile=%mmpath%\pyinfo.bat
set filepath=%~dp0
set sourcefile=pyinfo.bat
call :install %*

set mmfile=%mmpath%\pypaths.bat
set filepath=%~dp0
set sourcefile=pypaths.bat
call :install %*

exit /b 0

::================================================================
:install
echo @echo off > %mmfile%
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
goto :eof
