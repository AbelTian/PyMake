import os
import sys
import codecs
import chardet

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
    with codecs.open(filePath, "r", encoding) as f:
        return f.read()

def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath,"wb") as f:
        f.write(u.encode(encoding, errors="ignore"))


def utf(path, recursive=False):
    print(path)
    if os.path.isfile(path):
        content = ""
        with open(path, 'r') as f:
            content = f.read()
        encoding = chardet.detect(content)['encoding']

        content = ""
        content = ReadFile(path, encoding)
        print(content)
        return
        newContent = codecs.decode(content, "unicode")
        WriteFile(path, newContent, "utf-8")

    else:
        for i in os.listdir(path):
            now_path = os.path.join(path, i)
            if os.path.isdir(now_path) and recursive:
                utf(now_path, recursive)
            elif os.path.splitext(i)[1] is '.cpp' or '.h':
                utf(now_path)


usage = """
        python pycodec.py haha.cpp #更改单文件
        python pycodec.py haha #更改文件夹下的全部文本文件(.cpp .h)
        python pycodec.py haha recursive #递归更改文件夹下的全部文本文件
        """

if __name__ == '__main__':
    # sys.argv = ['main', r'C:\Users\weidiao\Desktop\电子书', 'recursive']
    if len(sys.argv) == 1:
        print(usage)
        exit()
    if len(sys.argv) > 3:
        print(usage)
        print('too many argument')
        exit()
    path = sys.argv[1]
    if not os.path.exists(sys.argv[1]):
        print(usage)
        print('no this file or folder')
        exit()
    recursive = (len(sys.argv) == 3 and sys.argv[2] == 'recursive')
    utf(path, recursive)









def convert(file,in_enc="GBK",out_enc="UTF-8"):
    try:
        print ("convert " +file)
        f=codecs.open(file,'r',in_enc)
        new_content=f.read()
        codecs.open(file,'w',out_enc).write(new_content)
        #print (f.read())
    except IOError as err:
        print ("I/O error: {0}".format(err))


def explore(dir):
    for root,dirs,files in os.walk(dir):
        for file in files:
            path=os.path.join(root,file)
            convert(path)

def main():
    for path in sys.argv[1:]:
        if(os.path.isfile(path)):
            convert(path)
        elif os.path.isdir(path):
                explore(path)

if __name__=="__main__":
    main()
