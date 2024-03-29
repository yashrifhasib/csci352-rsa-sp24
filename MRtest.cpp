#include <iostream>
#include <gmpxx.h>

#include <cstdlib> 
#include <ctime>   

using namespace std;

#include "MRtest.h"

//g++ -o MRtest MRtest.cpp -I/opt/homebrew/Cellar/gmp/6.3.0/include/ -L/opt/homebrew/Cellar/gmp/6.3.0/lib/  -lgmp -lgmpxx


bool MB_failure(const mpz_class& a, const mpz_class& b, const mpz_class&k, const mpz_class& n){
    //return true with MB_test failed, number is not a prime

    //mpz_class bb = mpz_class(a).powm(b.get_ui(), n); //power modular function (allowed?)
    // Calculate result = (base^exponent) mod modulus using mpz_powm
    mpz_class bb;
    mpz_powm(bb.get_mpz_t(), a.get_mpz_t(), b.get_mpz_t(), n.get_mpz_t());


    if (bb == 1 || bb == n - 1) {
        return false; 
    }

    for (int i = 0; i < k; ++i) {
        mpz_class exponent = pow(2,i) *b;

        //bb = mpz_class(a).powm((exponent*b), n);
        mpz_powm(bb.get_mpz_t(), a.get_mpz_t(), exponent.get_mpz_t(), n.get_mpz_t());

        if (bb == n - 1) {
            return false;
        }
    }

    return true;
}


bool MR_Test(const mpz_class& num){
    mpz_class phiPow = num - 1;
    mpz_class TwoCount = 0; // Counts for the need to multiply the exponent by 2 later

    while (phiPow % 2 == 0) {
        phiPow >>= 1; // Divide by 2 (shift the binary bits right by 1)
        ++TwoCount;   // Count the times to sqaure in each MB test
    }
    int rounds = 20;

    srand(time(0)); // Seed the random number generator
    for (int a_ = 0; a_ < rounds; ++a_) {
        mpz_class round_test = mpz_class(rand()) % (num - 2) + 2; // Generate random a's
        //num.get_ui() can get the numerical value of the mpz_class num. (if necessary.)

        if (MB_failure(round_test, phiPow, TwoCount, num)) {
            return false;
        }
    }
    return true;

}
