from src.ab_test import chi_square, relative_lift, two_proportion_ztest
from src.power import sample_size_per_group


def test_no_difference_not_significant():
    res = two_proportion_ztest(100, 1000, 100, 1000)
    assert res.p_value > 0.05
    assert not res.significant


def test_large_difference_is_significant():
    res = two_proportion_ztest(100, 1000, 140, 1000)
    assert res.significant


def test_chi_square_agrees():
    assert chi_square(100, 1000, 140, 1000).significant


def test_relative_lift():
    assert round(relative_lift(100, 1000, 120, 1000), 4) == 0.2


def test_sample_size_positive():
    assert sample_size_per_group(0.10, 0.02) > 0
