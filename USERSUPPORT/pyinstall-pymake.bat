@echo off
set filepath=%~dp0..
set mmfile=C:\Windows\pymake.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pymake.bat" %* >> %mmfile%
rem ��ʹ�� pyinstall-pymake.bat %* ���а�װ

