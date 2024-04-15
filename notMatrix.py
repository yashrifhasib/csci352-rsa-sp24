from pprint import pprint
from sieve import get_relaitons, relation_combine_factor
from rsa import prime_factors_of as pfo
from rsa import is_prime
from squarerootAttack import real_sqrt as sqrt
from factorBaseRecipricol import open_factorbase
from typing import Generator
from math import comb
import subprocess
from dickman import dickman_rho_best_smoothness
from factorBaseRecipricol import create_factor_base_from_absolute, highest_prime_order
from rsa import rand_prime;



TEMP_MATRIX_FILE = "meataxe/intermediatematrix"
TEMP_MATRIX_FILE_NULL = "meataxe/intermediatematrixNull"

def new_representation(factorBase, relation, composite):
    """
    This function returns an integer. This integer is the value of a row in a matrix.

    The max size of this integer is pow(2, (len(factorBase))) - 1. This can create the
    zero vector, or the complete vector, or any possible row configuration.

    parameters:
        factorBase - list of primes \n
        relation - a specific number from a relations list. \n
        composite - the modulus we need to factor.
    """
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
    return binary_list

'''    string = ""
    for value in binary_list:
        if value:
            string += '1'
        else:
            string += '0'
    representation = int(string, base=2)'''


'''
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
    return ret'''

def export_matrixTXT(matrix, filename):
    '''
    output the vectors of our relations(as rows) in matrix forms, where columns is the len(factorBase)
    -matrix -- the generated matrix to output 
    -filename -- where the file will be stored 
    '''
    rows = len(matrix)
    cols = len(matrix[0])
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"matrix field=2 rows={rows} cols={cols}\n")
        for vector in (matrix):
            # Convert the vector to a space-separated string
            vector_text = ' '.join('1' if val else '0' for val in vector)
            file.write(vector_text + '\n')

def extract_elements(relations, solution):
    '''
    it maps relations at all indices of solution set with one and returns this linear dependent set out in a list 
    - relations -- contains the full list of smooth relations generated for QS
    - solution -- refers to each row input from the null space (our solution set)

    '''

    if len(relations) != len(solution):
        raise ValueError(f"relations and index_vector must have the same length{len(relations),len(solution)}")

    elements = []
    for i in range(len(solution)):
        if solution[i] == 0:
            continue
        entry = relations[i]
        elements.append(entry)

    return elements

def read_matrix_from_file(filename):
    '''
    - filename -- stored location of the txt file of null space basis vectors
    meataxe output matrix in rows of max of 80. If it has over 80 cols, it will be written on the next line
    '''
    matrix = list()
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the first line to get matrix dimensions
        line = file.readline().strip()
        _, field, rows, cols = line.split()
        rows = int(rows.split('=')[1])
        cols = int(cols.split('=')[1])
        # Read the remaining lines containing the matrix
        line = file.readline().strip()
        for _ in range(rows):
            row = []
            count = 0
            while(count < cols):
                if(line != ""):
                    char = line[0]
                    line = line[1:]
                    if char.isdigit():
                        row.append(int(char))
                        count+=1
                else:
                    line = file.readline().strip()
            matrix.append(row)

    return matrix

def n_zero_vector_combination(nullSpace, relations):
    """    blank docstring    """    
    for index_v in nullSpace:

        print(len(index_v), len(relations))
        linear_dependance = extract_elements(relations, index_v)
        print(linear_dependance)
        factors = relation_combine_factor(linear_dependance, composite)
        condition = len(factors) > 2 or ((factors[0] != 1 and factors[0] != composite) or (factors[1] != 1 and factors[1] != composite))
        if condition:
            return linear_dependance, factors
    return None, None
            

            

def build_matrix(factorBase, relations, composite_number):
    '''
    build matrix with given factorBase and list of smooth relations
    '''
    ret = list()
    for relation in relations:
        newRep = new_representation(factorBase, relation, composite_number)
        ret.append(newRep)
    return ret

def meataxe_linear_dependance(factorBase, composite_number, relations):
    """
    We do stuff.

    - factorBase -- you need to supply factor base list

    - composite_number -- you need to supply the number you want factored

    - relations -- you need to supply a list of relations. These numbers are between sqrt(composite_number) and composite_number.
    """
    # create a 'matrix' of representations of all the relations
    mymatrix = build_matrix(factorBase, relations, composite_number)
    print("-------------")
    export_matrixTXT(mymatrix, "meataxe/matrix1.txt")
    subprocess.run(["zcv", "meataxe/matrix1.txt", TEMP_MATRIX_FILE])

    subprocess.run(["znu", TEMP_MATRIX_FILE, TEMP_MATRIX_FILE_NULL])

    subprocess.run(["zpr", TEMP_MATRIX_FILE_NULL, "meataxe/matrix2.txt"])
    print("-------------")

    mymatrix2 = read_matrix_from_file("meataxe/matrix2.txt")
    #(len(mymatrix2), len(mymatrix2[0]))
    # find the set of relations that give us the zero representation
    print(mymatrix2, relations, len(mymatrix2), len(relations))
    return n_zero_vector_combination(mymatrix2, relations)


def sieve(composite):
    '''
    combine all method we have and perform sieve on numbers
    '''
    temp_factor = list()
    while(composite%2 == 0):
        temp_factor.append(2)
        composite = composite >> 1
    print("Composite number",composite)
    absolute_smoothness, search_range = dickman_rho_best_smoothness(composite)
    print("absolute smoothness:",absolute_smoothness)
    factorBase = create_factor_base_from_absolute(absolute_smoothness, composite)

    #factorBase = open_factorbase("factor_base_13_new.txt")
    relation_start = sqrt(composite)
    interval = 1_000_000
    relations = list()
    while len(relations) < len(factorBase) + 100:
        relations = relations + get_relaitons(relation_start, relation_start + interval, composite, factorBase)
        relation_start = relation_start + interval
        print("relations found:", len(relations))
    linear_dependant_relations, factors = meataxe_linear_dependance(factorBase, composite, relations)
    
    if(factors != None):
        factors = factors + temp_factor
        all_prime = all(is_prime(f) for f in factors)

        if (not all_prime):
            new_factors = list()
            for f in factors:
                if(not is_prime(f)):
                    linear_ind, sub_factors = sieve(f)
                    if(sub_factors != None):
                        new_factors.extend(sub_factors)
                    else: 
                        new_factors.append(f);
                    print("Factor composite factor:" + f);
                else:
                    new_factors.append(f);
            factors = new_factors;
        return linear_dependant_relations, factors
    else:
        return linear_dependant_relations,temp_factor

if __name__ == '__main__':
    composite = rand_prime(30)*rand_prime(30)
    #composite = 2**2**7 + 1
    print(composite)
    try:
        linear_dependant_relations, factors = sieve(composite)

        print("Relation:" , linear_dependant_relations)
        print("Factor of ",composite," = ", factors)
        product = 1;
        for i in range(len(factors)):
            product *= factors[i]

        print(f"Check if they are the factor: {product == composite}")

    except ValueError as e:
        print("An error occurred:", e)

