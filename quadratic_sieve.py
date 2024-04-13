from dickman import dickman_rho_best_smoothness
from factorBaseRecipricol import create_factor_base_from_absolute, highest_prime_order
from sieve import relation_combine_factor, get_relaitons
from squarerootAttack import real_sqrt
from notMatrix import meataxe_row_reduction
from rsa import rand_prime

if __name__ == "__main__":
    composite = 227179
    #composite = rand_prime(30)*rand_prime(30)
    print("running quadratic sieve on", composite)
    print("calculating our smoothness parameter")
    absolute_smoothness, search_range = dickman_rho_best_smoothness(composite)
    search_range = int(search_range*.0001)
    search_range = 300 # override for baby number
    absolute_smoothness = 40 # we override for our baby number
    print("absolute smoothness:",absolute_smoothness)
    print("prime index:", highest_prime_order(absolute_smoothness))
    print("creating our factor base")
    factor_base = create_factor_base_from_absolute(absolute_smoothness, composite)
    print(factor_base)
    print("finding our relations")
    relation_start = real_sqrt(composite)
    relation_end = min(real_sqrt(2*composite)-1,relation_start + search_range)
    print("max search range:",int(relation_start*1.4142135)- relation_start,"total search range:",relation_end-relation_start)
    relations = get_relaitons(relation_start, relation_end, composite, factor_base)
    print("our relations:", relations, sep='\n')
    print("count factorbase:", len(factor_base), "count relations:", len(relations))
    print("finding linear dependance")
    linear_dependance = meataxe_row_reduction(factor_base, composite, relations)
    print("our relations that are linearly dependant:", linear_dependance, sep='\n')
    print("finishing the job:")
    factors = relation_combine_factor(linear_dependance, composite)
    print(f"composite number: {composite}", f"factors: {factors}", sep='\n')
