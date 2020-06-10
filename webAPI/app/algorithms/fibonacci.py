from math import sqrt
from typing import List

# pre-calculated constant for fibonacci_formula function
SQRT_5 = sqrt(5)


def fibonacci_formula(n: int) -> int:
    """
       Simple calculation of Fibonacci number by math formula

       :param n: n >= 0, stands for first argument (n) of Fibonacci function
       :return: Fibonacci function value for given argument
     """
    result = (pow(((1 + SQRT_5) / 2), n) - pow(((1 - SQRT_5) / 2), n)) / SQRT_5
    return int(result)


def fibonacci_sequence(n: int) -> int:
    """
       Simple sequential calculation of Fibonacci number

       :param n: n >= 0, stands for first argument (n) of Fibonacci function
       :return: Fibonacci function value for given argument
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
    """
       Straightforward / naive recursive approach calculation of Fibonacci number

       :param n: n >= 0, stands for first argument (n) of Fibonacci function
       :return: Fibonacci function value for given argument
     """
    if n < 2:
        return n
    return fibonacci_recursive(n -2) + fibonacci_recursive(n - 1)


def fibonacci_recursive_dp(n: int) -> int:
    """
       Straightforward / naive recursive approach calculation of Fibonacci number
       with 'cache',  dp stands for Dynamic Programming

       :param n: n >= 0, stands for first argument (n) of Fibonacci function
       :return: Fibonacci function value for given argument
     """
    if n < 2:
        return n
    fibonacci_val = [-1 for _ in range(n + 1)]
    fibonacci_val[0] = 0
    fibonacci_val[1] = 1
    return _fibonacci_recursive_dp_calc(n, fibonacci_val)


def _fibonacci_recursive_dp_calc(n: int, fibonacci_val: List[int]) -> int:
    """
        Recursive helper for function fibonacci_recursive_dp,

        :param n: n >= 0, stands for first argument (n) of Fibonacci function
        :param fibonacci_val: current storage of already calculated values
        :return: Fibonacci function value for given argument
    """
    if fibonacci_val[n] != -1:
        return fibonacci_val[n]
    fibonacci_val[n] = _fibonacci_recursive_dp_calc(n - 2, fibonacci_val) + \
                       _fibonacci_recursive_dp_calc(n - 1, fibonacci_val)
    return fibonacci_val[n]
