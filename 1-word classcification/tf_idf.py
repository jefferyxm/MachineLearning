# -*- coding: utf-8 -*-
import sys
import os
from sklearn.datasets.base import Bunch
import cPickle as pickle
from sklearn import feature_extraction
from  sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

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


#stop words
stopwordpath = "data/stop words/stop word.txt"
swlst = readfile(stopwordpath).splitlines()

path = "wordbag/wordbag.dat"
bunch = readbunchobj(path)

# create tf-idf vector space
tfidfspace = Bunch(target_name=bunch.target_name,
                   label=bunch.label,
                   filename=bunch.filename,
                   tdm=[],
                   vocabulary={})


vectorizer = TfidfVectorizer(stop_words=swlst, sublinear_tf=True, max_df=0.5)
transformer = TfidfTransformer()

tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary = vectorizer.vocabulary_

space_path = "wordbag/tfidfspace.dat"
writebunchobj(space_path, tfidfspace)