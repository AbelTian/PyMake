@echo off
set mmfile=C:\Windows\mm.bat
set filepath=%~dp0
set sourcefile=pymake.bat

echo @echo off > %mmfile% 
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
rem 请使用 install.bat %* 进行安装
