from vectors import logic_vector as vec


def do_copy(matrix):
    new_matrix = matrix
    return new_matrix


def copy_matrix(a, do_copy=True):
    if do_copy:
        return [b[:] for b in a]
    return a


def scalar_matrix(matrix_a, scalar):
    '''умножение на скаляр'''
    res = []
    for i in range(len(matrix_a)):
        res.append(vec.mult_scalar(matrix_a[i], scalar))
    return res


def div_matrix(matrix_a, scalar):
    '''деление на скаляр'''
    res = []
    for i in range(len(matrix_a)):
        res.append(vec.div_scalar(matrix_a[i], scalar))
    return res


def sum(matrix_a, matrix_b):
    '''сложение'''
    if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
        res = []
        for i in range(len(matrix_a)):
            res.append(vec.summ(matrix_a[i], matrix_b[i]))
        return res
    else:
        raise ValueError("Невозможно выполнить оперцию!")


def sub(matrix_a, matrix_b):
    '''вычиатание'''
    if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
        res = []
        for i in range(len(matrix_a)):
            res.append(vec.sub(matrix_a[i], matrix_b[i]))
        return res
    else:
        raise ValueError("Невозможно выполнить оперцию!")


def transposition(matrix_a):
    '''
    транспанирование
    сделать транспонирование для одномерной матрицы
    '''
    null_matrix = [[0 for j in range(len(matrix_a))] for i in range(len(matrix_a[0]))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            null_matrix[j][i] = matrix_a[i][j]
    return null_matrix


def permutations_str(matrix_a, a, b):
    '''перестановка строк местами'''
    # matrix = do_copy(matrix_a)
    if (len(matrix_a) <= a) or (len(matrix_a) <= b):
        raise ValueError("Невозможно выполнить оперцию!")
    else:
        matrix_a[a], matrix_a[b] = matrix_a[b], matrix_a[a]
        return matrix_a


def mult_str(matrix_a, n, scalar, do_copy=True):
    '''умножение на скаляр одной строки'''
    a = copy_matrix(matrix_a, do_copy)
    return vec.mult_scalar(number_index(a, n), scalar)


def div_str(matrix_a, a, scalar):
    '''деление на скаляр одной строки'''
    matrix = do_copy(matrix_a)
    if len(matrix) <= a:
        raise ValueError("Неверный размер!")
    else:
        for j in range(len(matrix[a])):
            matrix[a][j] = matrix[a][j] / scalar
        return matrix


def number_index(matrix_a, a):
    '''Получение строки по индексу'''
    return matrix_a[a]


def column_index(matrix_a, i):
    '''Получение столбца по индексу'''
    column = transposition(matrix_a)
    return column[i]


def mult_strs(matrix_a, num_a, matrix_b, num_b, n):
    '''Вычитание строки из другой строки умноженной на число'''
    return vec.sub(matrix_a[num_a], mult_str(matrix_b, num_b, n))


def matrix_multiplication(matrix_a, matrix_b):
    '''умножение матриц'''
    s = 0
    t = []
    res = []
    if len(matrix_b) != len(matrix_a[0]):
        raise ValueError("Матрицы не могут быть перемножены!")
    else:
        for z in range(0, len(matrix_a)):
            for j in range(0, len(matrix_b[0])):
                for i in range(0, len(matrix_a[0])):
                    s = s + matrix_a[z][i] * matrix_b[i][j]
                t.append(s)
                s = 0
            res.append(t)
            t = []
        return res


def one_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def connect_matrix(a, e):
    ab = []
    for i in range(len(a)):
        a_new = number_index(a, i)
        for j in range(len(e)):
            a_new.append(e[i][j])
        ab.append(a_new)
    return ab
