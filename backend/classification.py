#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:03:52 2019

@author: wenzhao
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Classifier():
    def __init__(self):
        # preprocession
        dataset = pd.read_csv('backend/result.csv')
        dataset = dataset.sort_values(by ='BodyType' )

        # split into three dataframes
        X = dataset.iloc[:, 1:].values
        y = dataset.iloc[:, 0].values

        # fid missing data for each df
        # from sklearn.preprocessing import Imputer

        imputer = SimpleImputer(missing_values = np.nan, strategy= 'mean')
        imputer = imputer.fit(X[:,:])
        X = imputer.transform(X)

        self.classifier = RandomForestClassifier(n_estimators = 3, criterion = 'entropy', random_state = 0)
        # Fitting SVM to the Training set
        # self.classifier = GaussianNB()
        self.classifier.fit(X, y)


    def predict(self, data):
        # Predicting the Test set results
        y_pred = self.classifier.predict(data.reshape(1, 11))
        print(y_pred)
        pass

    # def recommend(self, data):

