import pandas as pd
df = pd.read_csv(r'Performance1.csv',dtype={'Performance score':'int'})
print(df)