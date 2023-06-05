"""
Interpolation

Functions for expanding samples into larger ones.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


def interpolate_constant(n: int, samples: Iterable[int]) -> Iterator[int]:
    """Interpolate by copying the previous sample"""
    for sample in samples:
        for _ in range(n):
            yield sample
