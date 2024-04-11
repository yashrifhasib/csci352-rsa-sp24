from math import log,sqrt,ceil,e
from TonelliShanks import tonelli_shanks
import time
Q = dict()
def compute_sequence(B,x,N):
    for i in range(20):
        Q[i] = (x+i)**2 - N
    
    
def sieve(step,p):
    i = step
    while i < len(Q):
        print(i)
        Q[i] = Q[i] // p
        i += p
    print(list(Q.values()))
    
if __name__ == "__main__":
    fbFile = open("factor_base_13_new.txt")
    factorBase = [int(f) for f in fbFile]
    # N = 9209839122440374002906008377605580208264841025166426304451583112053
    N = 227179
    x = ceil(sqrt(N))
    compute_sequence(len(factorBase),x,N)
    # first, iterate through primes
    #   solve for n to see what primes in factor base to sieve using shanks tonelli
    #   (x + n)^2 = N mod p_i
    #   (x + n) = sqrt(N) mod p_i
    #   n =  sqrt(N) - x mod p_i
    for p in factorBase:
        if p == -1:
            continue
        square1,square2 = tonelli_shanks(N, p)
        n1 = (square1 - x ) % p
        n2 = (square2 - x ) % p
        if(n1 == n2):
            #only need to pass once
            sieve(n1,p)
        else:
            sieve(n1,p)
            sieve(n2,p)
    
    
    