from math import ceil
from math import sqrt
from time import time
from euclid import gcd
from rsa import prime_factors_of
from rsa import is_prime

def is_smooth(b, square):
    if square <= 1:
        return False
    prime_factors = prime_factors_of(square)
    if prime_factors[-1] <= b:
        return True
    return False


def dixon(n, b):
    z = list()
    a = ceil(sqrt(n))
    y = 1
    x = 1
    for i in range(a, n):
        if is_smooth(b, pow(i, 2, n)):
            z.append(i)
    breaking = False
    for i in z:
        for j in z:
            if pow(i*j, 2, n) != 0 and i != j:
                a = (i * j) % n
                prime_x = prime_factors_of(pow(i, 2, n))
                prime_y = prime_factors_of(pow(j, 2, n))
                prime_xy = list()
                #print("The prime factors of " + str(i) + " are " + str(prime_x))
                #print("The prime factors of " + str(j) + " are " + str(prime_y))
                x = 0
                y = 0
                no_change_x = False
                no_change_y = False
                while True:
                    if x == len(prime_x) and not no_change_x:
                        no_change_x = True
                        x = len(prime_x) - 1
                    if y == len(prime_y) and not no_change_y:
                        no_change_y = True
                        y = len(prime_y) - 1
                    if no_change_x and no_change_y:
                        break
                    temp_x = prime_x[x]
                    temp_y = prime_y[y]
                    #print("no_change_x = " + str(no_change_x) + ", no_change_y = " + str(no_change_y))
                    #print("x = " + str(x) + " and y = " + str(y))
                    #print("temp_x = " + str(temp_x) + ", temp_y = " + str(temp_y))
                    #print(prime_xy)
                    if temp_x == temp_y:
                        prime_xy.append(temp_x)
                        prime_xy.append(temp_y)
                        if not no_change_x:
                            x += 1
                        if not no_change_y:
                            y += 1
                        #print("== condition values are " + str(temp_x) + " and " + str(temp_y))
                    elif temp_x < temp_y and no_change_x:
                        prime_xy.append(temp_y)
                        y += 1
                        #print("temp_x < temp_y and no_change_x condition values are " + str(temp_x) + " and " + str(temp_y))
                    elif temp_x < temp_y and not no_change_x:
                        prime_xy.append(temp_x)
                        x += 1
                        #print("temp_x < temp_y and not no_change_x condition values are " + str(temp_x) + " and " + str(temp_y))
                    elif temp_y < temp_x and no_change_y:
                        prime_xy.append(temp_x)
                        x += 1
                        #print("temp_y < temp_x and no_change_y condition values are " + str(temp_x) + " and " + str(temp_y))
                    elif temp_y < temp_x and not no_change_y:
                        prime_xy.append(temp_y)
                        y += 1
                        #print("temp_y < temp_x and not no_change_y condition values are " + str(temp_x) + " and " + str(temp_y))
                #print(prime_xy)
                last_m = prime_xy[0]
                primes = [[prime_xy[0], 0]]
                last_index = 0
                for m in prime_xy:
                    if m == last_m:
                        primes[last_index][1] += 1
                    else:
                        last_m = m
                        primes.append([m, 1])
                        last_index += 1
                #print(primes)
                product = 1
                for m in primes:
                    m[1] //= 2
                    product *= pow(m[0], m[1]) 
                b = pow(product, 1, n)
                if ((a - b) != 0) and ((a + b) != n) and gcd(a - b, n) != 1 and gcd(a + b, n) != 1:
                    breaking = True
                    break
        if (breaking):
            break
    return [gcd(a - b, n), gcd(a + b, n)]

def dixon_factorization(n, b):
    return_val = list()
    while n != 1:
        factors = dixon(n, b)
        factors_prime = [is_prime(factors[0]), is_prime(factors[1])]
        if factors_prime[0] and factors_prime[1]:
            n //= factors[0]
            n //= factors[1]
            return_val.append(factors[0])
            return_val.append(factors[1])
        elif factors_prime[0]:
            n //= factors[0]
            return_val.append(factors[0])
        elif factors_prime[1]:
            n //= factors[1]
            return_val.append(factors[1])
        else:
            small = max(factors)
            factors = dixon(small, b)
            if is_prime(factors[0]): 
                n //= factors[0]
                return_val.append(factors[0])
            if is_prime(factors[1]): 
                n //= factors[1]
                return_val.append(factors[1])
    return return_val

num = 91
b = 3
print("The number is " + str(num) + " and B is " + str(b))
start_time = time()
print(dixon_factorization(num, b))
end_time = time()
print("runtime:", end_time - start_time)