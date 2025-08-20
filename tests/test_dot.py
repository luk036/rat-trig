from rat_trig.trigonom import dot
from fractions import Fraction


def test_dot():
    """Test dot product"""
    v_1 = [1, 2]
    v_2 = [3, 4]
    assert dot(v_1, v_2) == 11

    v_1 = [1.0, 2.0]
    v_2 = [3.0, 4.0]
    assert dot(v_1, v_2) == 11.0

    v_1 = [Fraction(1, 2), Fraction(1, 4)]
    v_2 = [Fraction(1, 6), Fraction(1, 8)]
    assert dot(v_1, v_2) == Fraction(11, 96)

    v_1 = [1, 2]
    v_2 = [-1, -2]
    assert dot(v_1, v_2) == -5

    v_1 = [1, 0]
    v_2 = [0, 1]
    assert dot(v_1, v_2) == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
