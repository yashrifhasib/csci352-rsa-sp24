import time
from math import log,e
from gmpy2 import isqrt, mpz
from pprint import pprint
from rsa import prime_factors_of as pfo
from TonelliShanks import tonelli_shanks
from squarerootAttack import real_sqrt as sqrt
from euclid import gcd
from factorBaseRecipricol import open_factorbase

FACTOR_BASE_FILE = "factor_base_13_new.txt"

def create_offsets(modulus: int, prime: int, start_number: int) -> list[int]:
    """This function runs tonelli shanks and
    modifies the outputs to work with the QS"""
    tonelli = tonelli_shanks(modulus, prime)
    offsets = list()
    for t in tonelli:
        offsets.append((t - start_number)%prime) # TODO Modify this to get outside range sqrt(N) to sqrt(2n)?
    return offsets

def reduce_sieve(sieve: list[int], modulus: int, factorBase: list[int], start_number: int) -> None:
    """This function modifies the sieve input,
    resulting in a value of 1 if it's smooth with
    respect to the factor base and modulus supplied."""
    # TODO: implement special -1 of factorbase
    for prime in factorBase[1:]:
        offsets = create_offsets(modulus, prime, start_number)
        for o in offsets:
            for i in range(o, len(sieve), prime):
                while sieve[i] % prime == 0:
                    sieve[i] //= prime

def give_row_numbers(base_numbers: list[int], sieve: list[int]) -> list[int]:
    """This function takes a reduced sieve base numbers
    and returns the base numbers which are smooth to how
    the sieve was reduced.
    
    """
    ret = list()
    for entry in zip(base_numbers, sieve):
        if entry[1] == 1:
            ret.append(entry[0])
    return ret

def get_relaitons(start_number: int, end_number: int, composite: int, factorBase: list[int]):
    """This is a one call wonder. Creates a sieve between the start and the end
    with respect to a factor base and a composite number to factor.
    
    start_number -- the start of your relation set

    end_number -- maximum of your relation set

    composite -- number you wish to factor

    factorBase -- your factor base

    Return values:
    - list[int] : values between start_number and end_number that quadratic modulo are smooth numbers over the factor base
    """
    base_numbers = list(range(start_number, end_number, 1))
    sieve = [pow(x,2,composite) for x in base_numbers]
    reduce_sieve(sieve, composite, factorBase, start_number)
    return give_row_numbers(base_numbers, sieve)

def mul(my_list) -> int:
    ret = 1
    for num in my_list:
        ret *= num
    return ret

def relation_combine_factor(relations, n):
    """
    This is the last, last part of the quadratic sieve. Take list of relations that
    corespond to a perfect square, and use it to get a factor out of n.
    """
    part1 = mul(relations) % n
    print("mul1 done")
    list2 = list()
    for val in relations:
        list2.append(pow(val,2,n))
    print("list2 created")
    part2 = isqrt(mpz(mul(list2)))
    print("part2 done")
    factor1 = gcd(abs(part1 - part2), n)
    print("gcd complete")
    return [int(factor1), int(n//factor1)]

def save_relations():
    raise NotImplementedError()

def load_relations():
    raise NotImplementedError()

if __name__ == "__main__":
    factorBase = open_factorbase(FACTOR_BASE_FILE)
    # N = 9209839122440374002906008377605580208264841025166426304451583112053
    N = 227179
    
    start_number = sqrt(N)
    end_number = sqrt(2*N)
    relations = get_relaitons(start_number, end_number, N, factorBase)
    
    print("The following is the range of numbers on the left, and the modulus quadratic on the right:")
    pprint(list(zip(list(range(start_number, end_number, 1)), [pow(x,2,N) for x in list(range(start_number, end_number, 1))])))
    print("The following is the relations we have discovered via sieving:")
    pprint(list(zip(relations, [pfo(pow(x,2,N)) for x in relations])))
