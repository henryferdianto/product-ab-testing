import pandas as pd

from src.ab_test import chi_square, relative_lift, two_proportion_ztest
from src.power import sample_size_per_group
from src.sample_data import make


def main():
    df = make()
    df.to_csv("data/raw/experiment.csv", index=False)
    agg = df.groupby("group")["converted"].agg(["sum", "count"])
    n_a, c_a = int(agg.loc["control", "count"]), int(agg.loc["control", "sum"])
    n_b, c_b = int(agg.loc["treatment", "count"]), int(agg.loc["treatment", "sum"])
    print(f"control: {c_a}/{n_a}  treatment: {c_b}/{n_b}")
    print(two_proportion_ztest(c_a, n_a, c_b, n_b))
    print(chi_square(c_a, n_a, c_b, n_b))
    print(f"relative lift = {relative_lift(c_a, n_a, c_b, n_b):.2%}")
    print("required per group for +2pp lift:",
          sample_size_per_group(0.10, 0.02))


if __name__ == "__main__":
    main()
