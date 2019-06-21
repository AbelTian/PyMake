@echo off

set command=pymake
echo %command%
call %command%

set command=pymake get all
echo %command%
call %command%

set command=pymake get all info
echo %command%
call %command%

set command=pymake get all information
echo %command%
call %command%

set command=pymake get all settings
echo %command%
call %command%

set command=pymake get all settings path
echo %command%
call %command%

set command=pymake get all settings env
echo %command%
call %command%

set command=pymake get all settings cmd
echo %command%
call %command%

set command=pymake get all settings -r
echo %command%
call %command%

set command=pymake get all settings -a
echo %command%
call %command%

set command=pymake get exec root default
echo %command%
call %command%

set command=pymake get exec root here
echo %command%
call %command%

set command=pymake get current env
echo %command%
call %command%

set command=pymake get default env
echo %command%
call %command%

set command=pymake get cur env
echo %command%
call %command%

set command=pymake get env
echo %command%
call %command%

set command=pymake cmd
echo %command%
call %command%

set command=pymake see
echo %command%
call %command%

set command=pymake clean
echo %command%
call %command%

set command=pymake program
echo %command%
call %command%

set command=pymake program root
echo %command%
call %command%

set command=pymake program file
echo %command%
call %command%

set command=pymake program configure
echo %command%
call %command%

set command=pymake program configure file
echo %command%
call %command%

set command=pymake program configure root
echo %command%
call %command%

set command=pymake source
echo %command%
call %command%

set command=pymake source file
echo %command%
call %command%

set command=pymake source root
echo %command%
call %command%

set command=pymake source config
echo %command%
call %command%

set command=pymake list
echo %command%
call %command%

set command=pymake list path
echo %command%
call %command%

set command=pymake list path -r
echo %command%
call %command%

set command=pymake list env
echo %command%
call %command%

set command=pymake list env -r
echo %command%
call %command%

set command=pymake list var
echo %command%
call %command%

set command=pymake list var -r
echo %command%
call %command%

set command=pymake env
echo %command%
call %command%

set command=pymake env current -r
echo %command%
call %command%

set command=pymake env current -r -p
echo %command%
call %command%

set command=pymake env current -r -v
echo %command%
call %command%

set command=pymake env current -r -a
echo %command%
call %command%

set command=pymake export
echo %command%
call %command%

set command=pymake type
echo %command%
call %command%

set command=pymake port
echo %command%
call %command%

set command=pymake port root
echo %command%
call %command%

set command=pymake port file
echo %command%
call %command%

set command=pymake port config
echo %command%
call %command%

set command=pymake translate
echo %command%
call %command%

set command=pymake translate path
echo %command%
call %command%

set command=pymake translate env
echo %command%
call %command%

set command=pymake translate cmd
echo %command%
call %command%

set command=pymake translate path-env-cmd
echo %command%
call %command%

set command=pymake translate all
echo %command%
call %command%

set command=pymake translate section
echo %command%
call %command%

for /F %%i in ('"pymake get default exec root"') do ( set "WORKROOT=%%i" )
set WORKROOT=%WORKROOT:/=\\%
md %WORKROOT%

set command=pymake cc dir
echo %command%
call %command%

set command=pymake exec dir
echo %command%
call %command%

set command=pymake exec here dir
echo %command%
call %command%

set command=pymake ccvp dir
echo %command%
call %command%

set command=pymake execvp dir
echo %command%
call %command%

set command=pymake ccvp dir %WORKROOT%
echo %command%
call %command%

set command=pymake execvp dir %WORKROOT%
echo %command%
call %command%

set command=pymake execvp here dir %WORKROOT%
echo %command%
call %command%

set command=pymake exec-with-params dir
echo %command%
call %command%

set command=pymake exec-with-params dir --workroot %WORKROOT%
echo %command%
call %command%

set command=pymake exec-with-params dir --params %WORKROOT%
echo %command%
call %command%

set command=pymake exec-with-params here dir
echo %command%
call %command%

set command=pymake ccvp "test.8 blank" 你好啊 “中国” "你好 中国"
echo %command%
call %command%
