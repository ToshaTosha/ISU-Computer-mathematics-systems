import approximation.MNK as a


def test_MNK_one():
    """пример с одной неизвестной"""
    A = [[2], [3]]
    b = [[4], [9]]
    exp = [[1.0, 2.6923076923076925]]
    res = a.MNK(A, b)
    assert res == exp


def test_MNK_two():
    """пример с двумя неизвестной"""
    A = [[2, 3], [3, 3], [4, 7]]
    b = [[7], [7], [3]]
    exp = [[1.0, 0.0, 4.680851063829789], [0.0, 1.0, -2.063829787234044]]
    res = a.MNK(A, b)
    assert res == exp
