"""Simulate users exposed to a control and treatment variant."""
from pathlib import Path

import numpy as np
import pandas as pd


def make(n: int = 5000, baseline: float = 0.10, lift: float = 0.02, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    group = rng.choice(["control", "treatment"], n, p=[0.5, 0.5])
    rate = np.where(group == "treatment", baseline + lift, baseline)
    converted = rng.binomial(1, rate)
    revenue = np.where(converted == 1, rng.gamma(2.0, 25.0, n), 0.0)
    return pd.DataFrame({"group": group, "converted": converted,
                         "revenue": np.round(revenue, 2)})


def main() -> Path:
    out = Path("data/raw/experiment.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    make().to_csv(out, index=False)
    print(f"wrote experiment data -> {out}")
    return out


if __name__ == "__main__":
    main()
