/**
 * @file test_quad.cpp
 * @brief Tests for quadrance function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing quad function") {
    SUBCASE("Test with integer vector") {
        std::array<int, 2> vector = {3, 4};
        CHECK(rat_trig::quad(vector) == 25);
    }

    SUBCASE("Test with float vector") {
        std::array<float, 2> vector = {3.0f, 4.0f};
        CHECK(rat_trig::quad(vector) == doctest::Approx(25.0f));
    }

    SUBCASE("Test with double vector") {
        std::array<double, 2> vector = {3.0, 4.0};
        CHECK(rat_trig::quad(vector) == doctest::Approx(25.0));
    }

    SUBCASE("Test with another integer vector") {
        std::array<int, 2> vector = {1, 1};
        CHECK(rat_trig::quad(vector) == 2);
    }

    SUBCASE("Test with zero vector") {
        std::array<int, 2> vector = {0, 0};
        CHECK(rat_trig::quad(vector) == 0);
    }

    SUBCASE("Test with fractions (using doubles)") {
        std::array<double, 2> vector = {3.0 / 5.0, 4.0 / 5.0};
        CHECK(rat_trig::quad(vector) == doctest::Approx(1.0).epsilon(1e-10));
    }
}
