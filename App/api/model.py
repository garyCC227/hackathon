#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:03:52 2019

@author: wenzhao
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# preprocession
dataset = pd.read_csv('result4.csv')
dataset = dataset.sort_values(by ='BodyType' )

# split into three dataframes
X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

# fid missing data for each df
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy= 'mean', axis= 0)
# for 0
imputer = imputer.fit(X[:,:])
X = imputer.transform(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Fitting SVM to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)