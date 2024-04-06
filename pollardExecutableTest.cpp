#include <iostream>
#include <gmpxx.h>
#include <string>
#include "pollardRho.h"

int main(int argc, char *argv[]) {
    mpz_class test; // F6
    if (argc > 1) {
        test = argv[1];
    } else {
        test = "18446744073709551617";
    }
    pollard(test);
    //std::cout << "factor is: " << pollard(test) << std::endl;
    return 0;
}
