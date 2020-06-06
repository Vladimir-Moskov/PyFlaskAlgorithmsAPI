import ackermann
import pytest

# MxN matrix
ackermann_values = [[1, 2, 3, 4, 5],
                    [2, 3, 4, 5, 6],
                    [3, 5, 7, 9, 11],
                    [5, 13, 29, 61, 125]]


@pytest.mark.parametrize("m, n, expected", [(i, j, ackermann_values[i][j])
                                            for i in range(len(ackermann_values))
                                            for j in range(len(ackermann_values[0]))])
def test_ackermann(m: int, n: int, expected: int):
    assert ackermann.ackermann(m, n) == expected


@pytest.mark.parametrize("m, n, expected", [(i, j, ackermann_values[i][j])
                                            for i in range(len(ackermann_values))
                                            for j in range(len(ackermann_values[0]))])
def test_ackermann_dp(m: int, n: int, expected: int):
    assert ackermann.ackermann_dp(m, n) == expected
