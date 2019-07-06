# Notice  

#### VC Command  

1. If you installed VC6, please check system environment, VC6 will add INCLUDE/LIB/LIBPATH to system environment, it has positive effects to pymake vc command.  
    - pymake vc command will make added env var and path to effect exec env.  


#### replace character

```bash   
# ${xxx}/%XXXX%/$XXXX
# In .json env file, ${} is the substitute character.%XXXX% is win bat env s.c., $XXXX is unix's.  

```

#### type2/export2 default behavior  

1. It will follow platform default script file. On windows, it is .bat, on UNIX, it is .sh.  

#### check is a good command  

1. When you configed .json file, it will help you check whether it is configed right.  

#### port/translate  

1. You can use them to translate with other's env confidently and handy.  

#### source/set/list[env]/ccvp

1. They are one group commands.  

#### debug command   

1. If you want to know what ccvp has done, pymake debug open can help you.

