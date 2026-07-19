import pandas as pd
df = pd.read_csv(r'Performance.csv',usecols=['ID','Salary'])
print(df)