import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cartwheeldata.csv")
data = data.dropna()
print(data.columns)
data = data.loc[:,["Gender","Complete"]]
print(data.head())
plt.plot(data["Gender"],data["Complete"])
plt.show()