# Product Feature Launch A/B Testing & Statistical Causal Inference

> **Power analysis, hypothesis testing and confidence intervals for product decisions**

## Overview

A statistical experimentation framework to evaluate conversion lift and engagement after a feature rollout, including power analysis, hypothesis testing and confidence intervals.

## Approach

1. **Design**: sample-size and power analysis for the target effect.
2. **Testing**: two-sample t-test, chi-square and Mann-Whitney U.
3. **Estimation**: confidence intervals and effect sizes.
4. **Decisioning**: interpret results against business thresholds.

## Repository Structure

```
product-ab-testing/
├── src/power.py          # sample size & power
├── src/ab_test.py        # hypothesis tests
├── tests/test_ab.py
├── requirements.txt
└── README.md
```

## Tech Stack

`Python` · `SciPy` · `statsmodels` · `pytest`

## Getting Started

```bash
git clone https://github.com/henryferdianto/product-ab-testing.git
cd product-ab-testing
pip install -r requirements.txt
```

```bash
python src/ab_test.py --control 1000 120 --treatment 1000 145
pytest -q
```

## Project Status

This repository contains the project documentation and a runnable implementation
skeleton. Scripts are structured so that each pipeline stage can be executed and
extended independently. Update the configuration and data paths to run against
your own datasets.

## License

MIT License — see [LICENSE](LICENSE).


---

**Author:** Rifky Henry Ferdianto — Data Science undergraduate at ITERA  
GitHub: [@henryferdianto](https://github.com/henryferdianto) · Portfolio: [rifky-henry-ferdianto](https://github.com/henryferdianto/rifky-henry-ferdianto)
