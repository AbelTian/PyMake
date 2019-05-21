# ENCODING LIST    

|PROGRAM|READ|WRITE|PLATFORM|FILE TYPE|
|----|----|----|-----|------|
|pymake| utf8 | utf8 | N/A | .json |
|pymake| utf8 | utf8 | unix / linux | .ini |
|pymake| utf8 | utf8 | unix / linux | .sh  |
|pymake| utf8 | utf8 | N/A | .py |
|pymake| ansi | ansi | windows 7/8/10 | .ini |
|pymake| ansi | ansi | windows 7/8/10 |.bat .ps1 |

Windows XP: NO
1. python 3.4.4
2. .bat path, no accept blank.
3. encoding = None, but I use encoding = ansi on windows.

MSYS: NO
1. $USERPROFILE != $HOMEDRIVE$HOMEPATH
2. no sudo ?
3. access cmd is OK, but default path is wrong.
