from random import randint

def factor(num):
    count = 0
    factors = [1]
    for i in range(2, int(num / 2)):
        if num % i == 0:
            count += 1
            factors.append(i)
    if count == 0:
        return [1, num]
    factors.append(num)
    return factors;

def prime_factors_of(number):
	divisor = 2
	remaining = number
	prime_factors = list()
	while(divisor <= remaining):
		if remaining % divisor == 0:
			prime_factors.append(divisor)
			remaining = remaining // divisor
		else:
			divisor += 1
	return prime_factors

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

def is_prime(number):
    for x in range(500):
        if not is_prime_helper(number):
            return False
    return True
