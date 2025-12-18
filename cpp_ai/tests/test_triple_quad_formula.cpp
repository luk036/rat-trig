/**
 * @file test_triple_quad_formula.cpp
 * @brief Tests for triple quad formula function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing triple_quad_formula function") {
    SUBCASE("Test with doubles") {
        double q1 = 5.0;
        double q2 = 25.0;
        double s3 = 4.0 / 125.0;
        CHECK(rat_trig::triple_quad_formula(q1, q2, s3) == doctest::Approx(416.0).epsilon(1e-10));
    }
    
    SUBCASE("Test with floats") {
        float q1 = 5.0f;
        float q2 = 25.0f;
        float s3 = 4.0f / 125.0f;
        CHECK(rat_trig::triple_quad_formula(q1, q2, s3) == doctest::Approx(416.0f).epsilon(1e-6f));
    }
    
    SUBCASE("Test with integers (s3 = 1)") {
        int q1 = 1;
        int q2 = 1;
        int s3 = 1;
        CHECK(rat_trig::triple_quad_formula(q1, q2, s3) == 4);
    }
    
    SUBCASE("Test with integers (s3 = 0)") {
        int q1 = 1;
        int q2 = 1;
        int s3 = 0;
        CHECK(rat_trig::triple_quad_formula(q1, q2, s3) == 0);
    }
}