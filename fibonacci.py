def time_elapsed(func):
    import time
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} finished in {(end_time - start_time):.5f}s")
        return result
    return wrapper


# Dynamic programming storing previous 2 numbers
# Time O(n)
def fib_1(n):
    x = 0
    y = 1
    for _ in range(abs(n)):
        x, y = y, x+y    
    return -x if n <= 0 and not n & 1 else x

# Using numpy ndarray with optimized power function
# Object option is to keep value as python integer
# O(log n)
def fib_2(n):    
    if n == 0: return 0

    import numpy as np
    M = np.array([[1,1],[1,0]], object)
    def power(F, n):
        if n <= 1: return M        
        F = power(F, n >> 1) # n // 2
        F = F.dot(F)
        if n % 2 == 0:
            return F
        if n % 2 != 0:
            return F.dot(M)
    F = M
    F = power(F, abs(n)-1)
    return -F[0,0] if n <= 0 and not n & 1 else F[0,0]

def _is_perfect_squared(n):
    s = n**0.5
    return int(s) == s

# A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 – 4) is a perfect square
# https://en.wikipedia.org/wiki/Fibonacci_number#Identification
def is_fib(n):
    return _is_perfect_squared(5*n*n + 4) or _is_perfect_squared(5*n*n - 4)

def fib_generator(negative=False):
    x = 0
    y = 1
    while True:        
        yield x
        if negative:
            x, y = y, x-y
        else:
            x, y = y, x+y

@time_elapsed
def fib(n, func = fib_1):
    # return func(n)
    if n < 100_000:
        return fib_1(n)
    return fib_2(n)

if __name__=="__main__":
    n = 1_000_000
    fib(n)

    # print(fib_4(n) == fib_6(n))
    # gen = fib_generator(True)
    # for i in range(10):
    #     print(next(gen))
