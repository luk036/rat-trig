#ifndef RAT_TRIG_TRIGONOM_HPP
#define RAT_TRIG_TRIGONOM_HPP

/**
 * @file trigonom.hpp
 * @brief Rational Trigonometry - A C++20 implementation of Norman Wildberger's rational trigonometry
 *
 * Rational Trigonometry is a new approach to classical trigonometry, developed by Norman
 * Wildberger, that aims to simplify and clarify the subject by using only rational numbers
 * and operations, rather than irrational numbers and limits.
 *
 * In traditional trigonometry, concepts such as the sine, cosine, and tangent of an angle
 * are typically defined using circles and the unit circle in particular. These definitions
 * involve irrational numbers and limits, which can make the subject more difficult to
 * understand and work with.
 *
 * In rational trigonometry, Wildberger replaces these circular definitions with ones based
 * on lines and line segments, which allows for a more straightforward and intuitive approach.
 * The fundamental concepts in rational trigonometry are the "quadaverage" and the "dilated
 * directed angle," which are defined in terms of lines and line segments, rather than circles.
 *
 * Rational trigonometry has been gaining popularity in recent years, as it provides a useful
 * alternative to traditional trigonometry for certain applications, such as computer graphics,
 * robotics, and physics. It can also be a helpful tool for students who struggle with the
 * irrational numbers and limits used in traditional trigonometry.
 *
 * In summary, Rational Trigonometry is a new approach to classical trigonometry that uses
 * rational numbers and operations, rather than irrational numbers and limits, making it a more
 * straightforward and intuitive subject to understand and work with.
 *
 * @verbatim
 *           A
 *           |
 *           |
 *        q1 |  \\ q3
 *           |
 *           |
 *           B-----C
 *             q2
 *
 *      where q1, q2, q3 are quadrances (squared distances)
 * @endverbatim
 */

#include <concepts>
#include <array>
#include <type_traits>
#include <cmath>

namespace rat_trig {

/**
 * @brief Concept for numeric types that can be used in rational trigonometry calculations.
 *
 * Supports integers, floating-point numbers, and any type that supports basic arithmetic operations.
 */
template<typename NumType>
concept Numeric = std::regular<NumType> && requires(NumType value_a, NumType value_b) {
    { value_a + value_b } -> std::convertible_to<NumType>;
    { value_a - value_b } -> std::convertible_to<NumType>;
    { value_a * value_b } -> std::convertible_to<NumType>;
    { value_a / value_b } -> std::convertible_to<NumType>;
    { NumType{0} } -> std::convertible_to<NumType>;
    { NumType{1} } -> std::convertible_to<NumType>;
    { NumType{4} } -> std::convertible_to<NumType>;
};

/**
 * @brief A 2D vector with numeric components
 */
template<Numeric NumType>
using Vector2 = std::array<NumType, 2>;

/**
 * @brief The function `archimedes` calculates the qudrea of a triangle using Archimedes' formula with
 * the lengths of the three sides `q_1`, `q_2`, and `q_3`. It can also be used to check if a quadraple
 * with length Q1, Q2, Q3, Q4 is on a circle.
 *
 * @param q_1 First quadrance of the triangle
 * @param q_2 Second quadrance of the triangle
 * @param q_3 Third quadrance of the triangle
 *
 * @return The result of the expression \(4 \times q_1 \times q_2 - \text{temp}^2\), where
 * \(\text{temp} = q_1 + q_2 - q_3\).
 *
 * @example
 * @code
 * auto q1 = 0.5;
 * auto q2 = 0.25;
 * auto q3 = 1.0 / 6.0;
 * auto result = archimedes(q1, q2, q3); // Should be 23/144 ≈ 0.159722
 * @endcode
 *
 * @verbatim
 *           A
 *           |\\
 *           | \\
 *        q1 |  \\\ q3
 *           |   \\
 *           |    \\
 *           B-----C
 *             q2
 * @endverbatim
 */
template<Numeric NumType>
constexpr NumType archimedes(NumType q_1, NumType q_2, NumType q_3) {
    NumType temp = q_1 + q_2 - q_3;
    return NumType{4} * q_1 * q_2 - temp * temp;
}

/**
 * @brief The `cross` function calculates the cross product of two vectors `v_1` and `v_2`.
 *
 * @param v_1 A 2D vector with numeric components
 * @param v_2 A 2D vector with numeric components
 *
 * @return The cross product of the two vectors.
 *
 * @example
 * @code
 * std::array v1 = {1, 2};
 * std::array v2 = {3, 4};
 * auto result = cross(v1, v2); // Should be -2
 * @endcode
 *
 * @verbatim
 *            v2
 *            ^
 *            |
 *            |    /
 *            |   /
 *            |  /
 *            | / v1
 *            |/____>
 *           O
 * @endverbatim
 */
template<Numeric NumType>
constexpr NumType cross(const Vector2<NumType>& v_1, const Vector2<NumType>& v_2) {
    return v_1[0] * v_2[1] - v_1[1] * v_2[0];
}

/**
 * @brief The `dot` function calculates the dot product of two vectors `v_1` and `v_2`.
 *
 * @param v_1 A 2D vector with numeric components
 * @param v_2 A 2D vector with numeric components
 *
 * @return The dot product of the two vectors.
 *
 * @example
 * @code
 * std::array v1 = {1, 2};
 * std::array v2 = {3, 4};
 * auto result = dot(v1, v2); // Should be 11
 * @endcode
 *
 * @verbatim
 *            v2
 *            ^
 *            |\\
 *            | \\
 *            |  \\
 *            |   \\
 *            |    \\ v1
 *            |     \\
 *            |      \\
 *            |_______\\
 *           O         projection
 * @endverbatim
 */
template<Numeric NumType>
constexpr NumType dot(const Vector2<NumType>& v_1, const Vector2<NumType>& v_2) {
    return v_1[0] * v_2[0] + v_1[1] * v_2[1];
}

/**
 * @brief The `quad` function calculates the quadrance of a vector `vector`.
 *
 * @param vector A 2D vector with numeric components
 *
 * @return The quadrance of the vector.
 *
 * @example
 * @code
 * std::array vector = {3, 4};
 * auto result = quad(vector); // Should be 25
 * @endcode
 *
 * @verbatim
 *           vector[1] ^
 *                     |
 *                     |\\
 *                     | \\
 *                     |  \\\  quad(vector) = vector[0]^2 + vector[1]^2
 *                     |   \\
 *                     |    \\
 *                     |     \\
 *                     |      \\
 *                     |_______\\\
 *                   O         vector[0]
 * @endverbatim
 */
template<Numeric NumType>
constexpr NumType quad(const Vector2<NumType>& vector) {
    return vector[0] * vector[0] + vector[1] * vector[1];
}

/**
 * @brief The `spread` function calculates the spread between two vectors `v_1` and `v_2`.
 * The spread is the square of the cross product divided by the product of the quadrances.
 * It represents the square of the sine of the angle between the vectors.
 *
 * @param v_1 A 2D vector with numeric components
 * @param v_2 A 2D vector with numeric components
 *
 * @return The spread between the two vectors.
 *
 * @example
 * @code
 * std::array v1 = {1.0, 2.0};
 * std::array v2 = {3.0, 4.0};
 * auto result = spread(v1, v2); // Should be 4/125 = 0.032
 * @endcode
 */
template<Numeric NumType>
constexpr NumType spread(const Vector2<NumType>& v_1, const Vector2<NumType>& v_2) {
    NumType cross_product = cross(v_1, v_2);
    NumType quad_1 = quad(v_1);
    NumType quad_2 = quad(v_2);
    return (cross_product * cross_product) / (quad_1 * quad_2);
}

/**
 * @brief The `spread_law` function calculates the spread of a triangle using the law of spreads.
 * In rational trigonometry, the spread law states that for a triangle with quadrances
 * Q1, Q2, Q3, the spread S3 opposite to Q3 can be calculated by:
 * S3 = 4*Q1*Q2 - (Q1 + Q_2 - Q3)^2 / (4*Q1*Q2)
 *
 * @param q_1 First quadrance of the triangle
 * @param q_2 Second quadrance of the triangle
 * @param q_3 Third quadrance of the triangle (opposite to the angle whose spread we're finding)
 *
 * @return The spread S3 opposite to the quadrance q_3
 *
 * @example
 * @code
 * auto q1 = 5.0;
 * auto q2 = 25.0;
 * auto q3 = 20.0;
 * auto result = spread_law(q1, q2, q3); // Should be 0.8
 * @endcode
 */
template<Numeric NumType>
constexpr NumType spread_law(NumType q_1, NumType q_2, NumType q_3) {
    NumType numerator = archimedes(q_1, q_2, q_3); // 4*q_1*q_2 - (q_1 + q_2 - q_3)^2
    NumType denominator = NumType{4} * q_1 * q_2;
    return numerator / denominator;
}

/**
 * @brief The `triple_quad_formula` function calculates a value based on two quadrances and a spread.
 * In rational trigonometry, this formula is related to the relationship between three quadrances
 * and the spread between them.
 *
 * @param q_1 First quadrance
 * @param q_2 Second quadrance
 * @param s_3 Spread value
 *
 * @return A calculated value using the triple quad formula
 *
 * @example
 * @code
 * auto q1 = 5.0;
 * auto q2 = 25.0;
 * auto s3 = 4.0 / 125.0;
 * auto result = triple_quad_formula(q1, q2, s3); // Should be 416
 * @endcode
 */
template<Numeric NumType>
constexpr NumType triple_quad_formula(NumType q_1, NumType q_2, NumType s_3) {
    // Formula: (q_1 + q_2)^2 - 4*q_1*q_2*(1-s_3)
    NumType sum = q_1 + q_2;
    return sum * sum - NumType{4} * q_1 * q_2 * (NumType{1} - s_3);
}

/**
 * @brief Fibonacci example function
 *
 * @param number integer (must be > 0)
 *
 * @return n-th Fibonacci number
 *
 * @example
 * @code
 * auto result = fib(1); // 1
 * auto result = fib(2); // 1
 * auto result = fib(3); // 2
 * auto result = fib(4); // 3
 * auto result = fib(5); // 5
 * auto result = fib(6); // 8
 * @endcode
 *
 * @verbatim
 * F(1)=1  F(2)=1  F(3)=2  F(4)=3  F(5)=5  F(6)=8  ...
 *   *     *     **    ***   ***** ******** ...
 * @endverbatim
 */
constexpr unsigned long long fib(unsigned long long number) {
    if (number == 0) return 0;
    if (number == 1) return 1;

    unsigned long long first = 1;
    unsigned long long second = 1;
    for (unsigned long long idx = 2; idx < number; ++idx) {
        unsigned long long temp_sum = first + second;
        first = second;
        second = temp_sum;
    }
    return second;
}

} // namespace rat_trig

#endif // RAT_TRIG_TRIGONOM_HPP
