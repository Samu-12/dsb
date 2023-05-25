import numpy as np
import pandas as pd

df=pd.read_csv("placement_data.csv")

print( "First 5 rows: \n", df.head().T)
print( "Last 5 rows:\n",df.tail().T)
print( "Any 5 rows: \n",df.sample(5).T)
print( "Information of Dataset: \n", df.info)
print( "Shape of Dataset:",df.shape)
print( "Columns Name:", df.columns)
print( "Total elements in dataset:", df.size)
print( "Datatype of columns:", df.dtypes)
print( "Describe: \n", df.describe())

print("Null Values:", df.isna().sum())

df["sl_no"]=df[ "sl_no"].astype( "int8")
print("Datatype of sl_no",df.dtypes)

df["gender"] =df["gender"].astype("category")
print("Data types of Gender=", df.dtypes["gender"])
df["gender"]=df["gender"].cat.codes
print("Gender Values:",df["gender"].unique())

print("Normalization using Min-Max Scaling: ")
df["salary"]=(df["salary"]-df["salary"].min())/(df ["salary"].max()-df["salary"].min())
print(df["salary"].head())
