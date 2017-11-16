# -*- coding: utf-8 -*-
import sys
import os
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

# test 1
# seg_list = jieba.cut("小明1995年毕业于清华大学", cut_all=False)
# print "Default mode:", " ".join(seg_list)


# test 2 jieba from txt
def savefile(savepath, content):
    fp = open(savepath, "wb")
    fp.write(content)
    fp.close()


def readfile(filepath):
    fp = open(filepath, "rb")
    content = fp.read()
    fp.close()
    return content


corpus_path = "data/train/"
result_path = "result/"

catelist = os.listdir(corpus_path)

for mydir in catelist:
    class_path = corpus_path + mydir + "/"
    seg_dir = result_path + mydir + "/"
    if not os.path.exists(seg_dir):
        os.makedirs(seg_dir)
    file_list = os.listdir(class_path)
    for filename in file_list:
        full_path = class_path + filename
        content = readfile(full_path).strip()
        content = content.replace("\r\n", "").strip()
        content_seg = jieba.cut(content)
        savefile(seg_dir + filename, " ".join(content_seg))

print "finish!"
