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
def fib(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


print(fib(10))