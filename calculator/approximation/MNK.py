import gaus.logic_gaus as g
import matrix.logic_matrix as m


def MNK(A, b):
    A_til = m.matrix_multiplication(m.transposition(A), A)
    b_til = m.matrix_multiplication(m.transposition(A), b)

    return g.gauss(A_til, b_til)
