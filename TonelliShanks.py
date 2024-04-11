def is_quadratic_residue(n, p):
    if n % p == 0:
        return True
    return pow(n , (p - 1)//2, p) == 1

def tonelli_shanks(n, p):
    if not is_quadratic_residue(n, p):
        print(f'n:{n} is not a quadratic residue modulo p:{p}')
        return None
    
    if p % 4 == 3:
        R = pow(n, (p + 1)//4, p)
        return R, (p - R)
    
    # find Q and S sucha that `p - 1 = Q*(2^S)` with Q odd
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        S += 1 
        Q //= 2
        
    # search for a `z` which is a quadratic non-residue
    z = 2
    while is_quadratic_residue(z,p):
        z += 1
    
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q+1) // 2, p)
    
    while t != 1:
        # find the least i, 0 < i < M, such that t^(2^i) = 1 (mod p)
        i = 0
        temp = t
        if (t == 0): 
            return 0
        while temp != 1:
            i += 1
            temp = pow(t, 2 ** i, p)
            if (t == 0): 
                return 0
        
        b = pow(c, (2 ** (M - i - 1)) , p)
        M = i
        c = (b ** 2) % p
        t = (t * b * b) % p
        R = (R * b) % p
        
    return R, (p - R)

if __name__ == '__main__':
    n = 5 
    p = 41
    print(f'Tonelli Shanks outputs: {tonelli_shanks(n, p)}')