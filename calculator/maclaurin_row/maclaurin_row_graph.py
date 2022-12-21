import matplotlib.pyplot as plt
import numpy as np
from math import *
import maclaurin_row.maclaurin_row_logic as m

def draw_graph(x_data, y_data):
    plt.ylim(ymax=max(y_data))
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.plot(x_data, y_data, color="orange")
    plt.grid()
    plt.show()

def maclaurin_row(val, n):
    x_data = [i / 10 for i in range(-50, 50)]
    y_data = 0
    if val == 'exp':
        y_exp = [exp(X) for X in x_data]
        plt.plot(x_data, y_exp, color="blue")
        y_data = [m.maclaurin_exp(X, n) for X in x_data]

    elif val == 'sin':
        y_sin = [sin(X) for X in x_data]
        plt.plot(x_data, y_sin, color="blue")
        y_data = [m.maclaurin_sin(X, n) for X in x_data]

    elif val == 'cos':
        y_cos = [cos(X) for X in x_data]
        plt.plot(x_data, y_cos, color="blue")
        y_data = [m.maclaurin_cos(X, n) for X in x_data]

    elif val == 'arcsin':
        plt.plot(x_data, np.arcsin(x_data), color="blue")
        y_data = [m.maclaurin_arcsin(X, n) for X in x_data]

    elif val == 'arccos':
        plt.plot(x_data, np.arccos(x_data), color="blue")
        y_data = [m.maclaurin_arccos(X, n) for X in x_data]


    draw_graph(x_data, y_data)

def test_graphs():
    maclaurin_row('exp', 2)
    maclaurin_row('sin', 1)
    maclaurin_row('cos', 5)
    maclaurin_row('arcsin', 0)
    maclaurin_row('arccos', 0)

test_graphs()