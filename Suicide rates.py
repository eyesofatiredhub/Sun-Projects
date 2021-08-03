import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("master.csv")
del df["generation"]
df.index = df.country
del df["country"]


df_num = pd.DataFrame(index=df.index, columns=["number","sex"])
df_num["number"] = df.suicides_no
df_num["sex"] = df.sex
#df_num.plot(color = "teal")

countries = set(df_num.index)
total_suicides = {}
for country in countries:
    df_country = df_num[df.index == country]
    total = df_country["number"].sum()
    total_suicides[country] = total
df_with_total = pd.DataFrame.from_dict(total_suicides, orient="index", columns=["total_number"])
df_with_total = df_with_total.sort_values(by = "total_number", ascending=False)
df_with_total = df_with_total.head(20)


def plot_total():
    df_with_total.plot(kind = "bar", color = "tomato", figsize = (12,8))
    plt.ylabel("total number of suicides")
    plt.xlabel("countries")
    plt.title("top 20 countries with the most suicides")
    plt.show()


male = {}
for country in countries:
    df_country_male = df_num[df_num.sex =="male"]
    df_country_male = df_country_male[df_country_male.index == country]
    male[country] = df_country_male["number"].sum()


female = {}
for country in countries:
    df_country_female = df_num[df_num.sex =="female"]
    df_country_female = df_country_female[df_country_female.index == country]
    female[country] = df_country_female["number"].sum()


df_with_total_males = pd.DataFrame.from_dict(male, orient="index", columns=["total_number_males"])
df_with_total_males = df_with_total_males.sort_values(by = "total_number_males", ascending=False)
df_with_total_females = pd.DataFrame.from_dict(female, orient="index", columns=["total_number_females"])
df_with_total_females = df_with_total_females.sort_values(by = "total_number_females", ascending=False)
dfs = [df_with_total_females, df_with_total_males]
finaldf = pd.concat(dfs, join = "inner", axis = 1)
finaldf = finaldf.head(15)

def plot_final_sex():
    finaldf.plot(kind = "bar", color = ["coral", "darkslateblue"])
    plt.title("suicide rates sorted by gender")
    plt.xlabel("countries")
    plt.ylabel("total number of suicides")
    plt.show()

