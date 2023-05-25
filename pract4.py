
def RemoveOutlier(df, var):
    Q1=df[var].quantile(0.25)
    Q3=df[var].quantile(0.75)
    IQR =Q3-Q1
    high, low=Q3+1.5*IQR, Q1-1.5+IQR

    df=df[((df[var] >= low) & (df[var] <=high))]
    return df

def DisplayOutlier(df, msg):
    fig,axes=plt.subplots(1,2)
    fig.suptitle(msg)
    sns.boxplot(data=df, x="rm", ax=axes[0])
    sns.boxplot(data = df, x="lstat", ax=axes[1])
    plt.show()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv ("Boston.csv")

print("First 5 rows: \n", df.head().T)
print("last 5 rows:\n",df.tail().T)
print("Any 5 rows: \n",df.sample(5).T)
print("Information of Dataset:\n", df.info)
print("Shape of Dataset row x column):", df.shape)
print("Columns Name:", df.columns)
print("Total elements in dataset:",df.size)
print("Datatype of attributes (columns):" ,df.dtypes)

print ("Missing values:",df.isnull().sum())

sns.heatmap(df.corr(),annot=True)
plt.title("correlation matrix using heatmap")
plt.show()

DisplayOutlier(df, "Before removing Outliers:")
df = RemoveOutlier(df, "lstat")
df = RemoveOutlier(df,"rm")
DisplayOutlier(df,"After removing Outliers")

x=df[["rm","lstat"]] #input data
y=df["medv"]         #output data

#Training and testing data
from sklearn.model_selection import train_test_split

#Assign test data size 20%
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size=0.20, random_state=0)

#Apply linear regression model on training data
from sklearn.linear_model import LinearRegression
model=LinearRegression().fit(x_train, y_train)
y_pred=model.predict(x_test)

#Display accuracy of the model
from sklearn.metrics import mean_absolute_error
print("MAE:",mean_absolute_error(y_test,y_pred))
print("Model Score:",model.score(x_test,y_test))

