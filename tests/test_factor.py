"""Tests for factoring periodic signals"""

from int_harmony.factor import factor


def test_factor():
    assert factor(tuple()) == tuple()
