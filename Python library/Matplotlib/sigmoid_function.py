import numpy as np
import matplotlib.pylab as plt

'''
x = np.arange(-8, 8, 0.1)
f = 1 / (1 + np.exp(-x))
plt.plot(x, f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
'''
'''
x = np.arange(-8, 8, 0.1)
w1 = 0.5
w2 = 1.0
w3 = 2.0
l1 = 'w = 0.5'
l2 = 'w = 1.0'
l3 = 'w = 2.0'
# for w, l in [(w1, l1), (w2, l2), (w3, l3)]:
#     f = 1 / (1 + np.exp(-x * w))
f1 = 1 / (1 + np.exp(-x * w1))
f2 = 1 / (1 + np.exp(-x * w2))
f3 = 1 / (1 + np.exp(-x * w3))
plt.plot(x, f1, label=l1)
plt.plot(x, f2, label=l2)
plt.plot(x, f3, label=l3)
plt.xlabel('x')
plt.ylabel('h_w(x)')
plt.legend(loc=2)
plt.grid(True)
plt.show()
'''

x = np.arange(-8, 8, 0.1)
w = 5.0
b1 = -8.0
b2 = 0.0
b3 = 8.0
l1 = 'b = -8.0'
l2 = 'b = 0.0'
l3 = 'b = 8.0'
# for b, l in [(b1, l1), (b2, l2), (b3, l3)]:
#     f = 1 / (1 + np.exp(-(x * w + b)))
# plt.plot(x, f, label=l)
f1 = 1 / (1 + np.exp(-x * w + b1))
f2 = 1 / (1 + np.exp(-x * w + b2))
f3 = 1 / (1 + np.exp(-x * w + b3))
plt.plot(x, f1, label=l1)
plt.plot(x, f2, label=l2)
plt.plot(x, f3, label=l3)
plt.xlabel('x')
plt.ylabel('h_wb(x)')
plt.legend(loc=2)
plt.grid(True)
plt.show()