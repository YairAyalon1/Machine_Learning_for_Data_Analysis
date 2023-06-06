# Written by: Yair Ayalon
# Last edition: 30/3/23
# Multi Linear Machine Learning model for flow rate 1 - write also the predicted results

import numpy as np
import pandas as pd
from ReadDataLogger import filename
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from openpyxl import load_workbook

print()
print("------------------------ MLR 1 is working -------------------------")

# Getting the correct file name
for i in range(len(filename)):
    if filename[i] == '_':
        index = i
filenameNew = "{}_Cleaned.xlsx".format(filename[0: index])

# Read the data from the Excel file
data_df = pd.read_excel(r'C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Processed/{}'
                        .format(filenameNew))
# print(data_df.head())

# Define the parameters y & x for the machine learning model
x = data_df.drop(['Flow Rate 1', 'Flow Rate 2'], axis=1).values
y = data_df['Flow Rate 1'].values

# Define the training & testing datasets and the size of each one of them
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
ml = LinearRegression()
ml.fit(x_train, y_train)

# Model predictions
y_pred = ml.predict(x_test)
print("1. The predictions for Flow Rate 1 is (testing):")
print(y)
print("2. The predicted Flow Rate 1 for the first line of the dataset is:")
print(ml.predict([[19.25, 20.5, 20.2, 20.2,	116.62,	116.08,	27,	27,	2.51, 2.51,	2.5, 0.2, 0.19,	0.06]]))

# Model performances evaluation
MLR1 = r2_score(y_test, y_pred)
MLR1 = np.round(MLR1, 4)

# Results displaying - actual measurements VS. predicted ones
print("3. Model performances evaluation: {}% accuracy".format(MLR1 * 100))

# Big data predictions
# Get the simulator Excel file name
print("4. Starts the predictions of the big dataset")
index = float
for i in range(len(filenameNew)):
    if filenameNew[i] == '_':
        index = i
SimulatorFilename = "{}_Simulator.xlsx".format(filenameNew[0: index])
bigData = pd.read_excel(r'C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Simulator/{}'
                        .format(SimulatorFilename))
bidDataForPredictions = bigData.drop(['Flow Rate 1', 'Flow Rate 2'], axis=1).values
predictedData = ml.predict(bidDataForPredictions)
print("5. Predictions have been done, writing the results to the Excel file")

# Writing the predictions to the Simulator Excel file
workbook = load_workbook(filename='C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Simulator'
                                  '/{}'.format(SimulatorFilename))
worksheet = workbook['Sheet1']
for index1, value in enumerate(predictedData):
    worksheet['O{}'.format(index1 + 2)] = np.round(value, 2)
workbook.save(filename='C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Simulator'
                                  '/{}'.format(SimulatorFilename))
print("6. Results have been written to the Excel file successfully !")

# Print the results
# plt.figure(figsize=(15, 10))
# plt.scatter(y_test, y_pred)
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# plt.title('Actual VS. Predicted')

print("------------------- Machine learning phase end --------------------")
# plt.show()
