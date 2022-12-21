import gaus.logic_gaus as g
import matrix.logic_matrix as matrix


def inverse(a):
    mxNull = (matrix.one_matrix(len(a)))
    return g.gauss(a, mxNull)
