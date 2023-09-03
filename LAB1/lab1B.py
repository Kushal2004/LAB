import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# A4. Please refer to the data present in “IRCTC Stock Price” data sheet of the above Excel file. Do the
# following after loading the data to your programming platform.

irctc = pd.read_excel('LAB1\LAB1DATA.xlsx',sheet_name="IRCTC Stock Price")
irctc = irctc.dropna(axis=1)
#print(irctc.head())

#----------------------------------------------------------------

# Calculate the mean and variance of the Price data present in column D.
# (Suggestion: if you use Python, you may use statistics.mean() & statistics.variance() methods).

# First Select feature Price
Mean = st.mean(irctc["Price"])
Variance = st.variance(irctc["Price"])
print("Mean            : ",Mean)
print("Variance        : ",Variance)

#  Select the price data for all Wednesdays and calculate the sample mean. Compare the mean
#  with the population mean and note your observations.
Wed = irctc[irctc['Day']=='Wed']
# print(Wed.head())
Wed_mean = st.mean(Wed['Price'])
# print("Sample mean: ",Wed_mean)

# Comparing the sample mean with population mean
if Wed_mean < Mean:
    print("Mean of price data for all Wednesdays is lesser than the mean of all price")
else:
    print("Mean of price data for all Wednesdays is greater than the mean of all price")

# Select the price data for the month of Apr and calculate the sample mean. Compare the
# mean with the population mean and note your observations.

Apr_data = irctc[irctc['Month']=='Apr']
Apr_mean = st.mean(Apr_data['Price'])
print("Mean of price of April month: ",Apr_mean)

if Apr_mean < Mean:
    print("Population mean is greater than the sample mean of April month")
else:
    print("Population mean is greater than the sample mean of April month")

# From the Chg% (available in column I) find the probability of making a loss over the stock.
# (Suggestion: use lambda function to find negative values)

# Calculate the probability of making a loss
loss_probability = len(irctc[irctc['Chg%'] < 0]) / len(irctc)
print("Probability of Making a Loss:", loss_probability)

#Calculate the probability of making a profit on Wednesday.
profit_wed = len(irctc[irctc['Chg%']>0])/len(Wed)
print("Probability of profit on Wednesday       : ",profit_wed)

#Calculate the conditional probability of making profit, given that today is Wednesday.
Total_wed = len(Wed)
profit_on_Wed = len(Wed['Chg%']>0)
Cnd_pr = profit_on_Wed/Total_wed
print("Conditional probability: ",Cnd_pr)

# Make a scatter plot of Chg% data against the day of the week
X = irctc['Chg%']
Y = irctc['Day']
plt.scatter(X,Y,label='Data Points',color='blue')
plt.xlabel("Chg%")
plt.ylabel("Week")
#plt.show()
