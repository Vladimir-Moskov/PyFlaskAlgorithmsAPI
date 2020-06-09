"""
    Implementation of Ackermann function
    (please, for more details visit https://en.wikipedia.org/wiki/Ackermann_function)

"""

from collections import defaultdict
from typing import List, Dict


def ackermann(m: int, n: int) -> int:
    """
        Direct Implementation of Ackermann function - recursive approach

        :param m: m >= 0, stands for first argument (m) of Ackermann function
        :param n: n >= 0, stands for second argument (n) of Ackermann function
        :return: Ackermann function value for given arguments
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def ackermann_dp(m: int, n: int) -> int:
    """
        Direct Implementation of Ackermann function - recursive approach with 'cache',
        dp stands for Dynamic Programming

        :param m: m >= 0, stands for first argument (m) of Ackermann function
        :param n: n >= 0, stands for second argument (n) of Ackermann function
        :return: Ackermann function value for given arguments
    """
    ackermann_calc_values = [defaultdict(int) for _ in range(m + 1)]
    return _ackermann_dp_calc(m, n, ackermann_calc_values)


def _ackermann_dp_calc(m: int, n: int, ackermann_calc_values: List[Dict]) -> int:
    """
        Recursive helper for function ackermann_dp,

        :param m: m >= 0, stands for first argument (m) of Ackermann function
        :param n: n >= 0, stands for second argument (n) of Ackermann function
        :param ackermann_calc_values: current storage of already calculated values
        :return: Ackermann function value for given arguments
    """
    if ackermann_calc_values[m][n] != 0:
        return ackermann_calc_values[m][n]
    if m == 0:
        ackermann_calc_values[m][n] = n + 1
    elif n == 0:
        ackermann_calc_values[m][n] = _ackermann_dp_calc(m - 1, 1, ackermann_calc_values)
    else:
        ackermann_calc_values[m][n] = \
            _ackermann_dp_calc(m - 1, _ackermann_dp_calc(m, n - 1, ackermann_calc_values), ackermann_calc_values)
    return ackermann_calc_values[m][n]
