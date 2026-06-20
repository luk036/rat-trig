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

.. svgbob::
   :align: center

           A
           |
           |
        q1 |  \\ q3
           |
           |
           B-----C
             q2

     where q1, q2, q3 are quadrances (squared distances)
"""

from fractions import Fraction
from typing import Sequence, TypeVar, Union

NumType = TypeVar("NumType", int, Fraction)
"""Type variable for numeric types: int or Fraction."""

Numeric = Union[int, Fraction]
"""Type alias for numeric types: int or Fraction."""


def archimedes(q_1: Numeric, q_2: Numeric, q_3: Numeric) -> Numeric:
    r"""Archimedes' formula for the quadrea of a triangle.

    Given three side quadrances :math:`q_1, q_2, q_3`, the quadrea (signed
    area squared) is:

    .. math::

       \mathcal{A} = 4 q_1 q_2 - (q_1 + q_2 - q_3)^2

    This is also used to test whether four points :math:`Q_1, Q_2, Q_3, Q_4`
    lie on a circle.

    :param q_1: First quadrance
    :param q_2: Second quadrance
    :param q_3: Third quadrance
    :return: The quadrea of the triangle

    Example:
        >>> from fractions import Fraction
        >>> q_1 = Fraction(1, 2)
        >>> q_2 = Fraction(1, 4)
        >>> q_3 = Fraction(1, 6)
        >>> archimedes(q_1, q_2, q_3)
        Fraction(23, 144)

    .. svgbob::
       :align: center

           A
           |\\
           | \\
        q1 |  \\\ q3
           |   \\
           |    \\
           B-----C
             q2
    """
    temp = q_1 + q_2 - q_3
    return 4 * q_1 * q_2 - temp * temp


def cross(v_1: Sequence[Numeric], v_2: Sequence[Numeric]) -> Numeric:
    r"""Scalar cross product of two 2D vectors.

    For vectors :math:`\mathbf{v}_1 = (x_1, y_1)` and
    :math:`\mathbf{v}_2 = (x_2, y_2)`:

    .. math::

       \mathbf{v}_1 \times \mathbf{v}_2 = x_1 y_2 - y_1 x_2

    This equals the signed area of the parallelogram spanned by the vectors.

    :param v_1: A sequence of two numbers
    :param v_2: A sequence of two numbers
    :return: The scalar cross product

    Example:
        >>> v_1 = [1, 2]
        >>> v_2 = [3, 4]
        >>> cross(v_1, v_2)
        -2

    .. svgbob::
       :align: center

            v2
            ^
            |
            |    /
            |   /
            |  /
            | / v1
            |/____>
           O
    """
    return v_1[0] * v_2[1] - v_1[1] * v_2[0]


def dot(v_1: Sequence[Numeric], v_2: Sequence[Numeric]) -> Numeric:
    r"""Dot product of two 2D vectors.

    For vectors :math:`\mathbf{v}_1 = (x_1, y_1)` and
    :math:`\mathbf{v}_2 = (x_2, y_2)`:

    .. math::

       \mathbf{v}_1 \cdot \mathbf{v}_2 = x_1 x_2 + y_1 y_2

    :param v_1: A sequence of two numbers
    :param v_2: A sequence of two numbers
    :return: The dot product

    Example:
        >>> v_1 = [1, 2]
        >>> v_2 = [3, 4]
        >>> dot(v_1, v_2)
        11

    .. svgbob::
       :align: center

            v2
            ^
            |\\
            | \\
            |  \\
            |   \\
            |    \\ v1
            |     \\
            |      \\
            |_______\\
           O         projection
    """
    return v_1[0] * v_2[0] + v_1[1] * v_2[1]


def quad(vector: Sequence[Numeric]) -> Numeric:
    r"""Quadrance (squared length) of a 2D vector.

    In rational trigonometry, quadrance replaces the classical notion of
    distance. For a vector :math:`\mathbf{v} = (x, y)`:

    .. math::

       Q(\mathbf{v}) = x^2 + y^2

    This is the squared Euclidean norm, always a rational number when
    :math:`x, y` are rational.

    :param vector: A sequence of two numbers
    :return: The quadrance of the vector

    Example:
        >>> vector = [3, 4]
        >>> quad(vector)
        25

    .. svgbob::
       :align: center

           vector[1] ^
                    |
                    |\\
                    | \\
                    |  \\\  quad(vector) = vector[0]^2 + vector[1]^2
                    |   \\
                    |    \\
                    |     \\
                    |      \\
                    |_______\\\
                  O         vector[0]
    """
    return vector[0] * vector[0] + vector[1] * vector[1]


def spread(v_1: Sequence[Numeric], v_2: Sequence[Numeric]) -> Numeric:
    r"""Spread between two 2D vectors.

    In rational trigonometry, spread replaces the classical angle. It is the
    square of the sine of the angle between :math:`\mathbf{v}_1` and
    :math:`\mathbf{v}_2`:

    .. math::

       s(\mathbf{v}_1, \mathbf{v}_2)
       = \frac{(\mathbf{v}_1 \times \mathbf{v}_2)^2}
              {Q(\mathbf{v}_1) \; Q(\mathbf{v}_2)}

    The result is always a rational number between 0 and 1.

    :param v_1: A sequence of two numbers
    :param v_2: A sequence of two numbers
    :return: The spread between the two vectors

    Example:
        >>> from fractions import Fraction
        >>> v_1 = [Fraction(1), Fraction(2)]
        >>> v_2 = [Fraction(3), Fraction(4)]
        >>> spread(v_1, v_2)
        Fraction(4, 125)
    """
    cross_product = cross(v_1, v_2)
    quad_1 = quad(v_1)
    quad_2 = quad(v_2)
    return Fraction(cross_product * cross_product, quad_1 * quad_2)


def spread_law(q_1: Numeric, q_2: Numeric, q_3: Numeric) -> Numeric:
    r"""Law of spreads for a triangle.

    In any triangle with quadrances :math:`q_1, q_2, q_3`, the spread
    :math:`S_3` opposite side :math:`q_3` is:

    .. math::

       S_3 = \frac{\mathcal{A}}{4 q_1 q_2}
           = \frac{4 q_1 q_2 - (q_1 + q_2 - q_3)^2}{4 q_1 q_2}

    where :math:`\mathcal{A}` is the quadrea from Archimedes' formula.

    :param q_1: First quadrance
    :param q_2: Second quadrance
    :param q_3: Third quadrance (opposite the angle whose spread is found)
    :return: The spread :math:`S_3` opposite :math:`q_3`

    Example:
        >>> from fractions import Fraction
        >>> q_1 = 5
        >>> q_2 = 25
        >>> q_3 = 20
        >>> spread_law(q_1, q_2, q_3)
        Fraction(4, 5)
    """
    numerator = archimedes(q_1, q_2, q_3)  # 4*q_1*q_2 - (q_1 + q_2 - q_3)^2
    denominator = 4 * q_1 * q_2
    return Fraction(numerator, denominator)


def triple_quad_formula(q_1: Numeric, q_2: Numeric, s_3: Numeric) -> Numeric:
    r"""Triple quad formula relating two quadrances and a spread.

    This formula relates two quadrances :math:`q_1, q_2` and a spread
    :math:`s_3` through the identity:

    .. math::

       T(q_1, q_2, s_3) = (q_1 + q_2)^2 - 4 q_1 q_2 (1 - s_3)
                        = (q_1 - q_2)^2 + 4 q_1 q_2 s_3

    When :math:`s_3 = 1` (right spread), this reduces to
    :math:`(q_1 + q_2)^2`; when :math:`s_3 = 0` (collinear), it reduces to
    :math:`(q_1 - q_2)^2`.

    :param q_1: First quadrance
    :param q_2: Second quadrance
    :param s_3: Spread value
    :return: Result of the triple quad formula

    Example:
        >>> from fractions import Fraction
        >>> q_1 = 5
        >>> q_2 = 25
        >>> s_3 = Fraction(4, 125)
        >>> triple_quad_formula(q_1, q_2, s_3)
        Fraction(416, 1)
    """
    return (q_1 + q_2) * (q_1 + q_2) - 4 * q_1 * q_2 * (1 - s_3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
