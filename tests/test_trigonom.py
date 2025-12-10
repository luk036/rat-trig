from fractions import Fraction

from rat_trig.trigonom import archimedes


def test_archimedes() -> None:
    """Test Archimedes' formula"""
    # Test with integers
    q_1_int = 2
    q_2_int = 4
    q_3_int = 6
    assert archimedes(q_1_int, q_2_int, q_3_int) == 32

    # Test with floats
    q_1_float = 2.0
    q_2_float = 4.0
    q_3_float = 6.0
    assert archimedes(q_1_float, q_2_float, q_3_float) == 32

    # Test with fractions
    q_1_frac = Fraction(1, 2)
    q_2_frac = Fraction(1, 4)
    q_3_frac = Fraction(1, 6)
    assert archimedes(q_1_frac, q_2_frac, q_3_frac) == Fraction(23, 144)

    # Test with zero quadrance
    q_1_zero = 0
    q_2_zero = 4
    q_3_zero = 6
    assert archimedes(q_1_zero, q_2_zero, q_3_zero) == -4

    # Test with degenerate triangle (collinear points)
    q_1_degen = 1
    q_2_degen = 4
    q_3_degen = 9
    assert archimedes(q_1_degen, q_2_degen, q_3_degen) == 0

    # Test with mixed types
    q_1_mixed = 1
    q_2_mixed = Fraction(1, 2)
    q_3_mixed = 2
    assert archimedes(q_1_mixed, q_2_mixed, q_3_mixed) == Fraction(7, 4)

    # Test with negative inputs
    q_1_neg = -1
    q_2_neg = 2
    q_3_neg = 3
    assert archimedes(q_1_neg, q_2_neg, q_3_neg) == -12


if __name__ == "__main__":
    import pytest

    pytest.main()
