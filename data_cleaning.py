import pandas as pd

df = pd.read_excel("Customer Call List.xlsx")
pd.set_option('display.max.columns', 40)

## Get rid of duplicate rows, where each column has the same value
df = df.drop_duplicates()
## Get rid of a column that is marked as not useful
df = df.drop(columns="Not_Useful_Column")

## Get rid of the ... in front of any value on the column Last Name (quite inefficient)
df["Last_Name"] = df["Last_Name"].str.lstrip("..")
## Get rid of any of the entered characters from anywhere on the string (efficient)
df["Last_Name"] = df["Last_Name"].str.strip("123._/")

## The regex expression is used in the replace function at the first position. It means replace any characters in the
## phone_number field that are not alphanumeric with the empty string. So this is like deleting any characters that
## don’t match the expression. The carat character ^ inside the brackets mean ‘not’. The range 0-9 means all integers
## in this range. A-Z and a-z mean all uppercase and lowercase characters respectively.
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '', regex=True)
## Convert everything in phone number column to string
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
## Separate the elements in phone number column and put '-' in between
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
## Replace the given strings with nothing
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

## Split the column address by comma into 3 columns
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',n=2, expand=True)

## Replace Yes with Y, No with N
df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')

## Replace the empty entries on the entire data with nothing
df = df.replace('N/a', '')
df = df.fillna('')

## Drop the rows with do not contact yes or nothing
## Alternative: df = df.dropna(subset="Phone Number", inplace=True)
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == '' or df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
## Reset the previously done operation
df = df.reset_index(drop=True)

print(df)