from math import *


def chek_size(vector_a, vector_b):
    '''проверка длин векторов'''
    if len(vector_a) != len(vector_b):
        raise ValueError("Неверные значения")
    else:
        return len(vector_a)


def summ(vector_a, vector_b):
    '''сумма векторов'''
    summ = []
    for i in range(chek_size(vector_a, vector_b)):
        summ.append(vector_a[i] + vector_b[i])
    return summ


def sub(vector_a, vector_b):
    '''разность векторов'''
    sub = []
    for i in range(chek_size(vector_a, vector_b)):
        sub.append(vector_a[i] - vector_b[i])
    return sub


def mult_scalar(vector, skalar):
    '''умножение на скаляр'''
    mult_skalar = []
    for i in vector:
        mult_skalar.append(i * skalar)
    return mult_skalar


def div_scalar(vector, skalar):
    '''деление на скаляр'''
    div_skalar = []
    for i in vector:
        div_skalar.append(i / skalar)
    return div_skalar


def scalar_product_of_vectors(vector_a, vector_b):
    '''Скалярное произведение векторов'''
    scalar_product_of_vectors = 0
    for i in range(chek_size(vector_a, vector_b)):
        scalar_product_of_vectors += vector_a[i] * vector_b[i]
    return scalar_product_of_vectors


def cos(vector_a, vector_b):
    '''косинус'''
    cos = (scalar_product_of_vectors(vector_a, vector_b)) / ((lenth(vector_a)) * (lenth(vector_b)))
    return cos


def angl(vector_a, vector_b):
    '''угол между векторами'''
    return acos(cos(vector_a, vector_b))


def collinear(vector_a, vector_b):
    '''коллинеарные векторы'''
    if abs(cos(vector_a, vector_b)) == 1:
        return True
    else:
        return False


def co_dir(vector_a, vector_b):
    '''Сонаправленные векторы'''
    if cos(vector_a, vector_b) == 1:
        return True
    else:
        return False


def opp_dir(vector_a, vector_b):
    '''Противоположно направленные векторы'''
    if cos(vector_a, vector_b) == -1:
        return True
    else:
        return False


def equality(vector_a, vector_b):
    '''Равенство векторов'''
    for i in range(chek_size(vector_a, vector_b)):
        if (vector_a[i] == vector_b[i]):
            return True
        else:
            return False


def equality_eps(vector_a, vector_b, eps):
    '''Равенство векторов по заданной точности'''
    for i in range(chek_size(vector_a, vector_b)):
        if (abs(vector_a[i] - vector_b[i]) < eps):
            return True
        else:
            return False


def orto(vector_a, vector_b):
    '''Ортогональность'''
    return cos(vector_a, vector_b) == 0


def lenth(vector):
    '''Длина вектора'''
    len = 0
    for i in vector:
        len += i ** 2
    return len ** (1 / 2)


def norm(vector):
    '''нормировка вектора'''
    norm = []
    for i in vector:
        norm.append(i / lenth(vector))
    return norm


def proj_scalar_b(vector_a, vector_b):
    '''Проекция (скалярная)'''
    proj_b = scalar_product_of_vectors(vector_a, vector_b) / lenth(vector_b)
    return proj_b


def proj_vector_b(vector_a, vector_b):
    '''Проекция (векторная)'''
    proj_b = mult_scalar(vector_a,
                         scalar_product_of_vectors(vector_a, vector_b) / scalar_product_of_vectors(vector_a, vector_a))
    return proj_b
