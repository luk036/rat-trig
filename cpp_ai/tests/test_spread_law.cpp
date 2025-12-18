/**
 * @file test_spread_law.cpp
 * @brief Tests for spread law function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing spread_law function") {
    SUBCASE("Test with doubles") {
        double q1 = 5.0;
        double q2 = 25.0;
        double q3 = 20.0;
        CHECK(rat_trig::spread_law(q1, q2, q3) == doctest::Approx(0.8).epsilon(1e-10));
    }
    
    SUBCASE("Test with floats") {
        float q1 = 5.0f;
        float q2 = 25.0f;
        float q3 = 20.0f;
        CHECK(rat_trig::spread_law(q1, q2, q3) == doctest::Approx(0.8f).epsilon(1e-6f));
    }
    
    SUBCASE("Test with integers (should give integer division result)") {
        int q1 = 1;
        int q2 = 1;
        int q3 = 4;
        CHECK(rat_trig::spread_law(q1, q2, q3) == 0);
    }
    
    SUBCASE("Test with zero quadrance") {
        double q1 = 1.0;
        double q2 = 1.0;
        double q3 = 0.0;
        CHECK(rat_trig::spread_law(q1, q2, q3) == doctest::Approx(0.0).epsilon(1e-10));
    }
}