import interpolation.logic_piece_linear_interpolation as interpolation


def test_piece_interpolation():
    """Кусочно-линейная интерполяция:"""
    data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x = [-1.5, 3, 5]
    exp = [-0.5, 4.0, 5.399999999999999]
    res = interpolation.piece_interpolation(x, data_xy)
    assert res == exp
