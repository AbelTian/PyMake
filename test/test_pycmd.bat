@echo off

:: ����ִ�� test
:: test
:: echo %CD%

call pymake source file "%CD%\..\example\pymake7-win-tai.json"
call pycmd test

echo "current path: %CD%"

:: Ŀ�꣬��ǰ·���Ͷ��ˡ�
if "" == "" (
    echo "Successed"
) else (
    echo "Failed"
)

:: ���ʹ�� pymake cc ִ�У�Ŀ��Ϊ��%pymm get default exec root%���Ͷ��ˡ�