from dickman import dickman_rho_best_smoothness
from factorBaseRecipricol import create_factor_base_from_absolute, highest_prime_order
from sieve import relation_combine_factor, get_relaitons
from squarerootAttack import real_sqrt
from notMatrix import find_linear_dependance

if __name__ == "__main__":
    composite = 227179
    print("calculating our smoothness parameter")
    absolute_smoothness = dickman_rho_best_smoothness(composite)
    absolute_smoothness = 40 # we override for our baby number
    print("absolute smoothness:",absolute_smoothness)
    print("prime index:", highest_prime_order(absolute_smoothness))
    print("creating our factor base")
    factor_base = create_factor_base_from_absolute(absolute_smoothness, composite)
    print(factor_base)
    print("finding our relations")
    relation_start = real_sqrt(composite)
    relation_end = real_sqrt(int( 2 * (relation_start**2) ))
    relations = get_relaitons(relation_start, relation_end, composite, factor_base)
    print("finding linear dependance")
    linear_dependance = find_linear_dependance(factor_base, composite, relations)
    print("finishing the job")
    factors = relation_combine_factor(linear_dependance, composite)
    print("composite number:", composite, "factors:", factors)