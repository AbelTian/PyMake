@echo off
set filepath=%~dp0..
set mmfile=C:\Windows\pymake.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pymake.bat" %* >> %mmfile%
rem 请使用 pyinstall-pymake.bat %* 进行安装

