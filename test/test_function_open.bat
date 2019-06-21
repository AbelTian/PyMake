@echo off

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=mm open pymake.shell
echo %command%
call %command%

set command=mm open ${pymake.env}
echo %command%
call %command%

set command=mm open "py"
echo %command%
call %command%

set command=mm open ${PYMAKE}/UserSource/${QKIT} --current
echo %command%
call %command%

set command=mm open \"${py}\"
echo %command%
call %command%

set command=mm open \"${py}\" --custom
echo %command%
call %command%

set command=mm open \"${py}\" --custom --current
echo %command%
call %command%

set command=mm open \"${py}\" --custom --envname android.mobile
echo %command%
call %command%

set command=mm open \"${py}\" --current
echo %command%
call %command%

set command=mm open \"${py}\" --envname android.mobile
echo %command%
call %command%

set command=mm open \"${py}\" android.mobile
echo %command%
call %command%

set command=mm open ${py} android.mobile
echo %command%
call %command%

set command=mm open sdk --custom
call :execmd

set command=mm open sdk --current
call :execmd

set command=mm open qtdir --custom
call :execmd

set command=mm open qtdir --current
call :execmd

set command=mm use current open qtdir
call :execmd

set command=mm use current open qtdir
call :execmd


exit /b 0

:execmd
echo -----------------------------------------------------
echo %command%
call %command%
goto :eof


