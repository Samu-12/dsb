import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("titanic.csv")

print( "First 5 rows: \n", df.head().T)
print( "Last 5 rows:\n",df.tail().T)
print( "Any 5 rows: \n",df.sample(5).T)
print( "Information of Dataset: \n", df.info)
print( "Shape:",df.shape)
print( "Columns Name:", df.columns)
print( "Total elements:", df.size)
print( "Datatype of columns:", df.dtypes)

print ("Missing values",df.isnull().sum())

df ["Age"].fillna (df["Age"].median(), inplace=True)
print ("Null values are: \n",df.isnull().sum())

#Boxplot of 1-variable
fig, axes =plt.subplots(1,2)
sns.boxplot (data =df, x="Age", ax=axes[0])
sns.boxplot (data =df, x="Fare",ax=axes[1])
plt.show()

#Boxplot of 2-variables
fig, axes =plt.subplots(2,2)
sns.boxplot (data = df, x="Survived", y="Age", hue="Survived", ax=axes[0,0])
sns.boxplot (data = df, x="Survived", y="Fare", hue="Survived",ax=axes[0,1])
sns.boxplot (data = df, x="Sex", y="Age", hue= "Sex", ax=axes[1,0])
sns.boxplot (data = df, x="Sex", y="Fare", hue="Sex", ax=axes[1,1])
plt.show()

#Boxplot of 3-variables
fig, axes= plt.subplots(1,2)
sns.boxplot (data=df, x="Sex", y="Age", hue="Survived", ax=axes[0])
sns. boxplot(data=df, x = "Sex", y="Fare",hue="Survived", ax=axes [1])
plt.show()

