@echo off
SETLOCAL ENABLEDELAYEDEXPANSION


set module_name=QQtTool
call :env_open qt5 %module_name%
call :build_module
call :env_close %module_name%

::只有这一句导致主路径退出。
exit /b 0

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: FUNCTION
:build_module
set src_path=R:/Develop/a0-develop
set build_path=V:/Develop/c0-buildstation
set src=%src_path%/%module_name%/%module_name%.pro
set build=%build_path%/%module_name%/%QSYS%/%QTVERSION%/Debug
echo build %src% 
echo in %build%
rem goto :eof
md %build:/=\\%
cd /d %build%
rem del /f /q /s demo examples src test
qmake %src% %QTSPEC% CONFIG+=debug CONFIG+=qml_debug %QTCONFIG% && mingw32-make qmake_all
mingw32-make -j10
goto :eof

:: FUNCTION 不会导致主路径退出。
:exit
exit /b 0

:env_open
::env effect
call mm export %1 %2
for /f "" %%a in ('mm source root') do call %%a\%2_effect.bat
goto :eof

:env_effect
::env effect
call mm export %1 %2
for /f "" %%a in ('mm source root') do call %%a\%2_effect.bat
goto :eof

:env_reset
::env reset (need)
for /f "" %%a in ('mm source root') do call %%a\%1_unset.bat
goto :eof

:env_unset
::env unset (need)
for /f "" %%a in ('mm source root') do call %%a\%1_unset.bat
goto :eof

:env_clean
::env unset (need)
for /f "" %%a in ('mm source root') do call %%a\%1_unset.bat
goto :eof

:env_close
::env unset (need)
for /f "" %%a in ('mm source root') do call %%a\%1_unset.bat
goto :eof