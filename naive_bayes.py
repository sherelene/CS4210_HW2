#-------------------------------------------------------------------------
# AUTHOR: Sherelene De Belen
# FILENAME: naive_bayes.py
# SPECIFICATION: output the classification of each test instance from the file
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here

db = []
test_db = []

#reading the data in a csv file
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
X = []
  # Dictionary to transform the data
features = {'Sunny': 1, 'Overcast': 2, 'Rain': 3, 'Hot': 1, 'Mild': 2, 'Cool': 3, 'High': 1, 'Normal': 2, 'Weak': 1,
              'Strong': 2}
for row in range(len(db)):
    temp = []
    for feature in range(1, 5):  # Skip the Day column
        temp.append(int(features[db[row][feature]]))
    X.append(temp)


#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
Y = []
for row in range(len(db)):
    if db[row][5] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         test_db.append(row)


#printing the header as the solution
#--> add your Python code here
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
testingData = []
for row in range(len(test_db)):
    temp = []
    for feature in range(1, 5): #Skip the Day and PlayTennis column
        temp.append(int(features[test_db[row][feature]]))
    testingData.append(temp)


for row in range(len(testingData)):
    predicted = clf.predict_proba([testingData[row]])[0]
    if predicted[0] >= 0.75:
        test_db[row][5] = 'Yes'
        for i in range(6):
            print(str(test_db[row][i]).ljust(15),  end='')
        print(round(predicted[0], 2))
    if predicted[1] >= 0.75:
        test_db[row][5] = 'No'
        for i in range(6):
            print(str(test_db[row][i]).ljust(15),  end='')
        print(round(predicted[1], 2))

