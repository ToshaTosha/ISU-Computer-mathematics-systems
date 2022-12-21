'''
import math
def e_x(x, n):
    res = 0
    for i in range(n):
        res += x ** n / math.factorial(n)
    return res
print(e_x(1, 5))

import numpy as np

vmysin = np.vectorize(mysin, excluded=['order'])

x = np.linspace(-80, 80, 500)
y2 = vmysin(x, 2)
y10 = vmysin(x, 10)
y = np.sin(x)

import matplotlib.pyplot as plt

plt.plot(x, y, label='sin(x)')
plt.plot(x, y2, label='order 2')
plt.plot(x, y10, label='order 10')
plt.ylim([-3, 3])
plt.legend()
plt.show()
'''

import math

x = float((input('x ? ')))
n = 5
b = 0
for i in range(n):
    a = (((((-1) ** i)) * (x ** ((2 * i) + 1))) / (math.factorial((2 * i) + 1)))
    b += a
print(b)
