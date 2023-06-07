# Written by: Yair Ayalon
# Last edition: 30/3/23
# Creation of a simulation environment according to a given dataset

import pandas as pd
import numpy as np
import xlsxwriter
import os.path
from ReadDataLogger import filename
import multiprocessing
import time

start_time = time.time()


def generate_random_values(observationNum, variable_range):
    return np.round(np.random.uniform(variable_range[0], variable_range[1], observationNum), 2)


def write_data_to_file(file_path, header, data):
    OutWorkbook = xlsxwriter.Workbook(file_path)
    OutSheet = OutWorkbook.add_worksheet()

    # Write headers
    for i, column in enumerate(header):
        OutSheet.write(0, i, column)

    # Transpose the data
    transposed_data = list(zip(*data))

    # Write transposed data to the file
    for i, row in enumerate(transposed_data):
        for j, value in enumerate(row):
            OutSheet.write(i + 1, j, value)

    OutWorkbook.close()


def main():
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

    variables = [
        'Temperature 1', 'Temperature 2', 'Temperature 3', 'Temperature 4',
        'Static Pressure 1', 'Static Pressure 2', 'Differential Pressure 1', 'Differential Pressure 2',
        'Voltage 1', 'Voltage 2', 'Voltage 3', 'Current 1', 'Current 2', 'Current 3'
    ]

    data = df[variables].values.T.tolist()

    # Define the total minimum and maximum limits
    min_values = [min(col) for col in data]
    max_values = [max(col) for col in data]

    print("1. The minimum values of the variables are: ")
    print(min_values)
    print("2. The maximum values of the variables are: ")
    print(max_values)

    # Define the ranges for each variable
    variable_ranges = list(zip(min_values, max_values))

    # Generate random values using multiprocessing
    with multiprocessing.Pool() as pool:
        random_values = pool.starmap(generate_random_values,
                                     [(observationNum, variable_range) for variable_range in variable_ranges])

    # Generate the simulator Excel file name
    index = float
    for i in range(len(filenameNew)):
        if filenameNew[i] == '_':
            index = i
    SimulatorFilename = "{}_Simulator.xlsx".format(filenameNew[0: index])

    # Check if an Excel file already exists
    simulator_file_path = 'C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Simulator/{}.xlsx'.format(
        SimulatorFilename)
    if os.path.isfile(simulator_file_path):
        print("---------------------------------------------------")
        print("The file {}.xlsx already exists".format(SimulatorFilename))
        print("---------------------------------------------------")
    else:
        # Write data to the file
        header = variables + ['Flow Rate 1', 'Flow Rate 2']
        data = random_values + [[0] * observationNum, [0] * observationNum]
        write_data_to_file(simulator_file_path, header, data)

        print()
        print("-------------------------------------------------------------------")
        print("The Simulation Excel file has been created successfully.")
        print("The file is named {}.xlsx".format(SimulatorFilename))
        print("-------------------------------------------------------------------")

    print()
    end_time = time.time()
    print("The execution time is: {} sec".format(end_time - start_time))
    print("--------------- Simulator creation has been completed ---------------")
    print()


if __name__ == '__main__':
    main()
