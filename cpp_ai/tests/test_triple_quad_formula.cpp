/**
 * @file test_triple_quad_formula.cpp
 * @brief Tests for triple quad formula function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing triple_quad_formula function") {
    SUBCASE("Test with doubles") {
        double quad1 = 5.0;
        double quad2 = 25.0;
        double spread3 = 4.0 / 125.0;
        CHECK(rat_trig::triple_quad_formula(quad1, quad2, spread3) == doctest::Approx(416.0).epsilon(1e-10));
    }
    
    SUBCASE("Test with floats") {
        float quad1 = 5.0f;
        float quad2 = 25.0f;
        float spread3 = 4.0f / 125.0f;
        CHECK(rat_trig::triple_quad_formula(quad1, quad2, spread3) == doctest::Approx(416.0f).epsilon(1e-6f));
    }
    
    SUBCASE("Test with integers (spread3 = 1)") {
        int quad1 = 1;
        int quad2 = 1;
        int spread3 = 1;
        CHECK(rat_trig::triple_quad_formula(quad1, quad2, spread3) == 4);
    }
    
    SUBCASE("Test with integers (spread3 = 0)") {
        int quad1 = 1;
        int quad2 = 1;
        int spread3 = 0;
        CHECK(rat_trig::triple_quad_formula(quad1, quad2, spread3) == 0);
    }
}