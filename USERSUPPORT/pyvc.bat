@echo off

::pyvc 的使用条件：
::在 <source-root>/<source-file>.json，即 $(mm source root) 里面添加，
::在每个使用 MSVC 的 ENV 里必须加入一个环境变量，"run-vcvarsall"="${vcvarsall-201x} amd64 ..."，${vcvarsall-201x} 路径集合保存到 path-assemblage。
::只有这样，pyvc.bat 才能执行有效。

::使用 pyenv.bat 开关环境
call pyenv.bat %*

::来自pyenv.bat
if %PYENVFLAG% == 0 (
    ::这里说一下，vcvarsall.bat 是一种更换环境后全覆盖式的，没有清理。
    ::call "%cls-vcvarsall%"
    echo user env : [%PYENVNAME%] closed，but you should use new env overlap it.
) else (
    ::这个环境变量已经被使用者设置进入确定的ENV，随时跟着ENV改变。
    call "%run-vcvarsall%"
    echo user env : [%PYENVNAME%] opened, sure.
)
