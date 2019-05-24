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

set command=pymake language exec-with-params py --params py中文.py --workroot %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params py --params py中文.py --params "你好 中国" --params "你好 美国" --params "Hello Japanese" --params %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params here py --params py中文.py
echo %command%
call %command%
echo --------------------------------------------

set command=pylanguage py py中文.py "你好 中国" "你好 美国" "你好 俄罗斯"
echo %command%
call %command%
echo --------------------------------------------