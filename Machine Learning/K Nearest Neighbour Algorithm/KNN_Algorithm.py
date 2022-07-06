from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)
    
class MarvellousKNN():
    def fit(self,TrainingData, TrainingTarget):
        self.TrainingData = TrainingData
        self.TrainingTarget = TrainingTarget
        
    def predict(self, TestData):
        predictions =[]
        for row in TestData:
            lebel = self.closest(row)
            predictions.append(lebel)
        return predictions 
        
def closest(self,row):
    bestdistance = ecu(row,self.TrainingData[0])
    bestindex = 0
    for i in range(1,len(self.TrainingData)):
        dist = ecu(row,self.TrainingData[i])
        if dist < bestdistance:
            bestdistance = dist
            bestindex = i
    return self.TrainingTarget[bestindex]

def MavellousKNeighbor():
    border = "-"*50
    
    iris = load_iris()
    
    data = iris.data
    target = iris.target
    
    print(border)
    print("Actual data set")
    print(border)
    
    for i in range(len(iris.target)):
        print("ID: %d, Label %s, Feature: %s" % (i,iris.data[i], iris.target[i]))
        
    print("Size of Actual data set %d"%(i+1))
    
    data_train, data_test, target_train, target_test, = train_test_split(data,target,test_size = 0.5)
    
    print(border)
    print("Training data set")
    print(border)
    for i in range(len(data_train)):
        print("ID : %d , Label %s, Feature: %s" % (i,data_train[i], target_train[i]))
    print("Size of Training data set %d"%(i+1))    
    
    print(border)
    print("Test data set")
    print(border)
    for i in range(len(data_test)):
        print("ID: %d, Label %s, Feature:%s" % (i,data_test[i],target_test[i]))
    print("Size of Test Data set %d"%(i+1))
    print(border)
    
    classifier = MarvellousKNN()

    classifier.fit(data_train,target_train)
    
    predictions = classifier.predict(data_test)
    
    Accuracy = accuracy_score(target_test,predictions)
    
    return Accuracy
    
    
def main():
    Accuracy = MavellousKNeighbor()
    print("Accuracy of classification algorithm with K Neighbor classifier is", Accuracy*100,"%")
    
if __name__ == "__main__":
    main()