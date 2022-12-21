import gaus.logic_gaus as g
import interpolation.logic_linear_interpolation_and_extrapolation as l


def learn(data_xy):
    mx_a, mx_b = l.create_two_arr(data_xy)
    model = []
    for i in range(len(mx_a) - 1):
        res = g.gauss(mx_a[i:i + 2], mx_b[i:i + 2])
        a = res[0][2]
        b = res[1][2]
        model.append([a, b])

    return model


def fit(model, data_xy, x):
    ind = i_iterval(data_xy, x)
    model_row = model[ind]
    a = model_row[0]
    b = model_row[1]
    y = a * x + b
    return y


def i_iterval(data_xy, x):
    if x <= data_xy[0][0]:
        return 0
    else:
        for i in range(len(data_xy)):
            if data_xy[i][0] <= x < data_xy[i + 1][0]:
                return i


def piece_interpolation(x, data_xy):
    arr = []
    model = learn(data_xy)
    for i in range(len(x)):
        arr.append(fit(model, data_xy, x[i]))
    return arr
