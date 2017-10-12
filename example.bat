::!bat cmd
::create mm link
::c:\windows\mm.bat
::@echo off
::call xxx\pymake.bat %*

::env effect
call mm set env cur qt.android
call mm export
for /f "" %%a in ('mm source root') do call %%a\env_effect.bat
::do command in this env


::env reset (need)
for /f "" %%a in ('mm source root') do call %%a\env_unset.bat


