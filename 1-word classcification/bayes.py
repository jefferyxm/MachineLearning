# -*- coding: utf-8 -*-
import sys
import os
from sklearn.naive_bayes import MultinomialNB
import cPickle as pickle

reload(sys)
sys.setdefaultencoding('utf-8')


def readfile(filepath):
    fp = open(filepath, "rb")
    content = fp.read()
    fp.close()
    return content


def readbunchobj(path):
    file_obj = open(path,"rb")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch


def writebunchobj(path, bunch_obj):
    file_obj = open(path, "wb")
    pickle.dump(bunch_obj, file_obj)
    file_obj.close()


trainpath = "wordbag/tfidfspace.dat"
trainset = readbunchobj(trainpath)

testpath = "wordbag/testspace.dat"
testset = readbunchobj(testpath)

clf = MultinomialNB(alpha=0.001).fit(trainset.tdm, trainset.label)

predicted = clf.predict(testset.tdm)
total = len(predicted)
rate = 0
for flabel,filename, expectlabel in zip(testset.label,testset.filename,predicted):
    print flabel, expectlabel
    if flabel != expectlabel:
        rate += 1
        print "act: ", flabel, "  ", " predict:", expectlabel

print "mistake rate: ", float(rate)*100/float(total), "%"