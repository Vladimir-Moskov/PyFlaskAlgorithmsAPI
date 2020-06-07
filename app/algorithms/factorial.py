"""
    Implementation of Factorial function
    (please, for more details visit https://en.wikipedia.org/wiki/Factorial)

"""

from math import factorial


def factorial_math(n: int) -> int:
    """
        Straightforward approach - use already existed, reliable and fast implementation of factorial
        function from math module

        :param n: n >= 0, stands for first argument (n) of Factorial function
        :return: Factorial function value for given argument
    """
    return factorial(n)


def factorial_recursive(n: int) -> int:
    """
        Straightforward / naive recursive approach of Factorial function

        :param n: n >= 0, stands for first argument (n) of Factorial function
        :return: Factorial function value for given argument
    """
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n


def factorial_sequence(n: int) -> int:
    iteration = 1
    result = 1
    while iteration <= n:
        result *= iteration
        iteration += 1
    return result


def factorial_div_and_conq(n):
    return _multiply_range(1, n)


def _multiply_range(n, m):
    if n == m:
        return n
    if m < n:
        return 1
    else:
        return _multiply_range(n, (n + m) // 2) * _multiply_range((n + m) // 2 + 1, m)



