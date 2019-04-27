@echo off

::env effect (need)
call mm set cur env "android.mobile"
::do command in this env
call mm exec qqt.build
::env reset (no need)



::env effect
call mm set current env "android.x86"
::do command in this env
call mm exec qqt.build
::env reset (no need)



::env effect
call mm set cur env qt5.x64
::do command in this env
call mm exec qqt.build
::env reset (no need)


::env effect
call mm set cur env qt5
::do command in this env
call mm exec qqt.build
::env reset (no need)

exit /b 0

call :env_effect qt5.x64
::do command in this env
:: error 这个函数的作用在于设置当前环境变量，这里的命令应当是调用本地函数，而不是调用mm。
call mm exec qqt.build 
call :env_reset

:exit
exit /b 0


:env_effect
::env effect
call mm export %1 to env
for /f "" %%a in ('mm get default exec root') do call %%a\env_effect.bat
goto :eof

:env_reset
::env reset (need)
for /f "" %%a in ('mm get default exec root') do call %%a\env_unset.bat
goto :eof