@echo off

echo %CD%

:: cloc ËùÔÚÂ·¾¶
set filepath=%~dp0
perl %filepath%/cloc-1.74.pl .

:: date
DATE /T
