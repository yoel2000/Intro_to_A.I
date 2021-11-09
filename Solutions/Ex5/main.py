import numpy as np
import pandas as pd

url = 'https://github.com/rosenfa/nn/blob/master/pima-indians-diabetes.csv?raw=true'
df = pd.read_csv(url, header=0, error_bad_lines=False)
X = np.asarray(df.drop('Outcome', 1))
y = np.asarray(df['Outcome'])

from sklearn import tree  # For decision trees
from sklearn.model_selection import cross_val_score  # For cross validation
import matplotlib.pyplot as plt  # for plotting graphs
from sklearn import datasets  # for datasets
from sklearn.metrics import plot_confusion_matrix, confusion_matrix, f1_score, recall_score

clf = tree.DecisionTreeClassifier()

clf.max_depth = 5
# print("Decision Tree: ")
accuracy = cross_val_score(clf, X, y, scoring='precision_weighted', cv=10)
# print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(accuracy.mean(), 3))

iris = datasets.load_iris()
# mylist = []
# do loop
clf = tree.DecisionTreeClassifier()
accuracy = 0

for i in range(10):
    clf.max_depth = i + 1
    clf.criterion = 'entropy'
    # print("Decision Tree: ")
    acc_temp = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
    if round(acc_temp.mean(), 3) > accuracy:
        accuracy = round(acc_temp.mean(), 3)
    # print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(acc_temp.mean(), 3))
    # mylist.append(accuracy.mean())  loop, can be used to plot later…
    precision = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
    # print("Average precision_weighted of  DT with depth ", clf.max_depth, " is: ", round(precision.mean(), 3))

    recall = cross_val_score(clf, iris.data, iris.target, scoring='recall_weighted', cv=10)
    # print("Average recall_weighted of  DT with depth ", clf.max_depth, " is: ", round(recall.mean(), 3))

    f1score = cross_val_score(clf, iris.data, iris.target, scoring='f1_weighted', cv=10)
    # print("Average f1_score_weighted of  DT with depth ", clf.max_depth, " is: ", round(f1score.mean(), 3)

print("max accuracy of iris dataset: ", accuracy)

class_names = iris.target_names
clf.max_depth = 2
clf = clf.fit(iris.data, iris.target)
titles_options = [("Confusion matrix")]

# confusion_matrix(iris.data, iris.target, labels=class_names)

for title in titles_options:
    disp = plot_confusion_matrix(clf, iris.data, iris.target,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues)
    disp.ax_.set_title(title)

    # print(title)
    # print(disp.confusion_matrix)

plt.show()

X = range(10)
plt.plot(X, acc_temp, 'r--', X, precision, 'b--', X, recall, 'g--', X, f1score, 'm--')
plt.xlabel("This is the X axis")
plt.ylabel("This is the Y axis")
plt.show()

wine = datasets.load_wine()

clf = tree.DecisionTreeClassifier()
accuracy = 0

for i in range(10):
    clf.max_depth = i + 1
    clf.criterion = 'entropy'
    # print("Decision Tree: ")
    acc_temp = cross_val_score(clf, wine.data, wine.target, scoring='accuracy', cv=10)
    if round(acc_temp.mean(), 3) > accuracy:
        accuracy = round(acc_temp.mean(), 3)
    # print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(acc_temp.mean(), 3))
    # mylist.append(accuracy.mean())  loop, can be used to plot later…
    precision = cross_val_score(clf, wine.data, wine.target, scoring='precision_weighted', cv=10)
    # print("Average precision_weighted of  DT with depth ", clf.max_depth, " is: ", round(precision.mean(), 3))

    recall = cross_val_score(clf, wine.data, wine.target, scoring='recall_weighted', cv=10)
    # print("Average recall_weighted of  DT with depth ", clf.max_depth, " is: ", round(recall.mean(), 3))

    f1score = cross_val_score(clf, wine.data, wine.target, scoring='f1_weighted', cv=10)
    # print("Average f1_score_weighted of  DT with depth ", clf.max_depth, " is: ", round(f1score.mean(), 3))

print("max accuracy of wine dataset: ", accuracy)

X = range(10)
plt.plot(X, acc_temp, 'r--', X, precision, 'b--', X, recall, 'g--', X, f1score, 'm--')
plt.xlabel("This is the X axis")
plt.ylabel("This is the Y axis")
plt.show()

from sklearn.datasets import load_digits

digits = load_digits()

clf = tree.DecisionTreeClassifier()
accuracy = 0

for i in range(10):
    clf.max_depth = i + 1
    clf.criterion = 'entropy'
    # print("Decision Tree: ")
    acc_temp = cross_val_score(clf, digits.data, digits.target, scoring='accuracy', cv=10)
    if round(acc_temp.mean(), 3) > accuracy:
        accuracy = round(acc_temp.mean(), 3)
    # print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(acc_temp.mean(), 3))
    # mylist.append(accuracy.mean())  loop, can be used to plot later…
    precision = cross_val_score(clf, digits.data, digits.target, scoring='precision_weighted', cv=10)
    # print("Average precision_weighted of  DT with depth ", clf.max_depth, " is: ", round(precision.mean(), 3))

    recall = cross_val_score(clf, digits.data, digits.target, scoring='recall_weighted', cv=10)
    # print("Average recall_weighted of  DT with depth ", clf.max_depth, " is: ", round(recall.mean(), 3))

    f1score = cross_val_score(clf, digits.data, digits.target, scoring='f1_weighted', cv=10)
    # print("Average f1_score_weighted of  DT with depth ", clf.max_depth, " is: ", round(f1score.mean(), 3))
print("max accuracy of digit dataset: ", accuracy)


X = range(10)
plt.plot(X, acc_temp, 'r--', X, precision, 'b--', X, recall, 'g--', X, f1score, 'm--')
plt.xlabel("This is the X axis")
plt.ylabel("This is the Y axis")
plt.show()
