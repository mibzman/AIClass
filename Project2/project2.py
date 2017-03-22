from sklearn import tree
import numpy as np
import csv
import sklearn.metrics as metrics

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
    result = True
    with open(testData) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        #number of samples is read from first line first word
        n_samples = int(temp[0])

        #number of features available
        n_features = int(temp[1])

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

        predictions = clf.predict(data)

        for i, ir in enumerate(predictions):
            if i == n_samples:
              continue
            if predictions[i] != target[i]:
               print ("wrong answer: %s != %s" %(predictions[i], target[i]))
               result = False
	if result:
		print("all tests have passed")
	else:
		print("some tests failed")
	print(metrics.confusion_matrix(target, predictions))

def GetDataPointsFromCSV(filename):
    with open(testData) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        #number of samples is read from first line first word
        return int(temp[0])



print("Formatting:")
print("     First row: [number of data points],[number of dimensions],[name of possiable result],[name of possiable result],[name of possiable result]....")
print("     The last collumn of the chart will be assumed to be the goal value")

print("Enter file name of data")
iris = LoadDataFromFile(raw_input())

#Create DecisionTreeClassifier
clf = tree.DecisionTreeClassifier()

#Fit the data read from file
clf = clf.fit(iris.data, iris.target)

print("data:")
#iris.data.set_printoptions(precision=3)
#print(iris.data)

print("Decision Tree Created")

while True:
	print("press 1 to test with csv file")
	print("press 2 to enter a custom value")
	print("press 3 to exit")

	inputChar = raw_input()
	if inputChar == '1':
		print("enter csv file for testing")
		testingFilename = raw_input()
		TestDataFromFile(testingFilename, clf)
	elif inputChar == '2':
        	print("enter number of data points")
	        numInputs = int(raw_input())
        	data = np.empty((1, numInputs))
		tempData = []
        	for i in range(1, numInputs +1):
			print("enter %sth value" %(i))
			tempData.append(int(raw_input()))
		data[0] = tempData
		print("prediction:")
        	print(iris.target_names[clf.predict(data)])
	elif inputChar == '3':
        	break
	else:
		print("invalid option")
#prediction for given value
#Note that [4.5,2.4,3.3,1.0] is not a given value in the input file

#numPoints = GetDataPointsFromCSV(testingFilename)
 
#print(clf.predict([[4.5,2.4,3.3,1.0],[4.5,2.4,3.3,1.0]]))

#Drawing Decision Tree Data in a dot file. Change the path 
#with open('output.dot', 'w') as f:
   # f = tree.export_graphviz(clf, out_file=f)


