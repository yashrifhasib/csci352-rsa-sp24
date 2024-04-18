
from math import sqrt, log
from math import e as math_e
import matplotlib.pyplot as plt

def rho(i):
    return 1/(i**(i))

def aproximate_search_range_size(smooth, x, F):
    x = sqrt(2*x);
    
    count = rho(log(x)/log(smooth)) * x
    numsearch = int((1/(count/x))*smooth/(2*log(F)))
    return numsearch

def print_dickman_rho_data(n):
    # F is the squareroot of e to the power of ( square root of n times sqrt of sqrt of n )
    F = math_e ** (sqrt(log(n) * log(log(n))))
    F = F**(1/2)
    smoothness = 10
    exponent = 2
    for _ in range(10):
        exponent = 1+(exponent-1)*0.5
        while aproximate_search_range_size(smoothness, n, F) > aproximate_search_range_size(smoothness**exponent, n, F):
            smoothness = smoothness**exponent
        smoothness = smoothness ** (1/exponent)
    smoothness = int(smoothness)
    print("function minimum absolute smoothness:",smoothness)
    for _ in range(smoothness//4, smoothness*2+1, smoothness//4):
        print("smoothness:", _, "search size:", aproximate_search_range_size(_, n, F))
    
    figure = plt.figure()
    x = list(range(smoothness//10, smoothness*4+1, smoothness//10))
    y = [aproximate_search_range_size(val, n, F) for val in x]
    # x = [val/100_000_000 for val in x]
    # y = [val/179687 for val in y]
    plt.xlabel("absolute smoothness parameter")
    plt.ylabel("approximate search size")
    plt.plot(x, y)
    plt.xlim(0,8_000_000)
    plt.ylim(0, 1_000_000_000)
    plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
    plt.gca().ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)
    plt.gca().ticklabel_format(axis='both', style='sci', scilimits=(0,0), useMathText=True)

    print(list(zip(x,y)))
    plt.show()
    
    

def dickman_rho_best_smoothness(n):
    """
    This function returns approximately the best possible smoothness parameter in absoulute terms

    n -- the number you want to factor

    return values:

    smoothness -- the smoothness

    aprox.search range -- aproximate search range of the optimal smoothness
    """
    F = math_e ** (  sqrt(log(n) * log(log(n)) ))
    F = F**(1/2)
    smoothness = 10
    exponent = 2
    for _ in range(10):
        exponent = 1+(exponent-1)*0.5
        while aproximate_search_range_size(smoothness, n, F) > aproximate_search_range_size(smoothness**exponent, n, F):
            smoothness = smoothness**exponent
        smoothness = smoothness ** (1/exponent)
    smoothness = int(smoothness)
    search_range = aproximate_search_range_size(_, n, F)
    print("approximate search range:", search_range)
    return smoothness, search_range



if __name__ == '__main__':
    n = 9209839122440374002906008377605580208264841025166426304451583112053;

    print_dickman_rho_data(n)
    print("best smoothness, search range:", dickman_rho_best_smoothness(n))
    

