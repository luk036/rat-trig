"""
Rational Trigonometry is a new approach to classical trigonometry, developed by Norman
Wildberger, that aims to simplify and clarify the subject by using only rational numbers
and operations, rather than irrational numbers and limits.

In traditional trigonometry, concepts such as the sine, cosine, and tangent of an angle
are typically defined using circles and the unit circle in particular. These definitions
involve irrational numbers and limits, which can make the subject more difficult to
understand and work with.

In rational trigonometry, Wildberger replaces these circular definitions with ones based
on lines and line segments, which allows for a more straightforward and intuitive approach.
The fundamental concepts in rational trigonometry are the "quadaverage" and the "dilated
directed angle," which are defined in terms of lines and line segments, rather than circles.

Rational trigonometry has been gaining popularity in recent years, as it provides a useful
alternative to traditional trigonometry for certain applications, such as computer graphics,
robotics, and physics. It can also be a helpful tool for students who struggle with the
irrational numbers and limits used in traditional trigonometry.

In summary, Rational Trigonometry is a new approach to classical trigonometry that uses
rational numbers and operations, rather than irrational numbers and limits, making it a more
straightforward and intuitive subject to understand and work with.
"""

from typing import TypeVar
from fractions import Fraction

T = TypeVar("T", int, Fraction, float)


def archimedes(q_1: T, q_2: T, q_3: T) -> T:
    r"""
    The function `archimedes` calculates the qudrea of a triangle using Archimedes' formula with
    the lengths of the three sides `q_1`, `q_2`, and `q_3`. It can also be used to check if a quadraple
    with length Q1, Q2, Q3, Q4 is on a circle.

    :param q_1: The function `archimedes` takes three parameters `q_1`, `q_2`, and `q_3` of type `T` and
        returns a value of type `T`
    :type q_1: T
    :param q_2: The `q_2` parameter in the `archimedes` function represents a value of type `T`. It is
        one of the input parameters along with `q_1` and `q_3`. The function performs a calculation using
        these parameters and returns a result of type `T`
    :type q_2: T
    :param q_3: The function `archimedes` takes three parameters `q_1`, `q_2`, and `q_3`, all of type
        `T`. It then calculates a value based on these parameters and returns the result
    :type q_3: T
    :return: the result of the expression \(4 \times q_1 \times q_2 - \text{temp}^2\), where
        \(\text{temp} = q_1 + q_2 - q_3\).

    Example:
        >>> q_1 = Fraction(1, 2)
        >>> q_2 = Fraction(1, 4)
        >>> q_3 = Fraction(1, 6)
        >>> archimedes(q_1, q_2, q_3)
        Fraction(23, 144)
    """
    return 4 * q_1 * q_2 - (q_1 + q_2 - q_3) ** 2


def cross(v_1: list[T], v_2: list[T]) -> T:
    r"""
    The `cross` function calculates the cross product of two vectors `v_1` and `v_2`.

    :param v_1: A list of two numbers (integers, fractions, or floats).
    :type v_1: list[T]
    :param v_2: A list of two numbers (integers, fractions, or floats).
    :type v_2: list[T]
    :return: The cross product of the two vectors.
    :rtype: T

    Example:
        >>> v_1 = [1, 2]
        >>> v_2 = [3, 4]
        >>> cross(v_1, v_2)
        -2
    """
    return v_1[0] * v_2[1] - v_1[1] * v_2[0]


def dot(v_1: list[T], v_2: list[T]) -> T:
    r"""
    The `dot` function calculates the dot product of two vectors `v_1` and `v_2`.

    :param v_1: A list of two numbers (integers, fractions, or floats).
    :type v_1: list[T]
    :param v_2: A list of two numbers (integers, fractions, or floats).
    :type v_2: list[T]
    :return: The dot product of the two vectors.
    :rtype: T

    Example:
        >>> v_1 = [1, 2]
        >>> v_2 = [3, 4]
        >>> dot(v_1, v_2)
        11
    """
    return v_1[0] * v_2[0] + v_1[1] * v_2[1]


def quad(v: list[T]) -> T:
    r"""
    The `quad` function calculates the quadrance of a vector `v`.

    :param v: A list of two numbers (integers, fractions, or floats).
    :type v: list[T]
    :return: The quadrance of the vector.
    :rtype: T

    Example:
        >>> v = [3, 4]
        >>> quad(v)
        25
    """
    return v[0] ** 2 + v[1] ** 2


def spread(v_1: list[T], v_2: list[T]) -> T:
    r"""
    The `spread` function calculates the spread between two vectors `v_1` and `v_2`.

    :param v_1: A list of two numbers (integers, fractions, or floats).
    :type v_1: list[T]
    :param v_2: A list of two numbers (integers, fractions, or floats).
    :type v_2: list[T]
    :return: The spread between the two vectors.
    :rtype: T

    Example:
        >>> v_1 = [1, 2]
        >>> v_2 = [3, 4]
        >>> spread(v_1, v_2)
        Fraction(4, 125)
    """
    return (v_1[0] * v_2[1] - v_1[1] * v_2[0]) ** 2 / ((v_1[0] ** 2 + v_1[1] ** 2) * (v_2[0] ** 2 + v_2[1] ** 2))


def triple_quad_formula(q_1: T, q_2: T, s_3: T) -> T:
    r"""
    The `triple_quad_formula` calculates the third quadrance of a triangle given two quadrances
    and the spread between them.

    :param q_1: The first quadrance.
    :type q_1: T
    :param q_2: The second quadrance.
    :type q_2: T
    :param s_3: The spread between the two vectors.
    :type s_3: T
    :return: The third quadrance.
    :rtype: T

    Example:
        >>> q_1 = 5
        >>> q_2 = 25
        >>> s_3 = Fraction(4, 125)
        >>> triple_quad_formula(q_1, q_2, s_3)
        20.0
    """
    return (q_1 + q_2) ** 2 - 4 * q_1 * q_2 * (1 - s_3)


def spread_law(q_1: T, q_2: T, q_3: T) -> T:
    r"""
    The `spread_law` calculates the spread of a triangle given two quadrances and the third quadrance.

    :param q_1: The first quadrance.
    :type q_1: T
    :param q_2: The second quadrance.
    :type q_2: T
    :param q_3: The third quadrance.
    :type q_3: T
    :return: The spread.
    :rtype: T

    Example:
        >>> q_1 = 5
        >>> q_2 = 25
        >>> q_3 = 20
        >>> spread_law(q_1, q_2, q_3)
        Fraction(1, 1)
    """
    return 1 - (q_1 + q_2 - q_3) ** 2 / (4 * q_1 * q_2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
