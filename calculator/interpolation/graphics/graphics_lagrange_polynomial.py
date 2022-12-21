import matplotlib.pyplot as plt

import interpolation.logic_lagrange_polynomial as lagrange

data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
res = lagrange.lagrange(data_xy, x)

plt.plot(x, res)
plt.show()
