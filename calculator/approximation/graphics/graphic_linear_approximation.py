import matplotlib.pyplot as plt
import numpy as np

import approximation.approximation_logic as a

x = np.linspace(-10, 10, 1000)
y = 0.99 * x + 0.67

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()

data_xy = [[1, 2],
           [3, 4],
           [3.5, 3],
           [6, 7]]
any_x = [[1], [3], [5]]
res = a.approximation(data_xy, a.degree_one, any_x)
x = []
y = []
for i in range(len(data_xy)):
    x.append(data_xy[i][0])
    y.append(data_xy[i][1])

plt.plot(x, y, 'ro', color='b')
plt.plot(any_x, res, 'ro')

plt.show()
