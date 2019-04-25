
cd QQtTool/multi-link & git co master & git pull
cd ../..

mkdir tempdir
call xcopy /s /q /y /i /r /h QQtTool\multi-link tempdir\multi-link
call rd /s /q tempdir\multi-link\.git

set mldir=QQtTool\project\QQtApplicationCreator\AppRoot\template\QQtTemplateApplication\multi-link
call rd /s /q %mldir%
ping 127.0.0.1 -n 1 >nul 2>nul
mkdir %mldir%
call xcopy /s /q /y /i /r /h tempdir\multi-link %mldir%

set mldir=QQtTool\project\QQtApplicationCreator-Multipel\AppRoot\template\QQtTemplateApplication\multi-link
call rd /s /q %mldir%
ping 127.0.0.1 -n 1 >nul 2>nul
mkdir %mldir%
call xcopy /s /q /y /i /r /h tempdir\multi-link %mldir%

set mldir=QQtTool\project\QQtLibraryCreator\AppRoot\template\QQtTemplateLibrary\multi-link
call rd /s /q %mldir%
ping 127.0.0.1 -n 1 >nul 2>nul
mkdir %mldir%
call xcopy /s /q /y /i /r /h tempdir\multi-link %mldir%

set mldir=QQtTool\project\QQtLibraryCreator-Multipel\AppRoot\template\QQtTemplateLibrary\multi-link
call rd /s /q %mldir%
ping 127.0.0.1 -n 1 >nul 2>nul
mkdir %mldir%
call xcopy /s /q /y /i /r /h tempdir\multi-link %mldir%

call rd /s /q tempdir
