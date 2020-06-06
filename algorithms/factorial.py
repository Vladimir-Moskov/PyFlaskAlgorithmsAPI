from math import factorial


def factorial_math(n: int) -> int:

    return factorial(n)


def factorial_sequence(n: int) -> int:
    iteration = 1
    result = 1
    while iteration <= n:
        result *= iteration
        iteration += 1
    return result


def _multiply_range(n, m):
    if n == m:
        return n
    if m < n:
        return 1
    else:
        return _multiply_range(n, (n + m) // 2) * _multiply_range((n + m) // 2 + 1, m)


def factorial_div_and_conq(n):
    return _multiply_range(1, n)
