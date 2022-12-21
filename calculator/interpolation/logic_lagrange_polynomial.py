def lagrange_E(data_xy, x, E):
    for i in range(len(data_xy)):
        P = 1
        for j in range(len(data_xy)):
            if data_xy[j] != data_xy[i]:
                t = data_xy[j][0]
                m = data_xy[i][0]
                P = P * ((x - t) / (m - t))
        E += P * data_xy[i][1]
    return E


def lagrange(data_xy, x):
    y = []
    for i in range(len(x)):
        E = 0
        y.append(lagrange_E(data_xy, x[i], E))
    return y
