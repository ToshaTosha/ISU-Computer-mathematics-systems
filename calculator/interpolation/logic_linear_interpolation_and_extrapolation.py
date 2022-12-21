import gaus.logic_gaus as g
import matrix.logic_matrix as m


# data_xy = [[2, 5],[6, 9]] => mx_a = [[2, 1], [6, 1]], mx_b = [[5], [9]]
def create_two_arr(data_xy):
    matrix = m.do_copy(data_xy)
    mx_a = []
    mx_b = []
    for i in range(len(matrix)):
        mx_a.append([matrix[i][0], 1])
        mx_b.append([matrix[i][1]])
    return mx_a, mx_b


def linear_interpolation_and_extrapolation(data_xy, x):
    mx_a, mx_b = create_two_arr(data_xy)
    res = g.gauss(mx_a, mx_b)

    a = res[0][2]
    b = res[1][2]
    y = a * x + b

    return y
