@echo off

echo %CD%

:: cloc ����·��
set filepath=%~dp0
perl %filepath%/cloc-1.74.pl .

:: date
DATE /T
