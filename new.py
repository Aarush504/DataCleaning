import csv
import pandas as pd
df = pd.read_csv("final.csv")
print(df.shape)
del df["luminosity"]
print(df.shape)
print(list(df))
print(list(df))
df.to_csv('new.csv')