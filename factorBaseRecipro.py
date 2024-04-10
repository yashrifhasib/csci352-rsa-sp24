from math import ceil
from math import sqrt
from time import time
from random import randint
import math

def is_prime_helper(n):
    # miller rabine implementation
    if n == 2:
        return True
    if n % 2 == 0 or n < 3:
        return False
    # n = pow(2,k) * m
    k = 0
    m = n - 1
    while m%2 == 0:
        k += 1
        m = m // 2
    if True:
        a = randint(2,n-1)
        # b starts at b0
        b = pow(a,m,n)
        if b in [1, n-1]:
            return True
        # check b1 - b(k-1)
        for b_count in range(1,k):
            b = pow(b, 2, n)
            # check if miller-rabin condition
            if b == 1:
                return False
            if b == n-1:
                return True
    return False

def is_prime(number, test_count=5):
    for x in range(test_count):
        if not is_prime_helper(number):
            return False
    return True

def prime_factors(n):
    factors = {}
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors[divisor] = count
        divisor += 1
        if divisor * divisor > n and n > 1:
            factors[n] = 1
            break
    return factors

def legendre(p,q):
    if(p>=q):
        p = p%q
    result =1;

    if(p == 2):
        if(q %8 == 1 or q%8 == 7):
            return 1
        elif(q%8 == 3 or q%8 == 5):
            return -1
    
    while(not is_prime(p)): #if top p is not a prime
        fac = prime_factors(p)
        for prime, exponent in fac.items():
            result *= legendre(prime,q)**exponent
        return result

    if(p%4 == 1 or q % 4 == 1):
        return legendre(q,p)
    elif(p%4 == 3 and q%4 == 3):
        return (-1)*legendre(q,p)
    

def next_prime(n):
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

def create_factor_base(count, n=9209839122440374002906008377605580208264841025166426304451583112053):
    primes = list()
    primes.append(-1)
    primes.append(2)
    primes.append(3)
    prime = 4
    loopcount = 0
    while len(primes) < count:
        loopcount += 1
        prime = next_prime(prime + 1)
        if legendre(prime, n)==1:
            primes.append(prime)
    print(f"created factor base with {len(primes)} length and searched {loopcount} numbers")
    return primes

def save_list_to_file(myList):
    name = "factor_base_" + str(len(myList)) + ".txt"
    with open(name, mode='w', encoding="utf-8") as file:
        for p in myList:
            file.write(str(p)+'\n')
    print("wrote to file", name)

if __name__ == '__main__':

    start_time = time()  
    primes = create_factor_base(2125)
    save_list_to_file(primes)
    


end_time = time()
print("runtime:", end_time - start_time)