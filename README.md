# Product Feature Launch A/B Testing & Statistical Causal Inference

![ci](https://github.com/henryferdianto/product-ab-testing/actions/workflows/ci.yml/badge.svg)

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


<!-- completed -->

## Quickstart with Sample Data

The repository ships a synthetic data generator so the full pipeline can be run
without any private dataset:

```bash
make sample && python -m src.run_demo
python -m src.ab_test --control 2500 250 --treatment 2500 300
```

## Tests

```bash
pip install -r requirements.txt
pytest -q
```

## Project Status

This repository contains the project documentation and a runnable reference
implementation. A synthetic data generator is included so every pipeline stage
can be executed end-to-end; replace the sample data with your own datasets in
`data/raw/` to reproduce real results.

## License

MIT License — see [LICENSE](LICENSE).


---

**Author:** Rifky Henry Ferdianto — Data Science undergraduate at ITERA  
GitHub: [@henryferdianto](https://github.com/henryferdianto) · Portfolio: [rifky-henry-ferdianto](https://github.com/henryferdianto/rifky-henry-ferdianto)
