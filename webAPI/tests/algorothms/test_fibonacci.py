"""
    Unit tests for Fibonacci algorithms implementasion

    for now, only simple-positive test cases has been implemented
"""

import app.algorithms.fibonacci as fibonacci
import pytest

# tested value from Fibonacci numbers table, where index = n, fibonacci_values[index] = Fibonacci(n) (result)
fibonacci_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_formula(n: int, expected: int) -> None:
    """
        Just verify that fibonacci_formula implementasion return correct value "expected" for case from "n"

        :param n: fibonacci sequence index
        :param expected: fibonacci sequence value for given index
        :return: None
    """
    assert fibonacci.fibonacci_formula(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_sequence(n: int, expected: int) -> None:
    """
        Just verify that fibonacci_sequence implementasion return correct value "expected" for case from "n"

        :param n: fibonacci sequence index
        :param expected: fibonacci sequence value for given index
        :return: None
    """
    assert fibonacci.fibonacci_sequence(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_recursive(n: int, expected: int) -> None:
    """
        Just verify that fibonacci_recursive implementasion return correct value "expected" for case from "n"

        :param n: fibonacci sequence index
        :param expected: fibonacci sequence value for given index
        :return: None
    """
    assert fibonacci.fibonacci_recursive(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_recursive_dp(n: int, expected: int) -> None:
    """
        Just verify that fibonacci_recursive_dp implementasion return correct value "expected" for case from "n"

        :param n: fibonacci sequence index
        :param expected: fibonacci sequence value for given index
        :return: None
    """
    assert fibonacci.fibonacci_recursive_dp(n) == expected


