def memoize(func):
    cache = {}

    def wrapper(*args):
        """
        A memoized version of the input function. It maintains a cache of previously
        computed results, and returns the cached result if the same inputs occur again.
        """
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@memoize
def fibonacci(n):
    """
    Computes the nth Fibonacci number.

    The Fibonacci sequence is a series of numbers in which each number is the sum of the
    two preceding numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...

    This function uses memoization to cache previously computed values, so it can compute
    large Fibonacci numbers efficiently.
    """
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(300))
