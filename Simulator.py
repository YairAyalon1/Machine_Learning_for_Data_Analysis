# Written by: Yair Ayalon
# Last edition: 30/3/23
# Creation of a simulation environment according to a given dataset

import pandas as pd
import numpy as np
import xlsxwriter
import os.path
from ReadDataLogger import filename

print()
print("--------------- Simulator creation has been started ---------------")

observationNum = 50000

# Getting the correct file name
for i in range(len(filename)):
    if filename[i] == '_':
        index = i
filenameNew = "{}_Cleaned.xlsx".format(filename[0: index])

# Get the variables from the Excel file
df = pd.read_excel('FILEPATH/{}'.format(filenameNew))     # Enter the file path
Temp1 = df['Temperature 1'].tolist()
Temp2 = df['Temperature 2'].tolist()
Temp3 = df['Temperature 3'].tolist()
Temp4 = df['Temperature 4'].tolist()
StaticPressure1 = df['Static Pressure 1'].tolist()
StaticPressure2 = df['Static Pressure 2'].tolist()
DifferentialPressure1 = df['Differential Pressure 1'].tolist()
DifferentialPressure2 = df['Differential Pressure 1'].tolist()
Voltage1 = df['Voltage 1'].tolist()
Voltage2 = df['Voltage 2'].tolist()
Voltage3 = df['Voltage 3'].tolist()
Current1 = df['Current 1'].tolist()
Current2 = df['Current 2'].tolist()
Current3 = df['Current 3'].tolist()

# Define the maximum and minimum values to all collected variables
temp1Range = [min(Temp1), max(Temp1)]
temp2Range = [min(Temp2), max(Temp2)]
temp3Range = [min(Temp3), max(Temp3)]
temp4Range = [min(Temp4), max(Temp4)]
staticPressure1Range = [min(StaticPressure1), max(StaticPressure1)]
staticPressure2Range = [min(StaticPressure2), max(StaticPressure2)]
diffPressure1Range = [min(DifferentialPressure1), max(DifferentialPressure1)]
diffPressure2Range = [min(DifferentialPressure2), max(DifferentialPressure2)]
voltage1Range = [min(Voltage1), max(Voltage1)]
voltage2Range = [min(Voltage2), max(Voltage2)]
voltage3Range = [min(Voltage3), max(Voltage3)]
current1Range = [min(Current1), max(Current1)]
current2Range = [min(Current2), max(Current2)]
current3Range = [min(Current3), max(Current3)]

# Define the total minimum and maximum limits
min_values = [temp1Range[0], temp2Range[0], temp3Range[0], temp4Range[0], staticPressure1Range[0],
              staticPressure2Range[0], diffPressure1Range[0], diffPressure2Range[0], voltage1Range[0], voltage2Range[0],
              voltage3Range[0], current1Range[0], current2Range[0], current3Range[0]]
max_values = [temp1Range[1], temp2Range[1], temp3Range[1], temp4Range[1], staticPressure1Range[1],
              staticPressure2Range[1], diffPressure1Range[1], diffPressure2Range[1], voltage1Range[1], voltage2Range[1],
              voltage3Range[1], current1Range[1], current2Range[1], current3Range[1]]

print("1. The minimum values of the variables are: ")
print(min_values)
print("2. The maximum values of the variables are: ")
print(max_values)

# Generating random values to all the 14 variables
random_temp1 = np.random.uniform(temp1Range[0], temp1Range[1], observationNum)
random_temp1 = np.round(random_temp1, 2)
random_temp2 = np.random.uniform(temp2Range[0], temp2Range[1], observationNum)
random_temp2 = np.round(random_temp2, 2)
random_temp3 = np.random.uniform(temp3Range[0], temp3Range[1], observationNum)
random_temp3 = np.round(random_temp3, 2)
random_temp4 = np.random.uniform(temp4Range[0], temp4Range[1], observationNum)
random_temp4 = np.round(random_temp4, 2)
random_SP1 = np.random.uniform(staticPressure1Range[0], staticPressure1Range[1], observationNum)
random_SP1 = np.round(random_SP1, 2)
random_SP2 = np.random.uniform(staticPressure2Range[0], staticPressure2Range[1], observationNum)
random_SP2 = np.round(random_SP2, 2)
random_DP1 = np.random.uniform(diffPressure1Range[0], diffPressure1Range[1], observationNum)
random_DP1 = np.round(random_DP1, 2)
random_DP2 = np.random.uniform(diffPressure2Range[0], diffPressure2Range[1], observationNum)
random_DP2 = np.round(random_DP2, 2)
random_V1 = np.random.uniform(voltage1Range[0], voltage1Range[1], observationNum)
random_V1 = np.round(random_V1, 2)
random_V2 = np.random.uniform(voltage2Range[0], voltage2Range[1], observationNum)
random_V2 = np.round(random_V2, 2)
random_V3 = np.random.uniform(voltage3Range[0], voltage3Range[1], observationNum)
random_V3 = np.round(random_V3, 2)
random_I1 = np.random.uniform(current1Range[0], current1Range[1], observationNum)
random_I1 = np.round(random_I1, 2)
random_I2 = np.random.uniform(current2Range[0], current2Range[1], observationNum)
random_I2 = np.round(random_I2, 2)
random_I3 = np.random.uniform(current3Range[0], current3Range[1], observationNum)
random_I3 = np.round(random_I3, 2)

# Generate the simulator Excel file name
index = float
for i in range(len(filenameNew)):
    if filenameNew[i] == '_':
        index = i
SimulatorFilename = "{}_Simulator.xlsx".format(filenameNew[0: index])

# Check if an Excel file is already exist
if os.path.isfile('C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Simulator/{}.xlsx'
                          .format(SimulatorFilename)):
    print("---------------------------------------------------")
    print("The file {}.xlsx is already exists".format(SimulatorFilename))
    print("---------------------------------------------------")

else:
    # Create an Excel file
    OutWorkbook = xlsxwriter.Workbook('C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/'
                                      'DataSets/Simulator/{}'.format(SimulatorFilename))
    OutSheet = OutWorkbook.add_worksheet()
    print("1. A file named {} has been created".format(SimulatorFilename))

    # Write headers
    print("2. Writing data to the file")
    OutSheet.write("A1", "Temperature 1")
    OutSheet.write("B1", "Temperature 2")
    OutSheet.write("C1", "Temperature 3")
    OutSheet.write("D1", "Temperature 4")
    OutSheet.write("E1", "Static Pressure 1")
    OutSheet.write("F1", "Static Pressure 2")
    OutSheet.write("G1", "Differential Pressure 1")
    OutSheet.write("H1", "Differential Pressure 2")
    OutSheet.write("I1", "Voltage 1")
    OutSheet.write("J1", "Voltage 2")
    OutSheet.write("K1", "Voltage 3")
    OutSheet.write("L1", "Current 1")
    OutSheet.write("M1", "Current 2")
    OutSheet.write("N1", "Current 3")
    OutSheet.write("O1", "Flow Rate 1")
    OutSheet.write("P1", "Flow Rate 2")

    # Write data to the file
    for i in range(0, len(random_temp1)):
        OutSheet.write("A{}".format(i + 2), random_temp1[i])
    for i in range(0, len(random_temp2)):
        OutSheet.write("B{}".format(i + 2), random_temp2[i])
    for i in range(0, len(random_temp3)):
        OutSheet.write("C{}".format(i + 2), random_temp3[i])
    for i in range(0, len(random_temp4)):
        OutSheet.write("D{}".format(i + 2), random_temp4[i])
    for i in range(0, len(random_SP1)):
        OutSheet.write("E{}".format(i + 2), random_SP1[i])
    for i in range(0, len(random_SP2)):
        OutSheet.write("F{}".format(i + 2), random_SP2[i])
    for i in range(0, len(random_DP1)):
        OutSheet.write("G{}".format(i + 2), random_DP1[i])
    for i in range(0, len(random_DP2)):
        OutSheet.write("H{}".format(i + 2), random_DP2[i])
    for i in range(0, len(random_V1)):
        OutSheet.write("I{}".format(i + 2), random_V1[i])
    for i in range(0, len(random_V2)):
        OutSheet.write("J{}".format(i + 2), random_V2[i])
    for i in range(0, len(random_V3)):
        OutSheet.write("K{}".format(i + 2), random_V3[i])
    for i in range(0, len(random_I1)):
        OutSheet.write("L{}".format(i + 2), random_I1[i])
    for i in range(0, len(random_I2)):
        OutSheet.write("M{}".format(i + 2), random_I2[i])
    for i in range(0, len(random_I3)):
        OutSheet.write("N{}".format(i + 2), random_I3[i])
    print("--------- Data has been writen successfully to the file ! ---------")

    OutWorkbook.close()

print("-------------------------------------------------------------------")
