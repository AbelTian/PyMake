# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import re
import sys
import uuid
import shutil
import time
import json
import copy
import types
from pycore.pycore import *
from pycore.pyenviron import *

def main_function():
    myenv = MyWin32Environ('user')
    print(1, myenv.search_key("windir"))
    print(2, myenv.search_key('bbb'))
    print(2.1, myenv.search_key('BBB'))
    print(3, myenv.search_key("path"))
    print(4, myenv.search_key("temp"))

    print(1, myenv.get_key("windir"))
    print(2, myenv.get_key('bbb'))
    print(3, myenv.get_key("path"))
    print(4, myenv.get_key("temp"))

    myenv.del_key('bbb')
    myenv.del_key('BBB')
    print(1111, myenv.get_key('bbb'))

    myenv.set_variable('bbb', 'T.D.R.')
    print(1, myenv.get_key('BBB'))
    myenv.set_variable('ccc', 'T.D.R.;BBB;ABC')
    print(2, myenv.get_key('ccc'))

    myenv.set_path('SitPath', "G:\\HELLO")
    print(1, myenv.get_key('SitPath'))
    print(1, myenv.get_key('SITPATH'))
    myenv.set_path('SITPATH', "G:\\HELLO;G:\\HELLO;B:\\BBBBBB;G:\\HELLO/BHUI\\BB;G:/HELLO")
    print(2, myenv.get_key('SITPATH'))
    myenv.del_path("SitPath", "G:\HELLO")
    myenv.del_path("SitPath", "G:/HELLO/BHUI/BB")
    print(3, myenv.get_key('SITPATH'))

    myenv.del_path("SitPath", "G:\\HELLO")
    print(3, myenv.get_key('SITPATH'))


    myenv.del_key("SITPATH")

    return

if __name__ == '__main__':
    main_function()
