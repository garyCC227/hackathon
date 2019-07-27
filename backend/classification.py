#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:03:52 2019

@author: wenzhao
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Classifier():
    def __init__(self):
        self.model = self.train_model()

    def train_model(self):
        # preprocession
        dataset = pd.read_csv('result.csv')
        dataset = dataset.sort_values(by ='BodyType' )

        # split into three dataframes
        X = dataset.iloc[:, 1:].values
        y = dataset.iloc[:, 0].values
        # print (type(X))
        # print (X)

        # fid missing data for each df
        # from sklearn.preprocessing import Imputer
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(missing_values = np.nan, strategy= 'mean')
        # for 0
        imputer = imputer.fit(X[:,:])
        X = imputer.transform(X)

        # Fitting SVM to the Training set
        from sklearn.naive_bayes import GaussianNB
        classifier = GaussianNB()
        classifier.fit(X, y)
        return classifier



    def classify(self, data):
        # Predicting the Test set results
        y_pred = self.model.predict(data)
        # TODO
        print(y_pred)
        pass
        # Making the Confusion Matrix
        # from sklearn.metrics import confusion_matrix
        # cm = confusion_matrix(y_test, y_pred)
