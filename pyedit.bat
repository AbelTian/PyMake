@echo off

rem set PYPROGRAMPATH=%~dp0
rem set PYPROGRAMNAME=tools\pyedit\pyedit.py
rem set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%
rem call py "%PYPROGRAMPATHNAME%" %*

set PYPROGRAMPATH=%~dp0
set PYPROGRAMNAME=tools\pyedit\pyedit.exe
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%

start "" "%PYPROGRAMPATHNAME%" %*
