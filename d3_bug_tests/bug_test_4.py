#minor ticks are not rotated when formatted
#want them to be formatted along with the major ticks

#need to add a which parameter to def autofmt_xdate(self, bottom=0.2, rotation=30, ha='right'): in figure
#that will update the specified ticks, defaults to major


import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange

date1 = datetime.datetime(2017, 3, 2)
date2 = datetime.datetime(2017, 3, 4)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)

y = arange(len(dates)*1.0)

fig, ax = plt.subplots()
ax.plot_date(dates, y*y)

ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(arange(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.xaxis.set_minor_formatter(DateFormatter('%H:%M'))

ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()

plt.show()
