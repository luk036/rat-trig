from fractions import Fraction

from rat_trig.trigonom import archimedes


def test_archimedes():
    """Test Archimedes' formula"""
    q_1 = 2
    q_2 = 4
    q_3 = 6
    assert archimedes(q_1, q_2, q_3) == 32

    q_1 = 2.0
    q_2 = 4.0
    q_3 = 6.0
    assert archimedes(q_1, q_2, q_3) == 32

    q_1 = Fraction(1, 2)
    q_2 = Fraction(1, 4)
    q_3 = Fraction(1, 6)
    assert archimedes(q_1, q_2, q_3) == Fraction(23, 144)

    # Test with zero quadrance
    q_1 = 0
    q_2 = 4
    q_3 = 6
    assert archimedes(q_1, q_2, q_3) == -4

    # Test with degenerate triangle (collinear points)
    q_1 = 1
    q_2 = 4
    q_3 = 9
    assert archimedes(q_1, q_2, q_3) == 0

    # Test with mixed types
    q_1 = 1
    q_2 = Fraction(1, 2)
    q_3 = 2
    assert archimedes(q_1, q_2, q_3) == Fraction(7, 4)

    # Test with negative inputs
    q_1 = -1
    q_2 = 2
    q_3 = 3
    assert archimedes(q_1, q_2, q_3) == -12


if __name__ == "__main__":
    import pytest

    pytest.main()
