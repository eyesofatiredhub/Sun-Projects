import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Admission_Predict.csv")
print (df.columns)
df = df.set_index(df["Serial No."])
df = df.drop("Serial No.", axis = 1)
#print(df.head())

df.rename(columns={'Chance of Admit ': 'Chance of Admit', 'LOR ': 'LOR'}, inplace=True)

def remove_outliers(column):

    q25, q50, q75 = np.percentile(df[column], [25, 70, 75])
    iqr = q75 - q25
    min = q25 - 1.5 * (iqr)
    max = q75 + 1.5 * (iqr)
    outliers = [x for x in df[column] if x > max or x < min]
    print(column,":", outliers)
    return outliers


print(df.shape)
for column in df.columns:
    outliers = remove_outliers(column)




#plt.figure(figsize=(15, 6))
#plt.bar(df["GRE Score"], df["Chance of Admit"], color = "teal")
#plt.title("GRE Score and Chance of Acceptance")
#plt.show()


