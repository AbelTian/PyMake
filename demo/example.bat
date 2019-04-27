@echo off
::env effect (no need)
::call mm set cur env qt.android
::do command in this env
call mm exec "java -version"
::env reset (no need)




::env effect (private, need)
call mm export android.mobile sscc
for /f "" %%a in ('mm get default exec root') do call %%a\sscc_effect.bat
::do command in this env
::env reset (need)
for /f "" %%a in ('mm get default exec root') do call %%a\sscc_unset.bat






call :env_effect android.x86 x86
::do command in this env
qmake -v

call :env_unset x86



:: pyenv
:: open env (need)
call pyenv open qt5
:: do command here
qmake -v
:: close env (need)
call pyenv close qt5


:: use pycmd (auto open) [android.x86, current, qt5, [empty]]
call pycmd test qt5
:: close env (need)
call pyenv close qt5



:exit
exit /b 0

:env_effect
::env effect
call mm export %1 %2
for /f "" %%a in ('mm get default exec root') do call %%a\%2_effect.bat
goto :eof

:env_reset
::env reset (need)
for /f "" %%a in ('mm get default exec root') do call %%a\%1_unset.bat
goto :eof