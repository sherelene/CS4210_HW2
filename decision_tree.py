# -------------------------------------------------------------------------
# AUTHOR: Sherelene De Belen
# FILENAME: decision_tree.py
# SPECIFICATION: Trains, tests, outputs performance of 3 datasets
# FOR: CS 4210- Assignment #2
# TIME SPENT: 5 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:
    dbTraining = []
    X = []
    Y = []


    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    # X =

    features_dic = {'Young': 1, 'Prepresbyopic': 2, 'Presbyopic': 3, 'Myope': 1, 'Hypermetrope': 2, 'Yes': 1, 'No': 2,
                  'Normal': 1, 'Reduced': 2}
    for row in range(len(dbTraining)):
        features = []

        for element in range(4):
            features.append(int(features_dic[dbTraining[row][element]]))

        X.append(features)

        # transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    # Y =
    for row in range(len(dbTraining)):
        if dbTraining[row][4] == 'Yes':
            Y.append(1)
        else:
            Y.append(2)

    # loop your training and test tasks 10 times here
    lowAcc = 1  # Lowest accuracy
    for loop in range(10):

        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        # dbTest =
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)

        x_test = []
        y_test = []
        for row in range(len(dbTest)):
            test_features = []
            for element in range(4):
                test_features.append(int(features_dic[dbTest[row][element]]))

            x_test.append(test_features)

        for row in range(len(dbTest)):
            if dbTest[row][4] == 'Yes':
                y_test.append(1)
            else:
                y_test.append(2)

            # class_predicted = []
            count = 0

        for row in range(len(x_test)):
            class_predicted = clf.predict([x_test[row]])[0]
            if y_test[row] == class_predicted:
                count = count + 1
        accuracy = count / len(x_test)
        if accuracy < lowAcc:
            lowAcc = accuracy


    # calculate and print average accuracy for the training data set

    print(f'Final accuracy when training on {ds}: {lowAcc:.3f}')



