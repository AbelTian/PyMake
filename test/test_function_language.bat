@echo off

set command=pymake language
echo %command%
call %command%

set command=pymake language info
echo %command%
call %command%

set command=pymake language information
echo %command%
call %command%

set command=pymake language stat
echo %command%
call %command%

set command=pymake language status
echo %command%
call %command%

set command=pymake language clean
echo %command%
call %command%

set command=pymake language type
echo %command%
call %command%

set command=pymake language use current type
echo %command%
call %command%

for /F %%i in ('"pymake source root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT%\MyShell
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=pymake language exec-with-params python --params py����.py --workroot %WORKROOT%
echo %command%
call %command%

set command=pymake language exec-with-params python --params py����.py --params "��� �й�" --params "��� ����" --params "Hello Japanese" --params %WORKROOT%
echo %command%
call %command%

set command=pymake language exec-with-params here python --params py����.py
echo %command%
call %command%
