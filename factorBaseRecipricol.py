from math import ceil,sqrt,log
from time import time
from random import randint
import math


def get_primesDict_frm_file(bound):
    primes = dict()
    with open("3Mil_primes3001134.txt","r") as primeFile:
        p = primeFile.readline()
        for i in range(bound):
            primes[i] = int(p)
            p = primeFile.readline()
    return primes
    
    

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

def legendre(top,bottom):
    if(top>=bottom):
        top = top%bottom
    result =1;

    if(top == 2):
        if(bottom %8 == 1 or bottom%8 == 7):
            return 1
        elif(bottom%8 == 3 or bottom%8 == 5):
            return -1
    
    while(not is_prime(top)): #if top top is not a prime
        fac = prime_factors(top)
        for prime, exponent in fac.items():
            result *= legendre(prime,bottom)**exponent
        return result

    if(top%4 == 1 or bottom % 4 == 1):
        return legendre(bottom,top)
    elif(top%4 == 3 and bottom%4 == 3):
        return (-1)*legendre(bottom,top)
    

def next_prime(n):
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

def create_factor_base(B, n):
    primes = get_primesDict_frm_file(2*B)
    factorBase = list()
    factorBase.append(-1)
    # factorBase.append(2)
    # factorBase.append(3)
    
    i = 0
    while len(factorBase) < B:
        p = primes[i]
        if legendre(n, primes[i])==1:
        # if pow(n,(p-1)//2,p) == 1:
            factorBase.append(p)
        i+=1
    print(f"created factor base with {len(factorBase)} length and searched {i} numbers")
    return factorBase

def save_list_to_file(myList):
    name = "factor_base_" + str(len(myList)) + "_new.txt"
    with open(name, mode='w', encoding="utf-8") as file:
        for p in myList:
            file.write(str(p)+'\n')
    print("wrote to file", name)

if __name__ == '__main__':

    start_time = time()  
    # n = 227179
    n = 9209839122440374002906008377605580208264841025166426304451583112053
    B = ceil(pow(math.e, (0.5)*sqrt(log(n)*log(log(n))) ))
    primes = create_factor_base(B,n)
    save_list_to_file(primes)
    


end_time = time()
print("runtime:", end_time - start_time)