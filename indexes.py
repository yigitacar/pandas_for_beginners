import pandas as pd

## Index is countries, not a set number
df = pd.read_csv("world_population.csv", index_col="Country")
## df.set_index('Country', inplace=True)
## Reset the indexing operation
df.reset_index(inplace=True)

## Index over first the continent, then the country
df.set_index(['Continent', 'Country'], inplace=True)
## Sort alphabetically and group the indexes
## If you df.loc here over country, not gonna work. do df.loc['Africa', 'Angola']
df = df.sort_index()
print(df)
