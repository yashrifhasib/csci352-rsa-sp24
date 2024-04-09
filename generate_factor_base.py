from rsa import next_prime

def euler_criterion(prime, n):
    number = pow(n,(prime-1)//2,prime)
    if number == 1:
        return True
    return False

def create_factor_base(count, n=9209839122440374002906008377605580208264841025166426304451583112053):
    primes = list()
    primes.append(-1)
    primes.append(2)
    primes.append(3)
    prime = 4
    loopcount = 0
    while len(primes) < count:
        loopcount += 1
        prime = next_prime(prime + 1)
        if euler_criterion(prime, n):
            primes.append(prime)
    print(f"created factor base with {len(primes)} length and searched {loopcount} numbers")
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
