import time


def timed(function, count, *arg, **kw):
    ts = time.time()
    for _ in range(count):
        result = function(*arg, **kw)
    te = time.time()

    return result, (te - ts) * 1000
