@echo off
set filepath=%~dp0
set mmfile=C:\Windows\pyvc.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pyvc.bat" %* >> %mmfile%
rem 请使用 pyinstall-pyvc.bat %* 进行安装

