import os
import re
from notMatrix import build_matrix, export_matrixTXT, read_relations, n_zero_vector_combination, read_matrix_from_file
import subprocess
from dickman import dickman_rho_best_smoothness
from factorBaseRecipricol import create_factor_base_from_absolute

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

    mymatrix2 = read_matrix_from_file(MATRIX2)
    return mymatrix2;

def find_LC(factorBase, composite_number, relations):
    matrix = build_matrix(factorBase, relations, composite_number)
    nullspace = meataxe(matrix , len(factorBase))
    return n_zero_vector_combination(nullspace, relations)


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


if __name__ == '__main__':
    composite = 9209839122440374002906008377605580208264841025166426304451583112053

    all_directory = 'work/'
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

    
    