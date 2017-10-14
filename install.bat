@echo off
set filepath=%~dp0
set mmfile=C:\Windows\mm.bat
echo @echo off > mmfile
echo call "%filepath%pymake.bat" %* >> mmfile

