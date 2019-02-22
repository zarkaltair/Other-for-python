import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


x = [0,5,9,10,15]
y = [0,1,2,3,4]

fig, ax = plt.subplots()
ax.plot(x,y)

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
plt.show()