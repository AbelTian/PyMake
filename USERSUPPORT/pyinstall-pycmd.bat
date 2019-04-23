@echo off
set mmfile=C:\Windows\pycmd.bat
set filepath=%~dp0
set sourcefile=pycmd.bat

echo @echo off > %mmfile% 
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
rem 请使用 pyinstall-pycmd.bat %* 进行安装

