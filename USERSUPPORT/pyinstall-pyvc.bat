@echo off
set mmfile=C:\Windows\pyvc.bat
set filepath=%~dp0
set sourcefile=pyvc.bat

echo @echo off > %mmfile% 
echo call "%filepath%\%sourcefile%" %* >> %mmfile%
rem ��ʹ�� pyinstall-pyvc.bat %* ���а�װ

