@echo off

set command=pyccvp
echo %command%
call %command%

set command=pyccvp dir
echo %command%
call %command%

set command=pyexecvp dir
echo %command%
call %command%

set command=pyccvp dir %WORKROOT%
echo %command%
call %command%

set command=pyexecvp dir %WORKROOT%
echo %command%
call %command%

set command=pyccvp ""
echo %command%
call %command%

set command=pyccvp test.7 "C:\Windows"
echo %command%
call %command%

set command=pyccvp "test.7" "C:\Windows"
echo %command%
call %command%

set command=pyccvp test.7 ""
echo %command%
call %command%

set command=pyccvp test.7 " "
echo %command%
call %command%

set command=pyccvp test.7 "你好 中国"
echo %command%
call %command%

set command=pyccvp "test.8 blank" 你好 中国
echo %command%
call %command%

set command=pyccvp "test.8 blank" C:\Windows "你好 中国" 你好 中国
echo %command%
call %command%

set command=pyccvp "test.8 blank" "C:\Windows"
echo %command%
call %command%
