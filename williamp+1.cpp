#include <iostream>
#include <gmpxx.h>
#include <ctime>
#include <iomanip>

#include <cstdlib> 
#include "MRtest.h"

using namespace std;

mpz_class coprimeGenerator(const mpz_class& n, int maxBit, gmp_randstate_t state){
    mpz_class randomBig;
    while(true){
        // Generate a random big integer with 1024 bits
        mpz_urandomb(randomBig.get_mpz_t(), state, maxBit);
        if(gcd(randomBig, n)==1){
            return randomBig;
        }
    }

}

mpz_class lucas(const& mpz_class A, const& mpz_class n, const& mpz_class M){
    int status = M%2;
    // V0 = 2, V1=A
    mpz_class mth;
    if(status == 0){
        mpz_powm(mth.get_mpz_t(), lucas(A, n, M/2).get_mpz_t(),2,n.get_mpz_t()) 
        mth = (mth+n-2)%n;
    }else if(status ==1){
        
    }
}
mpz_class gcd(const mpz_class& a_, const mpz_class& b_){

    mpz_class a = a_;
    mpz_class b = b_;
    while(true){
        if(a==b){
            return a;
        }
        if(a==0){
            return b;
        }
        if(b==0){
            return a;
        }
        if(a>b){  //directly compares mpz_class objects.
            a = a%b; 
        }else{
            b = b%a;
        }
    }


}




void pollard(const mpz_class& num){
    mpz_class n = num;
    mpz_class a("2"); // pick 2 to be the coprime number of the factor p
    mpz_class B("2"); // the value for B, the exponent of a

    while(true){

        if(n % 2 == 0){
            cout << 2 << ", ";
            n=n/2;
            continue;
        }

        if(MR_Test(n))
            break;

        mpz_powm(a.get_mpz_t(), a.get_mpz_t(), B.get_mpz_t(), n.get_mpz_t());
        mpz_class p(gcd(a-1,n));

        if(p!=1 && p!=n){
            cout << p << ", ";
            pollard(n/p);
            return;
        }
        B++;
    }

    cout << "Last factor: " << n << endl << "Factoring completed" << endl;


}



int main() {

    time_t start, end; 
    time(&start); 

    gmp_randstate_t state;
    gmp_randinit_default(state);
    // Set the seed for the random number generator
    gmp_randseed_ui(state, time(NULL));

    mpz_class n; // Declare a GMP arbitrary precision integer
    n="12312390218321842748324732847234";

    //get random number A to be the base.
    mpz_class A = coprimeGenerator(100000002, 100, state);



    time(&end); 

    double second = double(end - start); 
    cout <<  fixed << second << setprecision(6) << " sec. "; 
    return 0; 



}

//g++ -o p+1 williamp+1.cpp MRtest.cpp -I/opt/homebrew/Cellar/gmp/6.3.0/include/ -L/opt/homebrew/Cellar/gmp/6.3.0/lib/  -lgmp -lgmpxx