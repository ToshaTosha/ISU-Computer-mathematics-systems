import matrix.logic_matrix as matrix


def test_sum():
    '''Сложение матриц:'''
    a = [[1, 2], [3, 4]]
    b = [[3, 4], [-1, 3]]
    exp = [[4, 6], [2, 7]]
    res = matrix.sum(a, b)
    assert res == exp


def test_sub():
    '''Вычитание матриц'''
    a = [[6, 7], [-4, 3]]
    b = [[1, 3], [2, -5]]
    exp = [[5, 4], [-6, 8]]
    res = matrix.sub(a, b)
    assert res == exp


def test_scalar_matrix():
    '''Умножение матрицы на скаляр'''
    a = [[1, 2], [3, 4]]
    scalar = 2
    exp = [[2, 4], [6, 8]]
    res = matrix.scalar_matrix(a, scalar)
    assert res == exp


def test_summa():
    '''Умножение матриц'''
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    exp = [[19, 22], [43, 50]]
    res = matrix.matrix_multiplication(a, b)
    assert res == exp


def test_transposition():
    '''Транспонирование матрицы'''
    a = [2, 3, 5]
    exp = [[2], [3], [5]]
    res = matrix.transposition(a)
    assert res == exp


def test_number_index():
    '''Получение строки по индексу'''
    matrix_a = [[2, 3, 5], [5, 7, 6]]
    a = 1
    exp = [5, 7, 6]
    res = matrix.number_index(matrix_a, a)
    assert res == exp


def test_column_index():
    '''Получение столбца по индексу'''
    matrix_a = [[2, 3, 5], [5, 7, 6]]
    a = 1
    exp = [3, 7]
    res = matrix.column_index(matrix_a, a)
    assert res == exp


def test_permutations_str():
    '''Перестановка строк матрицы местами'''
    matrix_a = [[2, 3, 5], [5, 7, 6]]
    a = 1
    b = 0
    exp = [[5, 7, 6], [2, 3, 5]]
    res = matrix.permutations_str(matrix_a, a, b)
    assert res == exp


def test_mult_str():
    '''умножение на скаляр одной строки'''
    matrix_a = [[2, 3, 5], [5, 7, 6]]
    a = 0
    scalar = 2
    exp = [[4, 6, 10], [5, 7, 6]]
    res = matrix.mult_str(matrix_a, a, scalar)

    # assert res == exp
