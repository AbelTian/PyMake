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

set command=pyccvp test.7 "��� �й�"
echo %command%
call %command%

set command=pyccvp "test.8 blank" ��� �й�
echo %command%
call %command%

set command=pyccvp "test.8 blank" C:\Windows "��� �й�" ��� �й�
echo %command%
call %command%

set command=pyccvp "test.8 blank" "C:\Windows"
echo %command%
call %command%

set command=pyccvp "test.8 blank" "���" "��� �й�" ���� "����á� ���й���"
echo %command%
call %command%

set command=pycmd "HEIHEI 2"
echo %command%
call %command%

set command=pycmd ""
echo %command%
call %command%

set command=pycmd " "
echo %command%
call %command%

set command=pycmd ''
echo %command%
call %command%

set command=pycmd ' '
echo %command%
call %command%

