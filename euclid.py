

def gcd(num1, num2):
    large = abs(num1)
    small = abs(num2)
    if large < small:
        large, small = small, large
    while small > 0:
        large, small = small, large % small
    return large

if __name__ == '__main__':
    print(15,4,gcd(15,4))
    print(512,240,gcd(512,240))
    print(91,17,gcd(91,17))