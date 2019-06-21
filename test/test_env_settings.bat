@echo off

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=mm use current ccvp "which lua"
echo %command%
call %command%

set command=mm use current ccvp "which go"
echo %command%
call %command%

rem set command=echo cmake & mm use current ccvp which cmake
set command=mm use current ccvp which cmake
echo %command%
call %command%


set command=mm use current ccvp which perl
echo %command%
call %command%

set command=mm use current ccvp which php
echo %command%
call %command%

set command=mm use current ccvp which ruby
echo %command%
call %command%

set command=mm use current ccvp which r
echo %command%
call %command%

set command=mm use current ccvp which node
echo %command%
call %command%

set command=mm use current ccvp which elixir
echo %command%
call %command%

set cmdname=qmake
call :find_exec

exit /b 0

:find_exec
set command=mm use current ccvp which %cmdname%
echo %command%
call %command%
goto :eof
