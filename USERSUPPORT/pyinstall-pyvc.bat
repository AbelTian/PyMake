@echo off
set filepath=%~dp0
set mmfile=C:\Windows\pyvc.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pyvc.bat" %* >> %mmfile%
rem ��ʹ�� pyinstall-pyvc.bat %* ���а�װ

