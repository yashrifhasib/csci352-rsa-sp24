from math import log,e
from TonelliShanks import tonelli_shanks
from squarerootAttack import real_sqrt as sqrt
from pprint import pprint
import time

FACTOR_BASE_FILE = "factor_base_13_new.txt"

Q = dict()
def compute_sequence(B,x,N):
    for i in range(20):
        # Q_i 
        Q[i] = (x+i)**2 - N
    
    
def sieve(step,p):
    i = step
    while i < len(Q):
        print(i)
        Q[i] = Q[i] // p
        i += p
    print(list(Q.values()))

# TODO make this function work -Matthew
def reduce_sieve(mysieve, sequence, modulus, factorBase):
    # TODO: implement special -1 of factorbase
    start_number = sequence[0]
    for prime in factorBase[1:]:
        offset = start_number % prime
        for i in range(offset-1, len(mysieve), prime):
            before = mysieve[i]
            mysieve[i] //= prime
            print('pre:',before,'sequence#:',sequence[i], ",", mysieve[i], 'prime', prime,'index',i)

if __name__ == "__main__":
    factorBase = None
    with open(FACTOR_BASE_FILE, 'r', encoding='utf-8') as file:
        factorBase = [int(line) for line in file]
    # N = 9209839122440374002906008377605580208264841025166426304451583112053
    N = 227179
    
    start_number = sqrt(N)
    end_number = start_number + 20
    base_numbers = list(range(start_number, end_number, 1))
    mysieve = [pow(x,2,N) for x in base_numbers]
    
    pprint(list(zip(base_numbers, mysieve)))
    # reduce_sieve(mysieve, base_numbers, N, factorBase)
    
    compute_sequence(len(factorBase), start_number, N)
    # first, iterate through primes
    #   solve for n to see what primes in factor base to sieve using shanks tonelli
    #   (x + n)^2 = N mod p_i
    #   (x + n) = sqrt(N) mod p_i
    #   n =  sqrt(N) - x mod p_i
    for p in factorBase:
        if p == -1:
            continue
        square1,square2 = tonelli_shanks(N, p)
        n1 = (square1 - start_number ) % p
        n2 = (square2 - start_number ) % p
        if(n1 == n2):
            #only need to pass once
            sieve(n1,p)
        else:
            sieve(n1,p)
            sieve(n2,p)
