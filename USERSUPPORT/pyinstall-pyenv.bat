@echo off
set filepath=%~dp0
set mmfile=C:\Windows\pyenv.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pyenv.bat" %* >> %mmfile%
rem 请使用 pyinstall-pyenv.bat %* 进行安装

