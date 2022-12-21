import interpolation.logic_lagrange_polynomial as lagrange


def test_interpolation():
    """Полином Лагранжа:"""
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [1, 2, 3, 4, 5]
    exp = [2.0, 4.92, 4.0, 2.12, 2.160000000000002]
    res = lagrange.lagrange(data_xy, x)
    assert res == exp
