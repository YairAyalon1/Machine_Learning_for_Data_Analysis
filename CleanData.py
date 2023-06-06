# Written by: Yair Ayalon
# Last edition: 30/3/23
# Clean all the raw data from outliers

import pandas as pd
import matplotlib.pyplot as plt
from ReadDataLogger import filename

print()
print("---------------------- Cleaning the raw data ----------------------")
# Get the required file name
index = float
for i in range(len(filename)):
    if filename[i] == '.':
        index = i
filename = filename[0: index]

# Read the raw data from the Excel file
df_raw = pd.read_excel('C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Processed/{}.xlsx'
                       .format(filename))
print("1. The size of the raw data set is: {}".format(df_raw.shape))


def plot_boxplot(df, ft):
    df.boxplot(column=[ft])
    plt.grid(False)
    plt.show()


def outliers(df, ft):
    q1 = df[ft].quantile(0.05)
    q3 = df[ft].quantile(0.95)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    ls = df.index[(df[ft] < lower_bound) | (df[ft] > upper_bound)]
    return ls


index_list = []
for variable in ['Temperature 1', 'Temperature 2', 'Temperature 3', 'Temperature 4', 'Static Pressure 1',
                 'Static Pressure 2', 'Differential Pressure 1', 'Differential Pressure 2', 'Voltage 1', 'Voltage 2',
                 'Voltage 3', 'Current 1', 'Current 2', 'Current 3']:
    index_list.extend(outliers(df_raw, variable))


def remove(df, ls):
    ls = sorted(set(ls))
    df = df.drop(ls)
    return df


# Getting the cleaned data
df_cleaned = remove(df_raw, index_list)
print("2. The cleaned data size is: {}".format(df_cleaned.shape))
print("----------- The raw data has been cleaned successfully ! ----------")
