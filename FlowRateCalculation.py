# Written by: Yair Ayalon
# Last edition: 30/3/23
# Calculation of both flow rates values based on the differential pressures 1 & 2

from ReadDataLogger import DifferentialPressure1, DifferentialPressure2
import math

print()
print("-------------------- Calculates the flow rates --------------------")
dp1 = float
dp2 = float
FlowRate1 = []
FlowRate2 = []

# Function 1 - flow rate 1 calculation
def fr1_calculation(dp1):
    r11 = 15 # Please enter the radius inlet at A1 (mm)
    r21 = 5 # Please enter the radius inlet at A2 (mm)
    a11 = 3.14 * (pow(r11, 2)) # Calculation of area 1 (mm^2)
    a21 = 3.14 * (pow(r21, 2)) # Calculation of area 2 (mm^2)
    q11 = 2120 # Typical KOH liquid density (kg/(m^3))
    Q11 = math.sqrt((2 * dp1) / (q11 * ((1 / pow(a21, 2)) - (1 / pow(a11, 2)))))
    # Flow rate via the first pipe
    return Q11

# Function 2 - flow rate 2 calculation
def fr2_calculation(dp2):
    r12 = 15 # Please enter the radius inlet at A1 (mm)
    r22 = 5 # Please enter the radius inlet at A2 (mm)
    a12 = 3.14 * (pow(r12, 2)) # Calculation of area 1 (mm^2)
    a22 = 3.14 * (pow(r22, 2)) # Calculation of area 2 (mm^2)
    q12 = 2120 # Typical KOH liquid density (kg/(m^3))
    Q12 = math.sqrt((2 * dp2) / (q12 * ((1 / pow(a22, 2)) - (1 / pow(a12, 2)))))
    # Flow rate via the first pipe
    return Q12

for i in range(0, len(DifferentialPressure1)):
    FlowRate1.append(fr1_calculation(DifferentialPressure1[i]))
for i in range(0, len(DifferentialPressure2)):
    FlowRate2.append(fr2_calculation(DifferentialPressure2[i]))

print("--------- Flow rates have been calculated successfully ! ----------")
