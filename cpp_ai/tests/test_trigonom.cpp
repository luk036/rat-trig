/**
 * @file test_trigonom.cpp
 * @brief Tests for rational trigonometry functions using doctest
 */

#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing archimedes function") {
    SUBCASE("Test with integers") {
        int quad1 = 2;
        int quad2 = 4;
        int quad3 = 6;
        CHECK(rat_trig::archimedes(quad1, quad2, quad3) == 32);
    }
    
    SUBCASE("Test with floats") {
        float quad1 = 2.0f;
        float quad2 = 4.0f;
        float quad3 = 6.0f;
        CHECK(rat_trig::archimedes(quad1, quad2, quad3) == doctest::Approx(32.0f));
    }
    
    SUBCASE("Test with doubles") {
        double quad1 = 2.0;
        double quad2 = 4.0;
        double quad3 = 6.0;
        CHECK(rat_trig::archimedes(quad1, quad2, quad3) == doctest::Approx(32.0));
    }
    
    SUBCASE("Test with zero quadrance") {
        int quad1 = 0;
        int quad2 = 4;
        int quad3 = 6;
        CHECK(rat_trig::archimedes(quad1, quad2, quad3) == -4);
    }
    
    SUBCASE("Test with degenerate triangle (collinear points)") {
        int quad1 = 1;
        int quad2 = 4;
        int quad3 = 9;
        CHECK(rat_trig::archimedes(quad1, quad2, quad3) == 0);
    }
    
    SUBCASE("Test with negative inputs") {
        int quad1 = -1;
        int quad2 = 2;
        int quad3 = 3;
        CHECK(rat_trig::archimedes(quad1, quad2, quad3) == -12);
    }
    
    SUBCASE("Test with fractions (using doubles)") {
        double quad1 = 1.0 / 2.0;
        double quad2 = 1.0 / 4.0;
        double quad3 = 1.0 / 6.0;
        double expected = 23.0 / 144.0;
        CHECK(rat_trig::archimedes(quad1, quad2, quad3) == doctest::Approx(expected).epsilon(1e-10));
    }
}