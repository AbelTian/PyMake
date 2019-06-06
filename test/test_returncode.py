# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import re
import sys
import uuid
import shutil
import time
import datetime
import json
import copy
import types

def main_function():
    print("BBB")
    print(__file__)
    print(os.getcwd())
    print(len(sys.argv))
    print(sys.argv)
    for path0 in sys.argv:
        print ("PARAMS:", path0)
    print ("exit code = 6")
    exit(6)
    return

if __name__ == '__main__':
    main_function()
