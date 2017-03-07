
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
            if i == 150:
              continue
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=np.int)
                 

    return DecisionTreeData(data=data, target=target,
                 target_names=target_names,
                 feature_names=['sepal length (cm)', 'sepal width (cm)',
                                'petal length (cm)', 'petal width (cm)'])



print("Press 1 to load a new decision tree from a csv file")
print("     Note: the last collumn of the chart will be assumed to be the goal value")
print("Press 2 to load an existing decision tree")
#read data from file
inputChar = input()

if inputChar == 1:
    print("Enter file name of data")
    iris = load_iris(input())

    #Create DecisionTreeClassifier
    clf = tree.DecisionTreeClassifier()

    #Fit the data read from file
    clf = clf.fit(iris.data, iris.target)
elif inputChar == 2:
    print("Loading a decision tree could be implemented with pickle, however Dr.Chan suggested that it would be outside the scope of this project.")
else:
    print("Invalid Input")

print("Decision Tree Created")

#TODO: break out csv read-in so we can do the tree test in a way that makes sense
# be able to get number of fields so we can do the interactive new case easily



#prediction for given value
#Note that [4.5,2.4,3.3,1.0] is not a given value in the input file
print(iris.target_names[clf.predict([[4.5,2.4,3.3,1.0]])])

#Drawing Decision Tree Data in a dot file. Change the path 
with open('output.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)


