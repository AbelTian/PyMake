@echo off
set filepath=%~dp0..
set mmfile=C:\Windows\pymm.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pymake.bat" %* >> %mmfile%
rem 请使用 pyinstall-pymm.bat %* 进行安装

