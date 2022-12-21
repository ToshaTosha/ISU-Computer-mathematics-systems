import interpolation.logic_linear_interpolation_and_extrapolation as interpolation


def test_interpolation():
    """Линейная интерполяция:"""
    data_xy = [[2, 5], [6, 9]]
    x = 4
    exp = 7
    res = interpolation.linear_interpolation_and_extrapolation(data_xy, x)
    assert res == exp


def test_extrapolation():
    """Линейная экстраполяция:"""
    data_xy = [[2, 5], [6, 9]]
    x = 1
    exp = 4
    res = interpolation.linear_interpolation_and_extrapolation(data_xy, x)
    assert res == exp
