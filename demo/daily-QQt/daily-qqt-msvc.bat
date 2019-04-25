@echo off

::env effect
call mm set cur env "qt5"
::do command in this env
call mm exec build.qqt
::env reset (no need)



::env effect
call mm set current env "qt5.x64"
::do command in this env
call mm exec build.qqt
::env reset (no need)



::env effect
call mm set cur env qt5.winrt
::do command in this env
call mm exec build.qqt
::env reset (no need)


::env effect
call mm set cur env qt5.winrt.simulator
::do command in this env
call mm exec build.qqt
::env reset (no need)

call mm set cur env "qt5"

exit /b 0

:: 这个调用函数的过程，环境变量没有设置到当前环境，不知道什么原因？事实上设置到了。
:: 当然不会设置到MM！
call :env_effect qt5.x64
::do command in this env
:: error 这个函数的作用在于设置当前环境变量，这里的命令应当是调用本地函数，而不是调用mm。
call mm exec build.qqt
call :env_reset

:exit
exit /b 0


:env_effect
::env effect
call mm export %1 to env
for /f "" %%a in ('mm source root') do call %%a\env_effect.bat
goto :eof

:env_reset
::env reset (need)
for /f "" %%a in ('mm source root') do call %%a\env_unset.bat
goto :eof