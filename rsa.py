from random import randint
import math

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

def is_prime(number, test_count=5):
    for x in range(test_count):
        if not is_prime_helper(number):
            return False
    return True

def pollard_rho_helper(value, exponent, constant, n):
    var_i = (value**exponent + constant) % n
    return var_i

def pollard_rho(n, x0, y0, fx_constant, fx_exponent=2):
    xi = pollard_rho_helper(x0, fx_exponent, fx_constant, n)
    yi = pollard_rho_helper(pollard_rho_helper(x0, fx_exponent, fx_constant, n), 2, fx_constant, n)
    possible_factors = [1]
    while possible_factors[0] == 1:
        xi = pollard_rho_helper(xi, fx_exponent, fx_constant, n)
        yi = pollard_rho_helper(pollard_rho_helper(yi, fx_exponent, fx_constant, n), fx_exponent, fx_constant, n)
        # print(str(xi) + " " + str(yi))
        possible_factors[0] = math.gcd(abs(xi-yi), n)
    n //= possible_factors[0]
    possible_factors.append(n)
    return possible_factors
