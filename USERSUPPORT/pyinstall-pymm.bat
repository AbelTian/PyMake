@echo off
set filepath=%~dp0..
set mmfile=C:\Windows\pymm.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pymake.bat" %* >> %mmfile%
rem ��ʹ�� pyinstall-pymm.bat %* ���а�װ

