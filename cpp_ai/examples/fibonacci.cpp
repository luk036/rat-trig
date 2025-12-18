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
 * @return The n value for Fibonacci calculation, or 0 if error
 */
unsigned long long parse_args(int argc, char* argv[], bool& verbose, bool& very_verbose) {
    verbose = false;
    very_verbose = false;
    unsigned long long n = 0;
    
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <n> [-v] [-V]\n";
        std::cerr << "  n: n-th Fibonacci number\n";
        std::cerr << "  -v: verbose output\n";
        std::cerr << "  -V: very verbose output\n";
        return 0;
    }
    
    // Parse all arguments
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        
        if (arg == "-v") {
            verbose = true;
        } else if (arg == "-V") {
            very_verbose = true;
        } else if (arg[0] != '-') {
            // This should be the n value
            if (n != 0) {
                std::cerr << "Error: Multiple n values specified\n";
                return 0;
            }
            
            char* endptr;
            n = std::strtoull(arg.c_str(), &endptr, 10);
            if (*endptr != '\0' || n == 0) {
                std::cerr << "Error: n must be a positive integer\n";
                return 0;
            }
        } else {
            std::cerr << "Warning: Unknown argument '" << arg << "' ignored\n";
        }
    }
    
    if (n == 0) {
        std::cerr << "Error: n must be specified\n";
        return 0;
    }
    
    return n;
}

/**
 * @brief Main function
 */
int main(int argc, char* argv[]) {
    bool verbose = false;
    bool very_verbose = false;
    
    unsigned long long n = parse_args(argc, argv, verbose, very_verbose);
    if (n == 0) {
        return 1;
    }
    
    if (very_verbose) {
        std::cout << "[DEBUG] Starting crazy calculations...\n";
    }
    
    unsigned long long result = rat_trig::fib(n);
    std::cout << "The " << n << "-th Fibonacci number is " << result << "\n";
    
    if (verbose || very_verbose) {
        std::cout << "[INFO] Script ends here\n";
    }
    
    return 0;
}
