import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Generate a series of dates (these are in matplotlib internal date format)
dates = mdates.drange(dt.datetime(2010, 1, 1), 
					  dt.datetime(2012, 11, 1), 
                      dt.timedelta(weeks=3))

# Create some data for the y-axis
counts = np.sin(np.linspace(0, np.pi, dates.size))

# Set up the axes and figure
fig, ax = plt.subplots()

# By default, the bars will have a width of 0.8 (days, in this case) We want
# them quite a bit wider, so we'll make them them the minimum spacing between
# the dates. (To use the exact code below, you'll need to convert your sequence
# of datetimes into matplotlib float-based date format.  
# Use "dates = mdates.date2num(dates)" to convert them.)
width = np.diff(dates).min()

# Make a bar plot. Note that I'm using "dates" directly instead of plotting
# "counts" against x-values of [0,1,2...]
ax.bar(dates, counts, align='center', width=width)

# Tell matplotlib to interpret the x-axis values as dates
ax.xaxis_date()

# Make space for and rotate the x-axis tick labels
fig.autofmt_xdate()
plt.show()