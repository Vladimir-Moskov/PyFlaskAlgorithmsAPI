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
    """
       Simple sequential calculation of Factorial function

       :param n: n >= 0, stands for first argument (n) of Factorial function
       :return: Factorial function value for given argument
     """

    iteration = 1
    result = 1
    while iteration <= n:
        result *= iteration
        iteration += 1
    return result


def factorial_div_and_conq(n):
    """
       Not really Simple divide-and-conquered algorithm for calculation of Factorial function
       The faster way to calculate factorial for big numbers, the idea is to minimize values in
       multiplication, because multiplication of smaller numbers is much faster the operate over large
       values.
        ( line 1845 on
        https://github.com/python/cpython/blob/master/Modules/mathmodule.c)

       :param n: n >= 0, stands for first argument (n) of Factorial function
       :return: Factorial function value for given argument
    """
    return _multiply_range(1, n)


def _multiply_range(n: int, m: int):
    """
        Recursive helper function - part of implementation divide-and-conquered algorithm

        :param n: start - from value
        :param m: end - to value
        :return: computation result of multiplication's from n to m
    """
    if n == m:
        return n
    if m < n:
        return 1
    else:
        return _multiply_range(n, (n + m) // 2) * _multiply_range((n + m) // 2 + 1, m)



