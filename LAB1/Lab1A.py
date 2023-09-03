import pandas as pd
from numpy.linalg import matrix_rank
from numpy.linalg import pinv

# A1. Please refer to the “Purchase Data” worksheet of Lab Session1 Data.xlsx. Please load the data
# and segregate them into 2 matrices A & C (following the nomenclature of AX = C). Do the following
# activities.

#----------------------------------------------------------------
# Load data
xls = pd.ExcelFile('LAB1\LAB1DATA.xlsx')
df = pd.read_excel(xls,'Purchase data')
df.drop(df.iloc[:,5:],inplace=True,axis=1)

#Dimension reduction

A = (df.iloc[:,1:4]).to_numpy()
B = (df.iloc[:,-1]).to_numpy()
#----------------------------------------------------------------

# What is the dimensionality of the vector space for this data?

dimensionality = A.shape[1]
num_vectors = A.shape[0]

print("DIMENSIONALITY :",dimensionality)
#print(num_vectors)

# How many vectors exist in this vector space?
num_vectors = A.shape[0]

# What is the rank of Matrix A?
rank_A = matrix_rank(A)
print("RANK :",rank_A)

# Using Pseudo-Inverse find the cost of each product available for sale.

pseudo_inv_A = pinv(A)
product_costs = pseudo_inv_A @ B  # AX=B , this is X
print("PRODUCT COSTS :",product_costs)

#------------------------------------------------------------------

#A2. Use the Pseudo-inverse to calculate the model vector X for predicting the cost of the products
#available with the vendo

predicted_cost = A @ product_costs
print("PREDICTED COSTS :",predicted_cost)


# A3 Mark customers as RICH or POOR based on payments
df['Customer Category'] = df['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')
selected_columns = df[['SPayment (Rs)','Customer Category']]
print(selected_columns)
