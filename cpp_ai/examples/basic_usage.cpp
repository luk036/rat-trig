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
    double q1 = 0.5;
    double q2 = 0.25;
    double q3 = 1.0 / 6.0;
    double arch_result = rat_trig::archimedes(q1, q2, q3);
    std::cout << "   archimedes(" << q1 << ", " << q2 << ", " << q3 << ") = " 
              << std::setprecision(10) << arch_result << "\n";
    std::cout << "   (Expected: 23/144 ≈ 0.1597222222)\n\n";
    
    // Example 2: Vector operations
    std::cout << "2. Vector operations:\n";
    std::array<int, 2> v1 = {1, 2};
    std::array<int, 2> v2 = {3, 4};
    int cross_result = rat_trig::cross(v1, v2);
    int dot_result = rat_trig::dot(v1, v2);
    int quad_result = rat_trig::quad(v1);
    std::cout << "   v1 = [" << v1[0] << ", " << v1[1] << "], v2 = [" 
              << v2[0] << ", " << v2[1] << "]\n";
    std::cout << "   cross(v1, v2) = " << cross_result << "\n";
    std::cout << "   dot(v1, v2) = " << dot_result << "\n";
    std::cout << "   quad(v1) = " << quad_result << "\n\n";
    
    // Example 3: Spread calculation
    std::cout << "3. Spread calculation:\n";
    std::array<double, 2> v3 = {1.0, 2.0};
    std::array<double, 2> v4 = {3.0, 4.0};
    double spread_result = rat_trig::spread(v3, v4);
    std::cout << "   v3 = [" << v3[0] << ", " << v3[1] << "], v4 = [" 
              << v4[0] << ", " << v4[1] << "]\n";
    std::cout << "   spread(v3, v4) = " << std::setprecision(10) << spread_result << "\n";
    std::cout << "   (Expected: 4/125 = 0.032)\n\n";
    
    // Example 4: Spread law
    std::cout << "4. Spread law:\n";
    double q1_sl = 5.0;
    double q2_sl = 25.0;
    double q3_sl = 20.0;
    double spread_law_result = rat_trig::spread_law(q1_sl, q2_sl, q3_sl);
    std::cout << "   spread_law(" << q1_sl << ", " << q2_sl << ", " << q3_sl << ") = " 
              << std::setprecision(10) << spread_law_result << "\n";
    std::cout << "   (Expected: 0.8)\n\n";
    
    // Example 5: Triple quad formula
    std::cout << "5. Triple quad formula:\n";
    double q1_tq = 5.0;
    double q2_tq = 25.0;
    double s3_tq = 4.0 / 125.0;
    double triple_quad_result = rat_trig::triple_quad_formula(q1_tq, q2_tq, s3_tq);
    std::cout << "   triple_quad_formula(" << q1_tq << ", " << q2_tq << ", " 
              << s3_tq << ") = " << triple_quad_result << "\n";
    std::cout << "   (Expected: 416)\n\n";
    
    // Example 6: Working with different numeric types
    std::cout << "6. Working with different numeric types:\n";
    
    // Integers
    int q1_int = 2;
    int q2_int = 4;
    int q3_int = 6;
    int arch_int = rat_trig::archimedes(q1_int, q2_int, q3_int);
    std::cout << "   Integers: archimedes(" << q1_int << ", " << q2_int << ", " 
              << q3_int << ") = " << arch_int << "\n";
    
    // Floats
    float q1_float = 2.0f;
    float q2_float = 4.0f;
    float q3_float = 6.0f;
    float arch_float = rat_trig::archimedes(q1_float, q2_float, q3_float);
    std::cout << "   Floats: archimedes(" << q1_float << ", " << q2_float << ", " 
              << q3_float << ") = " << arch_float << "\n";
    
    // Example with mixed types (using doubles for fractions)
    double q1_frac = 1.0;
    double q2_frac = 0.5;
    double q3_frac = 2.0;
    double arch_frac = rat_trig::archimedes(q1_frac, q2_frac, q3_frac);
    std::cout << "   Fractions: archimedes(" << q1_frac << ", " << q2_frac << ", " 
              << q3_frac << ") = " << std::setprecision(10) << arch_frac << "\n";
    std::cout << "   (Expected: 7/4 = 1.75)\n\n";
    
    // Example 7: Fibonacci
    std::cout << "7. Fibonacci example:\n";
    for (int i = 1; i <= 10; ++i) {
        std::cout << "   fib(" << i << ") = " << rat_trig::fib(i) << "\n";
    }
    
    return 0;
}
