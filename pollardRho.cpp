#include "pollardRho.h"

void quadratic(mpz_class& input, const mpz_class& mod) {
    input = 3 * input * input + 2;
    input = input % mod;
}

mpz_class gcd(mpz_class op1, mpz_class op2) {
    mpz_class temp;
    if(op1 < op2) {
        temp = op1;
        op1 = op2;
        op2 = temp;
    }
    while(!(op2 == 0 || op2 == 1)){
        temp = op2;
        op2 = op1 % op2;
        op1 = temp;
    }
    if(op2 == 1){
        return op2;
    } else {
        return op1;
    }
}

mpz_class pollard(const mpz_class& input) {
    mpz_class x = 2;
    mpz_class y = x;
    mpz_class d = 1;
    while(d == 1) {
        quadratic(x, input);
        quadratic(y, input);
        quadratic(y, input);
        d = gcd(input, y - x);
    }
    return d;
}
