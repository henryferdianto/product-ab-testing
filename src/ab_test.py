"""Hypothesis testing for A/B experiments."""
import argparse
from dataclasses import dataclass

import numpy as np
from scipy import stats


@dataclass
class Result:
    test: str
    statistic: float
    p_value: float
    significant: bool


def two_proportion_ztest(conv_a, n_a, conv_b, n_b, alpha=0.05) -> Result:
    p_a, p_b = conv_a / n_a, conv_b / n_b
    p_pool = (conv_a + conv_b) / (n_a + n_b)
    se = (p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b)) ** 0.5
    z = (p_b - p_a) / se if se else 0.0
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return Result("two-proportion z-test", float(z), float(p), p < alpha)


def chi_square(conv_a, n_a, conv_b, n_b, alpha=0.05) -> Result:
    table = np.array([[conv_a, n_a - conv_a], [conv_b, n_b - conv_b]])
    chi2, p, _, _ = stats.chi2_contingency(table)
    return Result("chi-square", float(chi2), float(p), p < alpha)


def relative_lift(conv_a, n_a, conv_b, n_b) -> float:
    return (conv_b / n_b - conv_a / n_a) / (conv_a / n_a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--control", nargs=2, type=int, required=True, metavar=("N", "CONV"))
    ap.add_argument("--treatment", nargs=2, type=int, required=True, metavar=("N", "CONV"))
    args = ap.parse_args()
    n_a, c_a = args.control
    n_b, c_b = args.treatment
    print(two_proportion_ztest(c_a, n_a, c_b, n_b))
    print(chi_square(c_a, n_a, c_b, n_b))
    print(f"relative lift = {relative_lift(c_a, n_a, c_b, n_b):.2%}")


if __name__ == "__main__":
    main()
