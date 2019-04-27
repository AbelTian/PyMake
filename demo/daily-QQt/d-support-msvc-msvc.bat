@echo off
SETLOCAL ENABLEDELAYEDEXPANSION


set module_name_dir=QQtSupport
set module_name=QQtSupportMSVC
call :env_open qt5 %module_name%
call :build_module
call :env_close %module_name%

call :env_open qt5.x64 %module_name%
rem call :build_module
call :env_close %module_name%

call :env_open qt5.winrt %module_name%
rem call :build_module
call :env_close %module_name%

call :env_open qt5.winrt.simulator %module_name%
rem call :build_module
call :env_close %module_name%

::只有这一句导致主路径退出。
exit /b 0

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: FUNCTION
:build_module
call %run-vcvarsall%
set src_path=C:/Users/Administrator/Develop/a0-develop
set build_path=D:/Develop/c0-buildstation
set src=%src_path%/%module_name_dir%/%module_name%.pro
set build=%build_path%/%module_name%/%QSYS%/%QTVERSION%/Debug
echo build %src% 
echo in %build%
rem goto :eof
md %build:/=\\%
cd /d %build%
rem del /f /q /s demo examples src test
call qmake %src% %QTSPEC% CONFIG+=debug CONFIG+=qml_debug %QTCONFIG% && %MSMAKE% qmake_all
call %MSMAKE%
goto :eof

:: FUNCTION 不会导致主路径退出。
:exit
exit /b 0

:env_open
::env effect
call mm export %1 %2
for /f "" %%a in ('mm get default exec root') do call %%a\%2_effect.bat
goto :eof

:env_effect
::env effect
call mm export %1 %2
for /f "" %%a in ('mm get default exec root') do call %%a\%2_effect.bat
goto :eof

:env_reset
::env reset (need)
for /f "" %%a in ('mm get default exec root') do call %%a\%1_unset.bat
goto :eof

:env_unset
::env unset (need)
for /f "" %%a in ('mm get default exec root') do call %%a\%1_unset.bat
goto :eof

:env_clean
::env unset (need)
for /f "" %%a in ('mm get default exec root') do call %%a\%1_unset.bat
goto :eof

:env_close
::env unset (need)
for /f "" %%a in ('mm get default exec root') do call %%a\%1_unset.bat
goto :eof