#-------------------------------------------------------------------------
# AUTHOR: Sherelene De Belen
# FILENAME: knn.py
# SPECIFICATION: Outputs LOO-CV error rate for 1NN
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

wrong = 0
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    # X =
    X = []

    for j, row in enumerate(db):
        if i != j:
            temp = []
            for ind in range(2):
                temp.append(float(row[ind]))

            X.append(temp)


    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    # Y =
    Y = []
    for k, row in enumerate(db):
        if i != k:
            if row[2] == '-':
                Y.append(float(1))
            else:
                Y.append(float(2))

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    #testSample =
    testSample = []
    for i in range(len(instance)):
        if i < 2:
            testSample.append(float(instance[i]))
        else:
            if instance[2] == '-':
                testSample.append(float(1))
            else:
                testSample.append(float(2))

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample[0:2]])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if testSample[2] != class_predicted:
        wrong = wrong + 1

#print the error rate
#--> add your Python code here

print('error rate', wrong/len(db))






