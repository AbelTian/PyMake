@echo off

:: ����ִ�� test
:: test
:: echo %CD%

call pymake source file "%CD%\..\example\pymake7-win-tai.json"
call pycmd test

echo "work path   : ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ is work path."
echo "current path: %CD%"

:: Ŀ�꣬��ǰ·���Ͷ��ˡ�
echo "two path equals, success."

:: ���ʹ�� pymake cc ִ�У�Ŀ��Ϊ��%pymm get default exec root%���Ͷ��ˡ�