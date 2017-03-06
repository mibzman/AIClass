
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

    
def load_iris():
    #change below csv file path
    with open('data.csv') as csv_file:
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
            if i == 150:
              continue
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=np.int)
                 

    return DecisionTreeData(data=data, target=target,
                 target_names=target_names,
                 feature_names=['sepal length (cm)', 'sepal width (cm)',
                                'petal length (cm)', 'petal width (cm)'])



#read data from file
iris = load_iris()
#print(iris)

#Create DecisionTreeClassifier
clf = tree.DecisionTreeClassifier()

#Fit the data read from file
clf = clf.fit(iris.data, iris.target)

#prediction for given value
#Note that [4.5,2.4,3.3,1.0] is not a given value in the input file
print(iris.target_names[clf.predict([[4.5,2.4,3.3,1.0]])])

#Drawing Decision Tree Data in a dot file. Change the path 
with open('output.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)


