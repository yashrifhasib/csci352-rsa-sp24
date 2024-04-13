import math

def rho(i):
    return 1/(i**(i))

def aproximate_search_range_size(smooth, x, F):
    x = math.sqrt(x);
    count = rho(math.log(x)/math.log(smooth)) * x
    numsearch = int((1/(count/x))*smooth/(2*math.log(F)))
    return numsearch

def print_dickman_rho_data(n):
    F = math.e ** (  math.sqrt(math.log(n) * math.log(math.log(n)) ))
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

def dickman_rho_best_smoothness(n):
    """
    This function returns approximately the best possible smoothness parameter in absoulute terms

    n -- the number you want to factor
    """
    F = math.e ** (  math.sqrt(math.log(n) * math.log(math.log(n)) ))
    F = F**(1/2)
    smoothness = 10
    exponent = 2
    for _ in range(10):
        exponent = 1+(exponent-1)*0.5
        while aproximate_search_range_size(smoothness, n, F) > aproximate_search_range_size(smoothness**exponent, n, F):
            smoothness = smoothness**exponent
        smoothness = smoothness ** (1/exponent)
    smoothness = int(smoothness)
    return smoothness



if __name__ == '__main__':
    n = 9209839122440374002906008377605580208264841025166426304451583112053;

    print_dickman_rho_data(n)
    print("best smoothness:", dickman_rho_best_smoothness(n))
    

