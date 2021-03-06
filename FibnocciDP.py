import functools
def memo(func):
    cache = {}
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
