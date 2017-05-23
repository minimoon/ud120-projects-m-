#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

xt = features_train
yt = labels_train
xs = features_test
ys = labels_test

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(xt, yt)

pred = clf.predict(xs)

from sklearn.metrics import accuracy_score
score = accuracy_score(pred,ys)
print score
#########################################################
'''
no. of Chris training emails: 7936
no. of Sara training emails: 7884
0.973265073948
'''

