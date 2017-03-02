#should not give error, try removing locator.MAXTICKS
#set MAXTICKS to none in https://github.com/matplotlib/matplotlib/blob/91261e7646947910e6c8d3f4a44eee774e8e3686/lib/matplotlib/ticker.py

import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

num_list=[]
date_list=[]

#Create List of Datetime Objects to Plot on X Axis
start = datetime.datetime(2017 , 2, 15)
end = datetime.datetime(2017, 2, 15, 15, 10, 0)

step=datetime.timedelta(minutes=1)

while start < end:
    date_list.append(start)
    start+=step

#Create List of Numbers to Plot on Y Axis
num=0
lastnum=len(date_list)

while num < lastnum:
    num_list.append(num)
    num+=1

locator = mpl.dates.MinuteLocator(interval=1)

fig, (ax1,ax2) = plt.subplots(2)

ax1.plot_date(date_list,num_list,'b.')
ax2.plot_date(date_list,num_list,'r.')

plt.gca().xaxis.set_major_locator(locator)

plt.show()
