@echo off
set filepath=%~dp0
set mmfile=C:\Windows\pymm.bat
echo @echo off > %mmfile% 
echo call "%filepath%pymake8.bat" %* >> %mmfile% 
rem ��ʹ�� install-pymm.bat %* ���а�װ

