import os
import re
from notMatrix import build_matrix, export_matrixTXT, read_relations, n_zero_vector_combination, read_matrix_from_file
import subprocess
from dickman import dickman_rho_best_smoothness
from factorBaseRecipricol import create_factor_base_from_absolute
from notMatrix import new_representation
from sieve import relation_combine_factor
from math import ceil

MASTER_FILE = "work/master_final.txt"
TEMP_MATRIX_FILE = "work/intermediatematrix"
TEMP_MATRIX_FILE_NULL = "work/intermediatematrixNull"
MATRIX1 = "work/matrix1.txt"
MATRIX2 = "work/matrix2.txt"


def meataxe(matrix, cols):
    mymatrix = matrix
    print("-------------")
    export_matrixTXT(mymatrix, MATRIX1, cols)
    subprocess.run(["zcv", MATRIX1, TEMP_MATRIX_FILE])

    subprocess.run(["znu", TEMP_MATRIX_FILE, TEMP_MATRIX_FILE_NULL])

    subprocess.run(["zpr", TEMP_MATRIX_FILE_NULL, MATRIX2])
    print("-------------")
    return MATRIX2

def find_LC(factorBase, composite_number, relations):
    matrix = build_matrix(factorBase, relations, composite_number)
    matrix2_file = meataxe(matrix , len(factorBase))
    temp_null_matrix = []
    row_interval = 1000

    with open(matrix2_file, 'r', encoding='utf-8') as file:
        # Read the first line to get matrix dimensions
        line = file.readline().strip()
        _, field, rows, cols = line.split()
        rows = int(rows.split('=')[1])
        cols = int(cols.split('=')[1])
        for _ in range(rows):
            if(len(temp_null_matrix) == row_interval):
                set, factor = n_zero_vector_combination(temp_null_matrix,relations)
                if(set != None):
                    return set,factor
                #reinitializer
                temp_null_matrix = []

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
            temp_null_matrix.append(row)
        return n_zero_vector_combination(temp_null_matrix, relations)



def master_read_from_folder(folder, file_pattern):
    all_files = []
    for filename in os.listdir(folder):
        if re.match(file_pattern, filename):
            with open(os.path.join(folder, filename), 'r') as file:
                file_data = file.read()
                all_files.append(file_data)                

    combined_data = '\n'.join(all_files)

    with open(MASTER_FILE, 'w') as outfile:
        outfile.write(combined_data)
    print(f"Combined data from {len(all_files)} files and saved to {MASTER_FILE}")

def create_master_file():
    all_directory = 'work/'
    pattern = r'work48763_\d+\.txt'
    master_read_from_folder(all_directory, pattern)

def generator_null_combinations(relations, nullspace_file_name) -> list[bool]:
    # MATRIX2  is the nullspace plaintext file
    with open(MATRIX2, 'r', encoding='utf-8') as file:
        header = file.readline().strip().split()
        rows = int(header[2][5:])
        cols = int(header[3][5:])
        string = ""
        for _ in range(ceil(cols/80)):
            string = string + file.readline().strip()
        yield [char == '1' for char in string]

def generate_my_matrix(matrix, factorBase, relations, composite):
    with open(matrix, 'w', encoding='utf-8') as file:
        row_count = len(relations)
        row_length = len(factorBase)
        header = f"matrix field=2 rows={row_count} cols={row_length}"
        file.write(header)
        for relation in relations:
            file.write('\n')
            rep = new_representation(factorBase, relation, composite)
            for entry in rep:
                file.write("1" if entry else "0")

def matthew_main():
    composite = 9209839122440374002906008377605580208264841025166426304451583112053
    create_master_file()
    print("master file created")
    absolute_smoothness, _ = dickman_rho_best_smoothness(composite)
    factorBase = create_factor_base_from_absolute(int(absolute_smoothness*.7), composite)
    print("factor base created")
    #calculate relations matrix
    relations = read_relations(MASTER_FILE)
    print("relations recieved from master file")
    print("generating relations X factorbase matrix")
    # MATRIX1 is the relations X factorbase file
    generate_my_matrix(MATRIX1, factorBase, relations, composite)
    print("converting matrix to meataxe")
    subprocess.run(["zcv", MATRIX1, TEMP_MATRIX_FILE])
    print("finding nullspace")
    subprocess.run(["znu", TEMP_MATRIX_FILE, TEMP_MATRIX_FILE_NULL])
    print("exporting from meataxe to text")
    subprocess.run(["zpr", TEMP_MATRIX_FILE_NULL, MATRIX2])
    print("finished finding nullspace")
    # generate linear relations
    # MATRIX2 is the nullspace text file in respect to MATRIX1
    for linearRelation in generator_null_combinations(relations, MATRIX2):
        #test linearRelation
        #TODO test relations, when factored print
        subset = [relations[i] for i in range(relations) if linearRelation[i]]
        factors = relation_combine_factor(subset, composite)
        if composite not in factors:
            break
    print("factors are:",factors)

if __name__ == '__main__':
    composite = 9209839122440374002906008377605580208264841025166426304451583112053

    all_directory = 'work/0-1599_2000-2399_4600-4900_5200-5900_7000-8000'
    pattern = r'work48763_\d+\.txt'
    #pattern = r'dummyFile.txt'
    master_read_from_folder(all_directory, pattern)
    relations = read_relations(MASTER_FILE)

    absolute_smoothness, _ = dickman_rho_best_smoothness(composite)
    factorBase = create_factor_base_from_absolute(int(absolute_smoothness*.7), composite)

    linear_dependant_relations, factors = find_LC(factorBase, composite, relations)

    if(factors != None):
        print("Relation:" , linear_dependant_relations)
        print("Factor of ",composite," = ", factors)
        product = 1;
        for i in range(len(factors)):
            product *= factors[i]

        print(f"Check if they are the factor: {product == composite}")
    else:
        print("No solution found.")

    
    