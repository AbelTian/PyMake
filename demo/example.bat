@echo off
::env effect (shared)
call mm set cur env qt.android
::do command in this env
call mm exec "java -version"
::env reset (no need)




::env effect (private)
call mm export android.mobile sscc
for /f "" %%a in ('mm source root') do call %%a\sscc_effect.bat
::do command in this env
::env reset (need)
for /f "" %%a in ('mm source root') do call %%a\sscc_unset.bat






call :env_effect android.x86 x86
::do command in this env
call :env_unset x86







:exit
exit /b 0

:env_effect
::env effect
call mm export %1 %2
for /f "" %%a in ('mm source root') do call %%a\%2_effect.bat
goto :eof

:env_reset
::env reset (need)
for /f "" %%a in ('mm source root') do call %%a\%1_unset.bat
goto :eof