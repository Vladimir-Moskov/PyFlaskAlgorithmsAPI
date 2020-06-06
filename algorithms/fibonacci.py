from math import sqrt

# pre-calculated constant
SQRT_5 = sqrt(5)


def fibonacci_formula(n: int) -> int:
    """

    :param n:
    :return:
    """
    result = (pow(((1 + SQRT_5) / 2), n) - pow(((1 - SQRT_5) / 2), n)) / SQRT_5
    return int(result)


def fibonacci_sequence(n: int) -> int:
    """

    :param n:
    :return:
    """
    if n == 0:
        return 0

    prev_0, current_1 = 0, 1
    iteration = 1
    while iteration < n:
        prev_0, current_1 = current_1, prev_0 + current_1
        iteration += 1

    return current_1
