import sys
from euclid import gcd
from rsa import is_prime
from random import randrange

def pollard_rho(number: int, g_a=1, g_b=1):
    if is_prime(number):
        return None
    def g(value, a=g_a, b=g_b):
        return (a*value**2 + b) % number
    
    x = randrange(2,number)
    y = x
    d = 1
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = gcd(number, abs(x - y))
    
    if d == number:
        return None
    return d

from rsa import next_prime
from time import time
if __name__ == '__main__':
    #n = 9209839122440374002906008377605580208264841025166426304451583112053
    n = next_prime(10**11*4) * next_prime(10**20*493)
    start_time = time()
    rho = pollard_rho(n, g_a=1, g_b=1)
    end_time = time()
    print("factor of n is: ", rho)
    print("if blank, pollard failed")
    print("n = ",n)
    print("runtime:", end_time - start_time)