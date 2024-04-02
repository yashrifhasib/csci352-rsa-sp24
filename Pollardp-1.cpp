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

void pollard(const mpz_class& num, const mpz_class& A){
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
            pollard(n/p, A);
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
    gmp_randseed_ui(state, time(NULL));


    mpz_class n; // Declare a GMP arbitrary precision integer
    n = "9209839122440374002906008377605580208264841025166426304451583112053";
    //67 digits ~ 201 bits (let's generate coprime of n that's less or = 100 bits )
    mpz_class A = coprimeGenerator(n, 100, state);
    //A = 2;
    //need to reasonable fix some B: hoping for B-smooth case

    //where composite n is set to be the string literal

    cout << n << endl << "Pollard p-1 factoring started: factor = gcd(A^B!-1, n)" << endl;
    cout << "A = " << A << endl;
    pollard(n, A);

    time(&end); 

    double second = double(end - start); 
    cout <<  fixed << second << setprecision(6) << " sec. "; 
    return 0; 


    /*;
    cout << n << " " << (MR_Test(n) ? "Prime":"Composite") <<endl;
    mpz_class a("1000000000000000000000000000");
    mpz_class b("10000000005");
    cout << "gcd of " << a << " and " << b << " is " << gcd(a,b);*/

}

//g++ -o p-1 Pollardp-1.cpp MRtest.cpp -I/opt/homebrew/Cellar/gmp/6.3.0/include/ -L/opt/homebrew/Cellar/gmp/6.3.0/lib/  -lgmp -lgmpxx
