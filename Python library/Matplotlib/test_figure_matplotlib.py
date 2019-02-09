import matplotlib.cbook as cbook
import matplotlib.dates as mdates
import numpy as np
import matplotlib.pyplot as plt


with cbook.get_sample_data('goog.npz') as datafile:
    r = np.load(datafile)['price_data'].view(np.recarray)

# Matplotlib prefers datetime instead of np.datetime64.
date = r.date.astype('O')
fig, ax = plt.subplots()
ax.plot(date, r.close)

# rotate and align the tick labels so they look better
fig.autofmt_xdate()

# use a more precise date string for the x axis locations in the
# toolbar
ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.set_title('fig.autofmt_xdate fixes the labels')
plt.show()