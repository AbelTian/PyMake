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

