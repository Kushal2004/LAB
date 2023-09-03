import pandas as pd
from numpy.linalg import matrix_rank
from numpy.linalg import pinv


# Load data
xls = pd.ExcelFile('LAB1DATA.xlsx')
df = pd.read_excel(xls,'IRCTC Stock Price')

