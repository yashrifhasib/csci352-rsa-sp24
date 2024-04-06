from sys import argv
from rsa import rand_prime
from subprocess import run

executable = 'a.exe'

def foo(number):
    run([executable, number])

from time import time
if __name__ == '__main__':
    rangecount = 20
    bitcount = int(argv[1])
    c_list = list()
    for _ in range(rangecount):
        c_list.append(str(rand_prime(223-bitcount)*rand_prime(bitcount)))
    time1 = time()
    for c in c_list:
        run([executable, c])
    print(f'running time for {rangecount} runs:', time() - time1)
