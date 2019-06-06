@echo off

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT%\MyShell
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=pymake system ccvp dir
echo %command%
call %command%

set command=pymake system ccvp "dir c:\\"
echo %command%
call %command%

set command=pymake system ccvp "go build"
echo %command%
call %command%


set command=pymake ccvp "HEI HEI.bat" C:\\
echo %command%
call %command%

set command=pymake ccvp "HEI HEI.bat C:\\"
echo %command%
call %command%

set command=pymake ccvp "HEIHEI.bat C:\\"
echo %command%
call %command%

set command=pymake language ccvp "HEI HEI.bat" C:\\
echo %command%
call %command%

set command=pymake language ccvp "dir c:\\"
echo %command%
call %command%

set command=pymake language ccvp "go build"
echo %command%
call %command%
