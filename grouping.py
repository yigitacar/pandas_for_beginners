import pandas as pd

df = pd.read_csv("Flavors.csv")

## Group by base flavor
## Take the mean values of groups and specify numeric only to avoid agg error
print(df.groupby('Base Flavor').mean(numeric_only=True))
## Counts the entries that are grouped
print(df.groupby('Base Flavor').count())
## Gives minimum and maximum values and sums in groups
print(df.groupby('Base Flavor').min())
print(df.groupby('Base Flavor').max())
print(df.groupby('Base Flavor').sum())

## Creates a set that shows flavor and texture rating values aggregated by mean, max, count and sum after grouping by
## Base Flavor
print(df.groupby('Base Flavor').agg({'Flavor Rating' : ['mean', 'max', 'count', 'sum'], 'Texture Rating' : ['mean', 'max', 'count', 'sum']}))

## Gives a lot of aggregations
print(df.groupby('Base Flavor').describe())