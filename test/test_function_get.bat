@echo off

set command=pymake set there exec root
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set exec root to there
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set starting exec root to there
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set there exec root to ""
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%


set command=pymake set there exec root to R:\Develop\b0-toolkits\a0-compiler\PyMake\UserSource\MyShell
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set there exec root to here
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set here exec root
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake get starting exec root -p
echo %command%
call %command%

set command=pymake get current exec root -p
echo %command%
call %command%

set command=pymake set there exec root to there
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set there exec root to default
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set there exec root to dd
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set there exec root to here
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set there exec root
echo %command%
call %command%

set command=pymake set tt exec root
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

set command=pymake set exec root
echo %command%
call %command%

set command=pymake get exec root -p
echo %command%
call %command%

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT:/=\\%
rem md %WORKROOT%
echo %WORKROOT%