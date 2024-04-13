from pprint import pprint
from sieve import get_relaitons
from rsa import prime_factors_of as pfo
from squarerootAttack import real_sqrt as sqrt
from factorBaseRecipricol import open_factorbase
from typing import Generator
from math import comb

def combinations(max):
    # if choose_count > max:
    #     raise ValueError("cannot return a proper value")
    for x in range(1,pow(2,max)):
        yield [char == '1' for char in bin(x)[2:]]

def new_representation(factorBase, relation, composite):
    number = pow(relation, 2, composite)
    binary_list = [False] * len(factorBase)
    if number < 0:
        binary_list[0] = True
        number = abs(number)
    else:
        binary_list[0] = False
    for index in range(1,len(binary_list)):
        prime = factorBase[index]
        while number%prime == 0:
            binary_list[index] = not binary_list[index]
            number = number // prime
    result = 0
    for count, bit in enumerate(binary_list):
        if bit:
            result += 2**count
    return binary_list, result

def n_factorial_linear_dependance(factorBase, composite_number, relations):
    """
    This does a crude version of finding a linear dependance in the matrix.

    factorBase -- you need to supply factor base list

    composite_number -- you need to supply the number you want factored

    relations -- you need to supply a list of relations. These numbers are between sqrt(composite_number) and composite_number.
    """
    # create a 'matrix' of representations of all the relations
    matrix = list()
    for relation in relations:
        newRep = new_representation(factorBase, relation, composite_number)
        matrix.append(newRep)
        #print(newRep)
    
    # find the set of relations that give us the zero representation
    linear_relations = []
    for matrix_set in combinations(len(matrix)):
        combination = [matrix[i] for i, bit in enumerate(matrix_set) if bit]
        result = 0
        # Iterate over the lists in parallel and perform bitwise XOR
        for number in combination:
            result = result ^ number[1]
        if result == 0:
            #print(combination)
            linear_relations = [relations[index] for index, x in enumerate(matrix_set) if x]
            break
    return linear_relations


if __name__ == '__main__':
    factorBase = open_factorbase("factor_base_13_new.txt")
    composite = 227179
    start_number = sqrt(composite)
    end_number = start_number +350
    relations = get_relaitons(start_number, end_number, composite, factorBase)
    linear_dependant_relations = n_factorial_linear_dependance(factorBase, composite, relations)
    print(linear_dependant_relations)
