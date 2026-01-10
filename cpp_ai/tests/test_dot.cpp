/**
 * @file test_dot.cpp
 * @brief Tests for dot product function using doctest
 */

#include "doctest.h"
#include "rat_trig/trigonom.hpp"

TEST_CASE("Testing dot function") {
    SUBCASE("Test with integer vectors") {
        std::array<int, 2> vec1 = {1, 2};
        std::array<int, 2> vec2 = {3, 4};
        CHECK(rat_trig::dot(vec1, vec2) == 11);
    }

    SUBCASE("Test with float vectors") {
        std::array<float, 2> vec1 = {1.0f, 2.0f};
        std::array<float, 2> vec2 = {3.0f, 4.0f};
        CHECK(rat_trig::dot(vec1, vec2) == doctest::Approx(11.0f));
    }

    SUBCASE("Test with double vectors") {
        std::array<double, 2> vec1 = {1.0, 2.0};
        std::array<double, 2> vec2 = {3.0, 4.0};
        CHECK(rat_trig::dot(vec1, vec2) == doctest::Approx(11.0));
    }

    SUBCASE("Test with integer vectors (negative dot product)") {
        std::array<int, 2> vec1 = {1, 2};
        std::array<int, 2> vec2 = {-1, -2};
        CHECK(rat_trig::dot(vec1, vec2) == -5);
    }

    SUBCASE("Test with integer vectors (orthogonal)") {
        std::array<int, 2> vec1 = {1, 0};
        std::array<int, 2> vec2 = {0, 1};
        CHECK(rat_trig::dot(vec1, vec2) == 0);
    }

    SUBCASE("Test with fractions (using doubles)") {
        std::array<double, 2> vec1 = {1.0 / 2.0, 1.0 / 4.0};
        std::array<double, 2> vec2 = {1.0 / 6.0, 1.0 / 8.0};
        double expected = 11.0 / 96.0;
        CHECK(rat_trig::dot(vec1, vec2) == doctest::Approx(expected).epsilon(1e-10));
    }
}
