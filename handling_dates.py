import pandas as pd
df = pd.read_csv(r'Performance1.csv',parse_dates=['Joining_Date']).info()
print(df)