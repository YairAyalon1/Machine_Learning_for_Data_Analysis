# Written by: Yair Ayalon
# Last edition: 30/3/23
# Writing the cleaned data to an Excel file

from ReadDataLogger import filename
from CleanData import df_cleaned

print()
print("-------------- Writing cleaned data to an Excel file --------------")
# Get the required file name
index = float
for i in range(len(filename)):
    if filename[i] == '_':
        index = i
filename = "{}_Cleaned.xlsx".format(filename[0: index])
cleaned_data = df_cleaned
cleaned_data.to_excel('C:/Users/ayaya/Desktop/Yair/University/Thesis/PythonCodeForThesis/DataSets/Processed/{}'
                      .format(filename), index=False)
print("1. A file named {}.xlsx has been created".format(filename))
print("2. Writing data to the file")
print(" The cleaned data has been written to an Excel file Successfully !")
