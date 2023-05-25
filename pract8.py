import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("titanic.csv")

print( "First 5 rows: \n", df.head().T)
print( "Last 5 rows:\n",df.tail().T)
print( "Any 5 rows: \n",df.sample(5).T)
print( "Information of Dataset: \n", df.info)
print( "Shape :",df.shape)
print( "Columns Name:", df.columns)
print( "Total elements in dataset:", df.size)
print( "Datatype of columns", df.dtypes)

print ("Missing values",df.isnull().sum())

df ["Age"].fillna (df["Age"].median(), inplace=True)
print ("Null values are: \n",df.isnull().sum())

fig, axes = plt.subplots(1,2)
sns.histplot(data=df, x="Age", ax=axes[0])
sns.histplot(data=df, x="Fare", ax=axes[1])
plt.show()

fig, axes = plt.subplots(2,2)
sns.histplot(data=df, x="Age", hue="Survived", multiple="dodge", ax=axes[0,0])
sns.histplot(data=df, x="Fare", hue="Survived", multiple="dodge", ax=axes[0,1])
sns.histplot(data=df, x="Fare", hue="Sex", multiple="dodge", ax=axes[1,0])
sns.histplot(data=df, x="Age", hue="Sex", multiple="dodge", ax=axes[1,1])
plt.show()


