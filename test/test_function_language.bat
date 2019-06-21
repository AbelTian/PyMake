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

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=pymake language exec-with-params py --params py中文 --suffix=.py --workroot %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params py --params py中文 --suffix=.py --params "你好 中国" --params "你好 美国" --params "Hello Japanese" --params %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params here py --params py中文 --suffix=.py
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params py --params py中文.py --params "你好 中国" --params "你好 美国" --params "Hello Japanese" --params %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

rem I cant know who you are.
rem illegal
set command=pylanguage py py中文 "你好 中国" "你好 美国" "你好 俄罗斯"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pylanguage py py中文.py "你好 中国" "你好 美国" "你好 俄罗斯"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp "powershell -File" p中文.ps1 "你好 中国" "你好  美国"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp python py中文.py "你好 中国" "你好 美国" \" 你好 美国\" 是吗？ "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp python py中文.py "你好 中国" "你好 美国"\" 你好 美国\" 是吗？ "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

rem illegal
set command=pymake language ccvp python py中文.py "你好 中国""你好 美国" \" 你好 美国\" 是吗？ "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp "cmd /c" test.7.bat  "你好 中国" "你好 美国" \" 你好 美国\" 是吗？ "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language ccvp "cmd /c" test.7  "你好 中国" "你好 美国" \" 你好 美国\" 是吗？ "B -c -y"
echo %command%
call %command%
echo --------------------------------------------
