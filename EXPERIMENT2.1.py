import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["target"] = wine.target

print("----- First Five Rows -----")
print(df.head())

print("\n----- Dataset Information -----")
df.info()

print("\n----- Statistical Summary -----")
print(df.describe())

print("\n----- Missing Values -----")
print(df.isnull().sum())

print("\n----- Dataset Shape -----")
print(df.shape)

print("\n----- Column Names -----")
print(df.columns)