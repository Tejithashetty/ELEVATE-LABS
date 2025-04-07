import pandas as pd
import numpy as np
fname="/content/marketing_campaign.csv"
df=pd.read_csv(fname,sep="\t")
print(df.head())
print(df.info())
print(df.columns.tolist())
cdf=cdf.dropna()
print("After removing missing values",len(df))
cdf=cdf.drop_duplicates()
print(cdf)
len(cdf.ID.unique())
print(cdf.Education.value_counts())
cdf["Dt_Customer"] = pd.to_datetime(cdf["Dt_Customer"],dayfirst=True)
dates = []
for i in cdf["Dt_Customer"]:
    i = i.date()
    dates.append(i)  
#Dates of the newest and oldest recorded customer
print("The newest customer's enrolment date in therecords:",max(dates))
print("The oldest customer's enrolment date in the records:",min(dates))
print(dates)
days = []
d1 = max(dates) #taking it to be the newest customer
for i in dates:
    delta = d1 - i
    days.append(delta)
    
cdf["Customer_For"] = days#represent days

cdf["Customer_For"] = pd.to_numeric(cdf["Customer_For"], errors="coerce")# represents nano seconds
print("Total categories in the column Marital_Status:\n", cdf["Marital_Status"].value_counts(), "\n")
print("Total categories in the column Education:\n", cdf["Education"].value_counts())
cdf.columns = cdf.columns.str.lower().str.replace(' ', '_')
cdf['income'] = cdf['income'].astype(float)
cdf.to_csv("cleaned_marketing_campaign.csv", index=False)
print(cdf)
print("***Dataset cleaned successfully.***")
print(f"Original rows: {len(df)}")
print(f"Rows after cleaning: {len(cdf)}")
print(f"Missing 'Income' rows removed: {df['income'].isnull().sum()}")
print(f"Duplicates removed: {df.duplicated().sum()}")
print("Date format converted: dt_customer →", cdf['dt_customer'].dtype)
print("Columns renamed:\n", list(cdf.columns))
