/**
 * @file basic_usage.cpp
 * @brief Basic usage examples for rat-trig library
 */

#include <iostream>
#include <iomanip>
#include "rat_trig/trigonom.hpp"

int main() {
    std::cout << "=== Rational Trigonometry Examples ===\n\n";
    
    // Example 1: Archimedes' formula
    std::cout << "1. Archimedes' formula:\n";
    double quad1 = 0.5;
    double quad2 = 0.25;
    double quad3 = 1.0 / 6.0;
    double arch_result = rat_trig::archimedes(quad1, quad2, quad3);
    std::cout << "   archimedes(" << quad1 << ", " << quad2 << ", " << quad3 << ") = " 
              << std::setprecision(10) << arch_result << "\n";
    std::cout << "   (Expected: 23/144 ≈ 0.1597222222)\n\n";
    
    // Example 2: Vector operations
    std::cout << "2. Vector operations:\n";
    std::array<int, 2> vec1 = {1, 2};
    std::array<int, 2> vec2 = {3, 4};
    int cross_result = rat_trig::cross(vec1, vec2);
    int dot_result = rat_trig::dot(vec1, vec2);
    int quad_result = rat_trig::quad(vec1);
    std::cout << "   vec1 = [" << vec1[0] << ", " << vec1[1] << "], vec2 = [" 
              << vec2[0] << ", " << vec2[1] << "]\n";
    std::cout << "   cross(vec1, vec2) = " << cross_result << "\n";
    std::cout << "   dot(vec1, vec2) = " << dot_result << "\n";
    std::cout << "   quad(vec1) = " << quad_result << "\n\n";
    
    // Example 3: Spread calculation
    std::cout << "3. Spread calculation:\n";
    std::array<double, 2> vec3 = {1.0, 2.0};
    std::array<double, 2> vec4 = {3.0, 4.0};
    double spread_result = rat_trig::spread(vec3, vec4);
    std::cout << "   vec3 = [" << vec3[0] << ", " << vec3[1] << "], vec4 = [" 
              << vec4[0] << ", " << vec4[1] << "]\n";
    std::cout << "   spread(vec3, vec4) = " << std::setprecision(10) << spread_result << "\n";
    std::cout << "   (Expected: 4/125 = 0.032)\n\n";
    
    // Example 4: Spread law
    std::cout << "4. Spread law:\n";
    double quad1_sl = 5.0;
    double quad2_sl = 25.0;
    double quad3_sl = 20.0;
    double spread_law_result = rat_trig::spread_law(quad1_sl, quad2_sl, quad3_sl);
    std::cout << "   spread_law(" << quad1_sl << ", " << quad2_sl << ", " << quad3_sl << ") = " 
              << std::setprecision(10) << spread_law_result << "\n";
    std::cout << "   (Expected: 0.8)\n\n";
    
    // Example 5: Triple quad formula
    std::cout << "5. Triple quad formula:\n";
    double quad1_tq = 5.0;
    double quad2_tq = 25.0;
    double spread3_tq = 4.0 / 125.0;
    double triple_quad_result = rat_trig::triple_quad_formula(quad1_tq, quad2_tq, spread3_tq);
    std::cout << "   triple_quad_formula(" << quad1_tq << ", " << quad2_tq << ", " 
              << spread3_tq << ") = " << triple_quad_result << "\n";
    std::cout << "   (Expected: 416)\n\n";
    
    // Example 6: Working with different numeric types
    std::cout << "6. Working with different numeric types:\n";
    
    // Integers
    int quad1_int = 2;
    int quad2_int = 4;
    int quad3_int = 6;
    int arch_int = rat_trig::archimedes(quad1_int, quad2_int, quad3_int);
    std::cout << "   Integers: archimedes(" << quad1_int << ", " << quad2_int << ", " 
              << quad3_int << ") = " << arch_int << "\n";
    
    // Floats
    float quad1_float = 2.0f;
    float quad2_float = 4.0f;
    float quad3_float = 6.0f;
    float arch_float = rat_trig::archimedes(quad1_float, quad2_float, quad3_float);
    std::cout << "   Floats: archimedes(" << quad1_float << ", " << quad2_float << ", " 
              << quad3_float << ") = " << arch_float << "\n";
    
    // Example with mixed types (using doubles for fractions)
    double quad1_frac = 1.0;
    double quad2_frac = 0.5;
    double quad3_frac = 2.0;
    double arch_frac = rat_trig::archimedes(quad1_frac, quad2_frac, quad3_frac);
    std::cout << "   Fractions: archimedes(" << quad1_frac << ", " << quad2_frac << ", " 
              << quad3_frac << ") = " << std::setprecision(10) << arch_frac << "\n";
    std::cout << "   (Expected: 7/4 = 1.75)\n\n";
    
    // Example 7: Fibonacci
    std::cout << "7. Fibonacci example:\n";
    for (int idx = 1; idx <= 10; ++idx) {
        std::cout << "   fib(" << idx << ") = " << rat_trig::fib(idx) << "\n";
    }
    
    return 0;
}
