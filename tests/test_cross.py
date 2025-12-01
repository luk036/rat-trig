from fractions import Fraction

from rat_trig.trigonom import cross


def test_cross() -> None:
    """Test cross product"""
    v_1 = [1, 2]
    v_2 = [3, 4]
    assert cross(v_1, v_2) == -2

    v_1 = [1.0, 2.0]
    v_2 = [3.0, 4.0]
    assert cross(v_1, v_2) == -2.0

    v_1 = [Fraction(1, 2), Fraction(1, 4)]
    v_2 = [Fraction(1, 6), Fraction(1, 8)]
    assert cross(v_1, v_2) == Fraction(1, 48)

    v_1 = [1, 2]
    v_2 = [1, 2]
    assert cross(v_1, v_2) == 0

    v_1 = [1, 0]
    v_2 = [0, 1]
    assert cross(v_1, v_2) == 1


if __name__ == "__main__":
    import pytest

    pytest.main()
