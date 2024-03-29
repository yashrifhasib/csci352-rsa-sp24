#include <iostream>
#include <gmpxx.h>
#include <ctime>
#include <iomanip>


#include <cstdlib> 


#include "MRtest.h"

using namespace std;

mpz_class gcd(const mpz_class& a, const mpz_class& b){

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
        return gcd(a%b, b);
    }
    return gcd(a, b%a);


}

void pollard(const mpz_class& num){
    mpz_class n = num;
    mpz_class a("2"); // pick 2 to be the coprime number of the factor p
    mpz_class B("2"); // the value for B, the exponent of a
    cout << n << endl << "Pollard p-1 factoring started: factor = gcd(2^B!-1, n)" << endl;

    while(n != 1){
        mpz_powm(a.get_mpz_t(), a.get_mpz_t(), B.get_mpz_t(), n.get_mpz_t());
        mpz_class p(gcd(a-1,n));
        if(p!=1 && p!=n){
            cout << "n divisible by " << p << endl;
            n = n/p;
            if(MR_Test(n)){
                break;
            }
        }
        B++;
    }

    cout << "Last factor: " << n << endl << "Factoring completed" << endl;


}



int main() {
    time_t start, end; 
    time(&start); 

    mpz_class n; // Declare a GMP arbitrary precision integer
    //n = "9209839122440374002906008377605580208264841025166426304451583112053";
    //where composite n is set to be the string literal
    n = "18446744073709551617";

    pollard(n);

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