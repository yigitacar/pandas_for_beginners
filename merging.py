import pandas as pd

df1 = pd.read_csv("LOTR.csv")
df2 = pd.read_csv("LOTR 2.csv")

## ---------------------------------------------Merge function----------------------------------------------------------
## Inner join (inner is default anyways)
print(df1.merge(df2, how='inner'))

## Merges over fellowship id, writes the other columns separately
print(df1.merge(df2, how='inner', on='FellowshipID'))

## Outer join
print(df1.merge(df2, how='outer'))

## Left join
print(df1.merge(df2, how='left'))

## Right join
print(df1.merge(df2, how='right'))

## Cross join
print(df1.merge(df2, how='cross'))

## ---------------------------------------------Join function----------------------------------------------------------
print(df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), how='outer', lsuffix='_left', rsuffix='_Right'))

## ---------------------------------------------Concatenate-------------------------------------------------------------
## Puts two dfs on top of each other
print(pd.concat([df1, df2]))
## Outer join using concat
print(pd.concat([df1, df2], join='outer', axis=1))
