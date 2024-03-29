# -*- coding: utf-8 -*-
"""targil4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttF4DQHP1gr6v_-yGhu0sOv9An1trMcn

In this homework, we will learn about SKLEARN and a little about how Python deals with files (using Dataframes) and arrays (numpy) and its graphing library, matplot.
"""

import numpy as np
import pandas as pd
url = 'https://github.com/rosenfa/nn/blob/master/pima-indians-diabetes.csv?raw=true'
df=pd.read_csv(url,  header=0, error_bad_lines=False) 
X = np.asarray(df.drop('Outcome',1))
y = np.asarray(df['Outcome'])

"""Let's print the dataset so we can see what we got!"""

df

"""Now let's add libraries for learning"""

from sklearn import tree #For decision trees
from sklearn.model_selection import cross_val_score #For cross validation
import matplotlib.pyplot as plt #for plotting graphs
from sklearn import datasets #for datasets

clf = tree.DecisionTreeClassifier()
clf.max_depth = 5
print("Decision Tree: ")
accuracy = cross_val_score(clf, X, y, scoring='accuracy', cv=10)
print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(accuracy.mean(),3))

"""We can do this for other datasets that are built-in to Sklearn:"""

iris = datasets.load_iris()
#mylist = []
#do loop
clf = tree.DecisionTreeClassifier()
clf.max_depth = 5
clf.criterion = 'entropy'
print("Decision Tree: ")
accuracy = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(accuracy.mean(),3))
#mylist.append(accuracy.mean())  loop, can be used to plot later…
precision = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
print("Average precision_weighted of  DT with depth ", clf.max_depth, " is: ", round(precision.mean(),3))

"""A confusion matrix for the data..."""

from sklearn.metrics import plot_confusion_matrix
class_names = iris.target_names
clf.max_depth = 2
clf = clf.fit(iris.data, iris.target)
titles_options = [("Confusion matrix")]
for title in titles_options:
    disp = plot_confusion_matrix(clf, iris.data, iris.target,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()

"""Hint for how to plot the results:"""

#X = range(10)
#plt.plot(X, [x * x for x in X])
#plt.xlabel("This is the X axis")
#plt.ylabel("This is the Y axis")
#plt.show()