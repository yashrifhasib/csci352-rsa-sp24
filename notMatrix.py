from pprint import pprint
from sieve import get_relaitons
from rsa import prime_factors_of as pfo
from squarerootAttack import real_sqrt as sqrt
from factorBaseRecipricol import open_factorbase
from typing import Generator
from math import comb
import subprocess

TEMP_MATRIX_FILE = "meataxe/intermediatematrix"

def combinations(max):
    # if choose_count > max:
    #     raise ValueError("cannot return a proper value")
    for x in range(1,pow(2,max)):
        yield [char == '1' for char in bin(x)[2:]]

def new_representation(factorBase, relation, composite):
    #calculate the related number
    number = pow(relation, 2, composite)
    # initialize our vector
    binary_list = [False] * len(factorBase)
    # fill the -1 colunm of the factor base
    if number < 0:
        binary_list[0] = True
        number = abs(number)
    else:
        binary_list[0] = False
    # divide out the number, create a row
    for index in range(1,len(binary_list)):
        prime = factorBase[index]
        while number%prime == 0:
            binary_list[index] = not binary_list[index]
            number = number // prime
    # binary_list is a row, a pylist of binary. index 0 is -1, index max is the highest prime
    # calc representation
    string = ""
    for value in binary_list:
        if value:
            string += '1'
        else:
            string += '0'
    representation = int(string, base=2)
    return representation


def n_factorial_linear_dependance(factorBase, composite_number, relations):
    """
    # DEPRICATED
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
            result = result ^ number
        if result == 0:
            #print(combination)
            linear_relations = [relations[index] for index, x in enumerate(matrix_set) if x]
            break
    return linear_relations

def left_pad_binary(number, length):
    """

    6,5 displays as '00110'
    """
    ret = bin(number)[2:]
    return ('0'*(length-len(ret))) + ret

def left_pad_binary_revert(string):
    """
    opposite of left_pad_binary.

    takes '00110' and returns 6
    """
    return int(string, base=2)

def export_matrix(matrix, row_length, filename):
    row_count = len(matrix)
    header = f"matrix field=2 rows={row_count} cols={row_length}"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(header)
        for representation in matrix:
            file.write(f"\n{left_pad_binary(representation, row_length)}")

def import_matrix(filename):
    ret = list()
    with open(filename, 'r', encoding='utf-8') as file:
        header = file.readline()
        for line in file:
            ret.append(left_pad_binary_revert(line.strip()))
    return ret

def meataxe_row_reduction(factorBase, composite_number, relations):
    """
    We do stuff.

    - factorBase -- you need to supply factor base list

    - composite_number -- you need to supply the number you want factored

    - relations -- you need to supply a list of relations. These numbers are between sqrt(composite_number) and composite_number.
    """
    # create a 'matrix' of representations of all the relations
    mymatrix = list()
    for relation in relations:
        newRep = new_representation(factorBase, relation, composite_number)
        mymatrix.append(newRep)
    export_matrix(mymatrix, len(factorBase), "meataxe/matrix1.txt")
    subprocess.run(["zcv", "meataxe/matrix1.txt", TEMP_MATRIX_FILE])

    # TODO do row reduction

    subprocess.run(["zpr", TEMP_MATRIX_FILE, "meataxe/matrix2.txt"])
    mymatrix = import_matrix("meataxe/matrix2.txt")
    # find the set of relations that give us the zero representation
    linear_relations = []
    for matrix_set in combinations(len(mymatrix)):
        combination = [mymatrix[i] for i, bit in enumerate(matrix_set) if bit]
        result = 0
        # Iterate over the lists in parallel and perform bitwise XOR
        for number in combination:
            result = result ^ number
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
    linear_dependant_relations = meataxe_row_reduction(factorBase, composite, relations)
    print(linear_dependant_relations)
