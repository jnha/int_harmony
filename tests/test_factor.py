"""Tests for factoring periodic signals"""

import pytest

from int_harmony.factor import factor

@pytest.mark.parametrize(
    ('period', 'factored'),
    [
        (tuple(), []),
        ((1,), [(1,)]),
        ((1,0), [(1,0)]),
    ]
)
def test_factor(period, factored):
    assert factor(period) == factored
