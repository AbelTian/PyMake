@echo off

call :env_effect qt5
call :build_exquisite
call :env_reset

call :env_effect qt5.x64
call :build_exquisite
call :env_reset

call :env_effect android.mobile
call :build_exquisite
call :env_reset

call :env_effect android.x86
call :build_exquisite
call :env_reset

::只有这一句导致主路径退出。
exit /b 0



:: FUNCTION
:build_exquisite
set src_path=R:/Develop/a0-develop
set build_path=V:/Develop/c0-buildstation
set src=%src_path%/QQtExquisite/QQtExquisite.pro
set build=%build_path%/QQtExquisite/%QSYS%/%QTVERSION%/Debug
echo build %src% 
echo in %build%
::goto :eof
md %build:/=\\%
cd /d %build%
rem del /f /q /s demo examples src test
qmake %src% %QTSPEC% CONFIG+=debug CONFIG+=qml_debug %QTCONFIG% && mingw32-make qmake_all
mingw32-make -j10
goto :eof


:: FUNCTION 不会导致主路径退出。
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