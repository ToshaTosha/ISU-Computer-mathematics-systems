import inverse_matrix.inverse_matrix as i


def test_inverse():
    '''Поиск обратной матрицы:'''
    mxA = [
        [1, 2],
        [3, 4]
    ]
    exp = [[1.0, 0.0, -2.0, 1.0], [-0.0, 1.0, 1.5, -0.5]]
    res = i.inverse(mxA)
    assert res == exp
