@echo off

set command=pymake python
echo %command%
call %command%

set command=pymake python info
echo %command%
call %command%

set command=pymake python information
echo %command%
call %command%

set command=pymake python stat
echo %command%
call %command%

set command=pymake python status
echo %command%
call %command%

set command=pymake python clean
echo %command%
call %command%

set command=pymake python type
echo %command%
call %command%

set command=pymake python use current type
echo %command%
call %command%

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT%\MyShell
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=pymake python exec-with-params py中文 --workroot %WORKROOT%
echo %command%
call %command%

set command=pymake python exec-with-params py中文 --params %WORKROOT%
echo %command%
call %command%

set command=pymake python exec-with-params here py中文
echo %command%
call %command%
