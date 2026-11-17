"""Sample-size and power analysis helpers (scipy only)."""
from scipy.stats import norm


def sample_size_per_group(baseline, lift, alpha=0.05, power=0.8):
    p1 = baseline
    p2 = baseline + lift
    z_alpha = norm.ppf(1 - alpha / 2)
    z_beta = norm.ppf(power)
    pooled_var = p1 * (1 - p1) + p2 * (1 - p2)
    return int(round(((z_alpha + z_beta) ** 2 * pooled_var) / ((p2 - p1) ** 2)))


def power_for_sample(n, baseline, lift, alpha=0.05):
    p1 = baseline
    p2 = baseline + lift
    se = ((p1 * (1 - p1) + p2 * (1 - p2)) / n) ** 0.5
    z = abs(p2 - p1) / se
    return float(norm.cdf(z - norm.ppf(1 - alpha / 2)))
