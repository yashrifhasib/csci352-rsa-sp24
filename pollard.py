import sys
from euclid import gcd
from rsa import is_prime
from rsa import next_prime
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
    return [d, number//d]

# pollard's p - 1 factoring
def pollard_factor(n, max_smooth=400000, a=None):
    B_smooth = 2
    if a is None:
        a = randrange(2,n)
    b = pow(a,B_smooth,n)
    while(gcd(b-1,n) == 1):
        B_smooth += 1
        #B_smooth = next_prime(B_smooth+1) # this does not calculate B!, which may cause slower factoring.
        b = pow(b,B_smooth,n)
        if B_smooth > max_smooth:
            return list()
    p = gcd(b-1,n)
    #print('a:',a,'smoothbase:',B_smooth)
    return [p, n//p]

from time import time
from rsa import next_prime
from test import factor_test

def rho_main():
    #n = 9209839122440374002906008377605580208264841025166426304451583112053
    #n = next_prime(10**11*4) * next_prime(10**20*493)
    n = 4980853165476541363
    start_time = time()
    rho = pollard_rho(n, g_a=1, g_b=1)
    end_time = time()
    print("factor of n is: ", rho)
    print("if blank, pollard failed")
    print("n = ",n)
    print("runtime:", end_time - start_time)

def factor_main():
    n = next_prime(342)*next_prime(654356)*next_prime(43254)*next_prime(7642)*next_prime(436)*next_prime(863357)*next_prime(3487)*next_prime(435487)*next_prime(4864187)
    factor_test(n, pollard_factor)
    print(pollard_factor(11951438413903,150,57))

if __name__ == '__main__':
    #rho_main()
    factor_main()
