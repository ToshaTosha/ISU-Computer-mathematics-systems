import matplotlib.pyplot as plt

import interpolation.logic_piece_linear_interpolation as interpolation

data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
x = []
y = []
for i in range(len(data_xy)):
    x.append(data_xy[i][0])
    y.append(data_xy[i][1])

x_i = [-1.5, 3, 5]
res_i = interpolation.piece_interpolation(x_i, data_xy)

plt.plot(x, y)
plt.plot(x_i, res_i, 'ro')
plt.show()
