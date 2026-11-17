from src.ab_test import two_proportion_ztest


def test_no_difference_not_significant():
    res = two_proportion_ztest(100, 1000, 100, 1000)
    assert res.p_value > 0.05
    assert not res.significant


def test_large_difference_is_significant():
    res = two_proportion_ztest(100, 1000, 200, 1000)
    assert res.significant
