# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""PyCodec 1.0.

Usage:
  pycodec.py <file>
  pycodec.py <path> --path
  pycodec.py <path> --recursive
  pycodec.py -h | --help
  pycodec.py --version

Params:
    <file>              #更改单文件
    <path> --path       #更改文件夹下的全部文本文件(.cpp .h)
    <path> --recursive  #递归更改文件夹下的全部文本文件

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import os
import sys
import codecs

#try:
#    from fake_useragent import UserAgent
#except ModuleNotFoundError as e:
#    print("要先安装包!!! pip install fake-useragent")
#    import os
#    p = os.popen("pip install fake-useragent")
#    print(p.read())
#    from fake_useragent import UserAgent
#finally:
#    agent = UserAgent()


#def install_package(package_name):
#    package_name = package_name.replace("_", "-")  # 下载pip fake_useragent 包时  包名是:fake-useragent
#    p = os.popen("pip list --format=columns")  # 获取所有包名 直接用 pip list 也可获取
#    pip_list = p.read()  # 读取所有内容
#    print(pip_list)
#    if package_name in pip_list:
#        print("已经安装{}".format(package_name))
#        return True
#    else:
#        print("没有安装{}!即将自动安装,请稍后".format(package_name))
#        p = os.popen("pip install {}".format(package_name))
#        if "Success" in p.read():
#            print("安装{}成功!".format(package_name))
#            return True if "Success" in p.read() else False

# 调用执行检测 如果没安装 则自动安装
#install_package('fake_useragent')
#from fake_useragent import UserAgent

try:
    import chardet
except ModuleNotFoundError as e:
    print("要先安装包!!! 请进入python安装目录，执行一下代码。")
    print("pip install chardet")
    os._exit(1)
finally:
    ''

from pycore.pycore import *

#detect codec
#read decode
#encode write
#maybe remove temp file

#file
#iconv

#charset
#codecs
#chardet

def ReadFile(filePath, encoding="utf-8"):
    with codecs.open(filePath, "rb", encoding) as f:
        return f.read()

def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath,"wb") as f:
        f.write(u.encode(encoding, errors="ignore"))


def utf(path, recursive=False):
    #print(path, os.path.isfile(path))
    if os.path.isfile(path) is True:

        content = ""
        with open(path, 'rb') as f:
            content = f.read()
        encodeName = chardet.detect(content)["encoding"]

        content = ""
        content = ReadFile(path, encodeName)
        b1 = bytes(content, encoding=encodeName)
        newContent = codecs.decode(b1, encodeName)

        newEncodeName = "utf-8"
        WriteFile(path, newContent, newEncodeName)

        print(path, encodeName, newEncodeName)

    else:
        for i in os.listdir(path):
            now_path = os.path.join(path, i)
            #print(path, now_path, os.path.splitext(i)[1], os.path.isdir(now_path) )
            if os.path.isdir(now_path) and recursive is True:
                utf(now_path, recursive)
            elif os.path.splitext(i)[1] == ".cpp" \
                    or os.path.splitext(i)[1] == ".bat"\
                    or os.path.splitext(i)[1] == ".sh"\
                    or os.path.splitext(i)[1] == ".cc"\
                    or os.path.splitext(i)[1] == ".hh"\
                    or os.path.splitext(i)[1] == ".sh"\
                    or os.path.splitext(i)[1] == ".c"\
                    or os.path.splitext(i)[1] == ".ui"\
                    or os.path.splitext(i)[1] == ".qrc"\
                    or os.path.splitext(i)[1] == ".rc"\
                    or os.path.splitext(i)[1] == ".in"\
                    or os.path.splitext(i)[1] == ".h"\
                    or os.path.splitext(i)[1] == ".pro"\
                    or os.path.splitext(i)[1] == ".pri"\
                    or os.path.splitext(i)[1] == ".c"\
                    or os.path.splitext(i)[1] == ".ui":
                #print ("inside", now_path)
                utf(now_path)
            else:
                continue;
                #print ("excide", now_path)



def main_function():

    args = docopt(__doc__, version='pycodec.py v1.0')
    #print(args)

    pycodecworkpath = os.getcwd()

    while(True):
        if(args['<file>'] is not None):
            if ( not os.path.exists(args['<file>']) ):
                print("please ensure the file is existed.")
                return

            if ( not os.path.isfile(args['<file>']) ):
                print("please ensure the file is really a file.")
                return

            utf(args['<file>'], False)
            return

        if(args['<path>'] is not None):
            if ( not os.path.exists(args['<path>']) ):
                print("please ensure the path is existed.")
                return

            if ( not os.path.isdir(args['<path>']) ):
                print("please ensure the path is really a path.")
                return

            recursive = False
            if(args['--recursive'] is True):
                recursive = True

            utf(args['<path>'], recursive)
            return

        break

    return

if __name__ == '__main__':
    main_function()
