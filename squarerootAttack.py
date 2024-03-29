from rsa import is_prime
import math

# this returns the integer ceiling of the real square root of a number.
def real_sqrt(n):
    n_sqrt = math.sqrt(n)
    if n < 10**8:
        return math.ceil(n_sqrt)
    upperBound = int(n_sqrt*1.0001)+1
    lowerBound = int(n_sqrt*0.9999)-1
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

if __name__ == '__main__':
    n = 9209839122440374002906008377605580208264841025166426304451583112053
    p, q = fermat_factorization(n, 0)
    print([p, q])

