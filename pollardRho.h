#pragma once

#include <gmpxx.h>

/**
 * @brief pollard rho that returns a single factor of input.
 * 
 * @param input this number must be composite, undefined when prime.
 * @return mpz_class some factor of input
 */
mpz_class pollard(const mpz_class& input);
