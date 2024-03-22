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