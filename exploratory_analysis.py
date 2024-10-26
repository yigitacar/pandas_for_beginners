## EDA in pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("world_population.csv")
pd.set_option('display.float_format', lambda x : '%.2f' % x)

df.info()
df.describe()
## Number of null values in each column
df.isnull().sum()
## Number of unique values in each column
df.nunique()

df.sort_values(by="World Population Percentage", ascending=False).head(10)
## Lists every column and how correlated they are with each other
df.corr()
## Heatmap of correlations described above
sns.heatmap(df.corr(), annot = True)
plt.rcParams['figure.figsize'] = (20,7)
plt.show()

## Grouped the countries by the continent and calculated the mean values for each column
df.groupby('Continent').mean().sort_values(by="2022 Population",ascending=False)

## List the rows that belong to the continent oceania
df[df['Continent'].str.contains('Oceania')]

## Selected specific columns for continents, took the mean values and sorted
df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by="2022 Population",ascending=False)

## Transpose of dataset
df3 = df2.transpose()
## Lists data types
df.dtypes
## Select columns that have numbers
df.select_dtypes(include='number')
df3.plot()

df.boxplot(figsize=(20,10))

df.select_dtypes(include='float')

print(df)