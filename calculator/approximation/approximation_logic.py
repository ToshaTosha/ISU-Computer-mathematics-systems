import gaus.logic_gaus as g
import matrix.logic_matrix as m


# Линейная аппроксимация
def degree_one(x):
    '''[x, 1]'''
    return [x, 1]


# Аппроксимация полиномом 2-й степени
def degree_two(x):
    '''[x^2, x, 1]'''
    return [x ** 2, x, 1]


# Аппроксимация полиномом 3-й степени
def degree_three(x):
    '''[x^3, x^2, x, 1]'''
    return [x ** 3, x ** 2, x, 1]


def get_arr(A, func):
    a = []
    b = []
    for i in range(len(A)):
        a.append(func(A[i][0]))
        b.append([A[i][-1]])
    return a, b


def approximation(data_xy, degree, any_x):
    A, b = get_arr(data_xy, degree)

    A_til = m.matrix_multiplication(m.transposition(A), A)
    b_til = m.matrix_multiplication(m.transposition(A), b)

    x = []

    for i in range(len(g.gauss(A_til, b_til))):
        x.append([g.gauss(A_til, b_til)[i][-1]])

    x_til, b = get_arr(any_x, degree)
    y = m.matrix_multiplication(x_til, x)
    return y
