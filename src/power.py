"""Sample-size and power analysis helpers."""
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize


def sample_size_per_group(baseline, lift, alpha=0.05, power=0.8):
    effect = proportion_effectsize(baseline + lift, baseline)
    analysis = NormalIndPower()
    return int(analysis.solve_power(
        effect_size=abs(effect), alpha=alpha, power=power, ratio=1.0
    ))
