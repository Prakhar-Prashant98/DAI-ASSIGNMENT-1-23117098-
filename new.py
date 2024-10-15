import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('smoking.csv')


print(df.head())
print(df.shape)
print(df.info())
print(df.dtypes)

# Check for missing values
print(df.isnull().sum())

# df.fillna(0, inplace=True)

#Number of unique values in each attribute
for i in df.columns :
    print(f"Number of unique values in {i} attribute is : {df.nunique()[i]}")

# Bar plot for categorical columns
sui = df['smoke'].value_counts()
plt.pie(x=sui,autopct="%1.1f%%",labels=sui.index)
plt.show()
sui = df['type'].value_counts()
plt.pie(x=sui,autopct="%1.1f%%",labels=sui.index)
plt.show()

#Plotting Number of smokers by marital status
plt.bar(x=df["marital_status"].value_counts().index,height=df["marital_status"].value_counts())
plt.show()

#Plotting Number of smokers by ethnicity
plt.bar(x=df["ethnicity"].value_counts().index,height=df["ethnicity"].value_counts())
plt.xticks(df["ethnicity"].unique())
plt.show()

#number of outliers in amt_weekends

outliers=[]
col="amt_weekends"

Q1=df[col].quantile(0.25)
Q2=df[col].quantile(0.5)
Q3=df[col].quantile(0.75)
IQR = Q3-Q1
for i in df[col] :
    if (i>(Q3 +1.5*IQR)) or (i<(Q1-1.5*IQR)) :
        outliers.append(i)

print(f"In {col} column, there are {len(outliers)} outliers")


#Boxplot of applicants on basis of cigarettes smoked per weekend
sns.boxplot(df.amt_weekends)
plt.show()

#HEATMAP
sns.heatmap(pd.crosstab(df.amt_weekends, df.age))
plt.show()

#MULTIVARIATE ANALYSIS
sns.pairplot(df[["amt_weekends","amt_weekdays"]])
plt.show()
