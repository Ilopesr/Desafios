from desafios.math.matrices import sum_matrix

m1 = [[1, 1, 1]]

simple_m1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
simple_m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

differente_size_m1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
differente_size_m2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

negative_m1 = [[1, 1, 1], [1, -15, 1], [1, 1, 1, 4], [1, 1, 1, 3]]
negative_m2 = [[1, 1, 1], [1, 1, -11], [-12, 1, 0]]
negative_m3 = [[1, -5, 1], [1, 1, -5], [-12, 1, 0, 15]]

result = [[3, 3, 3], [3, -15]]


def test_with_zero_arguments():
    result = sum_matrix()
    assert result == "No arguments"


def test_with_one_argument():
    result = sum_matrix(m1)
    assert result == "Only one argument"


def test_with_two_args_with_same_size():
    result = sum_matrix(simple_m1, simple_m2)
    assert result == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]


def test_with_two_args_with_differentes_size():
    result = sum_matrix(differente_size_m1, differente_size_m2)
    assert result == [[2, 2, 2], [2, 2, 2], [2, 2, 2], [1, 1, 1]]


def test_in_a_real_calc():
    result = sum_matrix(negative_m1, negative_m2, negative_m3)
    assert result == [[3, -3, 3], [3, -13, -15], [-23, 3, 1, 19], [1, 1, 1, 3]]
