# import pandas as pd
# df = pd.read_csv(r'Performance.csv',skiprows=[1,4])
# print(df)




import pandas as pd
df = pd.read_csv(r'Performance.csv',nrows=10)
print(df)