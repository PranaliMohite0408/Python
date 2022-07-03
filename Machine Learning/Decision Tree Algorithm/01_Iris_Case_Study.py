"""
Classifier : Decision Tree
datasets : Iris Dataset
features: Sepal width, sepal Length, petal width, petal Length
Labels: Versicolor, sentosa, Virginica
Trainging dataset :150 Entries

"""

from sklearn.datasets import load_iris

iris = load_iris()

print("\nFeature Name of iris data set ")
print(iris.feature_names)

print("\nTarget names of iris data set")
print(iris.target_names)

print("\nElements from Iris Data set =>")

for i in range(len(iris.target)):
    print("ID : %d, Feature: %s , Labels: %s" % (i,iris.data[i],iris.target[i]))