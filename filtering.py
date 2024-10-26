import pandas as pd
df = pd.read_csv("world_population.csv")

## ----------------------------------------------- Filtering operations -----------------------------------------------
## Filter countries with ranks less than 10
print(df[df['Rank'] < 10])

specific_countries = ['Bangladesh', 'Brazil']
## Filter specific countries
print(df[df['Country'].isin(specific_countries)])
## Filter countries with the name containing the string United
print(df[df['Country'].str.contains('United')])

## Index over country
df2 = df.set_index('Country')
## Filter according to the given items on axis 1, which is column axis
df2 = df2.filter(items=['Continent', 'CCA3'], axis=1)
## Filter according to the given items on axis 0, which is row axis
df2 = df2.filter(items=['Zimbabwe'], axis=0)
## Filter rows that contain the given entry
df2 = df2.filter(like ='United', axis=0)

print(df2)

## ----------------------------------------------- Sorting operations -----------------------------------------------
## First filter less than 10, then sort in descending order
df = df[df['Rank'] < 10].sort_values(by='Rank', ascending=False)
## First sort by the continent in descending, and then sort according to the country in ascending (alphabetical)
df = df[df['Rank'] < 10].sort_values(by=['Continent', 'Country'], ascending=[False, True])
print(df)