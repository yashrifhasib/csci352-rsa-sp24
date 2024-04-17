from sys import argv
from dickman import dickman_rho_best_smoothness
from factorBaseRecipricol import create_factor_base_from_absolute
from sieve import get_relaitons
from squarerootAttack import real_sqrt as sqrt

def create_output(name_seed, myrelations):
    with open("work/work"+str(name_seed)+".txt", 'w', encoding='utf-8') as file:
        for number in myrelations:
            file.write(str(number)+'\n')

if __name__ == '__main__':
    if len(argv)<3:
        print("need args")
        exit()
    
    arg1 = int(argv[1]) 
    arg2 = int(argv[2]) 
    
    
    N = 9209839122440374002906008377605580208264841025166426304451583112053
    #factor base
    
    absolute_smoothness, _ = dickman_rho_best_smoothness(N)
    factorBase = create_factor_base_from_absolute(int(absolute_smoothness), N)

    relations = list()

    for x in range(arg1, arg2):
        interval = 5_000_000
        iterations = 12
        offset = x * iterations * interval
        start = sqrt(N) + offset
        print("start sieving")
        for _ in range(iterations):
            print("sieving: ",start)
            end = start + interval
            relations = get_relaitons(start, end, N, factorBase)
            start = end
        print("end sieving, new found relations:", len(relations))
        create_output(x, relations)