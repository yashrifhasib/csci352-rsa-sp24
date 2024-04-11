
from time import time

def Eratosthenes(num):
    primeBools = {i:True for i in range(2,num+1)}
# boolean array
    p = 2
    while (p * p <= num):
        
        # If prime[p] is not
        # changed, then it is a prime
        if (primeBools[p] == True):
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                primeBools[i] = False
        p += 1
    return [p for p in range(2,num+1) if primeBools[p]]



def save_list_to_file(myList):
    name = "3Mil_primes" + str(len(myList)) + ".txt"
    with open(name, mode='w', encoding="utf-8") as file:
        for p in myList:
            file.write(str(p)+'\n')
    print("wrote to file", name)
    
 
if __name__ == "__main__":
    start = time()
    primes = Eratosthenes(50000000)
    save_list_to_file(primes)
        
    end = time()
    
    print(len(primes),end-start)