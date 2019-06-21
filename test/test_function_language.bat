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

set command=pymake language exec-with-params py --params py���� --suffix=.py --workroot %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params py --params py���� --suffix=.py --params "��� �й�" --params "��� ����" --params "Hello Japanese" --params %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params here py --params py���� --suffix=.py
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language exec-with-params py --params py����.py --params "��� �й�" --params "��� ����" --params "Hello Japanese" --params %WORKROOT%
echo %command%
call %command%
echo --------------------------------------------

rem I cant know who you are.
rem illegal
set command=pylanguage py py���� "��� �й�" "��� ����" "��� ����˹"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pylanguage py py����.py "��� �й�" "��� ����" "��� ����˹"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp "powershell -File" p����.ps1 "��� �й�" "���  ����"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp python py����.py "��� �й�" "��� ����" \" ��� ����\" ���� "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp python py����.py "��� �й�" "��� ����"\" ��� ����\" ���� "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

rem illegal
set command=pymake language ccvp python py����.py "��� �й�""��� ����" \" ��� ����\" ���� "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

rem legal
set command=pymake language ccvp "cmd /c" test.7.bat  "��� �й�" "��� ����" \" ��� ����\" ���� "B -c -y"
echo %command%
call %command%
echo --------------------------------------------

set command=pymake language ccvp "cmd /c" test.7  "��� �й�" "��� ����" \" ��� ����\" ���� "B -c -y"
echo %command%
call %command%
echo --------------------------------------------
