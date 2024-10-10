import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('netflix_titles.csv')

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.dtypes)

# Check for missing values
print(df.isnull().sum())

#since most of the director's name are missing so we'll drop the whole director column
df.drop(['director' ],axis = 1, inplace=True)

#we'll drop any duplicate movies or series if there are any
# df.drop_duplicates(subset=df['title'])


#Drop null rows
df = df.dropna(axis=0,how="all")
#Number of unique values in each attribute
for i in df.columns :
    print(f"Number of unique values in {i} attribute is : {df.nunique()[i]}")
print(df.isnull().sum())
print(df.shape)
print(df.info())
print(df.describe())

# Histogram for numerical columns
df['release_year'].hist(bins=20, color='skyblue', edgecolor='black')
# sns.lineplot(df['release_year'])
plt.title('Year Released')
plt.xlabel('release year')
plt.ylabel('number of movies released')
plt.show()

df['rating'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Rating')
plt.xlabel('Age-Rating')
plt.ylabel('number of movies')
plt.show()
# print(df['cast'].head())
# # Bar plot for categorical columns
# sui = df['type'].value_counts()
# plt.pie(x=sui,autopct="%1.1f%%",labels=sui.index)
# plt.show()
