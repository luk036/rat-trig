from rat_trig.trigonom import spread_law


def test_spread_law() -> None:
    """Test spread law"""
    q_1 = 5
    q_2 = 25
    q_3 = 20
    assert spread_law(q_1, q_2, q_3) == 0.8

    q_1 = 1
    q_2 = 1
    q_3 = 4
    assert spread_law(q_1, q_2, q_3) == 0

    q_1 = 1
    q_2 = 1
    q_3 = 0
    assert spread_law(q_1, q_2, q_3) == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
