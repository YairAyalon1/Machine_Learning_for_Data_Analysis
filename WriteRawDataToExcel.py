# Written by: Yair Ayalon
# Last edition: 30/3/23
# Interpret the DataLogger vectors info to an Excel format
import xlsxwriter
from ReadDataLogger import Temp1, Temp2, Temp3, Temp4, StaticPressure1, StaticPressure2, DifferentialPressure1, \
                           DifferentialPressure2, Voltage1, Voltage2, Voltage3, Current1,Current2,Current3, filename
from FlowRateCalculation import FlowRate1, FlowRate2
import os.path

print()
print("---------------- Writing raw data to an Excel file ----------------")
for i in range(len(filename)):
    if filename[i] == '.':
        index = i
filenameNew = filename[0: index]

# Check if an Excel file is already exist
if os.path.isfile('C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Processed/{}.xlsx'
                          .format(filenameNew)):
    print("---------------------------------------------------")
    print("The file {}.xlsx is already exists".format(filenameNew))
    print("---------------------------------------------------")
else:

    # Create an Excel file
    OutWorkbook = xlsxwriter.Workbook('FILEPATH/{}.xlsx'.format(filenameNew))        # Enter the file path
    OutSheet = OutWorkbook.add_worksheet()
    print("---------------------------------------------------")
    print("1. A file named {}.xlsx has been created".format(filenameNew))

    # Declare data
    Temperature1 = Temp1
    Temperature2 = Temp2
    Temperature3 = Temp3
    Temperature4 = Temp4
    Static_Pressure1 = StaticPressure1
    Static_Pressure2 = StaticPressure2
    Differential_Pressure1 = DifferentialPressure1
    Differential_Pressure2 = DifferentialPressure2
    Flow_Rate1 = FlowRate1
    Flow_Rate2 = FlowRate2
    V1 = Voltage1
    V2 = Voltage2
    V3 = Voltage3
    I1 = Current1
    I2 = Current2
    I3 = Current3

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
    for i in range(0, len(Temperature1)):
        OutSheet.write("A{}".format(i + 2), Temperature1[i])
    for i in range(0, len(Temperature2)):
        OutSheet.write("B{}".format(i + 2), Temperature2[i])
    for i in range(0, len(Temperature3)):
        OutSheet.write("C{}".format(i + 2), Temperature3[i])
    for i in range(0, len(Temperature4)):
        OutSheet.write("D{}".format(i + 2), Temperature4[i])
    for i in range(0, len(Static_Pressure1)):
        OutSheet.write("E{}".format(i + 2), Static_Pressure1[i])
    for i in range(0, len(Static_Pressure2)):
        OutSheet.write("F{}".format(i + 2), Static_Pressure2[i])
    for i in range(0, len(Differential_Pressure1)):
        OutSheet.write("G{}".format(i + 2), Differential_Pressure1[i])
    for i in range(0, len(Differential_Pressure2)):
        OutSheet.write("H{}".format(i + 2), Differential_Pressure2[i])
    for i in range(0, len(V1)):
        OutSheet.write("I{}".format(i + 2), V1[i])
    for i in range(0, len(V2)):
        OutSheet.write("J{}".format(i + 2), V2[i])
    for i in range(0, len(V3)):
        OutSheet.write("K{}".format(i + 2), V3[i])
    for i in range(0, len(I1)):
        OutSheet.write("L{}".format(i + 2), I1[i])
    for i in range(0, len(I2)):
        OutSheet.write("M{}".format(i + 2), I2[i])
    for i in range(0, len(I3)):
        OutSheet.write("N{}".format(i + 2), I3[i])
    for i in range(0, len(Flow_Rate1)):
        OutSheet.write("O{}".format(i + 2), Flow_Rate1[i])
    for i in range(0, len(Flow_Rate2)):
        OutSheet.write("P{}".format(i + 2), Flow_Rate2[i])
    print("--------- Data has been writen successfully to the file ! ---------")

    OutWorkbook.close()
print("-------------------------------------------------------------------")
