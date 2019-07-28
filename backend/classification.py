#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:03:52 2019

@author: wenzhao
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition, datasets


class Classifier():
    def __init__(self):
        # preprocession
        dataset = pd.read_csv('result.csv')
        dataset = dataset.sort_values(by ='BodyType' )

        # split into three dataframes
        self.X = dataset.iloc[:, 1:].values
        self.y = dataset.iloc[:, 0].values

        X = np.array(self.X)
        y = np.array(self.y)
        # fid missing data for each df
        # from sklearn.preprocessing import Imputer

        imputer = SimpleImputer(missing_values = np.nan, strategy= 'mean')
        imputer = imputer.fit(X[:,:])
        X = imputer.transform(X)

        self.classifier = RandomForestClassifier(n_estimators = 3, criterion = 'entropy', random_state = 0)
        # Fitting SVM to the Training set
        # self.classifier = GaussianNB()
        self.classifier.fit(X, y)

    def getPlot(self, data):
        dataset = pd.read_csv('backend/plotData.csv')
        dataset = dataset.sort_values(by ='BodyType' )

        # split into three dataframes
        X = dataset.iloc[:, 1:].values
        y = dataset.iloc[:, 0].values

        X = X.tolist()
        X.append(data)
        X = np.array(X)

        y = y.tolist()
        y.append(3)
        y = np.array(y)


        fig = plt.figure(figsize=(15, 8))
        ax = Axes3D(fig, rect=[0, 0, .7, 1], elev=48, azim=134)

        pca = decomposition.PCA(n_components=3)
        pca.fit(X)
        X = pca.transform(X)

        labelTups = [('fat', 0), ('muscular', 1), ('slim', 2), ('You', 3)]
        for name, label in labelTups:
            ax.text3D(X[y == label, 0].mean(),
                      X[y == label, 1].mean() + 1.5,
                      X[y == label, 2].mean(), name,
                      horizontalalignment='center',
                      bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
        # Reorder the labels to have colors matching the cluster results
        y = np.choose(y, [1, 2, 0, 7]).astype(np.float)
        sc = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap="Spectral", edgecolor='k', s=100)

        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])

        colors = [sc.cmap(sc.norm(i)) for i in [1, 2, 0, 7]]
        custom_lines = [plt.Line2D([],[], ls="", marker='.',
                        mec='k', mfc=c, mew=.1, ms=20) for c in colors]
        ax.legend(custom_lines, [lt[0] for lt in labelTups],
                  loc='center left', bbox_to_anchor=(1.0, .5))

        # plt.show()
        # plt.savefig('resutl.png')
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        return 'data:image/png;base64,{}'.format(graph_url)




    def predict(self, data):
        # Predicting the Test set results
        y_pred = self.classifier.predict(data.reshape(1, 11))
        return y_pred[0]
