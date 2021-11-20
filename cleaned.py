import csv
import pandas as pd

df = pd.read_csv("finaloutput.csv")
# print(df.columns)

df.drop(['Unnamed: 0','Unnamed: 6', 'name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'], axis= 1, inplace= True)

finaloutput = df.dropna()
finaloutput.reset_index(drop=True,inplace = True)

# finaloutput.to_csv("final.csv")
print(finaloutput.head())
print(finaloutput.dtypes)
