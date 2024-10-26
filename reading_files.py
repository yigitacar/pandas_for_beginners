import pandas as pd

## Displays all rows instead of only showing a few from the front and a few from the back
pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 40)

## if there is any need to use \, use r".."
## header=None converts headers to 0,1,2...
## you can also add names=['', '']
df1 = pd.read_csv("countries of the world.csv")

## important to separate cuz no comma in txt
## alternative: df2 = pd.read_table("countries of the world.txt")
df2 = pd.read_csv("countries of the world.txt", sep='\t')

## gives a group of first and last rows
# df2.head(10)
# df2.tail(10)

## gives info about the dataframe
# df2.info()
# df2.loc(10)
# df2.iloc(10)

df3 = pd.read_json("json_sample.json")

df4 = pd.read_excel("world_population_excel_workbook.xlsx", sheet_name='Sheet1')

#print(df4)