"""
    Integration tests for every endpoint of Algorithms Wep API application

    for now, only simple-positive test cases has been implemented
"""
from app.config import Config
# set application in state for testing (turn off logging and monitoring dashboard)
Config.TESTING = True


import pytest
from algorithms_api import app


# strategies / endpoints to  check  for every algorithm respectively
ackermann_strategies = ["ackermann", "ackermann_dp"]
factorial_strategies = ["factorial_math", "factorial_recursive", "factorial_sequence", "factorial_div_and_conq"]
fibonacci_strategies = ["fibonacci_formula", "fibonacci_sequence", "fibonacci_recursive", "fibonacci_recursive_dp"]


@pytest.fixture
def client():
    """
        Create "lambda service" / application to handle http request for test case

        :return: client - "lambda service" / application to handle http request
    """
    with app.test_client() as client:
        yield client

# Ackermann ################################################3


@pytest.mark.parametrize("strategy", ackermann_strategies)
def test_algorithms_api_ackermann(client, strategy) -> None:
    """
        Check ackermann web API, simple test case - one call one value to verify

        :param client: current instance of application / service
        :param strategy: current algorithm implementasion
        :return: None
    """
    api_response = client.get(f'{Config.SERVER_NAME_API_APP}/{strategy}?m=3&n=4')
    assert api_response.status_code == 200
    assert api_response.json["data"] == 125


@pytest.mark.parametrize("strategy", ackermann_strategies)
def test_algorithms_api_ackermann_negative_no_args(client, strategy):
    """
        Check ackermann web API for negative scenario, simple test case - one call with no arguments

        :param client: current instance of application / service
        :param strategy: current algorithm implementasion
        :return: None
    """
    api_response = client.get(f'{Config.SERVER_NAME_API_APP}/{strategy}')
    assert api_response.status_code == 400
    assert api_response.json["message"]["m"] == "m is mandatory argument (m >= 0)"
    assert api_response.json["message"]["n"] == "n is mandatory argument (n >= 0)"


#  Factorial #####################################################


@pytest.mark.parametrize("strategy", factorial_strategies)
def test_algorithms_api_factorial(client, strategy):
    """
        Check Factorial web API, simple test case - one call one value to verify

        :param client: current instance of application / service
        :param strategy: current algorithm implementasion
        :return: None
    """
    api_response = client.get(f'{Config.SERVER_NAME_API_APP}/{strategy}?n=10')
    assert api_response.status_code == 200
    assert api_response.json["data"] == 3628800


@pytest.mark.parametrize("strategy", factorial_strategies)
def test_algorithms_api_factorial_negative_no_args(client, strategy):
    """
        Check Factorial web API for negative scenario, simple test case - one call with no arguments

        :param client: current instance of application / service
        :param strategy: current algorithm implementasion
        :return: None
    """
    api_response = client.get(f'{Config.SERVER_NAME_API_APP}/{strategy}')
    assert api_response.status_code == 400
    assert api_response.json["message"]["n"] == "n is mandatory argument (n >= 0)"


# Fibonacci #####################################################

@pytest.mark.parametrize("strategy", fibonacci_strategies)
def test_algorithms_api_fibonacci(client, strategy):
    """
        Check Fibonacci web API, simple test case - one call one value to verify

        :param client: current instance of application / service
        :param strategy: current algorithm implementasion
        :return: None
    """
    api_response = client.get(f'{Config.SERVER_NAME_API_APP}/{strategy}?n=15')
    assert api_response.status_code == 200
    assert api_response.json["data"] == 610


@pytest.mark.parametrize("strategy", fibonacci_strategies)
def test_algorithms_api_fibonacci_negative_no_args(client, strategy):
    """
        Check Fibonacci web API for negative scenario, simple test case - one call with no arguments

        :param client: current instance of application / service
        :param strategy: current algorithm implementasion
        :return: None
    """
    api_response = client.get(f'{Config.SERVER_NAME_API_APP}/{strategy}')
    assert api_response.status_code == 400
    assert api_response.json["message"]["n"] == "n is mandatory argument (n >= 0)"