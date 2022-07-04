"""
Classifier : Decision Tree
datasets : Iris Dataset
features: Sepal width, sepal Length, petal width, petal Length
Labels: Versicolor, sentosa, Virginica
Trainging dataset :150 Entries
Target => Labels
data => features
"""
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

print("feature names of iris datasets is =>")
print(iris.feature_names)

print("Target names of iris datasets is =>")
print(iris.target_names)

#Indices of removed elements
test_index = [1,51,101]

#Training Data with removed elements
train_target = np.delete(iris.target,test_index)
train_data = np.delete(iris.data, test_index,axis =0)

#Testing data for testing on trainning data
test_target = iris.target[test_index]
test_data = iris.data[test_index]

#from decision tree classifier
classifier = tree.DecisionTreeClassifier()

#Applay training data to form tree
classifier.fit(train_data,train_target)

print("values that we removed for testing")
print(test_target)

print("Result of testing")
print(classifier.predict(test_data))