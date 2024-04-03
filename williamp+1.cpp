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

mpz_class lucas(const mpz_class& A, const mpz_class& n, const mpz_class& M){
    mpz_class status = M%2;
    // V0 = 2, V1=A
    mpz_class mth;
    if(status == 0){
        mpz_class base = lucas(A, n, M / 2);
        mpz_class exp = 2;
        mpz_powm(mth.get_mpz_t(), base.get_mpz_t(), exp.get_mpz_t(), n.get_mpz_t());
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


            
bool properFactor(const mpz_class& factor, const mpz_class& Msmooth, const mpz_class& MCount){
    mpz_class n = factor + 1;
    mpz_class r;
    mpz_class d;

    while(true){
        d = gcd(n, Msmooth);
        if(d>1){
            r = n/gcd(n, Msmooth);
            if(r==1){
                return true;
            }
            n = r;
        }else{
            return false;
        }
    }
}

void williams(const mpz_class& N, const mpz_class& A){
    mpz_class V0 = 2;
    mpz_class V1 = A;
    mpz_class Vm = V1; 
    mpz_class M = 1;
    mpz_class MCount =1;
    cout << "A: " << V1 << endl;


    while(N!=1 || !MR_Test(N)){
        MCount = M+1;
        M = M*(MCount);
        Vm = lucas(A, N, M);
        mpz_class d = gcd(Vm,N);

        if(d!=1 && properFactor(d, M, MCount)){
            cout << "factor:" << d << endl;
            williams(N/d, A);
            break;
        }
    }
    cout << "factor:" << N << endl;

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
    mpz_class A = coprimeGenerator(n, 100, state);
    williams(n, A);



    time(&end); 

    double second = double(end - start); 
    cout <<  fixed << second << setprecision(6) << " sec. "; 
    return 0; 



}

//g++ -o p+1 williamp+1.cpp MRtest.cpp -I/opt/homebrew/Cellar/gmp/6.3.0/include/ -L/opt/homebrew/Cellar/gmp/6.3.0/lib/  -lgmp -lgmpxx
