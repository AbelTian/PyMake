@echo off
::��ʹ�� install.bat %* ���а�װ

set mmpath=C:\Windows

set mmfile=mm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=pymm.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=pymake.bat
set filepath=%~dp0
set sourcefile=pymake.bat
call :install %*

set mmfile=pyenv.bat
set filepath=%~dp0
set sourcefile=pyenv.bat
call :install %*

set mmfile=pyvc.bat
set filepath=%~dp0
set sourcefile=pyvc.bat
call :install %*

set mmfile=pycmd.bat
set filepath=%~dp0
set sourcefile=pycmd.bat
call :install %*

set mmfile=pyexecvp.bat
set filepath=%~dp0
set sourcefile=pyexecvp.bat
call :install %*

set mmfile=pyccvp.bat
set filepath=%~dp0
set sourcefile=pyccvp.bat
call :install %*

set mmfile=pyinfo.bat
set filepath=%~dp0
set sourcefile=pyinfo.bat
call :install %*

set mmfile=pypaths.bat
set filepath=%~dp0
set sourcefile=pypaths.bat
call :install %*

echo ��װ�ɹ���
exit /b 0

::================================================================
:install
echo @echo off > %mmfile%
echo call "%filepath%\%sourcefile%" %* >> "%mmpath%\%mmfile%"
echo ��װ %mmpath%\%mmfile%
goto :eof
