from sklearn import tree
import numpy as np
import csv

class DecisionTreeData(dict):
    
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    
def LoadDataFromFile(filename):
    #change below csv file path
    with open(filename) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        #number of samples is read from first line first word
        n_samples = int(temp[0])

        #number of features available
        n_features = int(temp[1])

        #class names available in first line staring second word
        target_names = np.array(temp[2:])

        #create 2D data array of size n_samples * n_features
        data = np.empty((n_samples, n_features))
        
        #create an array of size n_samples * n_features
        target = np.empty((n_samples,), dtype=np.int)

        #iterate over remaining data and fill in data and target arrays
        for i, ir in enumerate(data_file):
            #print (i)
            if i == n_samples:
              continue
            data[i] = np.asarray(ir[:n_features], dtype=np.float64)
            target[i] = np.asarray(ir[n_features:], dtype=np.int)
                 

    return DecisionTreeData(data=data, target=target,
                 target_names=target_names,
                 feature_names=['sepal length (cm)', 'sepal width (cm)',
                                'petal length (cm)', 'petal width (cm)'])



def TestDataFromFile(testData, clf):

    with open(testData) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        #number of samples is read from first line first word
        n_samples = int(temp[0])

        #number of features available
        n_features = int(temp[1])

        #iterate over remaining data and fill in data and target arrays
        for i, ir in enumerate(data_file):
            #print (i)
            if i == n_samples:
              continue
            data[i] = np.asarray(ir[:n_features], dtype=np.float64)
            target[i] = np.asarray(ir[n_features:], dtype=np.int)

        predictions = clf.predict(data)

        for i, ir in enumerate(predictions):
            if i == n_samples:
              continue
            if predictions[i] != target[i]:
               print ("wrong answer: %s != %s" %(predictions[i], target[i]))
               #print("wow")



print("Formatting:")
print("     First row: [number of data points],[number of dimensions],[name of possiable result],[name of possiable result],[name of possiable result]....")
print("     The last collumn of the chart will be assumed to be the goal value")

print("Enter file name of data")
iris = LoadDataFromFile(raw_input())

#Create DecisionTreeClassifier
clf = tree.DecisionTreeClassifier()

#Fit the data read from file
clf = clf.fit(iris.data, iris.target)

print("Decision Tree Created")

print("enter csv file for testing")

TestDataFromFile(raw_input(), clf)
#prediction for given value
#Note that [4.5,2.4,3.3,1.0] is not a given value in the input file
print(clf.predict([[4.5,2.4,3.3,1.0],[4.5,2.4,3.3,1.0]]))

#Drawing Decision Tree Data in a dot file. Change the path 
with open('output.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)


