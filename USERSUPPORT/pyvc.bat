@echo off

:: 在<source-root>/<source-file>.json，即$(mm source)文件里面添加，
:: 在每个使用MSVC的ENV配置里必须加入两个环境变量，
:: "VCVARSALL"="${vcvarsall-201x}"，${vcvarsall-201x} 路径集保存到 path-assemblage。  
:: "VCVARSALLPARAM"="amd64_x86"，这个环境变量根据ENV的目标决定。    
:: 只有这样，pyvc.bat 才能执行有效。  

:: bat环境变量不区分大小写。
:: 建议增加"RUN-VCVARSALL"="${VCVARSALL} ${VCVARSALLPARAM}"。
:: 用户自行决定配置"CLS-VCVARSALL"和"CLS-VCVARSALLPARAM"。

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
