import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.10f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    print(s)


@timer
def fast_function():
    s = 0
    for i in range(100000000):
        s += i
    print(s)

slow_function()