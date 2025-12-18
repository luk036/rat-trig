/**
 * @file test_quad.cpp
 * @brief Tests for quadrance function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing quad function") {
    SUBCASE("Test with integer vector") {
        std::array<int, 2> v = {3, 4};
        CHECK(rat_trig::quad(v) == 25);
    }
    
    SUBCASE("Test with float vector") {
        std::array<float, 2> v = {3.0f, 4.0f};
        CHECK(rat_trig::quad(v) == doctest::Approx(25.0f));
    }
    
    SUBCASE("Test with double vector") {
        std::array<double, 2> v = {3.0, 4.0};
        CHECK(rat_trig::quad(v) == doctest::Approx(25.0));
    }
    
    SUBCASE("Test with another integer vector") {
        std::array<int, 2> v = {1, 1};
        CHECK(rat_trig::quad(v) == 2);
    }
    
    SUBCASE("Test with zero vector") {
        std::array<int, 2> v = {0, 0};
        CHECK(rat_trig::quad(v) == 0);
    }
    
    SUBCASE("Test with fractions (using doubles)") {
        std::array<double, 2> v = {3.0 / 5.0, 4.0 / 5.0};
        CHECK(rat_trig::quad(v) == doctest::Approx(1.0).epsilon(1e-10));
    }
}