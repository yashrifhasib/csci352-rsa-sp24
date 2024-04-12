import math
from sieve import get_relaitons
from factorBaseRecipricol import create_factor_base
from rsa import rand_prime

def find_factors(factor_base, relations, N):
    # Find the product of relations
    square1 = 1
    for relation in relations:
        square1 *= relation
    
    # Calculate the difference between the product and N
    diff = abs(square1 - N)
    
    # Find factors using the difference
    i = math.floor(math.sqrt(diff))
    if i * i != diff:
        raise ValueError("No solution exists for the given factor base, relations, and composite number")
    
    j = math.floor(math.sqrt(square1))
    factors = [j - i, j + i]
    
    return factors

# Example usage
prime_factor1 = rand_prime(10)
prime_factor2 = rand_prime(10)
N = prime_factor1 * prime_factor2
print(prime_factor1)
print(prime_factor2)
print(N)
factor_base = create_factor_base(17, N)# Example factor base
print(factor_base)
start_number = math.floor(math.sqrt(N))
relations = get_relaitons(start_number, start_number+100, N, factor_base)
try:
    factors = find_factors(factor_base, relations, N)
    print("Factors of", N, ":", factors)
except ValueError as e:
    print(e)
