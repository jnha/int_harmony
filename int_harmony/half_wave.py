"""Half-wave symmetry

A waveform has half-wave symmetry if the second half cycle
is a flipped (negative) copy of the first half cycle.
For a waveform f with period P:
  f(t + P/2) = -f(t)

A waveform with half-wave symmetry has only odd harmonics.
"""

from itertools import chain
from typing import Protocol, Sequence, TypeVar


class Negatable(Protocol):
    """Unary minus protocol"""

    def __neg__(self):
        pass


N = TypeVar("N", bound=Negatable)


def half_wave(samples: Sequence[N]) -> Sequence[N]:
    """Make a half-wave symmetric cycle from a half-cycle."""
    return tuple(chain(samples, (-sample for sample in samples)))


def half_wave_odd(samples: Sequence[int]) -> Sequence[int]:
    """Make a half-wave symmetric cycle with an odd length from a half-cycle."""
    return tuple(chain(samples, (0,), (-sample for sample in samples)))
