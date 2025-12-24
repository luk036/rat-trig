/**
 * @file test_spread_law.cpp
 * @brief Tests for spread law function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing spread_law function") {
    SUBCASE("Test with doubles") {
        double quad1 = 5.0;
        double quad2 = 25.0;
        double quad3 = 20.0;
        CHECK(rat_trig::spread_law(quad1, quad2, quad3) == doctest::Approx(0.8).epsilon(1e-10));
    }
    
    SUBCASE("Test with floats") {
        float quad1 = 5.0f;
        float quad2 = 25.0f;
        float quad3 = 20.0f;
        CHECK(rat_trig::spread_law(quad1, quad2, quad3) == doctest::Approx(0.8f).epsilon(1e-6f));
    }
    
    SUBCASE("Test with integers (should give integer division result)") {
        int quad1 = 1;
        int quad2 = 1;
        int quad3 = 4;
        CHECK(rat_trig::spread_law(quad1, quad2, quad3) == 0);
    }
    
    SUBCASE("Test with zero quadrance") {
        double quad1 = 1.0;
        double quad2 = 1.0;
        double quad3 = 0.0;
        CHECK(rat_trig::spread_law(quad1, quad2, quad3) == doctest::Approx(0.0).epsilon(1e-10));
    }
}