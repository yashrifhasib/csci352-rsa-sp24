from sys import argv
from dickman import dickman_rho_best_smoothness
from factorBaseRecipricol import create_factor_base_from_absolute
from sieve import get_relaitons
from squarerootAttack import real_sqrt as sqrt

def create_output(start, myrelations):
    with open("work"+str(start)+".txt", 'w', encoding='utf-8') as file:
        for number in myrelations:
            file.write(str(number)+'\n')

if __name__ == '__main__':
    N = 9209839122440374002906008377605580208264841025166426304451583112053
    #factor base
    
    absolute_smoothness, _ = dickman_rho_best_smoothness(N)
    factorBase = create_factor_base_from_absolute(int(absolute_smoothness*.7), N)

    relations = list()

    interval = 5_000_000
    iterations = 3
    offset = int(argv[1]) * iterations * interval
    start = sqrt(N) + offset
    print("start sieving")
    for _ in range(iterations):
        end = start + interval
        relations = get_relaitons(start, end, N, factorBase)
        start = end
    print("end sieving, new found relations:", len(relations))
    create_output(start, relations)