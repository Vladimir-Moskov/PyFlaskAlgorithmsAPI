import app.algorithms.fibonacci as fibonacci
import pytest

fibonacci_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_formula(n: int, expected: int):
    """
    :param n:
    :param expected:
    :return:
    """
    assert fibonacci.fibonacci_formula(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_sequence(n: int, expected: int):
    """
    :param n:
    :param expected:
    :return:
    """
    assert fibonacci.fibonacci_sequence(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_recursive(n: int, expected: int):
    """
    :param n:
    :param expected:
    :return:
    """
    assert fibonacci.fibonacci_recursive(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(fibonacci_values))
def test_fibonacci_recursive_dp(n: int, expected: int):
    """
    :param n:
    :param expected:
    :return:
    """
    assert fibonacci.fibonacci_recursive_dp(n) == expected


