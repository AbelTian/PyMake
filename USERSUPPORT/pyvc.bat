@echo off

:: ��<source-root>/<source-file>.json����$(mm source)�ļ�������ӣ�
:: ��ÿ��ʹ��MSVC��ENV��������������������������
:: "VCVARSALL"="${vcvarsall-201x}"��${vcvarsall-201x} ·�������浽 path-assemblage��  
:: "VCVARSALLPARAM"="amd64_x86"�����������������ENV��Ŀ�������    
:: ֻ��������pyvc.bat ����ִ����Ч��  

:: bat�������������ִ�Сд��
:: ��������"RUN-VCVARSALL"="${VCVARSALL} ${VCVARSALLPARAM}"��
:: �û����о�������"CLS-VCVARSALL"��"CLS-VCVARSALLPARAM"��

set PYFILEPATH=%~dp0
call %PYFILEPATH%\pyenv.bat %*

if %PYENVFLAG% == 0 (
    echo pyvc env : CLS-VCVARSALL="%CLS-VCVARSALL:/=\%"
    call "%CLS-VCVARSALL:/=\%" %CLS-VCVARSALLPARAM%
    echo pyvc env : [%PYENVNAME%] closed, but you should use new vcvarsall overlap it.
) else (
    echo pyvc env : VCVARSALL="%VCVARSALL:/=\%" "%VCVARSALLPARAM%"
    call "%VCVARSALL:/=\%" %VCVARSALLPARAM%
    echo pyvc env : [%PYENVNAME%] opened, sure.
)
