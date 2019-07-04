@echo off

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=mm outport cmd hh cc0 to cc0 -f
call :execmd

set command=type cc0.bat
call :execmd

set command=mm outport cmd hh cc0 to cc0 -f --suffix .bb
call :execmd

set command=type cc0.bb
call :execmd

set command=mm outport cmd hh open.sdk to open.sdk -f
call :execmd

set command=type open.sdk.bat
call :execmd

set command=mm outport cmd hh open.sdk to open.sdk -f --suffix .bb
call :execmd

set command=type open.sdk.bb
call :execmd

set command=mm outport cmd hh build.qmake to build.qmake  -f
call :execmd

set command=type build.qmake.bat
call :execmd

set command=mm outport cmd hh build.qmake to build.qmake  -f --suffix .bb
call :execmd

set command=type build.qmake.bb
call :execmd

set command=mm outport cmd hh build.qmake to build.qmake  -fr
call :execmd

set command=type build.qmake.bat
call :execmd

set command=mm outport cmd hh build.qmake to build.qmake  -f --raw --suffix .bb
call :execmd

set command=type build.qmake.bb
call :execmd

exit /b 0

:execmd
echo -----------------------------------------------------
echo %command%
call %command%
goto :eof


