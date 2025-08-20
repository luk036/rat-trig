from rat_trig.trigonom import quad
from fractions import Fraction


def test_quad():
    """Test quadrance"""
    v = [3, 4]
    assert quad(v) == 25

    v = [3.0, 4.0]
    assert quad(v) == 25.0

    v = [Fraction(3, 5), Fraction(4, 5)]
    assert quad(v) == 1

    v = [1, 1]
    assert quad(v) == 2

    v = [0, 0]
    assert quad(v) == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
