/**
 * @file fibonacci.cpp
 * @brief Fibonacci CLI example for rat-trig library
 *
 * This is a skeleton file that can serve as a starting point for a C++
 * console script. To run this script, use:
 * `./fibonacci <n>`
 *
 * Besides console scripts, this file can also be used as template for C++ modules.
 *
 * Note:
 *     This file can be renamed depending on your needs or safely removed if not needed.
 */

#include <iostream>
#include <string>
#include <cstdlib>
#include "rat_trig/trigonom.hpp"

/**
 * @brief Parse command line arguments
 *
 * @param argc Argument count
 * @param argv Argument values
 * @param verbose Reference to store verbose flag
 * @param very_verbose Reference to store very verbose flag
 *
 * @return The number value for Fibonacci calculation, or 0 if error
 */
unsigned long long parse_args(int argc, char* argv[], bool& verbose, bool& very_verbose) {
    verbose = false;
    very_verbose = false;
    unsigned long long number = 0;

    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <number> [-v] [-V]\n";
        std::cerr << "  number: n-th Fibonacci number\n";
        std::cerr << "  -v: verbose output\n";
        std::cerr << "  -V: very verbose output\n";
        return 0;
    }

    // Parse all arguments
    for (int idx = 1; idx < argc; ++idx) {
        std::string arg = argv[idx];

        if (arg == "-v") {
            verbose = true;
        } else if (arg == "-V") {
            very_verbose = true;
        } else if (arg[0] != '-') {
            // This should be the number value
            if (number != 0) {
                std::cerr << "Error: Multiple number values specified\n";
                return 0;
            }

            char* endptr;
            number = std::strtoull(arg.c_str(), &endptr, 10);
            if (*endptr != '\0' || number == 0) {
                std::cerr << "Error: number must be a positive integer\n";
                return 0;
            }
        } else {
            std::cerr << "Warning: Unknown argument '" << arg << "' ignored\n";
        }
    }

    if (number == 0) {
        std::cerr << "Error: number must be specified\n";
        return 0;
    }

    return number;
}

/**
 * @brief Main function
 */
int main(int argc, char* argv[]) {
    bool verbose = false;
    bool very_verbose = false;

    unsigned long long number = parse_args(argc, argv, verbose, very_verbose);
    if (number == 0) {
        return 1;
    }

    if (very_verbose) {
        std::cout << "[DEBUG] Starting crazy calculations...\n";
    }

    unsigned long long result = rat_trig::fib(number);
    std::cout << "The " << number << "-th Fibonacci number is " << result << "\n";

    if (verbose || very_verbose) {
        std::cout << "[INFO] Script ends here\n";
    }

    return 0;
}
