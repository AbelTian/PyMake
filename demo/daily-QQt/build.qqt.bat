@echo off

::env effect
call mm set cur env "qt.android"
::do command in this env
call mm exec qqt.build
::env reset (no need)



::env effect
call mm set cur env "android.x86"
::do command in this env
call mm exec qqt.build
::env reset (no need)



::env effect
call mm set cur env android.mobile
::do command in this env
call mm exec qqt.build
::env reset (no need)




call :env_effect qt.android
::do command in this env
call java -version
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