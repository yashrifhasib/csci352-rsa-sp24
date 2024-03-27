

def gcd(large, small):
    large = abs(large)
    small = abs(small)
    if large == small:
        return 1
    if large < small:
        temp = large
        large = small
        small = temp
    while large % small > 0:
        remainder = large % small
        large = small
        small = remainder
    return small

if __name__ == '__main__':
    print(15,4,gcd(15,4))
    print(512,240,gcd(512,240))
    print(91,17,gcd(91,17))