@echo off
set mmfile=C:\Windows\pymm.bat
set filepath=%~dp0..
set sourcefile=pymake.bat

echo @echo off > %mmfile% 
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
rem ��ʹ�� pyinstall-pymm.bat %* ���а�װ

