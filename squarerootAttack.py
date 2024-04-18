from rsa import is_prime
from rsa import next_prime
from rsa import prev_prime
import math

# this returns the integer ceiling of the real square root of a number.
def real_sqrt(n):
    if n < (1<<40):
        return math.ceil(math.sqrt(n))
    hl = len(bin(n)[2:])//2
    upperBound = int(1 << hl+1)
    lowerBound = int(1 << hl-1)
    while(upperBound-lowerBound > 1):
        mid = lowerBound + ((upperBound - lowerBound) // 2)
        if mid**2 - n > 0:
            upperBound = mid
        else:
            lowerBound = mid
    if lowerBound**2 == n:
        return lowerBound
    return upperBound

def sqrtAttack(n):
    m = real_sqrt(n)
    print(m,"real sqrt     ")
    while not is_prime(m):
        m = m+1
    print("primality test",m, is_prime(m))
    print(m," times ", n//m,"remainder",n - (n//m * m))
    count = 0
    while (n%m != 0 ):
        m += 1
        count += 1
        print(count, m, n//m,n%m)
        print(m*(n//m)+n%m ==n)
        if count % 10000000 == 120:
            break
    print("factor is:",m)

def fermat_factorization(n, start_from=0):
    n_sqrt = real_sqrt(n)
    m = n_sqrt + start_from
    j_sqr = pow(m,2) - n
    j = real_sqrt(j_sqr)
    try:
        while pow(j,2) != j_sqr:
            m += 1
            j_sqr = pow(m,2) - n
            j = real_sqrt(j_sqr)
    except KeyboardInterrupt:
       print("number of numbers tried:",m - n_sqrt - 1)
       print("max offset:",(m - j) - n_sqrt, "length", len(str((m - j) - n_sqrt)))
       exit(1)
    p = m - j
    q = m + j
    return p, q

from math import sqrt
def demo(n):
    time1 = time()
    print("factoring n =", n)
    print("m increments, a² = m²-n")
    n_sqrt = real_sqrt(n)
    m = n_sqrt
    a_sqr = pow(m,2) - n
    a = real_sqrt(a_sqr)
    try:
        while pow(a,2) != a_sqr:
            print(f"m: {m}",f"m²: {a_sqr + n}",f"a²: {m**2 - n}",f"a: {sqrt(m**2 - n)}", sep= '   ')
            m += 1
            a_sqr = pow(m,2) - n
            a = real_sqrt(a_sqr)
    except KeyboardInterrupt:
       print("number of numbers tried:",m - n_sqrt - 1)
       print("max offset:",(m - a) - n_sqrt, "length", len(str((m - a) - n_sqrt)))
       exit(1)
    print(f"m: {m}",f"m²: {a_sqr + n}",f"a²: {m**2 - n}",f"a: {sqrt(m**2 - n)}", sep= '   ')
    p = m - a
    q = m + a
    print("(m + a), (m - a):",m-sqrt(m**2 - n),m+sqrt(m**2 - n))
    print("time spent in seconds:",time() - time1)
    print([p, q])


from time import time
from rsa import next_prime as np
if __name__ == '__main__':
    # n = 9209839122440374002906008377605580208264841025166426304451583112053
    # time1 = time()
    # p, q = fermat_factorization(n, 3094352807)
    # print("time spent in seconds:",time() - time1)
    # print([p, q])
    demo(np(3442)* np(3801))

