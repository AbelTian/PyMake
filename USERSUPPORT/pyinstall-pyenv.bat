@echo off
set filepath=%~dp0
set mmfile=C:\Windows\pyenv.bat
echo @echo off > %mmfile% 
echo call "%filepath%\pyenv.bat" %* >> %mmfile%
rem ��ʹ�� pyinstall-pyenv.bat %* ���а�װ

