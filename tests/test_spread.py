from fractions import Fraction

from rat_trig.trigonom import spread


def test_spread() -> None:
    """Test spread"""
    # Test with Fraction vectors
    v_1_frac1 = [Fraction(1), Fraction(2)]
    v_2_frac1 = [Fraction(3), Fraction(4)]
    assert spread(v_1_frac1, v_2_frac1) == Fraction(4, 125)

    # Test with float vectors
    v_1_float = [1.0, 2.0]
    v_2_float = [3.0, 4.0]
    assert spread(v_1_float, v_2_float) == 0.032

    # Test with different Fraction vectors
    v_1_frac2 = [Fraction(1, 2), Fraction(1, 4)]
    v_2_frac2 = [Fraction(1, 6), Fraction(1, 8)]
    assert spread(v_1_frac2, v_2_frac2) == Fraction(4, 125)

    # Test with integer vectors (parallel)
    v_1_int1 = [1, 2]
    v_2_int1 = [1, 2]
    assert spread(v_1_int1, v_2_int1) == 0

    # Test with integer vectors (perpendicular)
    v_1_int2 = [1, 0]
    v_2_int2 = [0, 1]
    assert spread(v_1_int2, v_2_int2) == 1


if __name__ == "__main__":
    import pytest

    pytest.main()
