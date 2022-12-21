import vectors.logic_vector as vec


def test_sum():
    '''Сложение векторов'''
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [5, 10, 6]
    res = vec.summ(a, b)
    assert res == exp


def test_sub():
    '''Вычитание векторов'''
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [-3, -6, 4]
    res = vec.sub(a, b)
    assert res == exp


def test_mult_scalar():
    '''Умножение вектора на скаляр'''
    a = [1, 2]
    scalar = 3
    exp = [3, 6]
    res = vec.mult_scalar(a, scalar)
    assert res == exp


def test_div_scalar():
    '''Деление вектора на скаляр'''
    a = [3, 6, 9]
    scalar = 3
    exp = [1, 2, 3]
    res = vec.div_scalar(a, scalar)
    assert res == exp


def test_scalar_product_of_vectors():
    '''Скалярное произведение векторов'''
    a = [1, 2, -5]
    b = [4, 8, 1]
    exp = 15
    res = vec.scalar_product_of_vectors(a, b)
    assert res == exp


def test_collinear():
    '''Коллинеарные векторы'''
    a = [0, 12]
    b = [0, 48]
    res = vec.collinear(a, b)
    assert res == True


def test_co_dir():
    '''Коллинеарные векторы'''
    a = [4, 0]
    b = [2, 0]
    res = vec.co_dir(a, b)
    assert res == True


def test_opp_dir():
    '''Коллинеарные векторы'''
    a = [-4, 0]
    b = [2, 0]
    res = vec.opp_dir(a, b)
    assert res == True


def test_equality():
    '''Равенство векторов'''
    a = [-4, 3, 5]
    b = [-4, 3, 5]
    res = vec.equality(a, b)
    assert res == True


def test_equality_eps():
    '''Равенство векторов'''
    a = [-4, 3, 5]
    b = [-4, 3, 5]
    res = vec.equality_eps(a, b, 2)
    assert res == True


def test_orto():
    '''Равенство векторов'''
    a = [1, 2]
    b = [2, -1]
    res = vec.orto(a, b)
    assert res == True


def test_lenth():
    '''Длина вектора'''
    a = [3, -4]
    exp = 5
    res = vec.lenth(a)
    assert res == exp


def test_norm():
    '''Длина вектора'''
    a = [3, -4]
    exp = [0.6, -0.8]
    res = vec.norm(a)
    assert res == exp


def equality_angl(vector_a, vector_b, eps):
    if (abs(vector_a - vector_b) < eps):
        return True
    else:
        return False


def test_angl():
    '''Угол между векторами'''
    a = [3, 4]
    b = [4, 3]
    exp = 0.28
    res = vec.angl(a, b)
    assert equality_angl(res, exp, 2)


def test_proj_scalar_b():
    '''Проекция (скалярная)'''
    a = [1, 2]
    b = [3, 4]
    exp = 2.2
    res = vec.proj_scalar_b(a, b)
    assert res == exp


def test_proj_vector_b():
    '''Проекция (скалярная)'''
    a = [1, 2]
    b = [3, 4]
    exp = [2.2, 4.4]
    res = vec.proj_vector_b(a, b)
    assert res == exp
