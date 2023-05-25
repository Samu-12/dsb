def RemoveOutlier(df,var):
    Q1 =df[var].quantile(0.25)
    Q3 =df[var].quantile(0.75)
    IQR = Q3-Q1
    high, low=Q3+1.5*IQR, Q1-1.5*IQR

    df=df[((df[var] >= low) & (df[var] <= high))]
    return df

def DisplayOutliers(df, message):
    fig, axes = plt.subplots(2,2)
    plt.suptitle(message)
    sns.boxplot(data=df, x="raisedhands", ax=axes[0,0])
    sns.boxplot(data=df, x="VisITedResources", ax=axes[0,1])
    sns.boxplot(data=df, x="AnnouncementsView", ax=axes[1,0])
    sns.boxplot(data=df, x="Discussion", ax=axes[1,1])
    plt.show()

import  numpy as np
import  pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("student_data.csv")

print("First 5 rows:",df.head().T)
print("Last 5 rows:",df.tail().T)
print("Any 5 rows:",df.sample(5).T)
print("Information of Dataset:n", df.info)
print("Shape of Dataset:", df.shape)
print("Columns Name:", df.columns)
print("Total elements in dataset:", df.size)
print("Datatype columns", df.dtypes)

print("Describe: \n",df.describe())

#Display null values
print(" Null values in Dataset:\n", df.isna().sum())

DisplayOutliers(df, "Before removing Outliers")
df=RemoveOutlier(df, "raisedhands")
df=RemoveOutlier(df, "VisITedResources")
df=RemoveOutlier(df, "AnnouncementsView")
df=RemoveOutlier(df, "Discussion")
DisplayOutliers(df, "After removing Outliers")


df["gender"]=df["gender"].astype("category")
df["gender"]=df["gender"].cat.codes
print("Gender Values:", df["gender"].unique())

