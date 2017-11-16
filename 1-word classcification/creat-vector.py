from sklearn.datasets.base import Bunch
import os
import pickle


def savefile(savepath, content):
    fp = open(savepath, "wb")
    fp.write(content)
    fp.close()


def readfile(filepath):
    fp = open(filepath, "rb")
    content = fp.read()
    fp.close()
    return content


bunch = Bunch(target_name=[], label=[], filename=[], contents=[])


# transfrom to bunch
wordbag_path = "wordbag/test_wordbag.dat"
seg_path = "result_test/"

catelist = os.listdir(seg_path)
bunch.target_name.extend(catelist)      # target name
for mydir in catelist:
    class_path = seg_path + mydir + "/"
    file_list = os.listdir(class_path)
    for filename in file_list:
        full_path = class_path + filename
        bunch.label.append(mydir)        # class label
        bunch.filename.append(filename)  # file name
        bunch.contents.append(readfile(full_path).strip())  # contents

file_obj = open(wordbag_path, "wb")
pickle.dump(bunch, file_obj)
file_obj.close()