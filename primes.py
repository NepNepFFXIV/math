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

# Trial division using 6k+-1 optimization
def is_prime(n): 
    if n <= 3: return n > 1
    if n % 2 == 0 or n % 3 == 0: return False

    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False    
    return True

# Brute force trial division
def is_prime_brute(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# prime_checker is used to check if a number is prime
def prime_generator(prime_checker=is_prime):
    yield 2
    n = 1
    while True:
        n += 2
        if prime_checker(n):
            yield(n)

# All primes less than or equal n - O(n log n)
@time_elapsed
def sieve_sundaram(n): 
    primes = []
    m = n//2
    marked = [False] * (m + 1)

    # Main logic of Sundaram. Mark all  
    # numbers which do not generate prime
    for i in range(1, m + 1):
        for j in range((i * (i+1)) << 1, m + 1, 2*i + 1):
            marked[j] = True

    primes.append(2)
  
    for i in range(1, m): 
        if (marked[i] == False): 
            primes.append(2*i + 1)

    if is_prime(n): primes.append(n)
    return primes

# All primes less than or equal n - O(n log log n)
@time_elapsed
def sieve_eratosthenes(n):
    # marked = [True for i in range(n+1)]
    marked = [True] * (n+1)
    p = 2
    while (p*p <= n):
        # If marked[p] is not changed, then it is a prime
        if marked[p]: # marked[p] == True
            # Update all multiplies of p
            for i in range(p*p, n+1, p):
                marked[i] = False
        p += 1

    return [p for p in range(2,n+1) if marked[p]]

# All primes less than or equal n - O(n / (log log n))
@time_elapsed
def sieve_atkin(n):
    #idk lol
    pass

# All primes less than or equal n using prime generator - O(lol)
@time_elapsed
def primes_lte_n(n):
    nums = []
    gen = prime_generator()
    m = next(gen)
    while m <= n:
        nums.append(m)
        m = next(gen)    
    return nums

# Prime Factorization - Optimized Trial division - O(sqrt(n))
def prime_factorization(n):
    result = []
    while n & 1 == 0:
        result.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            result.append(i)            
            n = n // i
    if n > 2: result.append(n)
    return result

# All possible pairs of Goldbach's conjecture
def goldbach(n, sieve=sieve_eratosthenes):
    # We only check even numbers greater than 2
    if n < 2 or n & 1 == 1: return []

    primes = sieve(n)
    result = []
    for i in primes:
        difference = n - i
        if difference < i: break
        if difference in primes:
            result.append([i, difference])    
    return result

if __name__ == "__main__":
    from timeit import timeit
    from itertools import islice
    # n = int(math.pow(10, 7))
    n = 1_000_000
    # print(is_prime(n))
    # print(is_prime_brute(n))
    # print(prime_factorization(n))    
    # print(primes_lte_n(n))
    # print(sieve_sundaram(n))
    print(sieve_eratosthenes(n)[-1])
    # sieve_atkin(n)
    # print(goldbach(n))