/**
 * @file test_trigonom.cpp
 * @brief Tests for rational trigonometry functions using doctest
 */

#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing archimedes function") {
    SUBCASE("Test with integers") {
        int q1 = 2;
        int q2 = 4;
        int q3 = 6;
        CHECK(rat_trig::archimedes(q1, q2, q3) == 32);
    }
    
    SUBCASE("Test with floats") {
        float q1 = 2.0f;
        float q2 = 4.0f;
        float q3 = 6.0f;
        CHECK(rat_trig::archimedes(q1, q2, q3) == doctest::Approx(32.0f));
    }
    
    SUBCASE("Test with doubles") {
        double q1 = 2.0;
        double q2 = 4.0;
        double q3 = 6.0;
        CHECK(rat_trig::archimedes(q1, q2, q3) == doctest::Approx(32.0));
    }
    
    SUBCASE("Test with zero quadrance") {
        int q1 = 0;
        int q2 = 4;
        int q3 = 6;
        CHECK(rat_trig::archimedes(q1, q2, q3) == -4);
    }
    
    SUBCASE("Test with degenerate triangle (collinear points)") {
        int q1 = 1;
        int q2 = 4;
        int q3 = 9;
        CHECK(rat_trig::archimedes(q1, q2, q3) == 0);
    }
    
    SUBCASE("Test with negative inputs") {
        int q1 = -1;
        int q2 = 2;
        int q3 = 3;
        CHECK(rat_trig::archimedes(q1, q2, q3) == -12);
    }
    
    SUBCASE("Test with fractions (using doubles)") {
        double q1 = 1.0 / 2.0;
        double q2 = 1.0 / 4.0;
        double q3 = 1.0 / 6.0;
        double expected = 23.0 / 144.0;
        CHECK(rat_trig::archimedes(q1, q2, q3) == doctest::Approx(expected).epsilon(1e-10));
    }
}