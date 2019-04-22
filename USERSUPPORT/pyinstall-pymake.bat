@echo off
set mmfile=C:\Windows\pymake.bat
set filepath=%~dp0..
set sourcefile=pymake.bat

echo @echo off > %mmfile% 
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
rem 请使用 pyinstall-pymake.bat %* 进行安装

