import pandas as pd
df = pd.read_csv(r'Performance.csv',index_col='ID')
print(df)