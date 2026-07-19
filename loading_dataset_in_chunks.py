import pandas as pd
df = pd.read_csv(r'Performance1.csv',chunksize=2)
print(df)
for chunks in df:
    print(chunks.shape)