from time import time
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
