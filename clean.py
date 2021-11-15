import pandas as pd
import csv

df = pd.read_csv("final.csv")
print(df.shape)
del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
print(df.shape)
df = df.rename({
    "Star_name.1": "Star_name",
    "Distance.1": "Distance",
    "Mass.1": "Mass",
    "Radius.1": "Radius"
}, axis="columns")
df = df.dropna()
df.columns
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.drop(['Unnamed: 6'],axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
df.to_csv("cleaned.csv")