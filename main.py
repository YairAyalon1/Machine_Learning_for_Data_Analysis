import subprocess
import sys
import time

time1 = time.time()
# Read the data logger information and translate it the vector data
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/ReadDataLogger.py"])
time2 = time.time()

# Flow rates calculation (based on the raw data)
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/"
                                 "FlowRateCalculation.py"])
time3 = time.time()

# Write raw data to an Excel file
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/"
                                 "WriteRawDataToExcel.py"])
time4 = time.time()

# Clean the data set and remove outliers
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/CleanData.py"])
time5 = time.time()

# Write cleaned data to an Excel file
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/"
                                 "WriteCleanedDataToExcel.py"])
time6 = time.time()

# Generating a simulator based on the variable ranges in the cleaned data Excel file
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/Simulator.py"])
time7 = time.time()

# Multiple Linear Regression 1 - model stands for predictions of Oxygen bubble flow rate
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/MLR_FlowRate1.py"])
time8 = time.time()

# Multiple Linear Regression 2 - model stands for predictions of Hydrogen bubble flow rate
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/MLR_FlowRate2.py"])
time9 = time.time()

# Calculations & Graphs generations
subprocess.call([sys.executable, "C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DatasetGraphs.py"])
time10 = time.time()

print()
print("The 'ReadDataLogger.py' execution time is: {} sec".format(time2 - time1))
print("The 'FlowRateCalculation.py' execution time is: {} sec".format(time3 - time2))
print("The 'WriteRawDataToExcel.py' execution time is: {} sec".format(time4 - time3))
print("The 'CleanData.py' execution time is: {} sec".format(time5 - time4))
print("The 'WriteCleanedDataToExcel.py' execution time is: {} sec".format(time6 - time5))
print("The 'Simulator.py' execution time is: {} sec".format(time7 - time6))
print("The 'MLR_FlowRate1.py' execution time is: {} sec".format(time8 - time7))
print("The 'MLR_FlowRate2.py' execution time is: {} sec".format(time9 - time8))
print("The 'DatasetGraphs.py' execution time is: {} sec".format(time10 - time9))

