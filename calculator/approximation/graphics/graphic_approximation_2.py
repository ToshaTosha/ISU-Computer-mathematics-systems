import matplotlib.pyplot as plt
import numpy as np

import approximation.approximation_logic as a

# create 1000 equally spaced points between -10 and 10
x = np.linspace(-10, 10, 1000)

# calculate the y value for each element of the x vector
y = 0.13 * x ** 2 + 0.07 * 2 * x + 1.89

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()

data_xy = [[1, 2],
           [3, 4],
           [3.5, 3],
           [6, 7]]
any_x = [[1], [3], [5]]
res = a.approximation(data_xy, a.degree_two, any_x)
x = []
y = []
for i in range(len(data_xy)):
    x.append(data_xy[i][0])
    y.append(data_xy[i][1])

plt.plot(x, y, 'ro', color='b')
plt.plot(any_x, res, 'ro')

plt.show()
