from rsa import is_prime
import math

# this returns the integer ceiling of the real square root of a number.
def real_sqrt(n):
    upperBound = int(math.sqrt(n)*1.0001)
    lowerBound = upperBound//2
    while(upperBound-lowerBound > 1):
        mid = lowerBound + ((upperBound - lowerBound) // 2)
        if mid**2 - n > 0:
            upperBound = mid
        else:
            lowerBound = mid
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


if __name__ == '__main__':
    n = 9209839122440374002906008377605580208264841025166426304451583112053
    print(n)
    sqrtAttack(n)

