from fractions import Fraction

from rat_trig.trigonom import triple_quad_formula


def test_triple_quad_formula() -> None:
    """Test triple quad formula"""
    # Test with int, int, Fraction
    q_1_case1 = 5
    q_2_case1 = 25
    s_3_case1 = Fraction(4, 125)
    assert triple_quad_formula(q_1_case1, q_2_case1, s_3_case1) == 416

    # Test with int, int, int (s_3 = 1)
    q_1_case2 = 1
    q_2_case2 = 1
    s_3_case2 = 1
    assert triple_quad_formula(q_1_case2, q_2_case2, s_3_case2) == 4

    # Test with int, int, int (s_3 = 0)
    q_1_case3 = 1
    q_2_case3 = 1
    s_3_case3 = 0
    assert triple_quad_formula(q_1_case3, q_2_case3, s_3_case3) == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
