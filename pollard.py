import sys
from euclid import gcd
from rsa import is_prime

def pollard_rho(number, g=None):
    if is_prime(number):
        return None
    b = 0
    def base_g(value):
        return (value**2 + 1) % number
    
    if g is None:
        g = base_g
    
    x = 2
    y = x
    d = 1
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = gcd(number, abs(x - y))
    
    if d == number:
        return None
    return d

if __name__ == '__main__':
    n = 9209839122440374002906008377605580208264841025166426304451583112053
    print(pollard_rho(n))