import approximation.approximation_logic as a


def test_linear_approximation():
    """Линейная аппроксимация:"""
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    any_x = [[1], [3], [5]]
    exp = [[1.660098522167488], [3.6305418719211824], [5.600985221674877]]
    res = a.approximation(data_xy, a.degree_one, any_x)
    assert res == exp


def test_linear_approximation_2_degree():
    """Линейная аппроксимация:"""
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    any_x = [[1], [3], [5]]
    exp = [[2.0889621087314683], [3.2586490939044466], [5.456342668863261]]
    res = a.approximation(data_xy, a.degree_two, any_x)
    assert res == exp


def test_linear_approximation_3_degree():
    """Линейная аппроксимация:"""
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    any_x = [[1], [3], [5]]
    exp = [[2.0000000000000515], [3.9999999999995293], [2.160000000002116]]
    res = a.approximation(data_xy, a.degree_three, any_x)
    assert res == exp
