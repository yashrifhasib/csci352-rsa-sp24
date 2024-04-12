import random
import math
import time

start_time = time.time()


def rho(i):
    return 1/(i**(i))

def foo(smooth, x, n, F, f):
    # print("Size of factor base", smooth/(2*math.log(F)))
    #smooth = 86400*2
    x = math.sqrt(x);

    #print(smooth/(2*math.log(F)))
    count = rho(math.log(x)/math.log(smooth)) * x
    # print("u", math.log(x)/math.log(smooth))
    #print(rho(math.log(x)/math.log(smooth)) * smooth);
    # print("dickman rho when max is sqrt of x", count)
    # print("ntrials to find 1 smooth number:", 1/(count/x))
    numsearch = int((1/(count/x))*smooth/(2*math.log(F)))
    print("binary length of number of numbers searched",smooth, numsearch)
    

if __name__ == '__main__':
    n = 9209839122440374002906008377605580208264841025166426304451583112053;
    x = 9209839122440374002906008377605580208264841025166426304451583112053;

    '''for i in range(1000):
        count = x*rho(i+1)
        if(count>0):
            print("smooth ", x**(1.0/(i+1)), ": ", count);'''

    F = math.e ** (  math.sqrt(math.log(n) * math.log(math.log(n)) ))
    F = F**(1/2)
    #B = B**(math.sqrt(2)/4)
    f = F/(2*math.log(F))

    #print(F);
    #print(f);
    #print(x*rho(math.log(x)/math.log(1127997)));
    smooth = 1127997
    smooth = 900000
    # End the timer
    for _ in range(100000,4000000,100000):
        foo(_, x, n, F, f)
    end_time = time.time()
    # Calculate the execution time
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

