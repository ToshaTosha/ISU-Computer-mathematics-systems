import gaus.logic_gaus as g


def test_gauss():
    """Решение СЛАУ (метод Жордана-Гаусса):"""
    mxA = [
        [1, 3],
        [3, 3]
    ]
    mxB = [[2], [7]]
    exp = [[1.0, 0.0, 2.5], [-0.0, 1.0, -1.0]]
    res = g.gauss(mxA, mxB)
    assert res == exp
