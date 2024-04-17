def gcd(num1, num2):
    large = abs(num1)
    small = abs(num2)
    if large < small:
        large, small = small, large
    while small > 0:
        large, small = small, large % small
    return large

def extended_euclidean(large, small):
    """
    Mathematical Extended Euclidean. Returns the coprime, I suggest
    you take the output and (mod large) it because it can be negative.
    """
    if small >= large or small <= 0:
        raise ValueError(f"extended euclidean recieved the wrong arguments. arglist:{(large, small)}")
    if gcd(large, small) != 1:
        raise ValueError(f"extended euclidean arguments are not coprime. arglist:{(large, small)} gcd:{gcd(large, small)}")
    # intro hack
    c = large
    d = small

    stack = list()
    while True:
        # formula: a = b * (c) + d where a and c are the carryover
        a = c
        c = d
        b = a // c
        d = a % c
        stack.append((a,b,c,d))
        if d == 1: # already raised a value error if gcd never hits 1
            break
    w = 0 # hack
    y = 1 # hack
    while len(stack) > 0:
        a,b,c,d = stack.pop()
        w,x,y,z = y, a, -b*y + w ,c
        print("abcd",a,b,c,d,'wxyz',w,x,y,z)
    return y

if __name__ == '__main__':
    print(15,4,gcd(15,4))
    print(512,240,gcd(512,240))
    print(91,17,gcd(91,17))
    n, d = 397,41
    ee = extended_euclidean(n, d)
    print("extended euclidean",ee, d, "with respect to", n,"congruence", (d*ee)%n)
