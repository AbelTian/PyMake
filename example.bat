::!bat cmd
::create mm link
::sudo ln -s xxx/pymake6.sh /usr/local/bin/mm

::env effect
call mm set env cur qt.android
call mm export
for /f "" %%a in ('mm source root') do call %%a\env_effect.bat
::do command in this env


::env reset (need)
for /f "" %%a in ('mm source root') do call %%a\env_unset.bat


