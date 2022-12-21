import matrix.logic_matrix as matrix

from vectors import logic_vector as vec


def connect_matrix(a, b):
    ab = []
    for i in range(len(a)):
        a_new = matrix.number_index(a, i)
        for k in range(len(b[0])):
            a_new.append(b[i][k])
        ab.append(a_new)
    return ab


def under_diagonal(ab, index):
    if ab[index][index] == 0:
        ab = matrix.permutations_str(ab, index, index + 1)
    ab[index] = vec.div_scalar(ab[index], ab[index][index])
    if index < len(ab):
        for i in range(index + 1, len(ab)):
            ab[i] = matrix.mult_strs(ab, i, ab, index, ab[i][index])
    return ab


def above_diagonal(ab, index):
    ab[index] = vec.div_scalar(ab[index], ab[index][index])

    if index - 1 >= 0:
        i = index - 1
        while i >= 0:
            ab[i] = vec.sub(ab[i], matrix.mult_str(ab, index, ab[i][index]))
            i -= 1
    return ab


def gauss(a, b, do_copy=True):
    a = matrix.copy_matrix(a, do_copy)
    b = matrix.copy_matrix(b, do_copy)
    ab = connect_matrix(a, b)
    for index in range(len(a)):
        ab = under_diagonal(ab, index)
    index = len(a) - 1
    while index > 0:
        ab = above_diagonal(ab, index)
        index -= 1
    return ab
