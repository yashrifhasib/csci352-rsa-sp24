from time import time
from rsa import is_prime
from typing import Generator

def prime_range(n: int) -> Generator[int, None, None]:
    sieve = [False] * n
    for i in range(2, n):
        if not sieve[i]:
            for j in range(0, n, i):
                sieve[j] = True
            yield i

def test_is_prime(func=None):
    n = 2**20
    prime_ans = [False] * n
    for prime in prime_range(n):
        prime_ans[prime] = True
    countError = 0
    time_start = time()
    for i, prime in enumerate(prime_ans):
        if func(i) != prime:
            print(f"Wrong answer for {i}, primality is {prime}")
            countError += 1
    time_end = time()
    print("Number of errors:", countError)
    print("Time elapse:", time_end - time_start)

# takes a number to factor n and a function that returns a list of factors factor_function.
# factor_function should always return a list.
def factor_test(n, factor_function):
    prime_factors = list()
    to_factor = list()
    if is_prime(n):
        prime_factors.append(n)
    else:
        to_factor.append(n)
    while len(to_factor) > 0:
        smaller_factors = list()
        for x in to_factor: # we factor every number in to_factor
            new_factors = factor_function(x)
            if len(new_factors) < 2:
                print("error, factor did not factor correctly!", new_factors)
            for new_num in new_factors:
                if is_prime(new_num):
                    prime_factors.append(new_num)
                else:
                    smaller_factors.insert(0, new_num)
        to_factor = smaller_factors # we change to_factor to numbers that need factoring
    print(prime_factors)
    return prime_factors
