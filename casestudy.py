import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('idealstudentlife.csv')

df = df.rename(columns = {'Q1-How many events have you Volunteered in ?':'Volunteered',
       'Q2-How many events have you Participated in ?':'Participated',
       'Q3-How many activities are you Interested in ?':'Interested_Activities',
       'Q4-How many activities are you Passionate about ?':'Passionate_Activities',
       'Q5-What are your levels of stress ?':'Stress_Levels',
       'Q6-How Satisfied You are with your Student Life ?':'Student_life_Satisfaction',
       'Q7-How much effort do you make to interact with others ?':'Effort_to_interact'})

cols_drop = ['Q9-What is an ideal student life ?','Q8-About How events are you aware about ?']
df = df.drop(cols_drop, axis = 1)
print(df.head())
print(df.info())
print(df.columns)
