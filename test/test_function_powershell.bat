@echo off

set command=pymake powershell
echo %command%
call %command%

set command=pymake powershell info
echo %command%
call %command%

set command=pymake powershell information
echo %command%
call %command%

set command=pymake powershell stat
echo %command%
call %command%

set command=pymake powershell status
echo %command%
call %command%

set command=pymake powershell clean
echo %command%
call %command%

set command=pymake powershell type
echo %command%
call %command%

set command=pymake powershell use current type
echo %command%
call %command%

for /F %%i in ('"pymake source root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT%\MyShell
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

echo .... %CD%

set command=pymake powershell exec-with-params p���� --workroot %WORKROOT%
echo %command%
call %command%

echo .... %CD%

set command=pymake powershell exec-with-params p���� --params "��ã�������"
echo %command%
call %command%

echo .... %CD%

set command=pymake powershell exec-with-params here p���� --params "��ã��й���"
echo %command%
call %command%

echo .... %CD%

set command=pypowershell p���� "��ã���һ�Σ��й���"
echo %command%
call %command%
