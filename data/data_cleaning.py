import pandas as pd
#Load amazon sales data
df = pd.read_csv('raw_amazon_data.csv',encoding='latin1')

#original data has 16 columns and 1465 rows
print("Rows" , df.shape[0])
print("Columns",df.shape[1])

#Check the first few rows of the dataframe
print(df.head())

#Check the column names and data types
print(df.columns)
print(df.info())

#check for duplicates
print(df.duplicated().sum())

# Inspect and remove rows with missing rating counts
print(df[df["rating_count"].isnull()])
print(df["rating_count"].isnull().sum())
#remove the rows with missing values in the rating_count column
df=df.dropna(subset=["rating_count"])
#verify that the missing values have been removed
print(df["rating_count"].isnull().sum())

# Convert analytical columns from text to numeric
#replace garbage values in the columns with appropriate values
print(df["discounted_price"].head())
df["discounted_price"]=df["discounted_price"].str.replace(r"[^\d.]","",regex=True)
df["discounted_price"]=pd.to_numeric(df["discounted_price"])

print(df["actual_price"].head())
df["actual_price"]=df["actual_price"].str.replace(r"[^\d.]","",regex=True)
df["actual_price"]=pd.to_numeric(df["actual_price"])

print(df["rating"].head())
df["rating"]=df["rating"].replace("|",pd.NA)
df.dropna(subset=["rating"],inplace=True)
df["rating"]=pd.to_numeric(df["rating"])

print(df["rating_count"].head())
df["rating_count"]=df["rating_count"].str.replace(",","",regex=False)
df["rating_count"]=pd.to_numeric((df["rating_count"]))

print(df["discount_percentage"].head())
df["discount_percentage"]=df["discount_percentage"].str.replace("%","",regex=False)
df["discount_percentage"]=pd.to_numeric(df["discount_percentage"])

#drop the columns that are not needed for analysis
columns_to_drop=[
    "product_link",
    "review_id",
    "review_content",
    "img_link"
]
df.drop(columns=columns_to_drop,inplace=True)

#generating maningful feature
df["discount_amount_rupees"]=df["actual_price"]-df["discounted_price"]

print(df.dtypes)
print("Rows" , df.shape[0])
print("Columns",df.shape[1])

df.to_csv("amazon_cleaned_data.csv",index=False)
print("Cleaned dataset exported successfully!")