"""
    Unit tests for Ackermann algorithms implementasion

    for now, only simple-positive test cases has been implemented
"""
import app.algorithms.ackermann as ackermann
import pytest

# tested value from Ackermann numbers table, where indexs = m, n, ackermann_values[m][n] = Ackermann(m, n) (result)
# MxN matrix
ackermann_values = [[1, 2, 3, 4, 5],
                    [2, 3, 4, 5, 6],
                    [3, 5, 7, 9, 11],
                    [5, 13, 29, 61, 125]]


@pytest.mark.parametrize("m, n, expected", [(i, j, ackermann_values[i][j])
                                            for i in range(len(ackermann_values))
                                            for j in range(len(ackermann_values[0]))])
def test_ackermann(m: int, n: int, expected: int) -> None:
    """
        Just verify that ackermann implementasion return correct value "expected" for case from "m, n"

        :param m: ackermann  first (m) argument
        :param n: ackermann  second (n) argument
        :param expected: ackermann function result
        :return: None
    """
    assert ackermann.ackermann(m, n) == expected


@pytest.mark.parametrize("m, n, expected", [(i, j, ackermann_values[i][j])
                                            for i in range(len(ackermann_values))
                                            for j in range(len(ackermann_values[0]))])
def test_ackermann_dp(m: int, n: int, expected: int) -> None:
    """
        Just verify that ackermann_dp implementasion return correct value "expected" for case from "m, n"

        :param m: ackermann  first (m) argument
        :param n: ackermann  second (n) argument
        :param expected: ackermann function result
        :return: None
    """
    assert ackermann.ackermann_dp(m, n) == expected
