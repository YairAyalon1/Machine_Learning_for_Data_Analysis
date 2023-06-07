# Written by: Yair Ayalon
# Last edition: 24/3/23
# Printing graphs to present the given data set

import pandas as pd
import numpy as np
from ReadDataLogger import filename

print()
print("---------------- Calculation & Graphs in progress -----------------")
# Get the required file name - cleaned data
index = float
for i in range(len(filename)):
    if filename[i] == '_':
        index = i
filename1 = "{}_Cleaned.xlsx".format(filename[0: index])
filename2 = "{}_Simulator.xlsx".format(filename1[0: index])

# Replace 'file_path' with the path to your Excel file 
file_path1 = 'FILEֹֹPATH/{}'.format(filename1) # Enter the file path
file_path2 = 'FILEֹֹPATH/{}'.format(filename2) # Enter the file path

# Replace 'sheet_name' with the name of the sheet containing your data
sheet_name = 'Sheet1'

# Replace 'column_name' with the name of the column you want to calculate the average for
column_name_1 = 'Temperature 1'
column_name_2 = 'Temperature 2'
column_name_3 = 'Temperature 3'
column_name_4 = 'Temperature 4'
column_name_5 = 'Static Pressure 1'
column_name_6 = 'Static Pressure 2'
column_name_7 = 'Differential Pressure 1'
column_name_8 = 'Differential Pressure 2'
column_name_9 = 'Voltage 1'
column_name_10 = 'Voltage 2'
column_name_11 = 'Voltage 3'
column_name_12 = 'Current 1'
column_name_13 = 'Current 2'
column_name_14 = 'Current 3'
column_name_15 = 'Flow Rate 1'
column_name_16 = 'Flow Rate 2'

# Read the Excel file into a pandas dataframe
df1 = pd.read_excel(file_path1, sheet_name=sheet_name)
df2 = pd.read_excel(file_path2, sheet_name=sheet_name)

# Calculate the average of the specified column
average1 = df1[column_name_1].mean()
average1 = np.round(average1, 2)
average2 = df1[column_name_2].mean()
average2 = np.round(average2, 2)
average3 = df1[column_name_3].mean()
average3 = np.round(average3, 2)
average4 = df1[column_name_4].mean()
average4 = np.round(average4, 2)
average5 = df1[column_name_5].mean()
average5 = np.round(average5, 2)
average6 = df1[column_name_6].mean()
average6 = np.round(average6, 2)
average7 = df1[column_name_7].mean()
average7 = np.round(average7, 2)
average8 = df1[column_name_8].mean()
average8 = np.round(average8, 2)
average9 = df1[column_name_9].mean()
average9 = np.round(average9, 2)
average10 = df1[column_name_10].mean()
average10 = np.round(average10, 2)
average11 = df1[column_name_11].mean()
average11 = np.round(average11, 2)
average12 = df1[column_name_12].mean()
average12 = np.round(average12, 2)
average13 = df1[column_name_13].mean()
average13 = np.round(average13, 2)
average14 = df1[column_name_14].mean()
average14 = np.round(average14, 2)
average15 = df1[column_name_15].mean()
average15 = np.round(average15, 2)
average16 = df1[column_name_16].mean()
average16 = np.round(average16, 2)

average17 = df2[column_name_1].mean()
average17 = np.round(average17, 2)
average18 = df2[column_name_2].mean()
average18 = np.round(average18, 2)
average19 = df2[column_name_3].mean()
average19 = np.round(average19, 2)
average20 = df2[column_name_4].mean()
average20 = np.round(average20, 2)
average21 = df2[column_name_5].mean()
average21 = np.round(average21, 2)
average22 = df2[column_name_6].mean()
average22 = np.round(average22, 2)
average23 = df2[column_name_7].mean()
average23 = np.round(average23, 2)
average24 = df2[column_name_8].mean()
average24 = np.round(average24, 2)
average25 = df2[column_name_9].mean()
average25 = np.round(average25, 2)
average26 = df2[column_name_10].mean()
average26 = np.round(average26, 2)
average27 = df2[column_name_11].mean()
average27 = np.round(average27, 2)
average28 = df2[column_name_12].mean()
average28 = np.round(average28, 2)
average29 = df2[column_name_13].mean()
average29 = np.round(average29, 2)
average30 = df2[column_name_14].mean()
average30 = np.round(average30, 2)
average31 = df2[column_name_15].mean()
average31 = np.round(average31, 2)
average32 = df2[column_name_16].mean()
average32 = np.round(average32, 2)

print("1. The average Temperature 1 is: --Cleaned data - {0}, Simulator - {1}".format(average1, average17))
print("2. The average Temperature 2 is: --Cleaned data - {0}, Simulator - {1}" .format(average2, average18))
print("3. The average Temperature 3 is: --Cleaned data - {0}, Simulator - {1}" .format(average3, average19))
print("4. The average Temperature 4 is: --Cleaned data - {0}, Simulator - {1}" .format(average4, average20))
print("5. The average Static Pressure 1 is: --Cleaned data - {0}, Simulator - {1}" .format(average5, average21))
print("6. The average Static Pressure 2 is: --Cleaned data - {0}, Simulator - {1}" .format(average6, average22))
print("7. The average Differential Pressure 1 is: --Cleaned data - {0}, Simulator - {1}" .format(average7, average23))
print("8. The average Differential Pressure 1 is: --Cleaned data - {0}, Simulator - {1}" .format(average8, average24))
print("9. The average Voltage 1 is: --Cleaned data - {0}, Simulator - {1}" .format(average9, average25))
print("10. The average Voltage 2 is: --Cleaned data - {0}, Simulator - {1}" .format(average10, average26))
print("11. The average Voltage 3 is: --Cleaned data - {0}, Simulator - {1}" .format(average11, average27))
print("12. The average Current 1 is: --Cleaned data - {0}, Simulator - {1}" .format(average12, average28))
print("13. The average Current 2 is: --Cleaned data - {0}, Simulator - {1}" .format(average13, average29))
print("14. The average Current 3 is: --Cleaned data - {0}, Simulator - {1}" .format(average14, average30))
print("15. The average Flow Rate 1 is: --Cleaned data - {0}, Simulator - {1}" .format(average15, average31))
print("16. The average Flow Rate 2 is: --Cleaned data - {0}, Simulator - {1}" .format(average16, average32))
print("-------------------------------------------------------------------")

# import matplotlib.pyplot as plt
# from ReadDataLogger import VoltageMatrix, FlowRateMatrix
#
# x1 = VoltageMatrix[0]
# x2 = VoltageMatrix[1]
# x3 = VoltageMatrix[2]
# y1 = FlowRateMatrix[0]
# y2 = FlowRateMatrix[1]
#
# plt.plot(x1, y1, '.')
# plt.show()
