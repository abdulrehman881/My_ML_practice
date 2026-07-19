import pandas as pd
df = pd.read_csv(r'Performance1.csv',error_bad_lines=False)
print(df)