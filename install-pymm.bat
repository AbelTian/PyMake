@echo off
set filepath=%~dp0
set mmfile=C:\Windows\pymm.bat
echo @echo off > %mmfile% 
echo call "%filepath%pymake8.bat" %* >> %mmfile% 
rem 请使用 install-pymm.bat %* 进行安装

