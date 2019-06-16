# ENCODING LIST    

|PROGRAM|READ|WRITE|PLATFORM|FILE TYPE|
|----|----|----|-----|------|
|pymake| utf8 | utf8 | N/A | .json |
|pymake| utf8 | utf8 | unix / linux | .ini |
|pymake| utf8 | utf8 | unix / linux | .sh  |
|pymake| utf8 | utf8 | N/A | .py |
|pymake| ansi | ansi | windows 7/8/10 | .ini |
|pymake| ansi | ansi | windows 7/8/10 |.bat .ps1 |

Windows XP: YES
1. python 3.4.4
2. .bat path, no accept blank.
3. encoding = None.
4. import and outport command maybe error decoding and encoding.

MSYS: YES
1. $USERPROFILE != $HOMEDRIVE$HOMEPATH
2. no sudo ? dont call install.bat and install.sh.
3. call cmd first is suggessted.

MSYS2: YES  
1. equals to MSYS.
2. not support chinese.  

