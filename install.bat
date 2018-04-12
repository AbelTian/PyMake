@echo off
set filepath=%~dp0
set mmfile=C:\Windows\mm.bat
echo @echo off > %mmfile% 
echo call "%filepath%pymake.bat" %* >> %mmfile% 
rem 请使用 install.bat %* 进行安装

