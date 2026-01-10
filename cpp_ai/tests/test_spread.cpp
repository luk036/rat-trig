/**
 * @file test_spread.cpp
 * @brief Tests for spread function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing spread function") {
    SUBCASE("Test with integer vectors") {
        std::array<int, 2> vec1 = {1, 2};
        std::array<int, 2> vec2 = {3, 4};
        double expected = 4.0 / 125.0;
        CHECK(rat_trig::spread(vec1, vec2) == doctest::Approx(expected).epsilon(1e-10));
    }

    SUBCASE("Test with float vectors") {
        std::array<float, 2> vec1 = {1.0f, 2.0f};
        std::array<float, 2> vec2 = {3.0f, 4.0f};
        float expected = 4.0f / 125.0f;
        CHECK(rat_trig::spread(vec1, vec2) == doctest::Approx(expected).epsilon(1e-6f));
    }

    SUBCASE("Test with double vectors") {
        std::array<double, 2> vec1 = {1.0, 2.0};
        std::array<double, 2> vec2 = {3.0, 4.0};
        double expected = 4.0 / 125.0;
        CHECK(rat_trig::spread(vec1, vec2) == doctest::Approx(expected).epsilon(1e-10));
    }

    SUBCASE("Test with integer vectors (parallel)") {
        std::array<int, 2> vec1 = {1, 2};
        std::array<int, 2> vec2 = {1, 2};
        CHECK(rat_trig::spread(vec1, vec2) == 0);
    }

    SUBCASE("Test with integer vectors (perpendicular)") {
        std::array<int, 2> vec1 = {1, 0};
        std::array<int, 2> vec2 = {0, 1};
        CHECK(rat_trig::spread(vec1, vec2) == 1);
    }

    SUBCASE("Test with fractions (using doubles)") {
        std::array<double, 2> vec1 = {1.0 / 2.0, 1.0 / 4.0};
        std::array<double, 2> vec2 = {1.0 / 6.0, 1.0 / 8.0};
        double expected = 4.0 / 125.0;
        CHECK(rat_trig::spread(vec1, vec2) == doctest::Approx(expected).epsilon(1e-10));
    }
}
