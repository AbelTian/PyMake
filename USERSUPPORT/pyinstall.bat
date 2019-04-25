@echo off
::请使用 pyinstall.bat %* 进行安装

set mmfile=C:\Windows\pycmd.bat
set filepath=%~dp0
set sourcefile=pycmd.bat
call :install %*

exit /b 0

::================================================================
:install
echo @echo off > %mmfile%
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
goto :eof