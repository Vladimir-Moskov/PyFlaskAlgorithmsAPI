"""
    Unit tests for Factorial algorithms implementasion

    for now, only simple-positive test cases has been implemented
"""
import app.algorithms.factorial as factorial
import pytest

# tested value from Factorial numbers table, where index = n, factorial_values[index] = Factorial(n) (result)
factorial_values = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800,
                    87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000,
                    121645100408832000, 2432902008176640000]


@pytest.mark.parametrize("n, expected", enumerate(factorial_values))
def test_factorial_math(n: int, expected: int) -> None:
    """
        Just verify that factorial_math implementasion return correct value "expected" for case from "n"

        :param n: factorial  index
        :param expected: factorial function result
        :return: None
    """
    assert factorial.factorial_math(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(factorial_values))
def test_factorial_recursive(n: int, expected: int) -> None:
    """
        Just verify that factorial_recursive implementasion return correct value "expected" for case from "n"

        :param n: factorial  index
        :param expected: factorial function result
        :return: None
    """
    assert factorial.factorial_recursive(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(factorial_values))
def test_factorial_sequence(n: int, expected: int) -> None:
    """
        Just verify that factorial_sequence implementasion return correct value "expected" for case from "n"

        :param n: factorial  index
        :param expected: factorial function result
        :return: None
    """
    assert factorial.factorial_sequence(n) == expected


@pytest.mark.parametrize("n, expected", enumerate(factorial_values))
def test_factorial_div_and_conq(n: int, expected: int) -> None:
    """
        Just verify that factorial_div_and_conq implementasion return correct value "expected" for case from "n"

        :param n: factorial  index
        :param expected: factorial function result
        :return: None
    """
    assert factorial.factorial_div_and_conq(n) == expected

