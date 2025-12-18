//! Rational Trigonometry is a new approach to classical trigonometry, developed by Norman
//! Wildberger, that aims to simplify and clarify the subject by using only rational numbers
//! and operations, rather than irrational numbers and limits.
//!
//! In traditional trigonometry, concepts such as the sine, cosine, and tangent of an angle
//! are typically defined using circles and the unit circle in particular. These definitions
//! involve irrational numbers and limits, which can make the subject more difficult to
//! understand and work with.
//!
//! In rational trigonometry, Wildberger replaces these circular definitions with ones based
//! on lines and line segments, which allows for a more straightforward and intuitive approach.
//! The fundamental concepts in rational trigonometry are the "quadaverage" and the "dilated
//! directed angle," which are defined in terms of lines and line segments, rather than circles.
//!
//! Rational trigonometry has been gaining popularity in recent years, as it provides a useful
//! alternative to traditional trigonometry for certain applications, such as computer graphics,
//! robotics, and physics. It can also be a helpful tool for students who struggle with the
//! irrational numbers and limits used in traditional trigonometry.
//!
//! In summary, Rational Trigonometry is a new approach to classical trigonometry that uses
//! rational numbers and operations, rather than irrational numbers and limits, making it a more
//! straightforward and intuitive subject to understand and work with.
//!
//! ```text
//!           A
//!           |
//!           |
//!        q1 |  \\ q3
//!           |
//!           |
//!           B-----C
//!             q2
//!
//!      where q1, q2, q3 are quadrances (squared distances)
//! ```

use num_traits::Num;
use std::ops::{Add, Mul, Sub};

/// A numeric type that can be used in rational trigonometry calculations.
/// Supports integers, rational numbers (fractions), and floating-point numbers.
pub trait Numeric:
    Num + Copy + PartialOrd + Add<Output = Self> + Sub<Output = Self> + Mul<Output = Self> + From<i32>
{
}
impl<T> Numeric for T where
    T: Num
        + Copy
        + PartialOrd
        + Add<Output = Self>
        + Sub<Output = Self>
        + Mul<Output = Self>
        + From<i32>
{
}

/// A 2D vector with numeric components
pub type Vector2<T> = [T; 2];

/// The function `archimedes` calculates the qudrea of a triangle using Archimedes' formula with
/// the lengths of the three sides `q_1`, `q_2`, and `q_3`. It can also be used to check if a quadraple
/// with length Q1, Q2, Q3, Q4 is on a circle.
///
/// # Arguments
///
/// * `q_1` - First quadrance of the triangle
/// * `q_2` - Second quadrance of the triangle  
/// * `q_3` - Third quadrance of the triangle
///
/// # Returns
///
/// The result of the expression \(4 \times q_1 \times q_2 - \text{temp}^2\), where
/// \(\text{temp} = q_1 + q_2 - q_3\).
///
/// # Examples
///
/// ```
/// use rat_trig::archimedes;
/// use num_rational::Ratio;
///
/// let q_1 = Ratio::new(1, 2);
/// let q_2 = Ratio::new(1, 4);
/// let q_3 = Ratio::new(1, 6);
/// assert_eq!(archimedes(q_1, q_2, q_3), Ratio::new(23, 144));
/// ```
///
/// ```text
///           A
///           |\\
///           | \\
///        q1 |  \\\ q3
///           |   \\
///           |    \\
///           B-----C
///             q2
/// ```
pub fn archimedes<T: Numeric>(q_1: T, q_2: T, q_3: T) -> T {
    let temp = q_1 + q_2 - q_3;
    T::from(4) * q_1 * q_2 - temp * temp
}

/// The `cross` function calculates the cross product of two vectors `v_1` and `v_2`.
///
/// # Arguments
///
/// * `v_1` - A 2D vector with numeric components
/// * `v_2` - A 2D vector with numeric components
///
/// # Returns
///
/// The cross product of the two vectors.
///
/// # Examples
///
/// ```
/// use rat_trig::cross;
///
/// let v_1 = [1, 2];
/// let v_2 = [3, 4];
/// assert_eq!(cross(v_1, v_2), -2);
/// ```
///
/// ```text
///            v2
///            ^
///            |
///            |    /
///            |   /
///            |  /
///            | / v1
///            |/____>
///           O
/// ```
pub fn cross<T: Numeric>(v_1: Vector2<T>, v_2: Vector2<T>) -> T {
    v_1[0] * v_2[1] - v_1[1] * v_2[0]
}

/// The `dot` function calculates the dot product of two vectors `v_1` and `v_2`.
///
/// # Arguments
///
/// * `v_1` - A 2D vector with numeric components
/// * `v_2` - A 2D vector with numeric components
///
/// # Returns
///
/// The dot product of the two vectors.
///
/// # Examples
///
/// ```
/// use rat_trig::dot;
///
/// let v_1 = [1, 2];
/// let v_2 = [3, 4];
/// assert_eq!(dot(v_1, v_2), 11);
/// ```
///
/// ```text
///            v2
///            ^
///            |\\
///            | \\
///            |  \\
///            |   \\
///            |    \\ v1
///            |     \\
///            |      \\
///            |_______\\
///           O         projection
/// ```
pub fn dot<T: Numeric>(v_1: Vector2<T>, v_2: Vector2<T>) -> T {
    v_1[0] * v_2[0] + v_1[1] * v_2[1]
}

/// The `quad` function calculates the quadrance of a vector `v`.
///
/// # Arguments
///
/// * `v` - A 2D vector with numeric components
///
/// # Returns
///
/// The quadrance of the vector.
///
/// # Examples
///
/// ```
/// use rat_trig::quad;
///
/// let v = [3, 4];
/// assert_eq!(quad(v), 25);
/// ```
///
/// ```text
///           v[1] ^
///                |
///                |\\
///                | \\
///                |  \\\  quad(v) = v[0]^2 + v[1]^2
///                |   \\
///                |    \\
///                |     \\
///                |      \\
///                |_______\\\
///              O         v[0]
/// ```
pub fn quad<T: Numeric>(v: Vector2<T>) -> T {
    v[0] * v[0] + v[1] * v[1]
}

/// The `spread` function calculates the spread between two vectors `v_1` and `v_2`.
/// The spread is the square of the cross product divided by the product of the quadrances.
/// It represents the square of the sine of the angle between the vectors.
///
/// # Arguments
///
/// * `v_1` - A 2D vector with numeric components
/// * `v_2` - A 2D vector with numeric components
///
/// # Returns
///
/// The spread between the two vectors.
///
/// # Examples
///
/// ```
/// use rat_trig::spread;
/// use num_rational::Ratio;
///
/// let v_1 = [Ratio::new(1, 1), Ratio::new(2, 1)];
/// let v_2 = [Ratio::new(3, 1), Ratio::new(4, 1)];
/// assert_eq!(spread(v_1, v_2), Ratio::new(4, 125));
/// ```
pub fn spread<T: Numeric>(v_1: Vector2<T>, v_2: Vector2<T>) -> T {
    let cross_product = cross(v_1, v_2);
    let quad_1 = quad(v_1);
    let quad_2 = quad(v_2);
    (cross_product * cross_product) / (quad_1 * quad_2)
}

/// The `spread_law` function calculates the spread of a triangle using the law of spreads.
/// In rational trigonometry, the spread law states that for a triangle with quadrances
/// Q1, Q2, Q3, the spread S3 opposite to Q3 can be calculated by:
/// S3 = 4*Q1*Q2 - (Q1 + Q_2 - Q3)^2 / (4*Q1*Q2)
///
/// # Arguments
///
/// * `q_1` - First quadrance of the triangle
/// * `q_2` - Second quadrance of the triangle
/// * `q_3` - Third quadrance of the triangle (opposite to the angle whose spread we're finding)
///
/// # Returns
///
/// The spread S3 opposite to the quadrance q_3
///
/// # Examples
///
/// ```
/// use rat_trig::spread_law;
///
/// let q_1 = 5.0;
/// let q_2 = 25.0;
/// let q_3 = 20.0;
/// assert_eq!(spread_law(q_1, q_2, q_3), 0.8);
/// ```
pub fn spread_law<T: Numeric>(q_1: T, q_2: T, q_3: T) -> T {
    let numerator = archimedes(q_1, q_2, q_3); // 4*q_1*q_2 - (q_1 + q_2 - q_3)^2
    let denominator = T::from(4) * q_1 * q_2;
    numerator / denominator
}

/// The `triple_quad_formula` function calculates a value based on two quadrances and a spread.
/// In rational trigonometry, this formula is related to the relationship between three quadrances
/// and the spread between them.
///
/// # Arguments
///
/// * `q_1` - First quadrance
/// * `q_2` - Second quadrance
/// * `s_3` - Spread value
///
/// # Returns
///
/// A calculated value using the triple quad formula
///
/// # Examples
///
/// ```
/// use rat_trig::triple_quad_formula;
/// use num_rational::Ratio;
///
/// let q_1 = Ratio::new(5, 1);
/// let q_2 = Ratio::new(25, 1);
/// let s_3 = Ratio::new(4, 125);
/// assert_eq!(triple_quad_formula(q_1, q_2, s_3), Ratio::new(416, 1));
/// ```
pub fn triple_quad_formula<T: Numeric>(q_1: T, q_2: T, s_3: T) -> T {
    // Formula: (q_1 + q_2)^2 - 4*q_1*q_2*(1-s_3)
    let sum = q_1 + q_2;
    sum * sum - T::from(4) * q_1 * q_2 * (T::one() - s_3)
}

#[cfg(test)]
mod tests {
    use super::*;
    use num_rational::Ratio;

    #[test]
    fn test_archimedes() {
        // Test with integers
        let q_1_int = 2;
        let q_2_int = 4;
        let q_3_int = 6;
        assert_eq!(archimedes(q_1_int, q_2_int, q_3_int), 32);

        // Test with floats
        let q_1_float = 2.0;
        let q_2_float = 4.0;
        let q_3_float = 6.0;
        assert_eq!(archimedes(q_1_float, q_2_float, q_3_float), 32.0);

        // Test with fractions
        let q_1_frac = Ratio::new(1, 2);
        let q_2_frac = Ratio::new(1, 4);
        let q_3_frac = Ratio::new(1, 6);
        assert_eq!(
            archimedes(q_1_frac, q_2_frac, q_3_frac),
            Ratio::new(23, 144)
        );

        // Test with zero quadrance
        let q_1_zero = 0;
        let q_2_zero = 4;
        let q_3_zero = 6;
        assert_eq!(archimedes(q_1_zero, q_2_zero, q_3_zero), -4);

        // Test with degenerate triangle (collinear points)
        let q_1_degen = 1;
        let q_2_degen = 4;
        let q_3_degen = 9;
        assert_eq!(archimedes(q_1_degen, q_2_degen, q_3_degen), 0);

        // Test with mixed types (Rust is statically typed, so we need to use same type)
        let q_1_mixed = Ratio::new(1, 1);
        let q_2_mixed = Ratio::new(1, 2);
        let q_3_mixed = Ratio::new(2, 1);
        assert_eq!(
            archimedes(q_1_mixed, q_2_mixed, q_3_mixed),
            Ratio::new(7, 4)
        );

        // Test with negative inputs
        let q_1_neg = -1;
        let q_2_neg = 2;
        let q_3_neg = 3;
        assert_eq!(archimedes(q_1_neg, q_2_neg, q_3_neg), -12);
    }

    #[test]
    fn test_cross() {
        // Test with integer vectors
        let v_1_int1 = [1, 2];
        let v_2_int1 = [3, 4];
        assert_eq!(cross(v_1_int1, v_2_int1), -2);

        // Test with float vectors
        let v_1_float = [1.0, 2.0];
        let v_2_float = [3.0, 4.0];
        assert_eq!(cross(v_1_float, v_2_float), -2.0);

        // Test with Fraction vectors
        let v_1_frac = [Ratio::new(1, 2), Ratio::new(1, 4)];
        let v_2_frac = [Ratio::new(1, 6), Ratio::new(1, 8)];
        assert_eq!(cross(v_1_frac, v_2_frac), Ratio::new(1, 48));

        // Test with integer vectors (parallel)
        let v_1_int2 = [1, 2];
        let v_2_int2 = [1, 2];
        assert_eq!(cross(v_1_int2, v_2_int2), 0);

        // Test with integer vectors (perpendicular)
        let v_1_int3 = [1, 0];
        let v_2_int3 = [0, 1];
        assert_eq!(cross(v_1_int3, v_2_int3), 1);
    }

    #[test]
    fn test_dot() {
        // Test with integer vectors
        let v_1_int1 = [1, 2];
        let v_2_int1 = [3, 4];
        assert_eq!(dot(v_1_int1, v_2_int1), 11);

        // Test with float vectors
        let v_1_float = [1.0, 2.0];
        let v_2_float = [3.0, 4.0];
        assert_eq!(dot(v_1_float, v_2_float), 11.0);

        // Test with Fraction vectors
        let v_1_frac = [Ratio::new(1, 2), Ratio::new(1, 4)];
        let v_2_frac = [Ratio::new(1, 6), Ratio::new(1, 8)];
        assert_eq!(dot(v_1_frac, v_2_frac), Ratio::new(11, 96));

        // Test with integer vectors (negative dot product)
        let v_1_int2 = [1, 2];
        let v_2_int2 = [-1, -2];
        assert_eq!(dot(v_1_int2, v_2_int2), -5);

        // Test with integer vectors (orthogonal)
        let v_1_int3 = [1, 0];
        let v_2_int3 = [0, 1];
        assert_eq!(dot(v_1_int3, v_2_int3), 0);
    }

    #[test]
    fn test_quad() {
        // Test with integer vector
        let v_int = [3, 4];
        assert_eq!(quad(v_int), 25);

        // Test with float vector
        let v_float = [3.0, 4.0];
        assert_eq!(quad(v_float), 25.0);

        // Test with Fraction vector
        let v_frac = [Ratio::new(3, 5), Ratio::new(4, 5)];
        assert_eq!(quad(v_frac), Ratio::new(1, 1));

        // Test with another integer vector
        let v_int2 = [1, 1];
        assert_eq!(quad(v_int2), 2);

        // Test with zero vector
        let v_zero = [0, 0];
        assert_eq!(quad(v_zero), 0);
    }

    #[test]
    fn test_spread() {
        // Test with Fraction vectors
        let v_1_frac1 = [Ratio::new(1, 1), Ratio::new(2, 1)];
        let v_2_frac1 = [Ratio::new(3, 1), Ratio::new(4, 1)];
        assert_eq!(spread(v_1_frac1, v_2_frac1), Ratio::new(4, 125));

        // Test with float vectors
        let v_1_float = [1.0, 2.0];
        let v_2_float = [3.0, 4.0];
        assert_eq!(spread(v_1_float, v_2_float), 0.032);

        // Test with different Fraction vectors
        let v_1_frac2 = [Ratio::new(1, 2), Ratio::new(1, 4)];
        let v_2_frac2 = [Ratio::new(1, 6), Ratio::new(1, 8)];
        assert_eq!(spread(v_1_frac2, v_2_frac2), Ratio::new(4, 125));

        // Test with integer vectors (parallel)
        let v_1_int1 = [1, 2];
        let v_2_int1 = [1, 2];
        assert_eq!(spread(v_1_int1, v_2_int1), 0);

        // Test with integer vectors (perpendicular)
        let v_1_int2 = [1, 0];
        let v_2_int2 = [0, 1];
        assert_eq!(spread(v_1_int2, v_2_int2), 1);
    }

    #[test]
    fn test_spread_law() {
        let q_1 = 5.0;
        let q_2 = 25.0;
        let q_3 = 20.0;
        assert_eq!(spread_law(q_1, q_2, q_3), 0.8);

        let q_1 = 1.0;
        let q_2 = 1.0;
        let q_3 = 4.0;
        assert_eq!(spread_law(q_1, q_2, q_3), 0.0);

        let q_1 = 1.0;
        let q_2 = 1.0;
        let q_3 = 0.0;
        assert_eq!(spread_law(q_1, q_2, q_3), 0.0);
    }

    #[test]
    fn test_triple_quad_formula() {
        // Test with int, int, Fraction - result should be Ratio
        let q_1_case1 = Ratio::new(5, 1);
        let q_2_case1 = Ratio::new(25, 1);
        let s_3_case1 = Ratio::new(4, 125);
        assert_eq!(
            triple_quad_formula(q_1_case1, q_2_case1, s_3_case1),
            Ratio::new(416, 1)
        );

        // Test with int, int, int (s_3 = 1)
        let q_1_case2 = 1;
        let q_2_case2 = 1;
        let s_3_case2 = 1;
        assert_eq!(triple_quad_formula(q_1_case2, q_2_case2, s_3_case2), 4);

        // Test with int, int, int (s_3 = 0)
        let q_1_case3 = 1;
        let q_2_case3 = 1;
        let s_3_case3 = 0;
        assert_eq!(triple_quad_formula(q_1_case3, q_2_case3, s_3_case3), 0);
    }
}

/// Fibonacci example function
///
/// # Arguments
///
/// * `n` - integer (must be > 0)
///
/// # Returns
///
/// n-th Fibonacci number
///
/// # Examples
///
/// ```
/// use rat_trig::fib;
/// assert_eq!(fib(1), 1);
/// assert_eq!(fib(2), 1);
/// assert_eq!(fib(3), 2);
/// assert_eq!(fib(4), 3);
/// assert_eq!(fib(5), 5);
/// assert_eq!(fib(6), 8);
/// ```
///
/// ```text
/// F(1)=1  F(2)=1  F(3)=2  F(4)=3  F(5)=5  F(6)=8  ...
///   *     *     **    ***   ***** ******** ...
/// ```
pub fn fib(n: u64) -> u64 {
    assert!(n > 0);
    let mut a = 1;
    let mut b = 1;
    for _ in 0..(n - 1) {
        let temp = a + b;
        a = b;
        b = temp;
    }
    a
}

#[cfg(test)]
mod fib_tests {
    use super::*;

    #[test]
    fn test_fib() {
        assert_eq!(fib(1), 1);
        assert_eq!(fib(2), 1);
        assert_eq!(fib(3), 2);
        assert_eq!(fib(4), 3);
        assert_eq!(fib(5), 5);
        assert_eq!(fib(6), 8);
        assert_eq!(fib(7), 13);
        assert_eq!(fib(8), 21);
        assert_eq!(fib(9), 34);
        assert_eq!(fib(10), 55);
    }

    #[test]
    #[should_panic]
    fn test_fib_zero() {
        fib(0);
    }
}
