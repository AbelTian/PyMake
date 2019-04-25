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

:: ������ú����Ĺ��̣���������û�����õ���ǰ��������֪��ʲôԭ����ʵ�����õ��ˡ�
:: ��Ȼ�������õ�MM��
call :env_effect qt5.x64
::do command in this env
:: error ��������������������õ�ǰ�������������������Ӧ���ǵ��ñ��غ����������ǵ���mm��
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