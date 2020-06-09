"""
    Time / performance measure utils

"""

import time


def timed(function, count, *arg, **kw):
    """
        Measure how long it take to execute given 'function' for 'count'
        amount of times, in order to get algorithm performance profile

        :param function: given function to measure execution time
        :param count: amount of times  to call function (does not effect result in any way)
        :param arg: order arguments for given function
        :param kw:  named arguments for given function
        :return: value for function(*arg, **kw), time it takes to perform all calls
    """
    ts = time.time()
    for _ in range(count):
        result = function(*arg, **kw)
    te = time.time()

    return result, (te - ts) * 1000
