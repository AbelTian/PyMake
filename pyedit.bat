@echo off

rem set PYPROGRAMPATH=%~dp0
rem set PYPROGRAMNAME=tools\pyedit\pyedit.py
rem set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%
rem start py "%PYPROGRAMPATHNAME%" %*

::set PYPROGRAMPATH=%~dp0
::set PYPROGRAMNAME=tools\pyedit\pyedit.py
::set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%
::call py "%PYPROGRAMPATHNAME%" %*

::set PYPROGRAMPATH=%~dp0
::set PYPROGRAMNAME=tools\pyedit\pyedit.exe
::set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%
::start "" "%PYPROGRAMPATHNAME%" %*

::set PYPROGRAMPATH=%~dp0
::set PYPROGRAMNAME=tools\pyedit\pyedit.exe
::set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%
::call "%PYPROGRAMPATHNAME%" %*

rem if "%1"=="h" goto begin
rem start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
rem :begin

set PYPROGRAMPATH=%~dp0
set PYPROGRAMNAME=tools\pyedit\pyedit.py
set PYPROGRAMPATHNAME=%PYPROGRAMPATH%%PYPROGRAMNAME%
set PYSTART=%~dp0\tools\pystart.vbs
"%PYSTART%" py %PYPROGRAMPATHNAME% %*
