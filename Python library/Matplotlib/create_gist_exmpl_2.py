import numpy as np
import matplotlib.pyplot as plt


plt.style.use('seaborn-deep')

x = np.random.normal(1, 2, 5000)
y = np.random.normal(-1, 3, 5000)
data = np.vstack([x, y]).T
bins = np.linspace(-10, 10, 30)

plt.hist(data, bins, alpha=0.7, label=['x', 'y'])
plt.legend(loc='upper right')
plt.show()