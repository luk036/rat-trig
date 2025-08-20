from rat_trig.trigonom import triple_quad_formula
from fractions import Fraction


def test_triple_quad_formula():
    """Test triple quad formula"""
    q_1 = 5
    q_2 = 25
    s_3 = Fraction(4, 125)
    assert triple_quad_formula(q_1, q_2, s_3) == 416

    q_1 = 1
    q_2 = 1
    s_3 = 1
    assert triple_quad_formula(q_1, q_2, s_3) == 4

    q_1 = 1
    q_2 = 1
    s_3 = 0
    assert triple_quad_formula(q_1, q_2, s_3) == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
