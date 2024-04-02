import math
from euclid import gcd
from rsa import prime_factors_of

def is_smooth(b, square):
    if square <= 1:
        return False
    prime_factors = prime_factors_of(square)
    if prime_factors[-1] <= b:
        return True
    return False


def dixon(n, b):
    z = list()
    a = math.ceil(math.sqrt(n))
    y = 1
    x = 1
    for i in range(a, n):
        if is_smooth(b, pow(i, 2, n)):
            z.append(i)
    breaking = False
    for i in z:
        for j in z:
            if pow(i*j, 2, n) != 0 and i != j:
                x = pow((i * j), 2, n)
                y = pow(x, 2, n)
                if (x - y != 0) and (x + y != n):
                    breaking = True
                    break
        if (breaking):
            break
    return [gcd(x-y, n), gcd(x+y, n)]

print(dixon(113781, 7))