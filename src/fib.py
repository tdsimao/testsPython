

def memoize(func):
    cache = {}

    def func_warapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    func_warapper.cache = cache
    return func_warapper


@memoize
def fib(n):
    if n < 3:
        return(1)
    else:
        return fib(n-1) + fib(n-2)
