import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# A4. Please refer to the data present in “IRCTC Stock Price” data sheet of the above Excel file. Do the
# following after loading the data to your programming platform.

df = pd.read_excel('LAB2DATA.xlsx',sheet_name="thyroid0387_UCI")
df= df.dropna(axis=1)
#print(data.info())
#print(data[['TSH']])
#df = pd.get_dummies(df, columns=['sick'], prefix=['VALUE'])
#print(df)

numeric_variables = df.select_dtypes(include=[np.number])
#print(numeric_variables.describe())

missing_values = (df == "?").sum()
#print(missing_values)

# Replace "?" with NaN
df.replace("?", float("nan"), inplace=True)
#print(df.describe()) # Since max value is higher than mean , the outlaiers exists

