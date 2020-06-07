from math import sqrt
from typing import List

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


def fibonacci_recursive(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_recursive(n -2) + fibonacci_recursive(n - 1)


def fibonacci_recursive_dp(n: int) -> int:
    if n < 2:
        return n
    fibonacci_val = [-1 for _ in range(n + 1)]
    fibonacci_val[0] = 0
    fibonacci_val[1] = 1
    return _fibonacci_recursive_dp_calc(n, fibonacci_val)


def _fibonacci_recursive_dp_calc(n: int, fibonacci_val: List[int]) -> int:
    if fibonacci_val[n] != -1:
        return fibonacci_val[n]
    fibonacci_val[n] = _fibonacci_recursive_dp_calc(n - 2, fibonacci_val) + \
                       _fibonacci_recursive_dp_calc(n - 1, fibonacci_val)
    return fibonacci_val[n]
