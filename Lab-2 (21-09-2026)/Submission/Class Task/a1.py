import pandas as pd

df = pd.read_csv("content/Admission_Predict.csv")

# Clean up column names by removing leading/trailing spaces
df.columns = df.columns.str.strip()

# Drop the correct serial number column
df.drop("Serial No.", axis=1, inplace=True)

# Define y (the trailing space is no longer needed due to strip)
y = df['Chance of Admit']

# Drop the target variable from the features dataframe
df.drop("Chance of Admit", axis=1, inplace=True)

df.head()

print(df.head())

import pandas as pd
df=pd.read_csv("content/Admission_Predict.csv")
columns=df.columns
df.drop("Serial No.",axis=1,inplace=True)
y = df['Chance of Admit']
df.drop("Chance of Admit",axis=1,inplace=True)
df.head()