from math import pi

def factorial(a):
    ''' Факториал '''
    product = 1
    for i in range(2, a + 1):
        product *= i
    return product


def maclaurin_exp(x, n):
    ''' e^x '''
    summ = 0
    for i in range(0, n + 1):
        summ += x ** i / factorial(i)
    return summ

def maclaurin_sin(x, n):
    ''' sinx '''
    summ = 0
    for i in range(0, n + 1):
        summ += ((-1) ** i / factorial(2 * i + 1)) * (x ** (2 * i + 1))
    return summ

def maclaurin_cos(x, n):
    ''' cosx '''
    summ = 0
    for i in range(0, n + 1):
        summ += ((-1) ** i / factorial(2 * i)) * (x ** (2 * i))
    return summ


def maclaurin_arcsin(x, n):
    ''' arcsinx '''
    summ = 0
    for i in range(0, n + 1):
        summ += (factorial(2 * i) * x ** (2 * i + 1)) / ((4 ** i) * (factorial(i) ** 2) * (2 * i + 1))
    return summ


def maclaurin_arccos(x, n):
    ''' arccosx '''
    return (pi / 2) - maclaurin_arcsin(x, n)
