# https://en.wikipedia.org/wiki/Greatest_common_divisor

# Fastest here so far
def gcd_euclid_iterative(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_euclid_recursive(a, b):
    if b == 0: return a
    return gcd_euclid_recursive(b, a % b)

def gcd_extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = gcd_extended_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Slow - Python limitation
def gcd_binary_recursive(a, b):
    if a == b: return a
    if a == 0: return b
    if b == 0: return a
    if a & 1 == 0: # a is even
        if b & 1 == 1: # b is odd
            return gcd_binary_recursive(a >> 1, b)
        else: # both a and b are even
            return gcd_binary_recursive(a >> 1, b >> 1) << 1

    if b & 1 == 0: # a is odd and b is even
        return gcd_binary_recursive(a, b >> 1)

    if (a > b):
        return gcd_binary_recursive((a-b) >> 1, b)
    return gcd_binary_recursive((b-a) >> 1, a)

# Slow - Python limitation
def gcd_binary_iterative(a, b):
    if a == 0: return b
    if b == 0: return a

    shift = 0
    while a & 1 == 0 and b & 1 == 0: # both a and b are even
        a >>= 1 # a = a / 2
        b >>= 1 # b = b / 2
        shift += 1

    while a != b:
        if a & 1 == 0: a >>= 1
        elif b & 1 == 0: b >>= 1
        elif a > b: a = (a - b) >> 1
        else: b = (b - a) >> 1
    return a << shift  # a * 2**shift

def gcd(*args, func = gcd_euclid_iterative):
    result = abs(args[0])
    for i in args[1:]:
        result = func(result, abs(i))
    return result

# LCM using GCD
def lcm(*args):
    result = abs(args[0])
    for i in args[1:]:
        result = abs(result * i) // gcd(result,abs(i))
    return result

if __name__=="__main__":
    a = 5**100 - 1
    b = 5**120 - 1
    c = 5**110 - 1

    print(lcm(2, 7, 3, 9, 4))
    print(gcd(a, b, c))
    