import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature

data = pd.read_csv("bird_tracking.csv")
data = data.dropna()
#print(data.head())
#index = data.bird_name == "Eric"
#x, y = data.longitude[index], data.latitude[index]
#plt.plot(x,y, "ro")

bird_names = pd.unique(data.bird_name)
#print(bird_names)

for bird in bird_names:
    index = data.bird_name == bird
    x, y = data.longitude[index], data.latitude[index]
    plt.plot(x, y,".")
#plt.legend(loc = "lower right")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("migration patterns")
plt.show()

index = data.bird_name == "Eric"
speed = data.speed_2d[index]
ind = np.isnan(speed)
plt.hist(speed[~ind], color = "teal",bins=np.linspace(0,30,20)) #the first bin starts at 0 and the last bin ends as 30
plt.show()
speed.plot(kind= "hist", range=[0,30])
plt.show()
#print(data.date_time[0:3])
date_str = data.date_time[0]
#print(date_str[:-3])
x = datetime.datetime.strptime(date_str[:-3],"%Y-%m-%d %H:%M:%S")
#print(type(x), x)

timestamps = []
for i in range(len(data)):
    time = datetime.datetime.strptime(data.date_time.iloc[i][:-3],"%Y-%m-%d %H:%M:%S")
    timestamps.append(time)
#print(timestamps)

data["timestamp"] = pd.Series(timestamps, index = data.index)
del data["date_time"]
#print(data.head())

times = data.timestamp[data.bird_name =="Eric"]
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time)/ datetime.timedelta(days = 1)
#print(elapsed_days)

plt.plot(np.array(elapsed_time)/datetime.timedelta(days = 1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time(days)")
plt.show()

#next_day = 1
#inds = []
#daily_mean_list=[]
#my_list = pd.Series(data.speed_2d)
#or (i,t) in enumerate(elapsed_days):
    #if t < next_day:
        #inds.append(i)
    #else:
        #mean = np.mean(my_list[ind])
        #daily_mean_list.append(mean)
        #next_day+=1
        #inds = []
#daily_mean_list= pd.Series(daily_mean_list)
#plt.figure(figsize=(8,6))
#plt.plot(daily_mean_list)
#plt.xlabel("day")
#plt.ylabel("daily mean speed")
#plt.show()

proj = ccrs.Mercator()
plt.figure(figsize=(8,6))
ax = plt.axes(projection = proj)
ax.set_extent((-25,-20,52,10))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle = ":")
for bird in bird_names:
    index = data.bird_name == bird
    x, y = data.longitude[index], data.latitude[index]
    ax.plot(x,y, ".", transform = ccrs.Geodetic(), label = bird)
plt.legend(loc = "upper left")
plt.show()


