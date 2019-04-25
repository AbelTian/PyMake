@echo off

:: 测试执行 test
:: test
:: echo %CD%

call pymake source file "%CD%\..\example\pymake7-win-tai.json"
call pycmd test

echo "current path: %CD%"

:: 目标，当前路径就对了。
if "" == "" (
    echo "Successed"
) else (
    echo "Failed"
)

:: 如果使用 pymake cc 执行，目标为，%pymm get default exec root%，就对了。