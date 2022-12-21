import matplotlib.pyplot as plt

import interpolation.logic_linear_interpolation_and_extrapolation as interpolation

data_xy = [[2, 5], [6, 9]]
x = []
y = []
for i in range(len(data_xy)):
    x.append(data_xy[i][0])
    y.append(data_xy[i][1])

x_i = 4
res_i = interpolation.linear_interpolation_and_extrapolation(data_xy, x_i)

x_e = 1
res_e = interpolation.linear_interpolation_and_extrapolation(data_xy, x_e)

plt.plot(x, y)
plt.plot(x_i, res_i, 'ro')
plt.plot(x_e, res_e, 'ro')
plt.show()
