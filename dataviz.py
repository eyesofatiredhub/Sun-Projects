import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib


for name, hex in matplotlib.colors.cnames.items():
    print(name,hex)

# with pandas df.plot(kind = "line")
#df["column"].plot(kind="hist")

df = pd.read_excel("Canada.xlsx", sheet_name="Canada by Citizenship", skiprows = range(20),skipfooter = 2)
df = df.dropna()
#df = df.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
del df["Type"]
del df["Coverage"]
del df["REG"]
del df["AREA"]
del df["DEV"]
#holy hell why tf couldn't you put them on a list
df = df.set_index(df["OdName"], drop = True)
del df["OdName"]

print(df.head())
df["Total"] = df.sum(axis=1)
years = list(range(1980,2014))
df.loc["Nepal",years].plot(kind="line", color ="cyan")
plt.title("Immigrants from Nepal over the years")
plt.xlabel("years")
plt.ylabel("no.of immigrants")
plt.show()


df= df.sort_values( by="Total", ascending= False)
df_top5 = df.head()
df_top5= df_top5[years].T
df_top5.plot(kind = "area", color=["turquoise","tomato","sienna","violet","springgreen"])
plt.title("immigration trend of the top 5 countries")
plt.ylabel("Number of immigrants")
plt.xlabel("years")
plt.show()

#df[2012].plot(kind = "hist")
#plt.show()

count, bin_edges = np.histogram(df[2013])
df[2013].plot(kind = "hist", xticks = bin_edges, bins = 15, color ="darkcyan")
plt.title("histogram")
plt.show()


df_iceland = df.loc["Iceland",years]
df_iceland.plot(kind = "barh",color = "teal")
plt.title("Iceland Immigration")
plt.show()


df_scan = df.loc[["Denmark","Norway","Sweden"],years].T
df_scan.plot(kind ="hist", figsize=(15,10),alpha = 0.6 , color=["coral","darkslateblue","mediumseagreen"], stacked = True)
plt.title("From Denmark, Norway and Swewden")
plt.show()

years = list(range(1980,2013))
df_years = pd.DataFrame(df[years].sum(axis = 0))
df_years = df_years.reset_index(drop=False)
df_years.columns = ["year", "total"]