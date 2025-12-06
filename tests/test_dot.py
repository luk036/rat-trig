from fractions import Fraction

from rat_trig.trigonom import dot


def test_dot() -> None:
    """Test dot product"""
    # Test with integer vectors
    v_1_int1 = [1, 2]
    v_2_int1 = [3, 4]
    assert dot(v_1_int1, v_2_int1) == 11

    # Test with float vectors
    v_1_float = [1.0, 2.0]
    v_2_float = [3.0, 4.0]
    assert dot(v_1_float, v_2_float) == 11.0

    # Test with Fraction vectors
    v_1_frac = [Fraction(1, 2), Fraction(1, 4)]
    v_2_frac = [Fraction(1, 6), Fraction(1, 8)]
    assert dot(v_1_frac, v_2_frac) == Fraction(11, 96)

    # Test with integer vectors (negative dot product)
    v_1_int2 = [1, 2]
    v_2_int2 = [-1, -2]
    assert dot(v_1_int2, v_2_int2) == -5

    # Test with integer vectors (orthogonal)
    v_1_int3 = [1, 0]
    v_2_int3 = [0, 1]
    assert dot(v_1_int3, v_2_int3) == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
