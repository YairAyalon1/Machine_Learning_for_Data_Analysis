# Written by: Yair Ayalon
# Last edition: 30/3/23
# Interpret the DataLogger information to vectors info
import numpy as np

filename = "DataLoggerHuge_Raw.txt"
Temp1 = []
Temp2 = []
Temp3 = []
Temp4 = []
Voltage1 = []
Voltage2 = []
Voltage3 = []
Current1 = []
Current2 = []
Current3 = []
Liquid = []
StaticPressure1 = []
StaticPressure2 = []
DifferentialPressure1 = []
DifferentialPressure2 = []
FlowRate1 = []
FlowRate2 = []

with open("C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Raw/{}".format(filename), "r")\
        as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("    Temperature 1"):
        colon_index = line.index(":")
        Temp1Str = line[(colon_index + 2) : (line.index("Celsius") - 1)]
        if Temp1Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Temp1)):
                sum = sum + Temp1[i]
            Temp1.append(sum / int(len(Temp1)))
        else:
            Temp1.append(float(Temp1Str))

    elif line.startswith("    Temperature 2"):
        colon_index = line.index(":")
        Temp2Str = line[(colon_index + 2) : (line.index("Celsius") - 1)]
        if Temp2Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Temp2)):
                sum = sum + Temp2[i]
            Temp2.append(sum / int(len(Temp2)))
        else:
            Temp2.append(float(Temp2Str))

    elif line.startswith("    Temperature 3"):
        colon_index = line.index(":")
        Temp3Str = line[(colon_index + 2) : (line.index("Celsius") - 1)]
        if Temp3Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Temp3)):
                sum = sum + Temp3[i]
            Temp3.append(sum / int(len(Temp3)))
        else:
            Temp3.append(float(Temp3Str))

    elif line.startswith("    Temperature 4"):
        colon_index = line.index(":")
        Temp4Str = line[(colon_index + 2) : (line.index("Celsius") - 1)]
        if Temp4Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Temp4)):
                sum = sum + Temp4[i]
            Temp4.append(sum / int(len(Temp4)))
        else:
            Temp4.append(float(Temp4Str))

    elif line.startswith("    DP 1"):
        colon_index = line.index(":")
        DifferentialPressure1Str = line[(colon_index + 2) : (line.index("[Pa]") - 1)]
        if (DifferentialPressure1Str == ("nan" or "na")) or (DifferentialPressure1Str[0] == '-'):
            sum = 0
            for i in range(0, len(DifferentialPressure1)):
                sum = sum + DifferentialPressure1[i]
            DifferentialPressure1.append(sum / int(len(DifferentialPressure1)))
        else:
            DifferentialPressure1.append(float(DifferentialPressure1Str))

    elif line.startswith("    Flow Rate 1"):
        colon_index = line.index(":")
        FlowRate1Str = line[(colon_index + 2) : (line.index("[m^3/s]") - 1)]
        if FlowRate1Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(FlowRate1)):
                sum = sum + FlowRate1[i]
            FlowRate1.append(sum / int(len(FlowRate1)))
        else:
            FlowRate1.append(float(FlowRate1Str))

    elif line.startswith("    Flow Rate 2"):
        colon_index = line.index(":")
        FlowRate2Str = line[(colon_index + 2) : (line.index("[m^3/s]") - 1)]
        if FlowRate2Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(FlowRate2)):
                sum = sum + FlowRate2[i]
            FlowRate2.append(sum / int(len(FlowRate2)))
        else:
            FlowRate2.append(float(FlowRate2Str))

    elif line.startswith("    DP 2"):
        colon_index = line.index(":")
        DifferentialPressure2Str = line[(colon_index + 2) : (line.index("[Pa]") - 1)]
        if (DifferentialPressure2Str == ("nan" or "na")) or (DifferentialPressure2Str[0] == '-'):
            sum = 0
            for i in range(0, len(DifferentialPressure2)):
                sum = sum + DifferentialPressure2[i]
            DifferentialPressure2.append(sum / int(len(DifferentialPressure2)))
        else:
            DifferentialPressure2.append(float(DifferentialPressure2Str))

    elif line.startswith("    SP 1"):
        colon_index = line.index(":")
        StaticPressure1Str = line[(colon_index + 2) : (line.index("[kPa]") - 1)]
        if StaticPressure1Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(StaticPressure1)):
                sum = sum + StaticPressure1[i]
            StaticPressure1.append(sum / int(len(StaticPressure1)))
        else:
            StaticPressure1.append(float(StaticPressure1Str))

    elif line.startswith("    SP 2"):
        colon_index = line.index(":")
        StaticPressure2Str = line[(colon_index + 2) : (line.index("[kPa]") - 1)]
        if StaticPressure2Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(StaticPressure2)):
                sum = sum + StaticPressure2[i]
            StaticPressure2.append(sum / int(len(StaticPressure2)))
        else:
            StaticPressure2.append(float(StaticPressure2Str))

    elif line.startswith("    Current 1"):
        colon_index = line.index(":")
        Current1Str = line[(colon_index + 2) : (line.index("[mA]") - 1)]
        if Current1Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Current1)):
                sum = sum + Current1[i]
            Current1.append(sum / int(len(Current1)))
        else:
            Current1.append(float(Current1Str))

    elif line.startswith("    Voltage 1"):
        colon_index = line.index(":")
        Voltage1Str = line[(colon_index + 2) : (line.index("[V]") - 1)]
        if Voltage1Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Voltage1)):
                sum = sum + Voltage1[i]
            Voltage1.append(sum / int(len(Voltage1)))
        else:
            Voltage1.append(float(Voltage1Str))

    elif line.startswith("    Current 2"):
        colon_index = line.index(":")
        Current2Str = line[(colon_index + 2) : (line.index("[mA]") - 1)]
        if Current2Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Current2)):
                sum = sum + Current2[i]
            Current2.append(sum / int(len(Current2)))
        else:
            Current2.append(float(Current2Str))

    elif line.startswith("    Voltage 2"):
        colon_index = line.index(":")
        Voltage2Str = line[(colon_index + 2) : (line.index("[V]") - 1)]
        if Voltage2Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Voltage2)):
                sum = sum + Voltage2[i]
            Voltage2.append(sum / int(len(Voltage2)))
        else:
            Voltage2.append(float(Voltage2Str))

    elif line.startswith("    Current 3"):
        colon_index = line.index(":")
        Current3Str = line[(colon_index + 2) : (line.index("[mA]") - 1)]
        if Current3Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Current3)):
                sum = sum + Current3[i]
            Current3.append(sum / int(len(Current3)))
        else:
            Current3.append(float(Current3Str))

    elif line.startswith("    Voltage 3"):
        colon_index = line.index(":")
        Voltage3Str = line[(colon_index + 2) : (line.index("[V]") - 1)]
        if Voltage3Str == ("nan" or "na"):
            sum = 0
            for i in range(0, len(Voltage3)):
                sum = sum + Voltage3[i]
            Voltage3.append(sum / int(len(Voltage3)))
        else:
            Voltage3.append(float(Voltage3Str))

# Define the measurements matrix according to DataLogger
TempMatrix = np.array([Temp1, Temp2, Temp3, Temp4])
DifferentialPressureMatrix = np.array([DifferentialPressure1, DifferentialPressure2])
FlowRateMatrix = np.array([FlowRate1, FlowRate2])
StaticPressureMatrix = np.array([StaticPressure1, StaticPressure2])
CurrentMatrix = np.array([Current1, Current2, Current3])
VoltageMatrix = np.array([Voltage1, Voltage2, Voltage3])

print("-------------------- Reading from DataLogger --------------------")
print("The temperature measurements are: ")
print(TempMatrix)
print("The differential pressure measurements are: ")
print(DifferentialPressureMatrix)
print("The static pressure measurements are: ")
print(StaticPressureMatrix)
print("The current measurements are: ")
print(CurrentMatrix)
print("The voltage measurements are: ")
print(VoltageMatrix)
print("The flow rate measurements are: ")
print(FlowRateMatrix)
print("The size of temperature matrix is: ")
print(TempMatrix.shape)
print("The size of differential pressure matrix is: ")
print(DifferentialPressureMatrix.shape)
print("The size of flow rate matrix is: ")
print(FlowRateMatrix.shape)
print("The size of static pressure matrix is: ")
print(StaticPressureMatrix.shape)
print("The size of current matrix is: ")
print(CurrentMatrix.shape)
print("The size of voltage matrix is: ")
print(VoltageMatrix.shape)
print("-------------- Data set has been read successfully ! --------------")
