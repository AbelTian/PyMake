@echo off

set command=pyenv current
echo %command%
call %command%


set command=pycmd dir
echo %command%
call %command%


set command=pyccvp dir C:\
echo %command%
call %command%

