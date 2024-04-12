import time
from math import log,e
from pprint import pprint
from TonelliShanks import tonelli_shanks
from squarerootAttack import real_sqrt as sqrt

FACTOR_BASE_FILE = "factor_base_13_new.txt"

def create_offsets(modulus, prime):
    tonelli = tonelli_shanks(modulus, prime)
    offsets = list()
    for t in tonelli:
        offsets.append((t - start_number)%prime)
    return offsets

def reduce_sieve(sieve, modulus, factorBase):
    # TODO: implement special -1 of factorbase
    for prime in factorBase[1:]:
        offsets = create_offsets(modulus, prime)
        for o in offsets:
            for i in range(o, len(sieve), prime):
                while sieve[i] % prime == 0:
                    sieve[i] //= prime

def give_row_numbers(base_numbers, sieve):
    ret = list()
    for entry in zip(base_numbers, sieve):
        if entry[1] == 1:
            ret.append(entry[0])
    return ret

def get_relaitons(start_number, end_number, modulus, factorBase):
    base_numbers = list(range(start_number, end_number, 1))
    sieve = [pow(x,2,modulus) for x in base_numbers]
    reduce_sieve(sieve, modulus, factorBase)
    return give_row_numbers(base_numbers, sieve)

if __name__ == "__main__":
    factorBase = None
    with open(FACTOR_BASE_FILE, 'r', encoding='utf-8') as file:
        factorBase = [int(line) for line in file]
    # N = 9209839122440374002906008377605580208264841025166426304451583112053
    N = 227179
    
    start_number = sqrt(N)
    end_number = start_number + 20
    relations = get_relaitons(start_number, end_number, N, factorBase)
    
    print("The following is the range of numbers on the left, and the modual quadratic on the right:")
    pprint(list(zip(list(range(start_number, end_number, 1)), [pow(x,2,N) for x in list(range(start_number, end_number, 1))])))
    print("The following is the relations we have discovered via sieving:")
    pprint(relations)
