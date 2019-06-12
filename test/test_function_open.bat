@echo off

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT%\MyShell
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
