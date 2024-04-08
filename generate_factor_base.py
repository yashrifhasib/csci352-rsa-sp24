from rsa import next_prime

def create_factor_base(count):
    primes = list()
    primes.append(-1)
    primes.append(2)
    primes.append(3)
    counter = 4
    while len(primes) < count:
        prime = next_prime(counter)
        primes.append(prime)
        counter = prime + 1
    return primes

def save_list_to_file(myList):
    name = "factor_base_" + str(len(myList)) + ".txt"
    with open(name, mode='w', encoding="utf-8") as file:
        for p in myList:
            file.write(str(p)+'\n')
    print("wrote to file", name)

from sys import argv
if __name__ == '__main__':
    if len(argv) < 2:
        print("need pass argument")
        exit()
    primes = create_factor_base(int(argv[1]))
    save_list_to_file(primes)