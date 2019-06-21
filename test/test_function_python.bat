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

set command=pymake python ccvp py中文 "你好 中国" 你好 中国 \"你好\" \" 你好 美国\" 是吗？ "B -c -y"
echo %command%
call %command%
