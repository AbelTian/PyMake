# BuildConfig
用Multi-environ Manager进行环境配置，我使用的.json配置文件和编译脚本。
编译脚本可以写在任何位置，已经得到了大大的简化。

使用Multi-environ Manager，可以随时更换Path+和Environment Variable环境，
执行命令之后还能够及时的清理干净环境，甚至可以在某个环境下执行命令而不影响环境。

.json就是配置不同环境的配置文件。  
Multi-environ Manager就是操作这些个配置文件的工具，
这个工具的工作目录会一直停留在sourceroot文件夹里，（当然执行命令中的切换目录还是会切换的）。  
在Shell中使用时这样的：
```bash
#pymake6.py
#env effect
mm export 'android.x86' envname
source $(mm source root)/envname_effect.sh
#do command in this env
java -version
#env reset (need)
source $(mm source root)/envname_unset.sh
```
或者
```bash
#env effect
mm set cur env 'qt.android'
#do command in this env
mm cc qqt.build
#env reset (no need)
```
shell文件可以编写在任意位置，更换环境的命令得到极大简化，
这样执行复杂命令再也不用为了每次都要更改复杂的环境而难过、头疼了。

pymake7.py
用户可以使用我提供的pyccvp pyvcccvp执行命令。
并且增加type2 export2命令，用户可以做很多自定义工作。
添加自定义环境，作为公共环境。
