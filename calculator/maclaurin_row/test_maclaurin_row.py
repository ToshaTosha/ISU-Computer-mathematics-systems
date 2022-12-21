import gaus.logic_gaus as g
import maclaurin_row.maclaurin_row_logic as m


def test_exp():
    """e^x"""
    n = 5
    x = 2
    exp = 7.266666666666667
    res = m.maclaurin_exp(x, n)
    assert res == exp

def test_sinx():
    """sinx"""
    n = 5
    x = 1.5
    exp = 0.9974949556821353
    res = m.maclaurin_sin(x, n)
    assert res == exp

def test_cosx():
    """cosx"""
    n = 5
    x = 5
    exp = -0.16274663800705724
    res = m.maclaurin_cos(x, n)
    assert res == exp

def test_arcsin():
    """arcsin"""
    n = 3
    x = 1
    exp = 1.286309523809524
    res = m.maclaurin_arcsin(x, n)
    assert res == exp

def test_arccos():
    """arccos"""
    n = 2
    x = 1
    exp = 0.32912966012822986
    res = m.maclaurin_arccos(x, n)
    assert res == exp