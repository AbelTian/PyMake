@echo off
set mmfile=C:\Windows\pyenv.bat
set filepath=%~dp0
set sourcefile=pyenv.bat

echo @echo off > %mmfile% 
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
rem 请使用 pyinstall-pyenv.bat %* 进行安装

