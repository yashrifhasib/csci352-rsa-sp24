from time import time
from rsa import is_prime, prev_prime, next_prime

def get_primesDict_frm_file(bound):
    primes = dict()
    with open("3Mil_primes3001134.txt","r") as primeFile:
        p = primeFile.readline()
        for i in range(bound):
            primes[i] = int(p)
            p = primeFile.readline()
    return primes

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

def create_factor_base(prime_smoothness, n) -> list[int]:
    """
    creates factor base list containing no primes above a certain prime in list of all primes
    
    arguments:

    prime_smoothness -- the index of the largest prime in the list of all prime numbers

    n -- the number we want to factor
    """
    primes = get_primesDict_frm_file(2*prime_smoothness)
    factorBase = list()
    factorBase.append(-1)
    # factorBase.append(2)
    # factorBase.append(3)
    
    prime_count = 0
    while prime_count < prime_smoothness:
        p = primes[prime_count]
        if legendre(n, primes[prime_count])==1:
        # if pow(n,(p-1)//2,p) == 1:
            factorBase.append(p)
        prime_count+=1
    factor_base_size = len(factorBase)
    print(f"created factor base with {factor_base_size} length and searched {prime_count} numbers")
    return factorBase

def create_factor_base_from_absolute(absolute_smoothness, n) -> list[int]:
    """
    creates factor base according to an absolute smoothness

    arguments:

    absolute_smoothness -- the upper bound for numbers in the factor base

    n -- the number we want to factor
    """
    prime_smoothness = highest_prime_order(absolute_smoothness)
    return create_factor_base(prime_smoothness, n)

def highest_prime_order(max_value):
    """ find the prime below input and returns
    what number prime it is."""
    if not is_prime(max_value):
        max_value = prev_prime(max_value)
    count = 1
    prime = 2
    while prime < max_value:
        count += 1
        prime = next_prime(prime+1)
    return count

def save_list_to_file(myList):
    # TODO re-implement better
    pass
    return
    #name = "factor_base_78500th_prime.txt"
    with open(name, mode='w', encoding="utf-8") as file:
        for p in myList:
            file.write(str(p)+'\n')
    print("wrote to file", name)

def open_factorbase(filename):
    factorBase = None
    with open(filename, 'r', encoding='utf-8') as file:
        factorBase = [int(line) for line in file]
    return factorBase

if __name__ == '__main__':

    start_time = time()  
    # n = 227179
    n = 9209839122440374002906008377605580208264841025166426304451583112053
    primes = create_factor_base(78500,n)
    save_list_to_file(primes)
    end_time = time()
    print("runtime:", end_time - start_time)