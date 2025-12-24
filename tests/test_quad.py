from fractions import Fraction

from rat_trig.trigonom import quad


def test_quad() -> None:
    """Test quadrance"""
    # Test with integer vector
    vec_int = [3, 4]
    assert quad(vec_int) == 25

    # Test with float vector
    vec_float = [3.0, 4.0]
    assert quad(vec_float) == 25.0

    # Test with Fraction vector
    vec_frac = [Fraction(3, 5), Fraction(4, 5)]
    assert quad(vec_frac) == 1

    # Test with another integer vector
    vec_int2 = [1, 1]
    assert quad(vec_int2) == 2

    # Test with zero vector
    vec_zero = [0, 0]
    assert quad(vec_zero) == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
