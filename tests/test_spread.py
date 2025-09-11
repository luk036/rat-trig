from fractions import Fraction

from rat_trig.trigonom import spread


def test_spread():
    """Test spread"""
    v_1 = [Fraction(1), Fraction(2)]
    v_2 = [Fraction(3), Fraction(4)]
    assert spread(v_1, v_2) == Fraction(4, 125)

    v_1 = [1.0, 2.0]
    v_2 = [3.0, 4.0]
    assert spread(v_1, v_2) == 0.032

    v_1 = [Fraction(1, 2), Fraction(1, 4)]
    v_2 = [Fraction(1, 6), Fraction(1, 8)]
    assert spread(v_1, v_2) == Fraction(4, 125)

    v_1 = [1, 2]
    v_2 = [1, 2]
    assert spread(v_1, v_2) == 0

    v_1 = [1, 0]
    v_2 = [0, 1]
    assert spread(v_1, v_2) == 1


if __name__ == "__main__":
    import pytest

    pytest.main()
